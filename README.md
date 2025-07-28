Personal Finance App in Python with Streamlit
This is a web application for managing and analyzing personal finances, built with Streamlit, Pandas, and Plotly. The app allows you to upload a CSV file with bank transactions, automatically or manually categorize expenses, visualize monthly spending and income trends, and display categorized amounts in an interactive and intuitive way.

Demo

(Add your app screenshot or a demo link)

Features
Upload CSV file with transactions (Debit/Credit).

Automatic data cleaning and preprocessing (date format, amounts, etc.).

Auto-categorization of transactions based on keywords in the details.

Ability to add and edit categories and keywords directly in the interface.

Visualization of monthly spending and income evolution with interactive line charts.

Display of expenses by category as a pie chart.

Custom styled UI with CSS and Google Fonts.

Automatic saving of custom categories in a JSON file.

Technologies Used
Python 3.x

Streamlit — fast Python web app framework

Pandas — data manipulation and analysis

Plotly Express — interactive visualizations

JSON & OS modules for local storage of categories

How to Use the App
Clone this repository locally:

bash
Copiază
Editează
git clone https://github.com/yourusername/personal-finance-app.git
cd personal-finance-app
Install dependencies:

bash
Copiază
Editează
pip install streamlit pandas plotly
Run the app:

bash
Copiază
Editează
streamlit run app.py
Upload your bank transactions CSV file (make sure it includes: Data, Detalii, Suma (RON), Tip tranzacție columns).

Explore charts, edit categories, and monitor your expenses and income!

Expected CSV File Structure
Data	Detalii	Suma (RON)	Tip tranzacție
01/07/2025	Grocery Store	150.00	Debit
03/07/2025	Salary	5000.00	Credit
...	...	...	...

Data in day/month/year format.

Detalii describes the transaction (e.g., store, utilities).

Suma (RON) may contain dots as thousand separators and commas as decimals.

Tip tranzacție must be either Debit or Credit.

Customizations & Extensions
Add new categories and keywords in-app to improve auto-categorization.

Categories are saved locally in category_of_expenses.json to persist between sessions.

The UI is custom styled with CSS injected in Streamlit for a pleasant user experience.

Charts use Plotly for modern interactivity and appearance.

Code can be extended with PDF export, financial alerts, bank API integration, and more.

Inspiration
This app is inspired by Tech With Tim’s tutorial and his repo AutomateFinancesWithPython, adapted and extended with additional features and localization for Romanian language and UX.
