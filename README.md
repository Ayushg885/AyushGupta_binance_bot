# AyushGupta_binance_bot

.

🚀 Binance Futures Trading Bot CLI

A menu-driven CLI trading bot for Binance USDT-M Futures supporting market, limit, stop-limit orders and basic automated strategies like Grid and TWAP, with proper validation and logging.

📌 Features

Check Futures USDT Balance

Place Market Orders

Place Limit Orders

Place Stop-Limit Orders

Grid Trading Strategy

TWAP Trading Strategy

Structured logging and error handling

⚙️ Requirements

Python 3.8 or higher

Binance account with USDT-M Futures enabled

Binance API Key & Secret

Internet connection

🛠 Setup Instructions

Clone the repository and install dependencies:

git clone <your-github-repo-url>
cd AyushGupta_binance_bot
pip install -r requirements.txt


Create a .env file in the project root:

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here


⚠️ Do not commit .env file to GitHub

▶️ How to Run the Bot

Start the interactive CLI:

python src/bot.py


You will see the following menu:

1. Check Balance
2. Place Market Order
3. Place Limit Order
4. Place Stop-Limit Order
5. Grid Trading Strategy
6. TWAP Trading Strategy
7. Exit

🧪 Example Usage

Check Futures Balance

Enter your choice: 1


Place Market Order

Enter your choice: 2
Enter the quantity for Market Order: 0.1


Place Limit Order

Enter your choice: 3
Enter quantity and price


Errors such as insufficient margin, invalid quantity, or price limits are handled gracefully and shown in the CLI.

📝 Logging

All bot activities are logged in:

bot.log


Logs include:

Binance connection status

Input validation results

Order placement details

API and runtime errors

ℹ️ Notes

Uses Binance Futures Testnet

Input validation for symbol, quantity, and price

Menu-based CLI (no command-line arguments required)

Designed for evaluation and educational purposes
