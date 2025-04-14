import streamlit as st

st.set_page_config(page_title="Salary Calculator", layout="wide")

st.title("📊 Salary Calculator App")

years = st.multiselect("Select Years", options=[2023, 2024, 2025, 2026, 2027], default=[2025])

for year in years:
    st.header(f"Year: {year}")

    with st.form(key=f"salary_form_{year}"):
        basic_salary = st.number_input(f"Basic Salary for {year} (PKR)", min_value=0.0, step=1000.0)
        cola_percentage = st.number_input(f"COLA % for {year}", min_value=0.0, max_value=100.0, value=0.0)

        # Predefined Calculations
        housing_rent = 0.45 * basic_salary
        utility = 0.10 * basic_salary
        cola = (cola_percentage / 100) * basic_salary

        st.subheader("Additional Income")
        add_income_titles = []
        add_income_values = []

        with st.expander("➕ Add Additional Income Fields"):
            num_income_fields = st.number_input(f"How many additional income items for {year}?", min_value=0, max_value=10, value=0, key=f"income_{year}")
            for i in range(int(num_income_fields)):
                col1, col2 = st.columns(2)
                with col1:
                    title = st.text_input(f"Title {i+1}", key=f"income_title_{year}_{i}")
                with col2:
                    amount = st.number_input(f"Amount {i+1}", min_value=0.0, step=100.0, key=f"income_amount_{year}_{i}")
                add_income_titles.append(title)
                add_income_values.append(amount)

        st.subheader("Salary Deductions")
        deduction_titles = []
        deduction_values = []

        with st.expander("➖ Add Deduction Fields"):
            num_deduction_fields = st.number_input(f"How many deductions for {year}?", min_value=0, max_value=10, value=0, key=f"deduction_{year}")
            for i in range(int(num_deduction_fields)):
                col1, col2 = st.columns(2)
                with col1:
                    title = st.text_input(f"Deduction Title {i+1}", key=f"deduct_title_{year}_{i}")
                with col2:
                    amount = st.number_input(f"Deduction Amount {i+1}", min_value=0.0, step=100.0, key=f"deduct_amount_{year}_{i}")
                deduction_titles.append(title)
                deduction_values.append(amount)

        submitted = st.form_submit_button("Calculate")

        if submitted:
            total_income = basic_salary + housing_rent + utility + cola + sum(add_income_values)
            total_deductions = sum(deduction_values)
            net_salary = total_income - total_deductions

            st.success(f"💰 Total Income for {year}: PKR {total_income:,.2f}")
            st.info(f"📉 Total Deductions: PKR {total_deductions:,.2f}")
            st.success(f"🧾 Net Salary for {year}: PKR {net_salary:,.2f}")

