import streamlit as st

from src.predict import predict_url


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PhishGuard | URL Security",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0b1020 0%,
            #111827 50%,
            #0f172a 100%
        );
    }

    /* Main content */
    .block-container {
        max-width: 900px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .brand {
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .brand-icon {
        font-size: 3.5rem;
        margin-bottom: 0.2rem;
    }

    .brand-title {
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -1px;
        color: #ffffff;
        margin: 0;
    }

    .brand-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
        margin-top: 0.4rem;
    }

    .tagline {
        text-align: center;
        color: #cbd5e1;
        margin-top: 1.2rem;
        margin-bottom: 2rem;
    }

    /* Input label */
    .input-heading {
        color: #e2e8f0;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-size: 1rem;
        font-weight: 700;
    }

    /* Result cards */
    .result-card {
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

    .safe-card {
        background: rgba(22, 163, 74, 0.12);
        border: 1px solid rgba(74, 222, 128, 0.35);
    }

    .phishing-card {
        background: rgba(220, 38, 38, 0.12);
        border: 1px solid rgba(248, 113, 113, 0.35);
    }

    .result-label {
        font-size: 2rem;
        font-weight: 800;
        margin: 0.3rem 0;
    }

    .result-description {
        color: #cbd5e1;
        font-size: 0.95rem;
    }

    /* Section headings */
    .section-title {
        color: #f1f5f9;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }

    /* Feature boxes */
    .feature-box {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 12px;
        padding: 0.8rem 1rem;
        margin-bottom: 0.6rem;
    }

    .feature-name {
        color: #94a3b8;
        font-size: 0.8rem;
    }

    .feature-value {
        color: #f8fafc;
        font-size: 1rem;
        font-weight: 700;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.8rem;
        margin-top: 2rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="brand">
        <div class="brand-icon">🛡️</div>
        <div class="brand-title">PhishGuard</div>
        <div class="brand-subtitle">
            AI-Powered Phishing URL Detection
        </div>
    </div>

    <div class="tagline">
        Analyze a website URL before you trust it.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# URL INPUT
# ============================================================

st.markdown(
    '<div class="input-heading">🔗 Enter a URL to analyze</div>',
    unsafe_allow_html=True
)

url = st.text_input(
    "URL",
    placeholder="https://example.com",
    label_visibility="collapsed"
)

analyze_button = st.button(
    "🔍  ANALYZE URL",
    type="primary",
    use_container_width=True
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze_button:

    if not url.strip():

        st.warning("⚠️ Please enter a URL.")

    else:

        try:

            result = predict_url(url)

            label = result["label"]
            score = result["phishing_score"]

            st.divider()

            # ------------------------------------------------
            # RESULT
            # ------------------------------------------------

            if label == "PHISHING":

                st.markdown(
                    """
                    <div class="result-card phishing-card">
                        <div class="result-label">
                            🔴 PHISHING
                        </div>
                        <div class="result-description">
                            The machine learning model classified this
                            URL as potentially unsafe.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    """
                    <div class="result-card safe-card">
                        <div class="result-label">
                            🟢 LEGITIMATE
                        </div>
                        <div class="result-description">
                            The machine learning model classified this
                            URL as legitimate.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # ------------------------------------------------
            # RISK SCORE
            # ------------------------------------------------

            if score is not None:

                score_percent = score * 100

                st.markdown(
                    '<div class="section-title">'
                    '📊 Phishing Risk Score'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.metric(
                    label="Model Score",
                    value=f"{score_percent:.2f}%"
                )

                st.progress(
                    min(max(score, 0.0), 1.0)
                )

                st.caption(
                    "Score shown is the Random Forest model's "
                    "phishing-class score."
                )


            # ------------------------------------------------
            # FEATURE ANALYSIS
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '🔎 Detected URL Features'
                '</div>',
                unsafe_allow_html=True
            )

            features = result["features"]

            col1, col2 = st.columns(2)

            with col1:

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">URL Length</div>
                        <div class="feature-value">
                            {features['url_length']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">Dot Count</div>
                        <div class="feature-value">
                            {features['dot_count']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">@ Symbol</div>
                        <div class="feature-value">
                            {features['has_at']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">HTTPS</div>
                        <div class="feature-value">
                            {features['has_https']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">IP Address</div>
                        <div class="feature-value">
                            {features['has_ip']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">
                            Suspicious Keywords
                        </div>
                        <div class="feature-value">
                            {features['suspicious_keyword_count']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">Hyphen Count</div>
                        <div class="feature-value">
                            {features['hyphen_count']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">Digit Count</div>
                        <div class="feature-value">
                            {features['digit_count']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">
                            Special Characters
                        </div>
                        <div class="feature-value">
                            {features['special_character_count']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">Path Depth</div>
                        <div class="feature-value">
                            {features['path_depth']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="feature-box">
                        <div class="feature-name">
                            Hostname Length
                        </div>
                        <div class="feature-value">
                            {features['hostname_length']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        except Exception as error:

            st.error(
                f"❌ Unable to analyze this URL: {error}"
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        PhishGuard • Random Forest URL Classification
        <br>
        College Hackathon Project
    </div>
    """,
    unsafe_allow_html=True
)