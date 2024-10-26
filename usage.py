import stripe_dash
from dash import Dash, callback, html, Input, Output
import os
app = Dash(__name__)

app.layout = html.Div([
    stripe_dash.StripeDash(
        id='input',
        label='Confirm Booking',
        paymentMethodId="asdfadfa",
        paymentStatus="asdfasdfa",
        paymentIntentId="",  # Add this prop to match the updated frontend code
        paymentMethodDetails="",
        amount=5555,
        customConfirmMessage='hello world',
        prePaymentMessage="Booking for 30 minutes at 12:30 pm on Thursday 10/24",
        stripe_key=os.getenv("STRIPE_KEY"),
        stripe_api=os.getenv("STRIPE_API"),
    ),
    html.Div(id='output')
])


@callback(Output('output', 'children'),
          [Input('input', 'paymentStatus'), Input('input', 'errorMessage'), Input('input', 'paymentIntentId'), Input('input', 'customConfirmMessage')])
def display_output(payment_status, error_message, payment_intent_id, confirm_message):
    if payment_status == 'success':
        return f'Payment Successful. Transaction ID: {payment_intent_id}'
    elif payment_status == 'payment_intent_success':
        return ""
    elif payment_status == 'payment_intent_error' or payment_status == 'error':
        # Handle complex error messages
        if isinstance(error_message, dict) and "detail" in error_message:
            details = error_message["detail"]
            if isinstance(details, list):
                # Extract messages from each error in the list and join them into a single string
                formatted_error = "; ".join([f"{err['msg']} at {'.'.join(map(str, err['loc']))}" for err in details])
                return f"Payment Failed. Details: {formatted_error}"
            else:
                return f"Payment Failed. Details: {details}"
        elif isinstance(error_message, list):
            formatted_error = "; ".join([f"{err['msg']} at {'.'.join(map(str, err['loc']))}" for err in error_message])
            return f"Payment Failed. Details: {formatted_error}"
        elif isinstance(error_message, str):
            return f"Payment Failed. Details: {error_message}"
        else:
            return "Payment Failed with unknown error."
    else:
        return "+++"

if __name__ == '__main__':
    app.run(debug=True)
