"""Telecom Marketing Campaign Optimizer (Streamlit app).

Run from the app/ folder:
    streamlit run Home.py

Upload a scored customer file (see sample_data/telco_scored_customers.csv, or the file
exported by notebook 03). Required columns include CustomerID, tenure, MonthlyCharges,
Contract, InternetService, PaymentMethod, OnlineSecurity, TechSupport, StreamingTV,
StreamingMovies, ChurnRiskLabel, ClusterCategory and "General marketing approach".
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
from marketing_strategies import MARKETING_STRATEGIES
from segment_report import generate_segment_report


# Page Configuration
st.set_page_config(
    page_title="Telecom Marketing Optimization System",
    page_icon="📱",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stAlert { 
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.5rem;
    }
    .dataframe { margin-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("📱 Telecom Marketing Campaign Optimizer ")
st.markdown("""
    > *"Turn Data into Customer Retention, Transform Insights into Growth!"*
""")


# Sidebar
with st.sidebar:
    st.header("Data Controls")
    
    uploaded_file = st.file_uploader("Upload your customer data (CSV)", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        st.subheader("Filter Options")
        churn_risk = st.selectbox(
            "Churn Risk Level",
            ["ALL"] + list(df["ChurnRiskLabel"].unique())
        )
        
        customer_value = st.selectbox(
            "Customer Value Segment",
            ["ALL"] + list(df["ClusterCategory"].unique())
        )
        
        st.subheader("Data Preview Options")
        show_preprocessed = st.checkbox("Show Preprocessed Data", False)
        
        st.subheader("Download Options")
        st.download_button(
            "Download Preprocessed Data",
            data=df.to_csv(index=False),
            file_name="preprocessed_telecom_data.csv",
            mime="text/csv"
        )
        
        # Add segment report download button if specific segment is selected
        if churn_risk != "ALL" and customer_value != "ALL":
            st.markdown("### Segment Report")
            # Filter data for the report
            filtered_df = df.copy()
            filtered_df = filtered_df[
                (filtered_df["ChurnRiskLabel"] == churn_risk) & 
                (filtered_df["ClusterCategory"] == customer_value)
            ]
            report_text = generate_segment_report(filtered_df, df, churn_risk, customer_value)
            st.download_button(
                label="📊 Download Segment Report",
                data=report_text,
                file_name=f"telecom_report_{churn_risk}_{customer_value}.txt",
                mime="text/plain",
                help="Download detailed analysis for the selected segment"
            )


# Main Content
if 'df' in locals():
    # Filter data
    filtered_df = df.copy()
    if churn_risk != "ALL":
        filtered_df = filtered_df[filtered_df["ChurnRiskLabel"] == churn_risk]
    if customer_value != "ALL":
        filtered_df = filtered_df[filtered_df["ClusterCategory"] == customer_value]
    
    # Key Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Customers", len(filtered_df))
    with col2:
        st.metric("Total Monthly Charges", f"${filtered_df['MonthlyCharges'].sum():,.2f}")
    with col3:
        st.metric("Average Tenure (months)", f"{filtered_df['tenure'].mean():.1f}")
    
    # Collapsible Data Preview
    with st.expander("Click to view Data Preview"):
        if show_preprocessed:
            df_processed = filtered_df.drop(columns=['CustomerID'])
            le = LabelEncoder()
            for col in df_processed.select_dtypes(include=['object']):
                df_processed[col] = le.fit_transform(df_processed[col])
            st.dataframe(df_processed, height=300)
        else:
            st.dataframe(filtered_df, height=300)

    if churn_risk == "ALL" and customer_value == "ALL":
        # ALL + ALL view
        st.subheader("Overall Business Overview")
        
        col1, col2 = st.columns(2)
        with col1:
            # Churn Risk Distribution
            fig_churn = px.pie(
                df, 
                names="ChurnRiskLabel",
                title="Overall Churn Risk Distribution"
            )
            st.plotly_chart(fig_churn, use_container_width=True)
            
            # Customer Value Distribution
            fig_value = px.pie(
                df,
                names="ClusterCategory",
                title="Customer Value Distribution"
            )
            st.plotly_chart(fig_value, use_container_width=True)
        
        with col2:
            # Marketing Approach Distribution
            fig_marketing = px.pie(
                df,
                names="General marketing approach",
                title="Marketing Approach Distribution"
            )
            st.plotly_chart(fig_marketing, use_container_width=True)
            
            # Revenue Trend
            fig_revenue = px.line(
                df.groupby('tenure')['MonthlyCharges'].mean().reset_index(),
                x='tenure',
                y='MonthlyCharges',
                title="Average Revenue by Tenure"
            )
            st.plotly_chart(fig_revenue, use_container_width=True)
    
    else:
        # Filtered view
        st.subheader("Segment Analysis")
        
        # Charts
        col1, col2 = st.columns(2)
        with col1:
            fig_contract = px.pie(
                filtered_df,
                names="Contract",
                title="Contract Distribution"
            )
            st.plotly_chart(fig_contract, use_container_width=True)
            
            fig_internet = px.pie(
                filtered_df,
                names="InternetService",
                title="Internet Service Distribution"
            )
            st.plotly_chart(fig_internet, use_container_width=True)
        
        with col2:
            fig_payment = px.pie(
                filtered_df,
                names="PaymentMethod",
                title="Payment Method Distribution"
            )
            st.plotly_chart(fig_payment, use_container_width=True)

            # Service features comparison
            service_cols = ['OnlineSecurity', 'TechSupport', 'StreamingTV', 'StreamingMovies']
            service_data = []
            for service in service_cols:
                percentage = (filtered_df[service] == 'Yes').mean() * 100
                service_data.append({'Service': service, 'Adoption Rate': percentage})
            
            fig_services = px.bar(
                pd.DataFrame(service_data),
                x='Service',
                y='Adoption Rate',
                title="Service Adoption Rates",
            )
            st.plotly_chart(fig_services, use_container_width=True)

        # Marketing Recommendations
        st.subheader("Marketing Strategy Recommendations")
        
        # Current approach
        st.markdown("### General Marketing Approach")
        approaches = filtered_df['General marketing approach'].unique()
        for approach in approaches:
            st.info(approach)
        
        # Targeted strategies
        st.markdown("### Recommended Marketing Strategies")
        strategy_key = (churn_risk, customer_value)
        if strategy_key in MARKETING_STRATEGIES:
            for strategy in MARKETING_STRATEGIES[strategy_key]:
                st.success(strategy)
        else:
            st.warning("No specific strategies defined for this segment combination. Using general approach.")

else:
    # Welcome message
    st.markdown("""
        ## Welcome to Our Telecom Marketing Optimizer System! 📱
        
        > *"Predict, Prevent, Prosper: Your Customer Retention Solution"*
        
        ### Getting Started:
        1. Upload your customer data CSV file using the sidebar
        2. Select your target customer segments
        3. Explore insights and recommended marketing strategies
        
        ### Features:
        - 📊 Interactive data visualization
        - 🎯 Targeted marketing recommendations
        - 📈 Churn risk analysis
        - 💡 Customer value segmentation
        
        Upload your data to begin optimizing your marketing campaigns!
    """)

# Footer
st.markdown("""
    ---
    > *"Every customer interaction is an opportunity to build a lasting relationship."*
""")