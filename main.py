import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

# Stilizare personalizată cu CSS pentru aplicație
# Custom CSS styling for the app
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Fundal aplicație / App background */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1751378639257-0aca1af0089b?q=80&w=2605&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 2rem;
    }

    /* Text alb peste tot / White text everywhere */
    html, body, [class*="st-"] {
        color: #ffffff !important;
        font-family: 'Poppins', sans-serif;
    }

    /* Stilizare tab-uri / Tabs styling */
    .stTabs [role="tab"] {
        background-color: #1f3b57 !important;
        color: white !important;
        border-radius: 10px 10px 0 0;
        margin-right: 5px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #3973ac !important;
        color: #ffffff !important;
    }

    /* Stilizare butoane primare / Primary buttons styling */
    button[kind="primary"] {
        background-color: #4b8bd4 !important;
        color: white !important;
        border-radius: 6px;
    }

    /* Stilizare inputuri, upload, metrici / Inputs, upload, metrics styling */
    .stTextInput > div > div > input,
    .stSelectbox > div,
    .stFileUploader > div {
        background-color: #2d4868 !important;
        color: white !important;
        border-radius: 6px;
        border: none;
    }

    .stMetricLabel, .stMetricValue {
        color: white !important;
    }
    </style>

    <div class="main-container">
    """,
    unsafe_allow_html=True
)

# Configurarea paginii: titlu, icon, layout
# Page configuration: title, icon, layout
st.set_page_config(page_title="Aplicație pentru finanțe personale", page_icon="🪙", layout="wide")

category_file = "category_of_expenses.json"  # Fișier pentru salvarea categoriilor / File to save categories

# Inițializare categorii în sesiune dacă nu există deja
# Initialize categories in session state if not present
if "categories" not in st.session_state:
    st.session_state.categories = {
        "Fără categorie": [],  # Categoria implicită / Default category
    }

# Încarcă categoriile salvate dacă există fișierul
# Load saved categories from file if exists
if os.path.exists(category_file):
    with open(category_file, "r") as f:
        st.session_state.categories = json.load(f)

# Funcție pentru salvarea categoriilor în fișier JSON
# Function to save categories to JSON file
def save_categories():
    with open(category_file, "w") as f:
        json.dump(st.session_state.categories, f)

# Funcție pentru auto-categorizarea tranzacțiilor după cuvinte cheie
# Function to auto-categorize transactions based on keywords
def categorize_transactions(df):
    df["Categorie"] = "Fără categorie"  # Inițializare categorie implicită / Default category init

    for category, keywords in st.session_state.categories.items():
        if category == "Fără categorie" or not keywords:
            continue  # Saltă categoria fără cuvinte cheie / Skip if no keywords or default category

        lowered_keywords = [keyword.lower().strip() for keyword in keywords]

        for idx, row in df.iterrows():
            details = row["Detalii"].lower().strip()
            if details in lowered_keywords:
                df.at[idx, "Categorie"] = category  # Atribuie categoria corespunzătoare / Assign matching category

    return df  

# Funcție pentru încărcarea și procesarea fișierului CSV de tranzacții
# Function to load and preprocess transactions CSV file
def load_tranzactii(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]  # Curăță numele coloanelor / Strip column names
        df["Data"] = pd.to_datetime(df["Data"], dayfirst=True, errors="coerce")  # Convert date format
        df["Suma (RON)"] = (
            df["Suma (RON)"]
            .astype(str)
            .str.replace(r"\.", "", regex=True)         # Elimină punctele - separator mii / Remove thousand separators
            .str.replace(",", ".", regex=False)         # Schimbă virgula cu punct pentru zecimale / Comma to dot decimals
            .str.replace(r"\s+", "", regex=True)        # Elimină spațiile / Remove spaces
            .astype(float)
        )
        # Format frumos pentru sume (cu spațiu ca separator de mii)
        # Nicely formatted sums (space as thousand separator)
        df["Suma primită(RON)"] = df["Suma (RON)"].apply(lambda x: f"{x:,.2f}".replace(",", " "))

        return categorize_transactions(df)  # Categorizare automată / Auto categorization

    except Exception as e:
        st.error(f"Eroare la procesarea fișierului: {str(e)}")  # Afișare eroare / Show error
        return None

# Funcție pentru adăugarea unui cuvânt cheie la o categorie existentă
# Function to add a keyword to an existing category
def add_keyword_to_category(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()  # Salvează modificările / Save changes
        return True
    return False

def main():
    st.title("Panou Finanțe Personale")  # Titlu aplicație / App title

    uploaded_file = st.file_uploader("Încarcă fișierul de tranzacții CSV", type=["csv"])  # Încărcare fișier / File uploader

    if uploaded_file is not None:
        df = load_tranzactii(uploaded_file)  # Încarcă și preprocesează fișierul

        if df is not None:
            st.success("Fișier încărcat cu succes!")  # Confirmare succes / Success message
            debits_df = df[df["Tip tranzacție"] == "Debit"].copy()
            credits_df = df[df["Tip tranzacție"] == "Credit"].copy()

            st.session_state.debits_df = debits_df.copy()

            # Grafic evoluție lunară a cheltuielilor și încasărilor
            # Monthly evolution chart of expenses and income
            df['AnLuna'] = df['Data'].dt.to_period('M').astype(str)  # Ex: '2025-07'

            monthly_summary = df.groupby(['AnLuna', 'Tip tranzacție'])['Suma (RON)'].sum().reset_index()
            monthly_pivot = monthly_summary.pivot(index='AnLuna', columns='Tip tranzacție', values='Suma (RON)').fillna(0)
            monthly_pivot = monthly_pivot.sort_index()
            monthly_pivot.index = pd.to_datetime(monthly_pivot.index)

            fig2 = px.line(
                monthly_pivot,
                x=monthly_pivot.index,
                y=['Debit', 'Credit'],
                labels={'Tip plată': 'Sumă (RON)', 'AnLuna': 'Lună'},
                title='Evoluția sumelor cheltuite și încasate pe luni',
            )
            fig2.update_layout(
                xaxis_title='Lună',
                yaxis_title='Sumă (RON)',
                legend_title_text='Tip tranzacție',
                hovermode='x unified'
            )

            st.plotly_chart(fig2, use_container_width=True)

            tab1, tab2 = st.tabs(["Scade sold (Debit)", "Crește sold (Credit)"])
            with tab1:
                new_category = st.text_input("Categorie nouă")  # Input pentru categorie nouă / New category input
                add_button = st.button("Adaugă categoria")    # Buton adăugare categorie / Add category button

                if add_button and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.success(f'Categoria „{new_category}” a fost adăugată cu succes!')
                        st.experimental_rerun()  # Reîncarcă aplicația / Rerun app

                st.subheader("Rezumat Cheltuieli")  # Subtitlu pentru cheltuieli / Expenses summary
                
                editor_df = st.session_state.debits_df.copy()
                editor_df["Suma formatată"] = editor_df["Suma (RON)"].apply(
                    lambda x: f"{x:,.2f}".replace(",", " ")
                )

                # Editor tabel pentru categorisire manuală / Editable table for manual categorization
                edited_df = st.data_editor(
                    editor_df[["Data", "Detalii", "Suma formatată", "Categorie"]],
                    column_config={
                        "Data": st.column_config.DateColumn("Data", format="DD/MM/YYYY"),
                        "Suma formatată": st.column_config.TextColumn("Suma (RON)", disabled=True),
                        "Categorie": st.column_config.SelectboxColumn(
                            "Categorie",
                            options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )
                st.subheader('Sume cheltuieli')  # Subtitlu pentru sumar cheltuieli / Expense sums summary
                refreshed_df = st.session_state.debits_df.copy()

                category_totals = st.session_state.debits_df.groupby("Categorie")["Suma (RON)"].sum().reset_index()
                category_totals = category_totals.sort_values("Suma (RON)", ascending=False)

                category_totals["Suma (RON)"] = category_totals["Suma (RON)"].apply(
                    lambda x: f"{x:,.2f}".replace(",", " ")
                )
                st.dataframe(
                    category_totals,
                    column_config={
                        "Suma (RON)": st.column_config.TextColumn("Suma (RON)")
                    },
                    use_container_width=True,
                    hide_index=True
                )
            save_button = st.button("Actualizează", type="primary")  # Buton salvare modificări / Save changes button
            if save_button:
                for idx, row in edited_df.iterrows():
                    new_category = row["Categorie"]
                    old_category = st.session_state.debits_df.at[idx, "Categorie"]
                    details = row["Detalii"].strip()

                    if new_category != old_category:
                        # Actualizează categoria în dataframe / Update category in dataframe
                        st.session_state.debits_df.at[idx, "Categorie"] = new_category

                        # Elimină detaliul din celelalte categorii / Remove detail from other categories
                        for cat, keywords in st.session_state.categories.items():
                            if details in keywords and cat != new_category:
                                keywords.remove(details)

                        # Adaugă detaliul la noua categorie / Add detail to new category
                        if new_category != "Fără categorie":
                            add_keyword_to_category(new_category, details)

                save_categories()
                st.success("Modificările au fost aplicate cu succes!")  # Confirmare aplicare / Success message

            # Grafic cheltuieli pe categorii / Pie chart expenses by category
            category_totals_numeric = st.session_state.debits_df.groupby("Categorie")["Suma (RON)"].sum().reset_index()

            fig = px.pie(
                category_totals_numeric,
                values="Suma (RON)",
                names="Categorie",
                title="Cheltuieli pe categorie",
                hole=0.3
            )
            fig.update_traces(textinfo="label+percent", textposition="inside")
            st.plotly_chart(fig, use_container_width=True)

            with tab2:
                st.subheader("Rezumat Încasări")  # Subtitlu pentru încasări / Income summary

                total_payments = credits_df["Suma (RON)"].sum()
                formatted_total = f"{total_payments:,.2f}".replace(",", " ")
                st.metric("Total", f"{formatted_total} RON")

                credits_df["Suma formatată"] = credits_df["Suma (RON)"].apply(lambda x: f"{x:,.2f}".replace(",", " "))

                st.dataframe(
                    credits_df[["Data", "Detalii", "Suma formatată"]],
                    column_config={
                        "Data": st.column_config.DateColumn("Data", format="DD/MM/YYYY"),
                        "Suma formatată": st.column_config.TextColumn("Suma (RON)"),
                    },
                    use_container_width=True,
                    hide_index=True
                )

main()
