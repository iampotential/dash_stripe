# stripe_dash

`stripe_dash` is a Dash component library that integrates Stripe payment functionality into your Plotly Dash applications.

## Installation

To install the library, run:
```bash
pip install stripe-dash
```

## Stripe Credentials

You need two keys from Stripe to use this library:

- **Publishable Key**: Used on the frontend.
- **Secret Key**: Used on the backend. An example backend implementation is provided below.

Ensure these keys are securely stored, e.g., using environment variables.

## Basic Usage

Below is an example of using `stripe_dash` in a Dash app:

```python
import stripe_dash
from dash import Dash, callback, html, Input, Output
import os
import dash_mantine_components as dmc

app = Dash(__name__)

app.layout = dmc.MantineProvider([
    stripe_dash.StripeDash(
        id='input',
        label='Confirm Booking',
        paymentMethodId="asdfadfa",
        paymentStatus="asdfasdfa",
        paymentIntentId="",  
        paymentMethodDetails="",
        amount=5555,  # Amount in cents
        customConfirmMessage='hello world confirmation',
        prePaymentMessage="Booking for 30 minutes at 12:30 pm on Thursday 10/24",
        stripe_key=os.getenv("STRIPE_KEY"),  # Publishable key
        stripe_api=os.getenv("STRIPE_API"),  # Backend API endpoint for payment intent
        termsLink=html.Div([
            html.P("This keyword argument is optional. If provided, it will display a checkbox to acknowledge terms."),
            html.Link("Terms Link", href="https://example.com/terms")
        ])
    ),
    html.Div(id='output')
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

### Backend API

The `stripe_api` argument specifies the backend API endpoint where the payment intent is created. Below is an example implementation using FastAPI:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import stripe
from fastapi.middleware.cors import CORSMiddleware
import os

# Set your Stripe Secret Key
stripe.api_key = os.getenv('STRIPE_BE_KEY')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PaymentRequest(BaseModel):
    payment_method_id: str
    amount: int
    currency: str = "usd"
    reference_id: str = Field(default=None)

@app.post("/create-payment-intent/")
async def create_payment_intent(request: PaymentRequest):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=request.amount,
            currency=request.currency,
            payment_method=request.payment_method_id,
            confirm=True,
            metadata={"reference_id": request.reference_id} if request.reference_id else {},
            automatic_payment_methods={"enabled": True, "allow_redirects": "never"}
        )

        return {"status": "success", "payment_intent_id": payment_intent.id}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=f"Payment failed: {e.user_message}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
```

### Key Points:
1. Replace `os.getenv('STRIPE_BE_KEY')` with your Stripe Secret Key.
2. The backend API should handle creating payment intents and confirming payments.

## Features
- **Flexible Configuration**: Customize messages and payment details.
- **Secure Payments**: Offload sensitive operations to the backend.
- **Integration with Dash Mantine**: Leverage Mantine components for a modern UI.

## Notes
- Ensure your server is configured to handle HTTPS for secure payment processing.
- Test the integration in Stripe's test environment before deploying to production.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contribution
Contributions are welcome! Please open an issue or submit a pull request to improve the library.

