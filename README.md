# 💰 Python Finance Tracker

A simple command-line based personal finance tracker built using Python. It allows users to add transactions, view filtered reports based on date range, and visualize income vs expenses over time using plots.

## 📌 Features

- Add and store financial transactions in a CSV file
- Categorize entries as **Income** or **Expense**
- Filter and display transactions between two dates
- View summary statistics (total income and expenses)
- Plot income and expense trends using **Matplotlib** and **Seaborn**

## 🛠️ Technologies Used

- Python 🐍
- pandas
- matplotlib
- seaborn
- CSV for data storage (no database needed)

## 📁 File Structure

```
.
├── main.py                # Main application entry point
├── data_entry.py          # Handles user input (functions like get_date, get_description, etc.)
├── Finance_data.csv       # Stores all transaction data
```

## ▶️ How to Use

1. Clone this repository:

```bash
git clone https://github.com/yourusername/finance-tracker.git
cd finance-tracker
```

2. Install dependencies:

```bash
pip install pandas matplotlib seaborn
```

3. Run the tracker:

```bash
python main.py
```

4. Choose one of the options:

- `1` – Add a new entry
- `2` – Get transactions in a date range (and optionally plot)
- `3` – Exit

## ✅ Sample Data Format (CSV)

```csv
Date,Description,Amount,Category
01-06-2024,Salary,50000,Income
05-06-2024,Groceries,-2000,Expense
10-06-2024,Freelance Project,8000,Income
```

## 🧠 Future Enhancements

- Add category-specific summaries
- Export graphs as images
- Add monthly budgets
- Add support for recurring transactions
- Web-based or GUI version (using streamlit)
- Implement the ML concept on the data that we get and in future provide some more info in the future.

## 🙋‍♂️ Author

**Aditya Kaushal**  
