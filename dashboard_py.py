import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# 1. SETUP & DATA CREATION
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Soullab Growth Dashboard", layout="wide")

# Custom CSS to match the report's look and feel
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Inter', sans-serif;
    }
    
    /* Card Style for Metrics */
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        color: #212529;
    }
    
    /* Metric Label */
    div[data-testid="metric-container"] > label {
        color: #6c757d;
        font-weight: 500;
        font-size: 0.9rem;
    }
    
    /* Metric Value */
    div[data-testid="metric-container"] > div[data-testid="stMetricValue"] {
        color: #212529;
        font-weight: 700;
        font-size: 1.8rem;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #212529;
        font-weight: 600;
    }
    
    /* Section Dividers */
    hr {
        border-top: 1px solid #ced4da;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Complete dataset including Week 0 and all extended metrics
data = [
    {
        "Week": "Week 0: Dec 01 - Dec 07, 2025",
        "Start Date": "2025-12-01",
        "End Date": "2025-12-07",
        "Total Subs": 640100,
        "New Subs": 12784,
        "Avg DAU": 956,
        "Total Plays": 18900,
        "Total Downloads": 107907,
        "New Downloads": 316,
        "Total Active Devices": 26464,
        "New Sign-ups": 222,
        "Masterclasses Played": 800,
        "Daily Journal Entries": 180,
        "Weekly Workshop": 110,
        "Content Likes": 140,
        "Content Shares": 15,
        "YT Views": 92645,
        "YT Watch Time": 6558,
        "YT Likes": 1500,
        "Top Track": "Satchit Anand (Short)"
    },
    {
        "Week": "Week 1: Dec 08 - Dec 14, 2025",
        "Start Date": "2025-12-08",
        "End Date": "2025-12-14",
        "Total Subs": 651328,
        "New Subs": 13052,
        "Avg DAU": 945,
        "Total Plays": 16900,
        "Total Downloads": 108227,
        "New Downloads": 320,
        "Total Active Devices": 26535,
        "New Sign-ups": 180,
        "Masterclasses Played": 1000,
        "Daily Journal Entries": 140,
        "Weekly Workshop": 90,
        "Content Likes": 100,
        "Content Shares": 60,
        "YT Views": 103903,
        "YT Watch Time": 7990,
        "YT Likes": 1800,
        "Top Track": "Heal Your Relationships"
    },
    {
        "Week": "Week 2: Dec 15 - Dec 21, 2025",
        "Start Date": "2025-12-15",
        "End Date": "2025-12-21",
        "Total Subs": 666541,
        "New Subs": 13337,
        "Avg DAU": 1002,
        "Total Plays": 21950,
        "Total Downloads": 108568,
        "New Downloads": 341,
        "Total Active Devices": 26600,
        "New Sign-ups": 208,
        "Masterclasses Played": 1350,
        "Daily Journal Entries": 260,
        "Weekly Workshop": 95,
        "Content Likes": 105,
        "Content Shares": 105,
        "YT Views": 68512,
        "YT Watch Time": 4296,
        "YT Likes": 1200,
        "Top Track": "Satchit Anand (Short)"
    },
    {
        "Week": "Week 3: Dec 22 - Dec 28, 2025",
        "Start Date": "2025-12-22",
        "End Date": "2025-12-28",
        "Total Subs": 682685,
        "New Subs": 19952,
        "Avg DAU": 957,
        "Total Plays": 18165,
        "Total Downloads": 109111,
        "New Downloads": 316,
        "Total Active Devices": 26505,
        "New Sign-ups": 199,
        "Masterclasses Played": 237,
        "Daily Journal Entries": 113,
        "Weekly Workshop": 90,
        "Content Likes": 85,
        "Content Shares": 158,
        "YT Views": 88631,
        "YT Watch Time": 3826,
        "YT Likes": 2026,
        "Top Track": "Prashanti Ke Pal"
    },
    {
        "Week": "Week 4: Dec 29 - Jan 04, 2026",
        "Start Date": "2025-12-29",
        "End Date": "2026-01-04",
        "Total Subs": 707024,
        "New Subs": 24338,
        "Avg DAU": 993,
        "Total Plays": 20572,
        "Total Downloads": 109475,
        "New Downloads": 364,
        "Total Active Devices": 26600,
        "New Sign-ups": 197,
        "Masterclasses Played": 1200,
        "Daily Journal Entries": 200,
        "Weekly Workshop": 80,
        "Content Likes": 120,
        "Content Shares": 150,
        "YT Views": 123871,
        "YT Watch Time": 5980,
        "YT Likes": 3000,
        "Top Track": "Healing Circle Meditation"
    },
    {
        "Week": "Week 5: Jan 05 - Jan 11, 2026",
        "Start Date": "2026-01-05",
        "End Date": "2026-01-11",
        "Total Subs": 732405,
        "New Subs": 25370,
        "Avg DAU": 730,
        "Total Plays": 21000,
        "Total Downloads": 109870,
        "New Downloads": 366,
        "Total Active Devices": 26510,
        "New Sign-ups": 190,
        "Masterclasses Played": 1750,
        "Daily Journal Entries": 245,
        "Weekly Workshop": 70,
        "Content Likes": 110,
        "Content Shares": 130,
        "YT Views": 102324,
        "YT Watch Time": 4681,
        "YT Likes": 539,
        "Top Track": "Anapanasati (Short)"
    },
    {
        "Week": "Week 6: Jan 12 - Jan 18, 2026",
        "Start Date": "2026-01-12",
        "End Date": "2026-01-18",
        "Total Subs": 756405,
        "New Subs": 24071,
        "Avg DAU": 1048,
        "Total Plays": 20850,
        "Total Downloads": 110158,
        "New Downloads": 288,
        "Total Active Devices": 26529,
        "New Sign-ups": 228,
        "Masterclasses Played": 1250,
        "Daily Journal Entries": 180,
        "Weekly Workshop": 75,
        "Content Likes": 140,
        "Content Shares": 90,
        "YT Views": 113782,
        "YT Watch Time": 4180,
        "YT Likes": 433,
        "Top Track": "Satchit Anand (Short)"
    },
    {
        "Week": "Week 7: Jan 19 - Jan 25, 2026",
        "Start Date": "2026-01-19",
        "End Date": "2026-01-25",
        "Total Subs": 794180,
        "New Subs": 37704,
        "Avg DAU": 1065,
        "Total Plays": 21500,
        "Total Downloads": 110521,
        "New Downloads": 363,
        "Total Active Devices": 26580,
        "New Sign-ups": 180,
        "Masterclasses Played": 1400,
        "Daily Journal Entries": 210,
        "Weekly Workshop": 85,
        "Content Likes": 130,
        "Content Shares": 110,
        "YT Views": 176077,
        "YT Watch Time": 4469,
        "YT Likes": 539,
        "Top Track": "Satchit Anand (Short)"
    }
]

df = pd.DataFrame(data)

# -----------------------------------------------------------------------------
# 2. SIDEBAR - DATE PICKER & LOGIC
# -----------------------------------------------------------------------------
st.sidebar.header("Filters")
st.sidebar.markdown("**Select the reporting week:**")

# Select Box for the Weeks (Reversed order to show latest first)
week_options = df["Week"].tolist()
selected_week = st.sidebar.selectbox(
    "Choose Week",
    options=week_options,
    index=len(week_options)-1 # Default to latest
)

# Filter Data based on selection
week_data = df[df["Week"] == selected_week].iloc[0]

# Calculate previous week's data for comparison (Delta)
current_index = df[df["Week"] == selected_week].index[0]
if current_index > 0:
    prev_week_data = df.iloc[current_index - 1]
    comparison_label = "vs last week"
else:
    prev_week_data = week_data # No change if it's the first week
    comparison_label = "(No prev data)"

def calculate_delta(current, prev, is_percentage=False):
    if current_index == 0: return None
    diff = current - prev
    if is_percentage:
        return f"{diff:+.1f}%"
    return f"{diff:+,.0f}"

# -----------------------------------------------------------------------------
# 3. DASHBOARD HEADER
# -----------------------------------------------------------------------------
st.title("📊 Soullab Growth Dashboard")
st.markdown(f"### **Reporting Period:** {week_data['Week']}")
st.markdown("---")

# -----------------------------------------------------------------------------
# 4. KPI GRID (ALL METRICS) - Styled like "Lifetime Totals" from Report
# -----------------------------------------------------------------------------
st.subheader("Lifetime Totals")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total App Downloads", f"{week_data['Total Downloads']:,}", f"+{week_data['New Downloads']:,} new")
with col2:
    st.metric("Total Active Devices", f"{week_data['Total Active Devices']:,}", calculate_delta(week_data['Total Active Devices'], prev_week_data['Total Active Devices']))
with col3:
    st.metric("Total YouTube Subscribers", f"{week_data['Total Subs']:,}", f"+{week_data['New Subs']:,} new")

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. APP PERFORMANCE OVERVIEW (WEEKLY)
# -----------------------------------------------------------------------------
st.subheader("App Performance Overview (Weekly)")
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("App Downloads", f"{week_data['New Downloads']:,}", calculate_delta(week_data['New Downloads'], prev_week_data['New Downloads']))
with c2:
    st.metric("New Sign-ups", f"{week_data['New Sign-ups']:,}", calculate_delta(week_data['New Sign-ups'], prev_week_data['New Sign-ups']))
with c3:
    st.metric("Avg Daily Active Users", f"{week_data['Avg DAU']:,}", calculate_delta(week_data['Avg DAU'], prev_week_data['Avg DAU']))

st.markdown("---")

# -----------------------------------------------------------------------------
# 6. IN-APP ENGAGEMENT (WEEKLY)
# -----------------------------------------------------------------------------
st.subheader("In-App Engagement (Weekly)")
e1, e2, e3 = st.columns(3)
with e1:
    st.metric("Total Audios Played", f"{week_data['Total Plays']:,}", calculate_delta(week_data['Total Plays'], prev_week_data['Total Plays']))
with e2:
    st.metric("Masterclasses Played", f"{week_data['Masterclasses Played']:,}", calculate_delta(week_data['Masterclasses Played'], prev_week_data['Masterclasses Played']))
with e3:
    st.metric("Daily Journal Entries", f"{week_data['Daily Journal Entries']:,}", calculate_delta(week_data['Daily Journal Entries'], prev_week_data['Daily Journal Entries']))

e4, e5, e6 = st.columns(3)
with e4:
    st.metric("Weekly Workshop", f"{week_data['Weekly Workshop']:,}", calculate_delta(week_data['Weekly Workshop'], prev_week_data['Weekly Workshop']))
with e5:
    st.metric("Content Likes", f"{week_data['Content Likes']:,}", calculate_delta(week_data['Content Likes'], prev_week_data['Content Likes']))
with e6:
    st.metric("Content Shares", f"{week_data['Content Shares']:,}", calculate_delta(week_data['Content Shares'], prev_week_data['Content Shares']))

st.markdown("---")

# -----------------------------------------------------------------------------
# 7. YOUTUBE PERFORMANCE (WEEKLY)
# -----------------------------------------------------------------------------
st.subheader("YouTube Performance (Weekly)")
y1, y2, y3, y4 = st.columns(4)

with y1:
    st.metric("Watch Time (Hours)", f"{week_data['YT Watch Time']:,}", calculate_delta(week_data['YT Watch Time'], prev_week_data['YT Watch Time']))
with y2:
    st.metric("Video Views", f"{week_data['YT Views']:,}", calculate_delta(week_data['YT Views'], prev_week_data['YT Views']))
with y3:
    st.metric("Likes", f"{week_data['YT Likes']:,}", calculate_delta(week_data['YT Likes'], prev_week_data['YT Likes']))
with y4:
    st.metric("Subscribers Gained", f"{week_data['New Subs']:,}", calculate_delta(week_data['New Subs'], prev_week_data['New Subs']))

st.markdown("---")

# -----------------------------------------------------------------------------
# 8. CHARTS & TRENDS
# -----------------------------------------------------------------------------
st.subheader("📈 Trends Over Time")

tab1, tab2, tab3 = st.tabs(["Subscriber Growth", "App Activity", "YouTube Views"])

with tab1:
    fig_subs = px.bar(df, x="End Date", y="New Subs", text="New Subs", title="Weekly New Subscribers", color="New Subs", color_continuous_scale="Teal")
    fig_subs.add_vrect(x0=week_data["Start Date"], x1=week_data["End Date"], fillcolor="red", opacity=0.1, annotation_text="Selected", annotation_position="top left")
    st.plotly_chart(fig_subs)

with tab2:
    fig_dau = px.line(df, x="End Date", y="Avg DAU", markers=True, title="Daily Active Users Trend")
    fig_dau.update_traces(line_color='#0A2342', line_width=4)
    fig_dau.add_trace(go.Scatter(x=[week_data["End Date"]], y=[week_data["Avg DAU"]], mode="markers", marker=dict(color="red", size=15), name="Selected"))
    st.plotly_chart(fig_dau)

with tab3:
    fig_views = px.bar(df, x="End Date", y="YT Views", title="Weekly YouTube Views", color_discrete_sequence=['#FF0000'])
    fig_views.add_vrect(x0=week_data["Start Date"], x1=week_data["End Date"], fillcolor="gray", opacity=0.1)
    st.plotly_chart(fig_views)

# -----------------------------------------------------------------------------
# 9. RAW DATA TABLE (HIDDEN BY DEFAULT)
# -----------------------------------------------------------------------------
with st.expander("View Raw Data for Selected Week"):
    st.table(pd.DataFrame([week_data]).T)
