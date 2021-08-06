from chatterbot import ChatterBot
from chatterbot.trainers import ListTrainer

if __name__ == '__main__':

    conversation = [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I'm doing great.",
        "That is good to hear",
        "Thank you.",
        "You're welcome.",
    ]

    chatbot = ChatterBot('chatbot')
    trainer = ListTrainer(chatbot)

    trainer.train(conversation)

    response = chatbot.get_response("Good morning!")
    print(response)
