import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# 🏷️ App Title
# ------------------------------
st.set_page_config(page_title="Insurance Dashboard", layout="wide")
st.title("🏥 Insurance Data Dashboard")

# ------------------------------
# 📂 Load Dataset
# ------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("insurance.csv")
    return df

df = load_data()

# ------------------------------
# 🧭 Sidebar Navigation
# ------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["📊 Dashboard", "💰 Insurance Money Predictor"])

# ------------------------------
# 📊 DASHBOARD PAGE
# ------------------------------
if page == "📊 Dashboard":
    st.header("📈 Insurance Data Overview")

    st.write("Here’s a quick look at the dataset:")
    st.dataframe(df.head())

    # Summary stats
    st.subheader("📋 Summary Statistics")
    st.write(df.describe())

    # Visualizations
    st.subheader("🎨 Visual Insights")

    # Charges distribution
    st.write("#### Distribution of Insurance Charges")
    fig, ax = plt.subplots()
    ax.hist(df['charges'], bins=30)
    ax.set_xlabel("Charges")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # Region-wise average charges
    st.write("#### Average Charges by Region")
    region_avg = df.groupby("region")["charges"].mean().sort_values()
    st.bar_chart(region_avg)

# ------------------------------
# 💰 INSURANCE MONEY PREDICTOR PAGE
# ------------------------------
elif page == "💰 Insurance Money Predictor":
    st.header("💰 Predict Future Insurance Value")

    st.markdown("Estimate how your insurance amount grows over time with compound interest.")

    # User inputs
    current_amount = st.number_input("Enter your current insurance amount (₹):", min_value=0.0, step=100.0)
    interest_rate = st.number_input("Enter the annual interest rate (%):", min_value=0.0, step=0.1)
    years = st.slider("Select number of years:", 1, 30, 5)

    # Prediction
    if st.button("Predict Future Value"):
        if current_amount == 0 or interest_rate == 0:
            st.warning("Please enter a valid amount and interest rate.")
        else:
            future_value = current_amount * ((1 + interest_rate / 100) ** years)
            st.success(f"💹 Your insurance value after {years} years will be approximately ₹{future_value:,.2f}")

            # Growth percentage
            growth = ((future_value / current_amount - 1) * 100)
            st.metric(label="Total Growth", value=f"{growth:.2f}%")

            # Chart
            years_list = list(range(1, years + 1))
            values = [current_amount * ((1 + interest_rate / 100) ** y) for y in years_list]
            df_chart = pd.DataFrame({"Year": years_list, "Predicted Value": values})
            st.line_chart(df_chart.set_index("Year"))

# ------------------------------
# Footer
# ------------------------------
st.sidebar.markdown("---")
st.sidebar.info("Developed with ❤️ using Streamlit")
