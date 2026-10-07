import os
from urllib.parse import urlparse

import joblib
import pandas as pd

from src.feature_extraction import extract_features, FEATURE_COLUMNS


# ============================================================
# MODEL FILE PATHS
# ============================================================

MODEL_PATH = os.path.join("models", "best_model.pkl")
FEATURE_COLUMNS_PATH = os.path.join(
    "models",
    "feature_columns.pkl"
)


# ============================================================
# URL NORMALIZATION
# ============================================================

def normalize_url(url):
    """
    Clean basic URL input.

    The original URL is preserved because the ML feature
    extractor must receive the same type of URL representation
    used by the training pipeline.
    """

    if url is None:
        raise ValueError("Please enter a URL.")

    url = str(url).strip()

    if not url:
        raise ValueError("Please enter a URL.")

    if any(char.isspace() for char in url):
        raise ValueError("URL cannot contain spaces.")

    return url


# ============================================================
# URL VALIDATION
# ============================================================

def validate_url(url):
    """
    Validate basic URL structure before prediction.

    This is only input validation.
    It does NOT decide whether a URL is phishing.
    """

    try:
        normalized = normalize_url(url)

        # Allow URLs such as:
        # google.com
        # example.com/login
        parse_target = normalized

        if "://" not in normalized:
            parse_target = "https://" + normalized

        parsed = urlparse(parse_target)

        if not parsed.netloc:
            return False, "Invalid URL. Please enter a valid domain."

        if not parsed.hostname:
            return False, "Invalid URL. Please enter a valid domain."

        return True, "Valid URL."

    except ValueError as error:
        return False, str(error)

    except Exception:
        return False, "Unable to process this URL."


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

def load_model():
    """
    Load Member 1's trained Random Forest model.
    """

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


# ============================================================
# LOAD FEATURE ORDER
# ============================================================

def load_feature_columns():
    """
    Load the exact feature order used during training.
    """

    if not os.path.exists(FEATURE_COLUMNS_PATH):
        raise FileNotFoundError(
            f"Feature columns file not found: "
            f"{FEATURE_COLUMNS_PATH}"
        )

    return joblib.load(FEATURE_COLUMNS_PATH)


# ============================================================
# MAIN PREDICTION FUNCTION
# ============================================================

def predict_url(url):
    """
    Complete live prediction pipeline:

    URL
      ↓
    Member 2's extract_features()
      ↓
    Exact feature order from feature_columns.pkl
      ↓
    Member 1's Random Forest model
      ↓
    LEGITIMATE / PHISHING
      ↓
    Phishing Risk Score
    """

    # --------------------------------------------------------
    # 1. Validate basic input
    # --------------------------------------------------------

    url = normalize_url(url)

    # --------------------------------------------------------
    # 2. Load trained model and feature order
    # --------------------------------------------------------

    model = load_model()
    feature_columns = load_feature_columns()

    # --------------------------------------------------------
    # 3. Verify feature order
    # --------------------------------------------------------

    if list(feature_columns) != list(FEATURE_COLUMNS):

        raise ValueError(
            "Feature column mismatch between "
            "feature_columns.pkl and feature_extraction.py."
        )

    # --------------------------------------------------------
    # 4. Use Member 2's EXACT feature extractor
    # --------------------------------------------------------

    features = extract_features(url)

    # --------------------------------------------------------
    # 5. Arrange features in exact training order
    # --------------------------------------------------------

    feature_values = [
        features[column]
        for column in feature_columns
    ]

    # --------------------------------------------------------
    # 6. Create model input
    # --------------------------------------------------------

    X = pd.DataFrame(
        [feature_values],
        columns=feature_columns
    )

    # --------------------------------------------------------
    # 7. Get actual Random Forest prediction
    # --------------------------------------------------------

    prediction = int(
        model.predict(X)[0]
    )

    # --------------------------------------------------------
    # 8. Get phishing score
    # --------------------------------------------------------

    phishing_score = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(X)[0]

        classes = list(model.classes_)

        # Class 1 = Phishing
        if 1 in classes:

            phishing_index = classes.index(1)

            phishing_score = float(
                probabilities[phishing_index]
            )

    # --------------------------------------------------------
    # 9. Convert prediction to readable label
    # --------------------------------------------------------

    if prediction == 1:

        label = "PHISHING"

    else:

        label = "LEGITIMATE"

    # --------------------------------------------------------
    # 10. Return everything required by Streamlit
    # --------------------------------------------------------

    return {
        "prediction": prediction,
        "label": label,
        "phishing_score": phishing_score,
        "features": features,
    }


# ============================================================
# COMMAND-LINE TEST
# ============================================================

if __name__ == "__main__":

    url = input("Enter a URL: ")

    try:

        result = predict_url(url)

        print()
        print("Prediction:", result["label"])

        if result["phishing_score"] is not None:

            print(
                "Phishing Risk Score:",
                f"{result['phishing_score'] * 100:.2f}%"
            )

        print()
        print("Extracted Features:")

        for name, value in result["features"].items():

            print(
                f"{name}: {value}"
            )

    except Exception as error:

        print(
            "ERROR:",
            error
        )