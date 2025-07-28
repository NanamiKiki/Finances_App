<div style="background: linear-gradient(135deg, #7b2ff7, #f107a3); padding: 2rem; border-radius: 10px; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">

<h1 style="text-align:center; font-weight: 700; margin-bottom: 0.2rem;">Personal Finance App with Streamlit</h1>

<p style="text-align:center; font-style: italic; margin-top: 0; margin-bottom: 2rem;">
  Manage and visualize your personal finances easily with Python, Streamlit, and Plotly.
</p>

---

<h2 style="color: #e0c3fc;">✨ Features</h2>
<ul>
  <li>Upload CSV files with Debit/Credit bank transactions</li>
  <li>Automatic data cleaning and preprocessing</li>
  <li>Auto-categorization of expenses based on keywords</li>
  <li>Add and edit categories and keywords in-app</li>
  <li>Interactive monthly spending and income charts with Plotly</li>
  <li>Pie chart showing expenses breakdown by category</li>
  <li>Custom styled UI with Google Fonts and purple-themed CSS</li>
  <li>Categories saved locally in JSON for persistence</li>
</ul>

---

<h2 style="color: #d4b9fc;">🚀 Getting Started</h2>
<pre style="background: #5c3db1; padding: 1rem; border-radius: 8px; overflow-x: auto;">
<code style="color: #f0e9ff;">
git clone https://github.com/yourusername/personal-finance-app.git
cd personal-finance-app
pip install streamlit pandas plotly
streamlit run app.py
</code>
</pre>

---

<h2 style="color: #d4b9fc;">📂 CSV File Format</h2>
<p>The CSV file should contain the following columns:</p>

<table style="width:100%; border-collapse: collapse; margin-bottom: 1rem;">
  <thead>
    <tr style="background-color: #6c4fd8; color: white;">
      <th style="padding: 8px; border: 1px solid #5c3db1;">Data</th>
      <th style="padding: 8px; border: 1px solid #5c3db1;">Detalii</th>
      <th style="padding: 8px; border: 1px solid #5c3db1;">Suma (RON)</th>
      <th style="padding: 8px; border: 1px solid #5c3db1;">Monedă</th>
      <th style="padding: 8px; border: 1px solid #5c3db1;">Tip tranzacție</th>
      <th style="padding: 8px; border: 1px solid #5c3db1;">Stare</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #8c68f9; color: white;">
      <td style="padding: 8px; border: 1px solid #5c3db1;">28.02.2025</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">Încasare card</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">"18.551,62"</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">RON</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">Credit</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">Decontată</td>
    </tr>
    <tr style="background-color: #9a7efc; color: white;">
      <td style="padding: 8px; border: 1px solid #5c3db1;">15.02.2025</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">ASIGURARE EUROINS</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">"137,95"</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">RON</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">Debit</td>
      <td style="padding: 8px; border: 1px solid #5c3db1;">Decontată</td>
    </tr>
  </tbody>
</table>

<p><i>Notes:</i></p>
<ul>
  <li><b>Data:</b> format day.month.year (e.g., 28.02.2025)</li>
  <li><b>Suma (RON):</b> decimal separator is comma, thousand separator is dot (e.g., "18.551,62")</li>
  <li><b>Tip tranzacție:</b> must be either <code>Debit</code> or <code>Credit</code></li>
  <li><b>Stare:</b> transaction status (e.g., Decontată)</li>
</ul>

---

<h2 style="color: #d4b9fc;">⚙️ Usage</h2>
<p>Upload your CSV file with transactions. The app will automatically clean and categorize your data. You can also add or edit categories and keywords to better fit your needs. Visualize your financial trends and get detailed breakdowns.</p>

---

<h2 style="color: #d4b9fc;">💡 Inspiration</h2>
<p>This project is inspired by <a href="https://www.youtube.com/watch?v=wqBlmAWqa6A" target="_blank" style="color:#f0e9ff; text-decoration: underline;">Tech With Tim's tutorial</a> and the <a href="https://github.com/techwithtim/AutomateFinancesWithPython" target="_blank" style="color:#f0e9ff; text-decoration: underline;">AutomateFinancesWithPython</a> repository, adapted with new features and Romanian localization.</p>

</div>
