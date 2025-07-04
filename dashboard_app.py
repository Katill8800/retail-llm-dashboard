#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("cleaned_retail_data.csv", parse_dates=["dispatch_date", "order_date"])

st.title("🛒 Supermart Retail Chain Dashboard")

# KPIs
st.metric("Total Revenue", f"${df['sales'].sum():,.2f}")
st.metric("Total Profit", f"${df['profit'].sum():,.2f}")
st.metric("Avg Discount", f"{df['discount'].mean() * 100:.1f}%")
st.metric("Avg Dispatch to Sale Days", f"{df['dispatch_to_sale_days'].mean():.2f} days")

# Charts
fig1 = px.bar(df, x="region", y="sales", color="state", title="Sales by Region")
st.plotly_chart(fig1)

fig2 = px.line(df.sort_values("order_date"), x="order_date", y="sales", title="Sales Over Time")
st.plotly_chart(fig2)

fig3 = px.bar(df.groupby("sub_category")["profit"].sum().reset_index(),
              x="sub_category", y="profit", title="Profit by Sub-Category")
st.plotly_chart(fig3)


# In[ ]:




