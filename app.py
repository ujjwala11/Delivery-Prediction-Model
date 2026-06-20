import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.sidebar.title("🍔 Project Overview")

st.sidebar.info("""
Machine Learning powered
Delivery Analytics Dashboard

Dataset: 45K+ Deliveries

Model:
Random Forest Regressor

Purpose:
Predict ETA and optimize delivery operations.
""")
st.set_page_config(
    page_title="Zomato Delivery Analytics",
    page_icon="🍔",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------

model = joblib.load(
    "models/delivery_time_model.pkl"
)

model_columns = joblib.load(
    "models/model_columns.pkl"
)

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def get_rating_category(rating):

    if rating <= 3.5:
        return "Low"

    elif rating <= 4.0:
        return "Average"

    elif rating <= 4.5:
        return "Good"

    return "Excellent"


def predict_eta(
    distance,
    age,
    rating,
    vehicle_condition,
    multiple_deliveries,
    traffic,
    weather,
    festival,
    city
):

    sample = {
        "Distance_km": distance,
        "Delivery_person_Age": age,
        "Delivery_person_Ratings": rating,
        "Vehicle_condition": vehicle_condition,
        "multiple_deliveries": multiple_deliveries,
        "Rating_Category": get_rating_category(rating),
        "Road_traffic_density": traffic,
        "Weather_conditions": weather,
        "Festival": festival,
        "City": city
    }

    df = pd.DataFrame([sample])

    df = pd.get_dummies(df)

    df = df.reindex(
        columns=model_columns,
        fill_value=0
    )

    prediction = model.predict(df)

    return prediction[0]


# -----------------------------
# TITLE
# -----------------------------

st.title("🍔 Zomato Delivery Analytics Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "ETA Prediction",
        "Business Insights",
        "Delivery Optimizer",
        "Model Performance"
    ]
)

# =============================
# TAB 1
# =============================

with tab1:

    st.header("ETA Prediction")

    col1, col2 = st.columns(2)

    with col1:

        distance = st.number_input(
            "Distance (km)",
            min_value=0.0,
            value=5.0
        )

        age = st.slider(
            "Delivery Person Age",
            18,
            50,
            30
        )

        rating = st.slider(
            "Delivery Rating",
            1.0,
            5.0,
            4.5
        )

    with col2:

        vehicle_condition = st.selectbox(
            "Vehicle Condition",
            [0,1,2,3]
        )

        multiple_deliveries = st.selectbox(
            "Multiple Deliveries",
            [0,1,2,3]
        )

        traffic = st.selectbox(
            "Traffic Density",
            ["Low","Medium","High","Jam"]
        )

        weather = st.selectbox(
            "Weather",
            [
                "Sunny",
                "Fog",
                "Stormy",
                "Windy",
                "Sandstorms"
            ]
        )

        festival = st.selectbox(
            "Festival",
            ["No","Yes"]
        )

        city = st.selectbox(
            "City",
            [
                "Urban",
                "Semi-Urban",
                "Metropolitan"
            ]
        )

    if st.button("Predict Delivery Time"):

        eta = predict_eta(
            distance,
            age,
            rating,
            vehicle_condition,
            multiple_deliveries,
            traffic,
            weather,
            festival,
            city
        )

        st.success(
            f"Estimated Delivery Time: {eta:.2f} minutes"
        )

# =============================
# TAB 2
# =============================

with tab2:

    st.header("📊 Business Insights")

    # KPI Cards
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Model R²", "0.814")

    with c2:
        st.metric("MAE", "3.18 min")

    with c3:
        st.metric("Records", "45K+")

    with c4:
        st.metric("Features", "26")

    st.divider()

    st.subheader("Key Business Findings")

    st.info("""
    • Higher traffic density significantly increases delivery time.
    
    • Multiple deliveries per rider increase ETA.
    
    • Festival days show noticeable delays.
    
    • Better rider ratings generally lead to faster deliveries.
    """)

    st.divider()

    st.subheader("Visualisation Reports")

    try:
        st.image(
            "visualisations/traffic_analysis.png",
            caption="Impact of Traffic Density on Delivery Time",
            use_container_width=True
        )
    except:
        st.warning("traffic_analysis.png not found")

    try:
        st.image(
            "visualisations/weather_analysis.png",
            caption="Weather vs Delivery Time",
            use_container_width=True
        )
    except:
        st.warning("weather_analysis.png not found")

    try:
        st.image(
            "visualisations/festival_analysis.png",
            caption="Festival Impact Analysis",
            use_container_width=True
        )
    except:
        st.warning("festival_analysis.png not found")


with tab3:

    st.header("🚀 Delivery Optimizer")

    st.write(
        "Compare current delivery conditions with an optimized scenario."
    )

    st.subheader("Current Delivery Conditions")

    col1, col2 = st.columns(2)

    with col1:

        distance_opt = st.number_input(
            "Distance (km)",
            min_value=0.0,
            value=8.0,
            key="opt_distance"
        )

        rating_opt = st.slider(
            "Rider Rating",
            1.0,
            5.0,
            4.0,
            key="opt_rating"
        )

    with col2:

        traffic_opt = st.selectbox(
            "Traffic Density",
            ["Low", "Medium", "High", "Jam"],
            index=3,
            key="opt_traffic"
        )

        deliveries_opt = st.selectbox(
            "Multiple Deliveries",
            [0, 1, 2, 3],
            index=3,
            key="opt_multi"
        )

    if st.button("Run Optimization"):

        # Current ETA
        current_eta = predict_eta(
            distance=distance_opt,
            age=30,
            rating=rating_opt,
            vehicle_condition=2,
            multiple_deliveries=deliveries_opt,
            traffic=traffic_opt,
            weather="Sunny",
            festival="No",
            city="Metropolitan"
        )

        # Optimized ETA
        optimized_eta = predict_eta(
            distance=distance_opt,
            age=30,
            rating=4.8,
            vehicle_condition=3,
            multiple_deliveries=1,
            traffic="Medium",
            weather="Sunny",
            festival="No",
            city="Metropolitan"
        )

        saved_time = current_eta - optimized_eta

        st.divider()

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Current ETA",
                f"{current_eta:.1f} min"
            )

        with c2:
            st.metric(
                "Optimized ETA",
                f"{optimized_eta:.1f} min"
            )

        with c3:
            st.metric(
                "Time Saved",
                f"{saved_time:.1f} min"
            )

        st.success(
            f"Potential improvement: {saved_time:.1f} minutes faster delivery."
        )

        st.subheader("Recommended Actions")

        recommendations = []

        if traffic_opt in ["High", "Jam"]:
            recommendations.append(
                "Reduce congestion by rerouting deliveries."
            )

        if deliveries_opt > 1:
            recommendations.append(
                "Limit multiple deliveries per rider."
            )

        if rating_opt < 4.5:
            recommendations.append(
                "Assign higher-rated riders when possible."
            )

        if recommendations:
            for rec in recommendations:
                st.write(f"✅ {rec}")
        else:
            st.write("✅ Current setup is already near optimal.")
# =============================
# TAB 4
# =============================

with tab4:

    st.header("Model Performance")

    st.metric(
        "Random Forest R²",
        "0.814"
    )

    st.metric(
        "MAE",
        "3.18 minutes"
    )

    st.metric(
        "RMSE",
        "4.03 minutes"
    )