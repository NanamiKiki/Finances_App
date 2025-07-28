<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Personal Finance App - README</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

  body {
    background-color: #4b367c; /* purple background */
    color: #e0d9f2; /* light lavender text */
    font-family: 'Poppins', sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 2rem;
  }

  h1, h2, h3 {
    color: #d6bcfa; /* lighter lavender */
  }

  a {
    color: #c9a7ff;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }

  code {
    background-color: #6f57a1;
    color: #f0ebff;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: monospace;
  }

  pre {
    background-color: #6f57a1;
    color: #f0ebff;
    padding: 1rem;
    border-radius: 8px;
    overflow-x: auto;
  }

  hr {
    border: none;
    border-top: 1px solid #a28fed;
    margin: 2rem 0;
  }

  ul {
    padding-left: 1.5rem;
  }

  .container {
    max-width: 900px;
    margin: auto;
  }

  .highlight {
    color: #b794f4;
    font-weight: 600;
  }

  .metric {
    font-weight: 700;
    color: #d6bcfa;
  }

</style>
</head>
<body>
  <div class="container">
    <h1>Personal Finance App in Python with Streamlit</h1>
    <p>
      This is a web application for managing and analyzing personal finances, built with
      <span class="highlight">Streamlit</span>, <span class="highlight">Pandas</span>, and <span class="highlight">Plotly</span>.
      The app allows you to upload a CSV file with bank transactions, automatically or manually categorize expenses,
      visualize monthly spending and income trends, and display categorized amounts in an interactive and intuitive way.
    </p>

    <hr />

    <h2>Features</h2>
    <ul>
      <li>Upload CSV file with transactions (<code>Debit</code>/<code>Credit</code>).</li>
      <li>Automatic data cleaning and preprocessing (date format, amounts, etc.).</li>
      <li>Auto-categorization of transactions based on keywords in the details.</li>
      <li>Ability to add and edit categories and keywords directly in the interface.</li>
      <li>Visualization of monthly spending and income evolution with interactive line charts.</li>
      <li>Display of expenses by category as a pie chart.</li>
      <li>Custom styled UI with CSS and Google Fonts.</li>
      <li>Automatic saving of custom categories in a JSON file.</li>
    </ul>

    <hr />

    <h2>Technologies Used</h2>
    <ul>
      <li><a href="https://www.python.org/" target="_blank" rel="noopener noreferrer">Python 3.x</a></li>
      <li><a href="https://streamlit.io/" target="_blank" rel="noopener noreferrer">Streamlit</a> — fast Python web app framework</li>
      <li><a href="https://pandas.pydata.org/" target="_blank" rel="noopener noreferrer">Pandas</a> — data manipulation and analysis</li>
      <li><a href="https://plotly.com/python/plotly-express/" target="_blank" rel="noopener noreferrer">Plotly Express</a> — interactive visualizations</li>
      <li>JSON &amp; OS modules for local storage of categories</li>
    </ul>

    <hr />

    <h2>How to Use the App</h2>
    <ol>
      <li>
        Clone this repository locally:<br />
        <pre><code>git clone https://github.com/yourusername/personal-finance-app.git
cd personal-finance-app</code></pre>
      </li>
      <li>
        Install dependencies:<br />
        <pre><code>pip install streamlit pandas plotly</code></pre>
      </li>
      <li>
        Run the app:<br />
        <pre><code>streamlit run app.py</code></pre>
      </li>
      <li>
        Upload your bank transactions CSV file (make sure it includes: <code>Data</code>, <code>Detalii</code>, <code>Suma (RON)</code>, <code>Tip tranzacție</code> columns).
      </li>
      <li>Explore charts, edit categories, and monitor your expenses and income!</li>
    </ol>

    <hr />

    <h2>Expected CSV File Structure</h2>
    <table style="border-collapse: collapse; width: 100%;">
      <thead>
        <tr style="background-color: #6f57a1; color: #f0ebff;">
          <th style="border: 1px solid #a28fed; padding: 0.5rem;">Data</th>
          <th style="border: 1px solid #a28fed; padding: 0.5rem;">Detalii</th>
          <th style="border: 1px solid #a28fed; padding: 0.5rem;">Suma (RON)</th>
          <th style="border: 1px solid #a28fed; padding: 0.5rem;">Tip tranzacție</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background-color: #7e6baa;">
          <td style="border: 1px solid #a28fed; padding: 0.5rem;">01/07/2025</td>
          <td style="border: 1px solid #a28fed; padding: 0.5rem;">Grocery Store</td>
          <td style="border: 1px solid #a28fed; padding: 0.5rem;">150.00</td>
          <td style="border: 1px solid #a28fed; padding: 0.5rem;">Debit</td>
        </tr>
        <tr style="background-color: #6f57a1;">
          <td style="border: 1px solid #a28fed; padding: 0.5rem;">03/07/2025</td>
          <td style="border: 1px solid #a28fed; padding: 0.5rem;">Salary</td>
          <td style="border: 1px solid #a28fed; padding: 0.5rem;">5000.00</td>
          <td style="border: 1px solid #a28fed; padding: 0.5rem;">Credit</td>
        </tr>
      </tbody>
    </table>
    <p>
      <em>
        - <code>Data</code> in day/month/year format.<br />
        - <code>Detalii</code> describes the transaction (e.g., store, utilities).<br />
        - <code>Suma (RON)</code> may contain dots as thousand separators and commas as decimals.<br />
        - <code>Tip tranzacție</code> must be either <code>Debit</code> or <code>Credit</code>.
      </em>
    </p>

    <hr />

    <h2>Customizations &amp; Extensions</h2>
    <ul>
      <li>Add new categories and keywords in-app to improve auto-categorization.</li>
      <li>Categories are saved locally in <code>category_of_expenses.json</code> to persist between sessions.</li>
      <li>The UI is custom styled with CSS injected in Streamlit for a pleasant user experience.</li>
      <li>Charts use Plotly for modern interactivity and appearance.</li>
      <li>Code can be extended with PDF export, financial alerts, bank API integration, and more.</li>
    </ul>

    <hr />

    <h2>Inspiration</h2>
    <p>
      This app is inspired by
      <a href="https://www.youtube.com/watch?v=wqBlmAWqa6A" target="_blank" rel="noopener noreferrer">Tech With Tim’s tutorial</a> and his repo
      <a href="https://github.com/techwithtim/AutomateFinancesWithPython" target="_blank" rel="noopener noreferrer">AutomateFinancesWithPython</a>,
      adapted and extended with additional features and localization for Romanian language and UX.
    </p>

    <hr />

    <h2>License</h2>
    <p>
      The code is open-source and free to use and modify.<br />
      Please credit the original source if you use it in your projects.
    </p>

    <hr />

    <h2>Contact</h2>
    <p>
      For questions or suggestions, reach me at: <a href="mailto:your.email@example.com">your.email@example.com</a><br />
      Or open an issue in this repo.
    </p>
  </div>
</body>
</html>
