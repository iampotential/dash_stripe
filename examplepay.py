from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import stripe
from fastapi.middleware.cors import CORSMiddleware

import os

from datetime import datetime,timedelta



stripe.api_key = os.environ['STRIPE_BE_KEY']


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


# Payment intent endpoint
@app.post("/create-payment-intent/")
async def create_payment_intent(request: PaymentRequest):
    try:
      
        payment_intent = stripe.PaymentIntent.create(
            amount=request.amount,
            currency=request.currency,
            payment_method=request.payment_method_id,
            confirm=True,
            metadata={"reference_id": request.reference_id} if request.reference_id else {},
            automatic_payment_methods={
                "enabled": True,
                "allow_redirects": "never"
            }
        )

        return {"status": "success", "payment_intent_id": payment_intent.id}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=f"Payment failed: {e.user_message}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
