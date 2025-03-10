# Import necessary libraries
import streamlit as st  # For creating a web-based UI using Streamlit
import pandas as pd  # For handling and processing tabular data
import datetime  # For working with dates
import csv  # For reading and writing CSV files
import os  # For handling file-related operations

# Define a constant for the CSV file where mood data will be stored
MOOD_FILE = 'mood_log.csv'

# Function to load existing mood data from the CSV file
def load_mood_data():
    """
    Checks if the mood data file exists.
    - If the file doesn't exist, it returns an empty DataFrame with appropriate columns.
    - If the file exists, it loads the data into a pandas DataFrame.
    """
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=['Date', 'Mood'])  # Return an empty DataFrame with predefined columns
    return pd.read_csv(MOOD_FILE)  # Read the CSV file and return it as a DataFrame

# Function to save a new mood entry to the CSV file
def save_mood_data(date, mood):
    """
    Appends a new mood entry (date and mood) to the mood_log.csv file.
    - Opens the file in append mode.
    - Writes the new mood entry as a row in the CSV file.
    """
    with open(MOOD_FILE, "a", newline="") as file:  # Use 'newline=""' to prevent extra blank lines in Windows
        writer = csv.writer(file)  # Create a CSV writer object
        writer.writerow([date, mood])  # Write the new mood entry (date, mood)

# Main function that runs the Streamlit app
def main():
    """
    Main function that creates the web UI and handles user interactions.
    - Configures the Streamlit page with a title and an emoji favicon.
    - Prompts the user to select their mood and logs it when they click the button.
    - Displays a bar chart showing mood trends over time.
    """
    
    # Configure the page with a title and an emoji favicon
    st.set_page_config(page_title="Mood Tracker", page_icon="🙂✍")

    # Display the app title with emojis
    st.title("Mood Tracker 🙂✍")

    # Get the current date
    today = datetime.date.today()

    # Section for mood selection
    st.subheader("How are you feeling today?")
    
    # Dropdown for selecting mood
    mood = st.selectbox("Select Your Mood", ["Happy", "Sad", "Angry", "Neutral"])

    # Button to log the selected mood
    if st.button("Log Mood"):
        save_mood_data(today, mood)  # Save the mood to the CSV file
        st.success("Mood logged successfully")  # Show success message

    # Load existing mood data
    data = load_mood_data()

    # If there is mood data available, display mood trends
    if not data.empty:
        st.subheader("Mood Trends Over Time")

        # Convert the 'Date' column to datetime format for better visualization
        data["Date"] = pd.to_datetime(data["Date"])

        # Count occurrences of each mood type
        mood_counts = data.groupby("Mood").count()["Date"]

        # Display the mood counts as a bar chart
        st.bar_chart(mood_counts)

    # Add a creator link for credit
    st.link_button("🔹 Created by Hammad Sheikh", "https://www.linkedin.com/in/hammad-sheikh-51294b284/")

# Run the app when executed as the main script
if __name__ == '__main__':
    main()
