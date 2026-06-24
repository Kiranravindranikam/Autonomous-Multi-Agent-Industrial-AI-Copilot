import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Industrial AI Copilot",
    page_icon="🏭",
    layout="wide"
)

# ==========================================
# DARK INDUSTRIAL THEME
# ==========================================

st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
    color:white;
}

section[data-testid="stSidebar"]{
    background-color:#111827;
}

div[data-testid="stMetric"]{
    background:#1E1E1E;
    border-radius:15px;
    padding:20px;
    box-shadow:0px 4px 12px rgba(255,255,255,0.05);
}

h1,h2,h3,h4,p,label{
    color:white !important;
}

</style>
""",
unsafe_allow_html=True)

chart_template = "plotly_dark"
gauge_bg = "#1E1E1E"
font_color = "white"

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<h1 style='text-align:center'>
🏭 Autonomous Multi-Agent Industrial AI Copilot
</h1>
""",
unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center'>
Real-Time Industrial Monitoring Dashboard
</h4>
""",
unsafe_allow_html=True)

st.markdown("---")
# ==========================================
# MODEL LOAD
# ==========================================

try:
    model = joblib.load(
        "../models/best_predictive_model.pkl"
    )
except:
    model = None

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title(
    "🏭 Industrial AI Copilot"
)

st.sidebar.header(
    "📡 Machine Sensor Inputs"
)

air_temp = st.sidebar.slider(
    "Air Temperature (K)",
    290,320,300
)

process_temp = st.sidebar.slider(
    "Process Temperature (K)",
    300,340,310
)

rpm = st.sidebar.slider(
    "Rotational Speed (RPM)",
    1000,3000,1500
)

torque = st.sidebar.slider(
    "Torque (Nm)",
    10,80,40
)

tool_wear = st.sidebar.slider(
    "Tool Wear (min)",
    0,300,50
)

failure_probability = 0.12

if model is not None:

    sample = pd.DataFrame({
        "air_temperature":[air_temp],
        "process_temperature":[process_temp],
        "rotational_speed":[rpm],
        "torque":[torque],
        "tool_wear":[tool_wear]
    })

    try:
        failure_probability = (
            model.predict_proba(sample)[0][1]
        )
    except:
        failure_probability = 0.12

health_score = (
    100 - failure_probability*100
)

predicted_rul = int(
    max(
        5,
        150-tool_wear
    )
)
# ==========================================
# STATUS
# ==========================================

if predicted_rul > 100:

    status = "🟢 HEALTHY"

elif predicted_rul > 30:

    status = "🟡 WARNING"

else:

    status = "🔴 CRITICAL"

# ==========================================
# KPI SECTION
# ==========================================

col1,col2,col3 = st.columns(3)

with col1:

    st.metric(
        "Health Score",
        f"{health_score:.2f}%"
    )

with col2:

    st.metric(
        "Failure Probability",
        f"{failure_probability*100:.2f}%"
    )

with col3:

    st.metric(
        "Remaining Useful Life",
        f"{predicted_rul} Cycles"
    )

st.markdown("---")

st.subheader(
    "🚨 Machine Status"
)

if predicted_rul > 100:

    st.success(status)

elif predicted_rul > 30:

    st.warning(status)

else:

    st.error(status)

st.markdown("---")
# ==========================================
# GAUGES
# ==========================================

g1,g2,g3 = st.columns(3)

with g1:

    fig1 = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=health_score,
            title={
                "text":"Health Score (%)"
            },
            gauge={
                "axis":{
                    "range":[0,100]
                }
            }
        )
    )

    fig1.update_layout(
        paper_bgcolor=gauge_bg,
        font={
            "color":font_color
        }
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with g2:

    fig2 = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=
            failure_probability*100,
            title={
                "text":"Failure Probability"
            },
            gauge={
                "axis":{
                    "range":[0,100]
                }
            }
        )
    )

    fig2.update_layout(
        paper_bgcolor=gauge_bg,
        font={
            "color":font_color
        }
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

with g3:

    fig3 = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=predicted_rul,
            title={
                "text":"Remaining Useful Life"
            },
            gauge={
                "axis":{
                    "range":[0,200]
                }
            }
        )
    )

    fig3.update_layout(
        paper_bgcolor=gauge_bg,
        font={
            "color":font_color
        }
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

st.markdown("---")
# ==========================================
# SENSOR DATA
# ==========================================

time = np.arange(50)

temperature_df = pd.DataFrame({

    "Time":time,

    "Temperature":
    np.random.normal(
        air_temp,
        1,
        50
    )
})

rpm_df = pd.DataFrame({

    "Time":time,

    "RPM":
    np.random.normal(
        rpm,
        30,
        50
    )
})

torque_df = pd.DataFrame({

    "Time":time,

    "Torque":
    np.random.normal(
        torque,
        1,
        50
    )
})

c1,c2 = st.columns(2)

with c1:

    fig_temp = px.line(
        temperature_df,
        x="Time",
        y="Temperature",
        title="Temperature Trend"
    )

    fig_temp.update_layout(
        template=chart_template
    )

    st.plotly_chart(
        fig_temp,
        use_container_width=True
    )

with c2:

    fig_rpm = px.line(
        rpm_df,
        x="Time",
        y="RPM",
        title="RPM Trend"
    )

    fig_rpm.update_layout(
        template=chart_template
    )

    st.plotly_chart(
        fig_rpm,
        use_container_width=True
    )

fig_torque = px.line(
    torque_df,
    x="Time",
    y="Torque",
    title="Torque Trend"
)

fig_torque.update_layout(
    template=chart_template
)

st.plotly_chart(
    fig_torque,
    use_container_width=True
)

st.subheader(
    "📋 Current Sensor Values"
)

sensor_table = pd.DataFrame({

    "Sensor":[
        "Air Temperature",
        "Process Temperature",
        "RPM",
        "Torque",
        "Tool Wear"
    ],

    "Value":[
        air_temp,
        process_temp,
        rpm,
        torque,
        tool_wear
    ]
})

st.dataframe(
    sensor_table,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.markdown("""
<div style='text-align:center'>

<h3>
🏭 Autonomous Multi-Agent Industrial AI Copilot
</h3>

<p>
Digital Twin Dashboard |
Predictive Maintenance |
Failure Forecasting
</p>

</div>
""",
unsafe_allow_html=True)