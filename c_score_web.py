import streamlit as st
from scipy.stats import norm

# Function to calculate the C-score
def calculate_c_score(G, L, mu_g=4.7, sigma_g=0.7, mu_l=5.6, sigma_l=1):
    # Step 1: Calculate percentiles (CDF values)
    Z_g = (G - mu_g) / sigma_g
    Z_l = (L - mu_l) / sigma_l
    P_g = norm.cdf(Z_g)  # Percentile for G
    P_l = norm.cdf(Z_l)  # Percentile for L
    
    # Step 2: Find the number of standard deviations from the mean
    std_dev_g = norm.ppf(P_g)
    std_dev_l = norm.ppf(P_l)
    
    # Step 3: Calculate the difference in standard deviations
    delta_std_dev = abs(std_dev_g - std_dev_l)
    
    # Step 4: Calculate the percentage of data within delta_std_dev standard deviations
    percentage_within = norm.cdf(delta_std_dev) - norm.cdf(-delta_std_dev)
    
    # Step 5: Calculate the C-score based on the percentage within delta_std_dev
    c_score = max(-1, min(1, percentage_within))
    
    return c_score

# Function to return a message based on C-score
def get_c_score_message(c_score):
    if -0.2 <= c_score <= 0.2:
        return st.selectbox("Message", ["Wow, so proportional!", "Booooringgggg", "Textbook"])
    elif 0.2 < c_score <= 0.6:
        return st.selectbox("Message", ["thick!", "cho-cho-cho-cho", "stumpyyyyy"])
    elif c_score > 0.6:
        return st.selectbox("Message", ["Beware of toilet paper rolls!", "tube sock full of coke cans", "hot dog with the bun and another bun around that."])
    elif -0.6 <= c_score < -0.2:
        return st.selectbox("Message", ["pencil!", "Stick figure frfr", "#longandproud"])
    else:
        return st.selectbox("Message", ["Don't poke an eye out", "Beware of papercuts", "fashtingele!!"])

# Title of the app
st.title("C-Score Calculator")

# User input fields for G and L values
G = st.number_input("Enter the G value", value=4.7)
L = st.number_input("Enter the L value", value=5.6)

# Calculate C-score
c_score = calculate_c_score(G, L)

# Show the calculated C-score
st.write(f"The C-score is: {c_score:.3f}")

# Display the message based on the C-score
message = get_c_score_message(c_score)
st.write(message)
