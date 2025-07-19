import streamlit as st

st.set_page_config(page_title="Side Hustle Calculator", layout="centered")
st.title("🔧 Side Hustle Income & Time Calculator")
st.write("Estimate how much to charge and how many projects you need to reach your monthly goal.")


# MONEY INPUT FUNCTION (Comma Support)
# -----------------------------
def parse_money_input(label, help_text):
    value_str = st.text_input(label, placeholder="e.g. 200,000", help=help_text)
    value_str = value_str.replace(",", "").strip()
    try:
        return int(value_str) if value_str else 0
    except ValueError:
        st.warning("❗ Please enter a valid number (only digits and commas).")
        return 0
# -----------------------------
# USER INPUTS with Descriptions
# -----------------------------

current_job = st.text_input(
    "1. What do you currently do?",
    placeholder="e.g. Accountant, Student, Customer Service Rep"
)

target_work = st.text_input(
    "2. What kind of work do you want to earn income from?",
    placeholder="e.g. Graphic Design, Hair Styling, Copywriting"
)

monthly_income_goal = parse_money_input(
    "3. What is your ideal monthly income? (₦)",
    help_text="Think about the total amount you would love to earn each month from your side hustle or service."
)

monthly_expenses = parse_money_input(
    "4. Optional: Add your estimated monthly expenses (₦)",
    help_text="This helps the calculator recommend a price that covers your needs."
)

weekly_hours_available = st.slider(
    "5. How many hours per week can you realistically dedicate to this work?",
    1, 60, 10,
    help="Consider your current schedule. Be honest with the time you can consistently give."
)

project_duration_hours = st.number_input(
    "6. On average, how many hours does it take you to complete one project?",
    min_value=1,
    max_value=40,
    help="If one job/task takes you a full day (e.g. 5 hours), type that here."
)

# -----------------------------
# CALCULATIONS
# -----------------------------

monthly_hours_available = weekly_hours_available * 4
total_needed_income = monthly_income_goal + monthly_expenses

if monthly_hours_available == 0:
    st.warning("⛔ Please enter a valid number of weekly hours.")
elif project_duration_hours == 0:
    st.warning("⛔ Project duration must be greater than zero.")
elif total_needed_income == 0:
    st.info("Please enter an income goal or expense to proceed.")
else:
    try:
        hourly_rate = total_needed_income / monthly_hours_available
        project_price = hourly_rate * project_duration_hours

        # Round to nearest ₦100 for practical pricing
        rounded_hourly_rate = round(hourly_rate, -2)
        rounded_project_price = round(project_price, -2)

        projects_needed = total_needed_income / project_price
        weekly_hours_needed = (projects_needed * project_duration_hours) / 4

        # -----------------------------
        #  OUTPUTS
        # -----------------------------
        st.subheader("💡 Your Suggested Plan")
        st.write(f"📌 **Suggested Hourly Rate:** ₦{rounded_hourly_rate:,.0f}")
        st.write(f"📦 **Suggested Price per Project:** ₦{rounded_project_price:,.0f}")
        st.write(f"📈 **Projects Needed per Month:** {projects_needed:.1f}")
        st.write(f"🕒 **Weekly Hours Needed to Reach Goal:** {weekly_hours_needed:.1f} hrs/week")

        st.markdown("---")
        st.caption("This is a rough estimate based on your input and general patterns from similar side hustles. Adjust as needed based on your experience. And remember Consistency is key")

    except ZeroDivisionError:
        st.error("⚠️ Error: Make sure your inputs are not zero in any critical field like hours or income.")