import telegram
from telegram.ext import Updater, CommandHandler
import pandas as pd

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = ''

# Function to read network.csv and return network information
def read_network(update, context):
    try:
        # Read the network.csv file with no header
        network_df = pd.read_csv('network.csv', header=None)
        
        # Check the status of the first and second values
        value1 = network_df.iloc[0, 0]
        value2 = network_df.iloc[0, 1]

        # Construct the network status message
        status_message = ""
        
        if value1 == 0:
            status_message += "Network One is down.\n"
        if value2 == 0:
            status_message += "Network Two is down.\n"
        
        # Send the network status message as a reply
        if status_message:
            update.message.reply_text(status_message)
        else:
            update.message.reply_text("Both networks are up.")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")

# Function to read node.csv and return node information
def read_node(update, context):
    try:
        # Read the node.csv file with no header
        node_df = pd.read_csv('node.csv', header=None)

        # Initialize a message
        message = "Node Status:\n"

        # Check the status of each node
        for i in range(1, 3):  # Two sets of nodes
            for j in range(1, 4):  # Three nodes in each set
                node_name = f'node_{i}_{j}'
                node_value = node_df.iloc[0, (i - 1) * 3 + (j - 1)]
                if node_value == 0:
                    message += f'{node_name} is down\n'
                else:
                    message += f'{node_name} is up\n'

        # Send the node status message as a reply
        update.message.reply_text(message)
    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")

def main():
    # Initialize the Telegram bot
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Define a command to read network.csv
    dispatcher.add_handler(CommandHandler('network', read_network))

    # Define a command to read node.csv
    dispatcher.add_handler(CommandHandler('node', read_node))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
