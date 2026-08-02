# ATM Simulator

A Python command-line application that simulates basic ATM banking operations — balance inquiry, cash withdrawal, deposit, and PIN authentication.

## Features

- PIN-based login/authentication
- Check account balance
- Deposit money
- Withdraw money (with insufficient-balance handling)
- Change PIN
- Transaction history log
- Input validation (invalid PIN, negative amounts, etc.)

## Demo

```
--- Welcome to the ATM ---
Enter your PIN: 1234
Login successful!

1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Transaction History
6. Exit

Select an option: 3
Enter amount to withdraw: 500
Withdrawal successful. New balance: ₹4500

Select an option: 1
Current Balance: ₹4500
```

## How It Works

1. User enters their PIN to authenticate
2. On successful login, a menu of banking operations is displayed
3. Each operation (deposit/withdraw/balance check) updates the account state
4. Withdrawals are validated against the current balance
5. All transactions are optionally logged and viewable via a history option

## Getting Started

### Prerequisites
- Python 3.x
- (Add here if used: a file/database like SQLite for persistent account storage)

### Installation
```bash
git clone https://github.com/vanshhiiikaa/ATM-Simulator.git
cd ATM-Simulator
```

### Usage
```bash
python atm_simulator.py
```
Then enter your PIN and follow the on-screen menu.

## Tech Stack
- Python 3
- (Add: SQLite/file handling if balance/PIN persist between runs)

## Possible Improvements
- [ ] Persist account data between sessions (file or database, if not already done)
- [ ] Support multiple user accounts
- [ ] Lock account after repeated failed PIN attempts
- [ ] Add a GUI using Tkinter
- [ ] Add unit tests

## Author
**Vanshika**
- GitHub: [@vanshhiiikaa](https://github.com/vanshhiiikaa)
- LinkedIn: [Vanshika Gupta](https://www.linkedin.com/in/vanshika-gupta-4a2002329)

## License
This project is open source and available under the [MIT License](LICENSE).
