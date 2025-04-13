# %% [markdown]
# # Customer Acquisition Cost (CAC) Analysis 

# %%
# Requirements
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
# Set default template for plots
pio.templates.default = "plotly_white"

# %% [markdown]
# # Load data

# %%
df = pd.read_csv('data/customer_acquisition_cost_dataset.csv')
df.head()

# %%


# %% [markdown]
# # DataFrame structure & types 

# %%
# Let's inspect the data
# Summary of the dataset
print("Summary of the dataset:\n")
df.info()


# %% [markdown]
# # Summary stats

# %%
#df.describe(include='all')
df.describe()


# %%
df.nunique()
  # Check for unique values in each column

# %% [markdown]
# # Customer Acquisition Cost (CAC)

# %%

# Lets Calculate Customer Acquisition Cost (CAC)
# CAC = Total Marketing Spend / Number of New Customers Acquired
df['CAC'] = df['Marketing_Spend']/ df['New_Customers']

# Lets calculate the customer per spend
# Customers per Spend = New Customers / Marketing Spend
df['Customers_Per_Spend'] = df['New_Customers'] / df['Marketing_Spend']

# Lets calculate the Conversion Rate
# Conversion Rate = (New Customers / Marketing Spend) * 100
df['Conversion_Rate'] = (df['New_Customers'] / df['Marketing_Spend']) * 100  

#Lets caculate the Break-even Customers
# Break-even Customers = Marketing Spend / CAC
df['BE_customers'] = df['Marketing_Spend'] / df['CAC']  

df_sorted = df.sort_values('CAC', ascending=False)
# display the head of the sorted DataFrame to see the top CAC values
df.head()

# %% [markdown]
# # Lets Check CAC by Market Channels

# %%
# Creating a box plot for CAC by Marketing Channel
fig1 = px.box(df_sorted, x='Marketing_Channel', y='CAC',
              color='Marketing_Channel', 
              title='Customer Acquisition Cost (CAC) by Marketing Channel',
              labels={'CAC': 'Customer Acquisition Cost (INR)'},
              color_discrete_sequence=px.colors.qualitative.Set2)
# Updating layout
fig1.update_layout(
    xaxis_title='Marketing Channel',
    yaxis_title='CAC (INR)',
    title_x=0.5,
    yaxis=dict(tickformat=".2f"),
    showlegend=False  # Hide legend since colors match x-axis
)
# Displaying the plot
fig1.show()

# %% [markdown]
# # CAC vs New Customers

# %%
fig2 = px.scatter(df_sorted, x='New_Customers', y='CAC', color='Marketing_Channel',
                  title='CAC vs New Customers by Channel', trendline='ols',
                  labels={'CAC': 'CAC (INR)', 'New_Customers': 'New Customers'},
                  color_discrete_sequence=px.colors.qualitative.Set2,
                  hover_data=['CAC', 'New_Customers', 'Marketing_Spend'])
fig2.update_traces(marker=dict(size=8, opacity=0.8, line=dict(width=1, color='DarkSlateGrey')),
                   text=df_sorted['CAC'].round(2).astype(str), textposition='top center')
fig2.update_layout(xaxis_title='New Customers', yaxis_title='CAC (INR)', 
                   title_x=0.5, yaxis=dict(tickformat=".2f"))
fig2.show()

# %% [markdown]
# # New Customers Acquisition Cost vs Marketing_Spend  by Marketing_Channel

# %%
fig3 = px.scatter(df_sorted, x='Marketing_Spend', y='CAC', color='Marketing_Channel',
                  title='Customer Acquisition Cost(CAC) vs Marketing Spend by Marketing Channel', 
                  trendline='ols',
                  labels={'CAC': 'CAC (INR)', 'Marketing_Spend': 'Marketing Spend (INR)'},
                  color_discrete_sequence=px.colors.qualitative.Set1,
                  hover_data=['CAC', 'Marketing_Spend', 'New_Customers'])
fig3.update_traces(marker=dict(size=8, opacity=0.8, line=dict(width=1, color='DarkSlateGrey')),
                   text=df_sorted['CAC'].round(2).astype(str), textposition='top center')
fig3.update_layout(xaxis_title='Marketing Spend (INR)', yaxis_title='CAC (INR)', 
                   title_x=0.5, xaxis=dict(tickformat=",.0f"), yaxis=dict(tickformat=".2f"))
fig3.show()

# %% [markdown]
# # Summary Stats

# %%
summary = df.groupby('Marketing_Channel')['CAC'].describe().reset_index()
# Display the summary DataFrame
print(summary)

# %% [markdown]
# # Conversion Rate by Marketing Channel

# %%
fig = px.box(df, x='Marketing_Channel', 
             y='Conversion_Rate',
             color='Marketing_Channel',
              title='Conversion Rate by Marketing Channel',
              labels={'Conversion_Rate': 'Conversion Rate (%)'},
              color_discrete_sequence=px.colors.qualitative.Set3)
fig.update_layout(xaxis_title='Marketing Channel', yaxis_title='Conversion Rate', 
                  title_x=0.5, yaxis=dict(tickformat=".4f"), showlegend=False)
fig.show()

# %% [markdown]
# # New Customers per Marketing Spend by Channel

# %%
# Bar chart for Customers per Marketing Spend
fig4 = px.bar(df, x='Marketing_Channel', y='Customers_Per_Spend', 
              color='Marketing_Channel', title='New Customers per Marketing Spend by Channel',
              labels={'Customers_Per_Spend': 'New Customers per INR Spent'},
              color_discrete_sequence=px.colors.qualitative.Set2,
              text=df['Customers_Per_Spend'].round(4).astype(str))  # 4 decimals for clarity

fig4.update_traces(textposition='auto', textfont=dict(size=12))
fig4.update_layout(xaxis_title='Marketing Channel', yaxis_title='New Customers per INR Spent', 
                   title_x=0.5, yaxis=dict(tickformat=".4f"), showlegend=False)  # Match format to small values
fig4.show()

# %% [markdown]
# # Break-even Customers by Marketing Channel

# %%

# Box plot for BE_customers
fig5 = px.box(df, x='Marketing_Channel', y='BE_customers',
              color='Marketing_Channel', 
              title='Break-even Customers by Channel',
              labels={'BE_customers': 'Break-even Customers'},
              color_discrete_sequence=px.colors.qualitative.Set2)

# Update layout
fig5.update_layout(
    xaxis_title='Marketing Channel',
    yaxis_title='Break-even Customers',
    title_x=0.5,
    yaxis=dict(tickformat=".2f"),
    showlegend=False
)

# Show the plot
fig5.show()

# %% [markdown]
# # CAC vs Conversion Rate

# %%
fig6 = px.scatter(df, x='CAC', y='Conversion_Rate', color='Marketing_Channel',
                  title='CAC vs Conversion Rate by Channel',
                  labels={'CAC': 'CAC (INR)', 'Conversion_Rate': 'Conversion Rate (%)'},
                  color_discrete_sequence=px.colors.qualitative.Set1,
                  hover_data=['CAC', 'Conversion_Rate', 'New_Customers'])
fig6.update_traces(marker=dict(size=8, opacity=0.8, line=dict(width=1, color='DarkSlateGrey')),
                   text=df['CAC'].round(2).astype(str) + '\n' + df['Conversion_Rate'].round(2).astype(str) + '%',
                   textposition='top center')
fig6.update_layout(xaxis_title='CAC (INR)', yaxis_title='Conversion Rate (%)', 
                   title_x=0.5, xaxis=dict(tickformat=".2f"), yaxis=dict(tickformat=".2f"))
fig6.show()

# %% [markdown]
# # CAC and New Customers side by side

# %%
fig = px.bar(df, x='Marketing_Channel', y=['CAC', 'New_Customers'], 
             barmode='group', title='CAC and New Customers by Channel',
             labels={'value': 'Value', 'variable': 'Metric'},
             color_discrete_map={'CAC': '#FFA500', 'New_Customers': '#228B22'}) 
fig.update_layout(title_x=0.5, yaxis=dict(tickformat=".2f"))
fig.show()

# %% [markdown]
# 


