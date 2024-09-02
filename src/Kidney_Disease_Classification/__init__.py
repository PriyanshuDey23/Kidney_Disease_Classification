import os,sys,logging

# Custom Logging

logging_str='[%(asctime)s: %(levelname)s: %(module)s: %(message)s]' #  level name:- information related to log

log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log") # running_logs.log :- all the log information will be created
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,  # Information related to log
    format=logging_str,  # Log str

    handlers=[
        logging.FileHandler(log_filepath), # Create the log file
        logging.StreamHandler(sys.stdout) # print Log inside the terminal
    ]    
)

logger=logging.getLogger("Kidney_Disease_Classification")