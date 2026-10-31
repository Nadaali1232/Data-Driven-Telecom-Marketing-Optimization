from marketing_strategies import MARKETING_STRATEGIES

def generate_segment_report(filtered_df, original_df, churn_risk, customer_value):
    """Generate a detailed report for the selected segment."""
    total_customers = len(original_df)
    total_monthly_charges = original_df['MonthlyCharges'].sum()
    
    segment_customers = len(filtered_df)
    segment_monthly_charges = filtered_df['MonthlyCharges'].sum()
    
    # Calculate percentages
    customer_percentage = (segment_customers / total_customers) * 100
    charges_percentage = (segment_monthly_charges / total_monthly_charges) * 100
    
    # Generate distribution percentages for various metrics
    contract_dist = filtered_df['Contract'].value_counts(normalize=True) * 100
    internet_dist = filtered_df['InternetService'].value_counts(normalize=True) * 100
    payment_dist = filtered_df['PaymentMethod'].value_counts(normalize=True) * 100
    
    # Service adoption rates
    service_cols = ['OnlineSecurity', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    service_rates = {col: (filtered_df[col] == 'Yes').mean() * 100 for col in service_cols}
    
    # Generate report text
    report = f"""Telecom Marketing Segment Report
=================================
Segment: {churn_risk} Churn Risk / {customer_value} Value

Customer Overview
----------------
Total Customers in Segment: {segment_customers:,}
Percentage of Total Customers: {customer_percentage:.1f}%
Monthly Charges: ${segment_monthly_charges:,.2f}
Percentage of Total Monthly Charges: {charges_percentage:.1f}%
Average Monthly Charge per Customer: ${(segment_monthly_charges/segment_customers):.2f}

Contract Distribution
-------------------
{contract_dist.to_string()}

Internet Service Distribution
--------------------------
{internet_dist.to_string()}

Payment Method Distribution
------------------------
{payment_dist.to_string()}

Service Adoption Rates
--------------------
{chr(10).join([f"{service}: {rate:.1f}%" for service, rate in service_rates.items()])}

Current Marketing Approach
------------------------
{chr(10).join(filtered_df['General marketing approach'].unique())}

Recommended Marketing Strategies
-----------------------------
{chr(10).join(MARKETING_STRATEGIES.get((churn_risk, customer_value), ['No specific strategies defined for this segment']))}
"""
    return report