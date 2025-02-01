from pymindwave2 import MindWaveMobile2, Session, SessionConfig

# Initialize and connect to the headset
headset = MindWaveMobile2()
success = headset.start(n_tries=5, timeout=30)

if success:  # if the headset is connected successfully
    # Create a session configuration
    sess_config = SessionConfig(
        user_name="User",
        classes=["left", "right"],
        baseline_duration=90
    )
    
    # Initialize and start the recording session
    session = Session(headset, config=sess_config)
    
    session.start()  # Start recording data
    
    while session.is_active:
        pass  # wait for the session to finish
    
    session.save()  # save the recorded data to disk