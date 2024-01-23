from django.shortcuts import render

# Create views here.

from .models import Transaction, Payment
from .utils import setup_openai_api_key # import setup function
import stripe
import openai

stripe.api_key = 'your-stripe-secret-key'
setup_openai_api_key() # Call the function to set up the OpenAI API key


# existing views here...

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'payment_gateway/transaction_list.html', {'transactions': transactions})


def make_payment(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']

        # Charge the user's card using Stripe
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=int(float(amount) * 100),  # Amount is in cents
                currency='usd',
                description=description,
            )

            # Save the payment information in your database
            Payment.objects.create(amount=amount, description=description, stripe_payment_id=payment_intent.id)

            return render(request, 'payment_gateway/payment_confirmation.html', {'payment': Payment})
        except stripe.error.CardError as e:
            # Display error to user
            return render(request, 'payment_gateway/payment_form.html', {'error': str(e)})

    return render(request, 'payment_gateway/payment_form.html')


def chat_assistant(request):
    if request.method == 'POST':
        user_question = request.POST['user_question']

        # Use ChatGPT API to get a response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"User: {user_question}\nAssistant:",
            temperature=0.7,
            max_tokens=150,
            n=1,
        )

        assistant_reply = response['choices'][0]['text']

        return render(request, 'payment_gateway/chat_response.html', {'user_question': user_question, 'assistant_reply': assistant_reply})

    return render(request, 'payment_gateway/chat_form.html')
