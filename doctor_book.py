from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot('jarvis',logic_adapters=['chatterbot.logic.BestMatch'])
trainer=ListTrainer(bot)

trainer.train([
    'i want to book a appointment',
    'ok, which doctor you want to make an appointment with?',
    'I want to make an appointment with the Dentist doctor',
    'Sure, Here are the available doctors for dentist, please choose a doctor: 1. Dr.Shilpa\n 2. Dr.Bindu\n 3. Dr.Manju',
    'Dr.Shilpa',
    'ok, she is a great doctor, when you want to book the appointment.',
    'tomorrow morning',
    'ok sir, can i know the patient name?',
    'amal',
    'ok, sir, i am going to book the appointment for tomorrow morning to Dr.Shilpa',
    'okay',
    'sir for appointment you have to pay 200 rupees in advance'
    'ok i will do that'
    'what is the payment method sir?',
    'what are the payment methods you have?',
    'debit card' 'upi',
    'ok i will choose upi',
    'you will recive a payment confirmation on gpay, please confir your payment and reply as done',
    'done',
    'ok sir, we have booked your appointment tomorrow morning to Dr.Manju, you will recieve text message shortly, thank you'

])

trainer.train([
    'Dr.Shilpa',
    'ok, she is a great doctor, when you want to book the appointment.'
])

trainer.train([
    'ok i will choose upi',
    'please provide your upi number',
    'abcd@oksbi',
])


name=input('enter your name:')
print('Welcome to MIMS Hospital, How can i help you')


while True:
    request=input(name+":")

    if request=='bye':
        print('bot:bye')
        break


    else:
        response=bot.get_response(request)
        print('bot:',response)