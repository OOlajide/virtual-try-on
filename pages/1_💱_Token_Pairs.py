import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_extras.colored_header import colored_header

st.cache_data.clear()

st.set_page_config(
    page_title="Uniswap Gas Subsidy On L2s",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/sageOlamide",
        "About": None
    }
)

###################################
############ CACHE DATA ###########
###################################

url2a = "https://flipsidecrypto.xyz/studio/queries/dd04e23a-5e13-4b3e-947d-76df1f2a1c5d"
@st.cache_data
def load_df2a():
    df2a = pd.read_csv('data/df2a.csv')
    return df2a

url3a = "https://flipsidecrypto.xyz/studio/queries/4ba875e6-18b7-4956-827d-c98b91d04dc7"
@st.cache_data
def load_df3a():
    df3a = pd.read_csv('data/df3a.csv')
    return df3a

###################################
############ LOAD DATA ############
###################################

df2a = load_df2a()
df3a = load_df3a()

###################################
########### PLOT CHARTS ###########
###################################


##################### DF2a #####################

########################################### FIG1
################ CHART START ###################
# Create separate line charts for Full and Partial Stablecoin Pairs
full_pairs = df2a[df2a['CATEGORY'] == 'Full Stablecoin Pairs']
partial_pairs = df2a[df2a['CATEGORY'] == 'Partial Stablecoin Pairs']
df2a_fig1_1 = px.line(full_pairs, x='DATE', y='TOTAL_ACTIVE_USERS', title='Full Stablecoin Pairs - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df2a_fig1_2 = px.line(partial_pairs, x='DATE', y='TOTAL_ACTIVE_USERS', title='Partial Stablecoin Pairs - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df2a_fig1_3 = px.line(df2a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis
df2a_fig1 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for Full Stablecoin Pairs
for trace in df2a_fig1_1.data:
    trace.update(name='Full Stablecoin Pairs - ACTIVE_USERS', hovertemplate='%{y}')
    df2a_fig1.add_trace(trace, secondary_y=False)

# Add traces for Partial Stablecoin Pairs
for trace in df2a_fig1_2.data:
    trace.update(name='Partial Stablecoin Pairs - ACTIVE_USERS', hovertemplate='%{y}')
    df2a_fig1.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df2a_fig1_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df2a_fig1.add_trace(trace, secondary_y=True)

# Set x-axis title
df2a_fig1.update_xaxes(title_text="DATE")

# Set y-axes titles
df2a_fig1.update_yaxes(title_text="ACTIVE_USERS", secondary_y=False)
df2a_fig1.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df2a_fig1.update_layout(
    title_text="Total Active Users per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df2a_fig1.update_layout(hovermode="x unified")
df2a_fig1.update_traces(line=dict(width=0.9))
df2a_fig1.update_traces(selector=dict(name='Full Stablecoin Pairs - ACTIVE_USERS'), line=dict(color="blue"), showlegend=True)
df2a_fig1.update_traces(selector=dict(name='Partial Stablecoin Pairs - ACTIVE_USERS'), line=dict(color="green"), showlegend=True)
df2a_fig1.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)

################### CHART END ##################

########################################### FIG2
################ CHART START ###################
# Create separate line charts for Full and Partial Stablecoin Pairs
full_pairs = df2a[df2a['CATEGORY'] == 'Full Stablecoin Pairs']
partial_pairs = df2a[df2a['CATEGORY'] == 'Partial Stablecoin Pairs']
df2a_fig2_1 = px.line(full_pairs, x='DATE', y='VOLUME_USD', title='Full Stablecoin Pairs - VOLUME_USD', labels={'VOLUME_USD': 'Volume USD'})
df2a_fig2_2 = px.line(partial_pairs, x='DATE', y='VOLUME_USD', title='Partial Stablecoin Pairs - VOLUME_USD', labels={'VOLUME_USD': 'Volume USD'})
df2a_fig2_3 = px.line(df2a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis

df2a_fig2 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for Full Stablecoin Pairs
for trace in df2a_fig2_1.data:
    trace.update(name='Full Stablecoin Pairs - VOLUME_USD', hovertemplate='%{y}')
    df2a_fig2.add_trace(trace, secondary_y=False)

# Add traces for Partial Stablecoin Pairs
for trace in df2a_fig2_2.data:
    trace.update(name='Partial Stablecoin Pairs - VOLUME_USD', hovertemplate='%{y}')
    df2a_fig2.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df2a_fig2_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df2a_fig2.add_trace(trace, secondary_y=True)

# Set x-axis title
df2a_fig2.update_xaxes(title_text="DATE")

# Set y-axes titles
df2a_fig2.update_yaxes(title_text="VOLUME_USD", secondary_y=False)
df2a_fig2.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df2a_fig2.update_layout(
    title_text="Total Volume USD per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df2a_fig2.update_layout(hovermode="x unified")
df2a_fig2.update_traces(line=dict(width=0.9))
df2a_fig2.update_traces(selector=dict(name='Full Stablecoin Pairs - VOLUME_USD'), line=dict(color="blue"), showlegend=True)
df2a_fig2.update_traces(selector=dict(name='Partial Stablecoin Pairs - VOLUME_USD'), line=dict(color="green"), showlegend=True)
df2a_fig2.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)

################### CHART END ##################

########################################### FIG3
################ CHART START ###################
# Create separate line charts for Full and Partial Stablecoin Pairs
full_pairs = df2a[df2a['CATEGORY'] == 'Full Stablecoin Pairs']
partial_pairs = df2a[df2a['CATEGORY'] == 'Partial Stablecoin Pairs']
df2a_fig3_1 = px.line(full_pairs, x='DATE', y='SWAP_TXNS', title='Full Stablecoin Pairs - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Transactions'})
df2a_fig3_2 = px.line(partial_pairs, x='DATE', y='SWAP_TXNS', title='Partial Stablecoin Pairs - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Transactions'})
df2a_fig3_3 = px.line(df2a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis

df2a_fig3 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for Full Stablecoin Pairs
for trace in df2a_fig3_1.data:
    trace.update(name='Full Stablecoin Pairs - SWAP_TXNS', hovertemplate='%{y}')
    df2a_fig3.add_trace(trace, secondary_y=False)

# Add traces for Partial Stablecoin Pairs
for trace in df2a_fig3_2.data:
    trace.update(name='Partial Stablecoin Pairs - SWAP_TXNS', hovertemplate='%{y}')
    df2a_fig3.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df2a_fig3_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df2a_fig3.add_trace(trace, secondary_y=True)

# Set x-axis title
df2a_fig3.update_xaxes(title_text="DATE")

# Set y-axes titles
df2a_fig3.update_yaxes(title_text="SWAP_TXNS", secondary_y=False)
df2a_fig3.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df2a_fig3.update_layout(
    title_text="Total Swap Transactions per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df2a_fig3.update_layout(hovermode="x unified")
df2a_fig3.update_traces(line=dict(width=0.9))
df2a_fig3.update_traces(selector=dict(name='Full Stablecoin Pairs - SWAP_TXNS'), line=dict(color="blue"), showlegend=True)
df2a_fig3.update_traces(selector=dict(name='Partial Stablecoin Pairs - SWAP_TXNS'), line=dict(color="green"), showlegend=True)
df2a_fig3.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)

################### CHART END ##################

########################################### FIG4
################ CHART START ###################
# Create separate line charts for Full and Partial Stablecoin Pairs
full_pairs = df2a[df2a['CATEGORY'] == 'Full Stablecoin Pairs']
partial_pairs = df2a[df2a['CATEGORY'] == 'Partial Stablecoin Pairs']
df2a_fig4_1 = px.line(full_pairs, x='DATE', y='TOTAL_ACTIVE_POOLS', title='Full Stablecoin Pairs - TOTAL_ACTIVE_POOLS', labels={'TOTAL_ACTIVE_POOLS': 'Total Active Pools'})
df2a_fig4_2 = px.line(partial_pairs, x='DATE', y='TOTAL_ACTIVE_POOLS', title='Partial Stablecoin Pairs - TOTAL_ACTIVE_POOLS', labels={'TOTAL_ACTIVE_POOLS': 'Total Active Pools'})
df2a_fig4_3 = px.line(df2a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis

df2a_fig4 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for Full Stablecoin Pairs
for trace in df2a_fig4_1.data:
    trace.update(name='Full Stablecoin Pairs - TOTAL_ACTIVE_POOLS', hovertemplate='%{y}')
    df2a_fig4.add_trace(trace, secondary_y=False)

# Add traces for Partial Stablecoin Pairs
for trace in df2a_fig4_2.data:
    trace.update(name='Partial Stablecoin Pairs - TOTAL_ACTIVE_POOLS', hovertemplate='%{y}')
    df2a_fig4.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df2a_fig4_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df2a_fig4.add_trace(trace, secondary_y=True)

# Set x-axis title
df2a_fig4.update_xaxes(title_text="DATE")

# Set y-axes titles
df2a_fig4.update_yaxes(title_text="TOTAL_ACTIVE_POOLS", secondary_y=False)
df2a_fig4.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df2a_fig4.update_layout(
    title_text="Total Active Pools per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df2a_fig4.update_layout(hovermode="x unified")
df2a_fig4.update_traces(line=dict(width=0.9))
df2a_fig4.update_traces(selector=dict(name='Full Stablecoin Pairs - TOTAL_ACTIVE_POOLS'), line=dict(color="blue"), showlegend=True)
df2a_fig4.update_traces(selector=dict(name='Partial Stablecoin Pairs - TOTAL_ACTIVE_POOLS'), line=dict(color="green"), showlegend=True)
df2a_fig4.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)

################### CHART END ##################

##################### DF3a #####################


########################################### FIG1
################ CHART START ###################
# Create separate line charts for Full and Partial Governance Pairs
full_pairs = df3a[df3a['CATEGORY'] == 'Full Governance Pairs']
partial_pairs = df3a[df3a['CATEGORY'] == 'Partial Governance Pairs']
df3a_fig1_1 = px.line(full_pairs, x='DATE', y='TOTAL_ACTIVE_USERS', title='Full Governance Pairs - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df3a_fig1_2 = px.line(partial_pairs, x='DATE', y='TOTAL_ACTIVE_USERS', title='Partial Governance Pairs - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df3a_fig1_3 = px.line(df3a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis
df3a_fig1 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for Full Governance Pairs
for trace in df3a_fig1_1.data:
    trace.update(name='Full Governance Pairs - ACTIVE_USERS', hovertemplate='%{y}')
    df3a_fig1.add_trace(trace, secondary_y=False)

# Add traces for Partial Governance Pairs
for trace in df3a_fig1_2.data:
    trace.update(name='Partial Governance Pairs - ACTIVE_USERS', hovertemplate='%{y}')
    df3a_fig1.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df3a_fig1_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df3a_fig1.add_trace(trace, secondary_y=True)

# Set x-axis title
df3a_fig1.update_xaxes(title_text="DATE")

# Set y-axes titles
df3a_fig1.update_yaxes(title_text="ACTIVE_USERS", secondary_y=False)
df3a_fig1.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df3a_fig1.update_layout(
    title_text="Total Active Users per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df3a_fig1.update_layout(hovermode="x unified")
df3a_fig1.update_traces(line=dict(width=0.9))
df3a_fig1.update_traces(selector=dict(name='Full Governance Pairs - ACTIVE_USERS'), line=dict(color="blue"), showlegend=True)
df3a_fig1.update_traces(selector=dict(name='Partial Governance Pairs - ACTIVE_USERS'), line=dict(color="green"), showlegend=True)
df3a_fig1.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)
################### CHART END ##################


########################################### FIG2
################ CHART START ###################
# Create separate line charts for Full and Partial Governance Pairs
full_pairs_volume = df3a[df3a['CATEGORY'] == 'Full Governance Pairs']
partial_pairs_volume = df3a[df3a['CATEGORY'] == 'Partial Governance Pairs']
df3a_fig2_1 = px.line(full_pairs_volume, x='DATE', y='VOLUME_USD', title='Full Governance Pairs - VOLUME_USD', labels={'VOLUME_USD': 'Volume USD'})
df3a_fig2_2 = px.line(partial_pairs_volume, x='DATE', y='VOLUME_USD', title='Partial Governance Pairs - VOLUME_USD', labels={'VOLUME_USD': 'Volume USD'})
df3a_fig2_3 = px.line(df3a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis
df3a_fig2 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for Full Governance Pairs
for trace in df3a_fig2_1.data:
    trace.update(name='Full Governance Pairs - VOLUME_USD', hovertemplate='%{y}')
    df3a_fig2.add_trace(trace, secondary_y=False)

# Add traces for Partial Governance Pairs
for trace in df3a_fig2_2.data:
    trace.update(name='Partial Governance Pairs - VOLUME_USD', hovertemplate='%{y}')
    df3a_fig2.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df3a_fig2_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df3a_fig2.add_trace(trace, secondary_y=True)

# Set x-axis title
df3a_fig2.update_xaxes(title_text="DATE")

# Set y-axes titles
df3a_fig2.update_yaxes(title_text="VOLUME_USD", secondary_y=False)
df3a_fig2.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df3a_fig2.update_layout(
    title_text="Volume USD per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df3a_fig2.update_layout(hovermode="x unified")
df3a_fig2.update_traces(line=dict(width=0.9))
df3a_fig2.update_traces(selector=dict(name='Full Governance Pairs - VOLUME_USD'), line=dict(color="blue"), showlegend=True)
df3a_fig2.update_traces(selector=dict(name='Partial Governance Pairs - VOLUME_USD'), line=dict(color="green"), showlegend=True)
df3a_fig2.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)

################### CHART END ##################



########################################### FIG3
################ CHART START ###################
# Create separate line charts for Full and Partial Governance Pairs
full_pairs_swap = df3a[df3a['CATEGORY'] == 'Full Governance Pairs']
partial_pairs_swap = df3a[df3a['CATEGORY'] == 'Partial Governance Pairs']
df3a_fig3_1 = px.line(full_pairs_swap, x='DATE', y='SWAP_TXNS', title='Full Governance Pairs - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Txns'})
df3a_fig3_2 = px.line(partial_pairs_swap, x='DATE', y='SWAP_TXNS', title='Partial Governance Pairs - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Txns'})
df3a_fig3_3 = px.line(df3a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis
df3a_fig3 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for Full Governance Pairs
for trace in df3a_fig3_1.data:
    trace.update(name='Full Governance Pairs - SWAP_TXNS', hovertemplate='%{y}')
    df3a_fig3.add_trace(trace, secondary_y=False)

# Add traces for Partial Governance Pairs
for trace in df3a_fig3_2.data:
    trace.update(name='Partial Governance Pairs - SWAP_TXNS', hovertemplate='%{y}')
    df3a_fig3.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df3a_fig3_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df3a_fig3.add_trace(trace, secondary_y=True)

# Set x-axis title
df3a_fig3.update_xaxes(title_text="DATE")

# Set y-axes titles
df3a_fig3.update_yaxes(title_text="SWAP_TXNS", secondary_y=False)
df3a_fig3.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df3a_fig3.update_layout(
    title_text="Swap Txns per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df3a_fig3.update_layout(hovermode="x unified")
df3a_fig3.update_traces(line=dict(width=0.9))
df3a_fig3.update_traces(selector=dict(name='Full Governance Pairs - SWAP_TXNS'), line=dict(color="blue"), showlegend=True)
df3a_fig3.update_traces(selector=dict(name='Partial Governance Pairs - SWAP_TXNS'), line=dict(color="green"), showlegend=True)
df3a_fig3.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)

################### CHART END ##################



########################################### FIG4
################ CHART START ###################
# Create separate line charts for Full and Partial Governance Pairs
full_pairs_pools = df3a[df3a['CATEGORY'] == 'Full Governance Pairs']
partial_pairs_pools = df3a[df3a['CATEGORY'] == 'Partial Governance Pairs']
df3a_fig4_1 = px.line(full_pairs_pools, x='DATE', y='TOTAL_ACTIVE_POOLS', title='Full Governance Pairs - TOTAL_ACTIVE_POOLS', labels={'TOTAL_ACTIVE_POOLS': 'Total Active Pools'})
df3a_fig4_2 = px.line(partial_pairs_pools, x='DATE', y='TOTAL_ACTIVE_POOLS', title='Partial Governance Pairs - TOTAL_ACTIVE_POOLS', labels={'TOTAL_ACTIVE_POOLS': 'Total Active Pools'})
df3a_fig4_3 = px.line(df3a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis
df3a_fig4 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for Full Governance Pairs
for trace in df3a_fig4_1.data:
    trace.update(name='Full Governance Pairs - TOTAL_ACTIVE_POOLS', hovertemplate='%{y}')
    df3a_fig4.add_trace(trace, secondary_y=False)

# Add traces for Partial Governance Pairs
for trace in df3a_fig4_2.data:
    trace.update(name='Partial Governance Pairs - TOTAL_ACTIVE_POOLS', hovertemplate='%{y}')
    df3a_fig4.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df3a_fig4_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df3a_fig4.add_trace(trace, secondary_y=True)

# Set x-axis title
df3a_fig4.update_xaxes(title_text="DATE")

# Set y-axes titles
df3a_fig4.update_yaxes(title_text="TOTAL_ACTIVE_POOLS", secondary_y=False)
df3a_fig4.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df3a_fig4.update_layout(
    title_text="Total Active Pools per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df3a_fig4.update_layout(hovermode="x unified")
df3a_fig4.update_traces(line=dict(width=0.9))
df3a_fig4.update_traces(selector=dict(name='Full Governance Pairs - TOTAL_ACTIVE_POOLS'), line=dict(color="blue"), showlegend=True)
df3a_fig4.update_traces(selector=dict(name='Partial Governance Pairs - TOTAL_ACTIVE_POOLS'), line=dict(color="green"), showlegend=True)
df3a_fig4.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)

################### CHART END ##################


###################################
############# LAYOUT ##############
###################################

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Stablecoin Pairs"}</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

st.plotly_chart(df2a_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url2a}")

st.plotly_chart(df2a_fig2, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url2a}")

st.plotly_chart(df2a_fig3, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url2a}")

st.plotly_chart(df2a_fig4, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url2a}")

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Arbitrum and Polygon emerge as prominent chains on Uniswap, each commanding a substantial 30% share of unique users. However, a deeper analysis reveals Arbitrum\'s dominance, boasting a remarkable 57% share of the total swap volume across all six chains. This stands 90% higher than Polygon\'s respectable 30% share. The significance lies in the fact that while both platforms attract an equal number of users, Arbitrum users are notably more active, collectively engaging in higher-value swaps compared to their Polygon counterparts.</p>'
st.markdown(insight_1, unsafe_allow_html=True)

insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">This trend is reinforced when examining the weekly active users and swap volume charts. Despite initial parity between the two chains, with Polygon even enjoying a higher count of active pools per week, a pivotal shift occurred in March 2023. Notably, this surge in Uniswap activity on Arbitrum coincided with the platform\'s inaugural airdrop in the same month. During the peak of this surge, the third week of March 2023 witnessed an impressive $3.5 billion worth of tokens being swapped on Uniswap via Arbitrum. This data underscores Arbitrum\'s growing prominence and user engagement, suggesting that airdrops can significantly impact the usage and adoption of Uniswap.</p>'
st.markdown(insight_2, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Governance Pairs"}</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

st.plotly_chart(df3a_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url3a}")

st.plotly_chart(df3a_fig2, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url3a}")

st.plotly_chart(df3a_fig3, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url3a}")

st.plotly_chart(df3a_fig4, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url3a}")

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_3 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Arbitrum and Polygon emerge as prominent chains on Uniswap, each commanding a substantial 30% share of unique users. However, a deeper analysis reveals Arbitrum\'s dominance, boasting a remarkable 57% share of the total swap volume across all six chains. This stands 90% higher than Polygon\'s respectable 30% share. The significance lies in the fact that while both platforms attract an equal number of users, Arbitrum users are notably more active, collectively engaging in higher-value swaps compared to their Polygon counterparts.</p>'
st.markdown(insight_3, unsafe_allow_html=True)

insight_4 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">This trend is reinforced when examining the weekly active users and swap volume charts. Despite initial parity between the two chains, with Polygon even enjoying a higher count of active pools per week, a pivotal shift occurred in March 2023. Notably, this surge in Uniswap activity on Arbitrum coincided with the platform\'s inaugural airdrop in the same month. During the peak of this surge, the third week of March 2023 witnessed an impressive $3.5 billion worth of tokens being swapped on Uniswap via Arbitrum. This data underscores Arbitrum\'s growing prominence and user engagement, suggesting that airdrops can significantly impact the usage and adoption of Uniswap.</p>'
st.markdown(insight_4, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)