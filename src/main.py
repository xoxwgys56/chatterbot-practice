from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from loguru import logger

if __name__ == '__main__':

    # chatbot = ChatBot('Ron Obvious')

    # # Create a new trainer for the chatbot
    # trainer = ChatterBotCorpusTrainer(chatbot)

    # # Train the chatbot based on the english corpus
    # trainer.train("chatterbot.corpus.english")

    # # Get a response to an input statement
    # chatbot.get_response("Hello, how are you today?")

    bot = ChatBot(
        'Norman',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter',
        ],
        database_uri='sqlite:///database.sqlite3',
    )

    while True:
        try:
            logger.info('input text:')
            input_text = input()

            bot_input = bot.get_response(input_text)
            logger.info(bot_input)

        except (KeyboardInterrupt, EOFError, SystemExit):
            break
