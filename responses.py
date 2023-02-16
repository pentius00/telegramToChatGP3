from datetime import datetime

def sample_response(input_text):
    user_message  = str(input_text).lower()
    
    if user_message in("hello","hi","sup"):
        return "hey"
    
    if user_message in ("who are you"):
        return "im a bot "
    
    if usser_message in ("time ", ):
        now = datetime.now()
        date_time = now.strftime("d%/%m/%y","%H:%M:%S:")
        
        return str(date_time)
    
        return "error"