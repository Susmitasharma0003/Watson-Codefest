import streamlit as st
import sympy as sp
from datetime import datetime, timedelta
import losartan as ls
import Amoldipine as am
from playsound import playsound
import time

def start_timer(t1):
    # Countdown timer
    while t1:
        mins, secs = divmod(t1, 60)  # Convert total seconds into minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Format the time
        print(timer, end='\r')  # Print the timer on the same line
        time.sleep(1)  # Wait for one second
        t1 -= 1  # Decrement the timer by one second

    st.write("Time to take medicine")
    playsound('Recorder.mp3')


st.title('Medication Reminder')

st.sidebar.header("Input Details")

medicine_name = st.sidebar.text_input("Medicine Name", placeholder="Enter the medicine name")
dosage = st.number_input('Enter your dosage (in mg):', min_value=0, step=1, format="%d")
dosage_limit = st.number_input('Enter your dosage-lower limit (in mg):', min_value=0, step=1, format="%d")
frequency = st.sidebar.selectbox("Frequency", [ "Twice a day", "Three times a day"])
current_time = datetime.now()
# Button to submit the information
if st.sidebar.button("Submit"):
    # Validate inputs
    if medicine_name is None or dosage ==0 :
        st.error("Please fill in all fields.")
    else:
        # Display the entered information
        st.success("Medication details submitted!")
        st.write(f"**Medicine:** {medicine_name}")
        st.write(f"**Dosage:** {dosage}")
        st.write(f"**Time:** {current_time}")
        st.write(f"**Lower Limit of dosage** {dosage_limit}")
        st.write(f"**Frequency:** {frequency}")
    
            # Optionally, you could add a reminder feature here
    t1 = ls.losartan_decay(dosage*10/11,dosage_limit*10/11)
    t2 = am.amlodipine_decay(dosage/11,dosage_limit/11)
    if t1>t2:
        st.write(int(t2))
        start_timer(int(t2))
    else:
        st.write(int(t1))
        start_timer(int(t1))
    # Footer with additional information

    st.markdown("---")
    st.markdown("### Tips for Medication Management")
    st.write("""
    - Always follow your doctor's instructions regarding medication.
    - Use reminders or alarms to help you remember your medication schedule.

    """)