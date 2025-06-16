import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Churn Mitigation Dashboard", layout="wide")
st.title("📉 Customer Churn Mitigation Dashboard")
st.markdown("Track metrics across Support, Churn Risk, Retention, Competitive Intel & CTA Volume.")

# Support Optimization
support_data = pd.DataFrame({
    'Month': pd.date_range(start='2025-01-01', periods=6, freq='M').strftime('%b %Y'),
    'Avg_Resolution_Time': [24, 22, 20, 19, 18, 17],
    'First_Contact_Resolution': [70, 72, 74, 76, 78, 80]
})

# Churn Risk
churn_risk_data = pd.DataFrame({
    'Segment': ['Enterprise', 'SMB', 'Startup', 'Government'],
    'Churn_Risk_Score': [0.25, 0.45, 0.60, 0.30]
})

# Retention Campaigns
campaign_data = pd.DataFrame({
    'Campaign': ['Loyalty Rewards', 'Flexible Billing', 'Win-back Offers'],
    'Response_Rate': [65, 55, 70],
    'Revenue_Saved': [100000, 75000, 113000]
})

# Competitive Intelligence
comp_data = pd.DataFrame({
    'Reason': ['Support Delays', 'Sold Company', 'Competitor Offers'],
    'Percent': [40, 36, 24]
})

# CTA Volume
cta_segment_data = pd.DataFrame({
    'Segment': ['Enterprise', 'SMB', 'Strategic', 'NULL'],
    'CTA_Count': [117, 6077, 17, 2029]
})
cta_month_data = pd.DataFrame({
    'Month': ['Jan-2025', 'Feb-2025', 'Mar-2025', 'Apr-2025', 'May-2025', 'Jun-2025'],
    'CTA_Count': [775, 584, 494, 558, 513, 226]
})

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📞 Support", "🚨 Churn Risk", "🎯 Campaigns", "📊 Competitors", "📈 CTA Volume"
])

with tab1:
    col1, col2 = st.columns(2)
    col1.plotly_chart(px.line(support_data, x='Month', y='Avg_Resolution_Time', title='Avg Resolution Time'), use_container_width=True)
    col2.plotly_chart(px.bar(support_data, x='Month', y='First_Contact_Resolution', title='FCR %'), use_container_width=True)

with tab2:
    st.plotly_chart(px.bar(churn_risk_data, x='Segment', y='Churn_Risk_Score', title='Churn Risk by Segment', text='Churn_Risk_Score'), use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    col1.plotly_chart(px.bar(campaign_data, x='Campaign', y='Response_Rate', title='Response Rate'), use_container_width=True)
    col2.plotly_chart(px.bar(campaign_data, x='Campaign', y='Revenue_Saved', title='Revenue Saved'), use_container_width=True)

with tab4:
    st.plotly_chart(px.pie(comp_data, names='Reason', values='Percent', title='Churn Reasons'), use_container_width=True)

with tab5:
    col1, col2 = st.columns(2)
    col1.plotly_chart(px.bar(cta_segment_data, x='Segment', y='CTA_Count', title='CTA by Segment', text='CTA_Count'), use_container_width=True)
    col2.plotly_chart(px.bar(cta_month_data, x='Month', y='CTA_Count', title='CTA by Month', text='CTA_Count'), use_container_width=True)
