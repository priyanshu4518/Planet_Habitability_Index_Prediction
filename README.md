# Project: Planet Habitability Index Prediction

---

## 📄 Project Overview
This project aims to predict the **habitability of exoplanets** using planetary and stellar parameters. The goal is to classify planets as:
- **0:** Non-habitable
- **1:** Slightly habitable
- **2:** Habitable

Additionally, a **Continuous Habitability Index** is derived to rank planets based on their habitability potential.

---

## 📊 Dataset Overview
- **Source:** Data obtained from the Exoplanet Archive.
- **Size:** ~5599 exoplanet observations.
- **Initial Features:** 57 features capturing detailed planetary and stellar properties.
- **Selected Important Columns:**
```
- p_name, p_mass, p_radius, p_period, p_semi_major_axis, p_eccentricity
- s_distance, s_temperature, s_mass, s_radius, p_escape, p_potential
- p_gravity, p_density, p_hill_sphere, p_distance, p_periastron, p_apastron
- p_distance_eff, p_flux, p_temp_equil, p_temp_surf, p_type, s_type_temp
- s_luminosity, s_snow_line, s_abio_zone, s_tidal_lock, p_habzone_opt
- p_habzone_con, p_type_temp, p_habitable, s_log_g
```

---

## 🛠️ Data Cleaning & Challenges
- **Null Values:**
  - Numerical columns with high null rates were filled using models (e.g., **XGBoost**, **ANN**).
  - Columns with fewer missing values were filled using **KNN Imputation**.
- **Categorical Columns:**
  - Missing values were filled using **RandomForestClassifier** models with correlated features.

---

## 🌍 Habitability Metrics
### Atmospheric Retention (AR)
- Measures a planet's ability to retain its atmosphere.
- Earth serves as the ideal benchmark with AR = **100**.

### Long-Term Stability (LTS)
- Assesses the planet's orbital stability.
- Earth’s orbital conditions (eccentricity = 0, semi-major axis = 1 AU) score **100**.

### Earth Similarity Index (ESI)
- Measures similarity to Earth on a 0-100 scale.
- **Key Parameters and Weights:**
  - **p_radius** (57%)
  - **p_temp_surf** (43%)
  - **p_escape** (60%)
  - **p_density** (27%)

---

## 🚀 Feature Engineering
- Constructed new metrics:
  - **Earth Similarity Index (ESI)** (0-100)
  - **Atmospheric Retention (AR)** (0-100)
  - **Long-Term Stability (LTS)** (0-100)

---

## 🔍 Model Overview
- **Model:** XGBoost Classifier
- **Input Features:** ESI, Atmospheric Retention, Long-Term Stability
- **Output:** Habitability Class (0, 1, 2)
- **Sample Weighting:** Applied inverse class frequency to handle data imbalance.

**Key Hyperparameters:**
- Deeper trees, regularization (gamma, reg_lambda), and histogram tree method for faster training.

---

## 📈 Results and Interpretation
- **Inversion Count:** 24,527 out of 15,671,601 total pairs
- **Error Percentage:** 0.16%
- **Continuous Habitability Index** successfully aligns with the three categories:
  - Class 2 (Habitable) → Highest scores
  - Class 1 (Slightly Habitable) → Mid-range scores
  - Class 0 (Non-Habitable) → Lowest scores

---

## 🧩 Key Observations
- **Class 0:** Driven primarily by low **Long-Term Stability**.
- **Class 1:** Characterized by moderate **Atmospheric Retention** and **ESI**.
- **Class 2:** Dominated by high **Atmospheric Retention** (> 16.46).

---

## 📋 Usage
1. **Input:** Planetary and stellar parameters.
2. **Output:** Predicted Habitability Class (0, 1, 2).
3. **Continuous Habitability Index:** Provides a detailed ranking of habitability potential.

--- 
## 📹Video Demo

- **[Click here to watch the demo video](https://drive.google.com/file/d/1EqXkEuGs_4O-u-LRh6nglYb7iLNcz6oO/view?usp=sharing)**

---

## 🔗 Resources & Links
- Additional Resources:
  - [Planetary Habitability - Wikipedia](https://en.wikipedia.org/wiki/Planetary_habitability)
  - [NASA Exoplanet Exploration](https://exoplanets.nasa.gov/news/109/in-the-zone-how-scientists-search-for-habitable-planets/)

--- 

## 📧 Contact
For questions, suggestions, or collaborations, feel free to reach out. 😊 
mail-b23cy1021@iitj.ac.in
mail-b23ee1029@iitj.ac.in
