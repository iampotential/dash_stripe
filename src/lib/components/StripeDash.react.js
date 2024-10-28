import React, { Component, useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { Elements } from '@stripe/react-stripe-js';
import { loadStripe } from '@stripe/stripe-js';
import { CardElement, useStripe, useElements } from '@stripe/react-stripe-js';
import './StripeDash.css';

export default class StripeDash extends Component {
    render() {
        const { id, label, setProps, referenceId, customConfirmMessage, amount, prePaymentMessage, stripe_key, stripe_api } = this.props;

        const stripePromise = loadStripe(stripe_key);

        return (
            <div id={id} className="stripe-dash-container">
                <h3 className="stripe-dash-label">{label}</h3>
                <Elements stripe={stripePromise}>
                    <CheckoutForm 
                        setProps={setProps} 
                        referenceId={referenceId} 
                        customConfirmMessage={customConfirmMessage} 
                        amount={amount} 
                        prePaymentMessage={prePaymentMessage}
                        stripe_api={stripe_api}  // Pass stripe_api to CheckoutForm
                    />
                </Elements>
            </div>
        );
    }
}

const CheckoutForm = ({ setProps, referenceId, customConfirmMessage, amount, prePaymentMessage, stripe_api }) => {
    const stripe = useStripe();
    const elements = useElements();
    const [paymentStatus, setPaymentStatus] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        if (setProps.paymentStatus) {
            setPaymentStatus(setProps.paymentStatus);
        }
    }, [setProps.paymentStatus]);

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!stripe || !elements) {
            return;
        }

        setIsLoading(true);

        const cardElement = elements.getElement(CardElement);
        const cardholderName = event.target.cardholderName.value;

        const { error, paymentMethod } = await stripe.createPaymentMethod({
            type: 'card',
            card: cardElement,
            billing_details: {
                name: cardholderName
            },
            metadata: { referenceId: referenceId }
        });

        if (error) {
            console.error('[error]', error);
            setProps({ paymentStatus: 'error', errorMessage: error.message });
            setPaymentStatus('error');
            setIsLoading(false);
        } else {
            console.log('[PaymentMethod]', paymentMethod);
            const paymentMethodString = JSON.stringify(paymentMethod);
            setProps({ paymentStatus: 'success', paymentMethodId: paymentMethod.id, referenceId: referenceId, paymentMethodDetails: paymentMethodString });
            setPaymentStatus('success');

            try {
                const response = await fetch(stripe_api, {  // Use stripe_api here
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        payment_method_id: paymentMethod.id,
                        amount: amount,
                        currency: 'usd',
                        reference_id: referenceId,
                    }),
                });
                const result = await response.json();
                if (response.ok) {
                    console.log('[PaymentIntent]', result);
                    setProps({ 
                        paymentStatus: 'payment_intent_success', 
                        paymentIntentId: result.payment_intent_id,
                        confirmMessage: `${customConfirmMessage}. Transaction ID: ${result.payment_intent_id}. Amount: $${(amount / 100).toFixed(2)}`
                    });
                    setPaymentStatus('payment_intent_success');
                } else {
                    console.error('[PaymentIntent Error]', result);
                    setProps({ paymentStatus: 'payment_intent_error', errorMessage: result.detail });
                    setPaymentStatus('error');
                }
            } catch (err) {
                console.error('[Fetch Error]', err);
                setProps({ paymentStatus: 'payment_intent_error', errorMessage: 'Unable to create payment intent' });
                setPaymentStatus('error');
            }
            setIsLoading(false);
        }
    };

    if (paymentStatus === 'payment_intent_success') {
        return (
            <div className="success-message">
                <div className="green-checkmark">✔</div>
                <h2>Payment Successful!</h2>
                <p>{customConfirmMessage}</p>
            </div>
        );
    }

    return (
        <form onSubmit={handleSubmit} className="stripe-dash-form">
            {prePaymentMessage && <p className="pre-payment-message">{prePaymentMessage}</p>}
            <div className="input-wrapper cardholder-wrapper">
                <label htmlFor="cardholderName" className="input-label">Cardholder Name</label>
                <input type="text" id="cardholderName" name="cardholderName" required className="input-element" placeholder="Enter cardholder name" />
            </div>
            <div className="card-element-wrapper">
                <CardElement options={{ hidePostalCode: true }} className="card-element" />
            </div>
            <button type="submit" disabled={!stripe || isLoading} className={`stripe-dash-button ${isLoading ? 'loading' : ''}`}>

                {isLoading ? <div className="spinner"></div> : `Pay $${amount / 100}`}
            </button>
        </form>
    );
};

StripeDash.propTypes = {
    id: PropTypes.string,
    label: PropTypes.string.isRequired,
    setProps: PropTypes.func,
    paymentStatus: PropTypes.string,
    errorMessage: PropTypes.string,
    paymentMethodId: PropTypes.string,
    referenceId: PropTypes.string,
    paymentMethodDetails: PropTypes.string,
    paymentIntentId: PropTypes.string,
    customConfirmMessage: PropTypes.string,
    amount: PropTypes.number,
    prePaymentMessage: PropTypes.string,
    stripe_key: PropTypes.string.isRequired,  // Stripe key as a prop
    stripe_api: PropTypes.string.isRequired   // New PropType for the Stripe API endpoint
};
