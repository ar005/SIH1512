import telegram
from telegram.ext import Updater, CommandHandler
import pandas as pd
import schedule
import time

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = ''

# Global variable to store the previous node status
previous_node_status = {}

# Function to read node.csv
def read_node(update, context):
    try:
        # Read the node.csv file
        node_df = pd.read_csv('node.csv')

        # Initialize a message
        message = ""

        # Check the status of each node
        for i in range(1, 3):  # Two sets of nodes
            for j in range(1, 4):  # Three nodes in each set
                node_name = f'node_{i}_{j}'
                node_value = node_df[f'Value{i}_{j}'][0]
                if node_value == 0:
                    message += f'{node_name} is down.\n'

        if message:
            update.message.reply_text(message)
        else:
            update.message.reply_text("All nodes are up.")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")
        
def read_network(update, context):
    try:
        # Read the network.csv file
        network_df = pd.read_csv('network.csv')
        
        # Check if the first value is zero
        if network_df['Value1'][0] == 0:
            update.message.reply_text("Network One is down.")
        
        # Check if the second value is zero
        if network_df['Value2'][0] == 0:
            update.message.reply_text("Network Two is down.")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")
        
        

# Function to periodically check the node status
def check_node_status():
    try:
        # Read the node.csv file
        node_df = pd.read_csv('node.csv')

        # Check the status of each node
        for i in range(1, 3):  # Two sets of nodes
            for j in range(1, 4):  # Three nodes in each set
                node_name = f'node_{i}_{j}'
                node_value = node_df[f'Value{i}_{j}'][0]
                if node_name not in previous_node_status:
                    previous_node_status[node_name] = -1
                if node_value == 0 and previous_node_status[node_name] != 0:
                    send_status_update(f'{node_name} is down.')
                previous_node_status[node_name] = node_value
    except Exception as e:
        print(f"An error occurred while checking node status: {str(e)}")

# Function to send status updates to Telegram
def send_status_update(message):
    updater = Updater(token=BOT_TOKEN)
    bot = updater.bot
    chat_id = ''  # Replace with your chat ID
    bot.send_message(chat_id=chat_id, text=message)

def main():
    # Initialize the Telegram bot
    bot = telegram.Bot(token=BOT_TOKEN)
    #updater = Updater(token=BOT_TOKEN, use_context=True)
    updater = Updater(bot=bot, use_context=True)
    dispatcher = updater.dispatcher
    
    # Define a command to read network.csv
    dispatcher.add_handler(CommandHandler('read_network', read_network))

    # Define a command to read node.csv
    dispatcher.add_handler(CommandHandler('read_node', read_node))

    # Define a command to check network status
    dispatcher.add_handler(CommandHandler('network', check_network_status))

    # Define a command to check node status
    dispatcher.add_handler(CommandHandler('node', check_node_status))

    # Schedule the periodic node status check
    schedule.every(5).minutes.do(check_node_status)

    # Start the bot
    updater.start_polling()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
