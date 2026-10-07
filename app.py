import streamlit as st

from src.predict import predict_url


st.set_page_config(
    page_title="PhishGuard",
    page_icon="🛡️",
    layout="centered"
)

# ---------- Header ----------

st.title("🛡️ PhishGuard")
st.subheader("AI-Powered Phishing URL Detection")

st.write(
    "Analyze a URL using our trained Random Forest machine learning model."
)

st.divider()

# ---------- URL Input ----------

st.markdown("### 🔗 Enter a URL")

url = st.text_input(
    "URL",
    placeholder="https://example.com",
    label_visibility="collapsed"
)

analyze = st.button(
    "🔍 Analyze URL",
    type="primary",
    use_container_width=True
)

# ---------- Prediction ----------

if analyze:

    if not url.strip():

        st.warning("⚠️ Please enter a URL.")

    else:

        try:

            result = predict_url(url)

            st.divider()

            # Result
            if result["label"] == "PHISHING":

                st.error("🔴 PHISHING")

            else:

                st.success("🟢 LEGITIMATE")

            # Risk score
            if result["phishing_score"] is not None:

                score = result["phishing_score"] * 100

                st.metric(
                    label="Phishing Risk Score",
                    value=f"{score:.2f}%"
                )

                st.progress(
                    min(max(result["phishing_score"], 0.0), 1.0)
                )

            # Features
            st.markdown("### 🔎 Detected URL Features")

            features = result["features"]

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**URL Length:** {features['url_length']}"
                )

                st.write(
                    f"**Dot Count:** {features['dot_count']}"
                )

                st.write(
                    f"**@ Symbol:** {features['has_at']}"
                )

                st.write(
                    f"**HTTPS:** {features['has_https']}"
                )

                st.write(
                    f"**IP Address:** {features['has_ip']}"
                )

                st.write(
                    f"**Suspicious Keywords:** "
                    f"{features['suspicious_keyword_count']}"
                )

            with col2:

                st.write(
                    f"**Hyphen Count:** {features['hyphen_count']}"
                )

                st.write(
                    f"**Digit Count:** {features['digit_count']}"
                )

                st.write(
                    f"**Special Characters:** "
                    f"{features['special_character_count']}"
                )

                st.write(
                    f"**Path Depth:** {features['path_depth']}"
                )

                st.write(
                    f"**Hostname Length:** "
                    f"{features['hostname_length']}"
                )

        except Exception as error:

            st.error(
                f"❌ Unable to analyze this URL: {error}"
            )

# ---------- Footer ----------

st.divider()

st.caption(
    "PhishGuard • Random Forest URL Classification • "
    "College Hackathon Project"
)