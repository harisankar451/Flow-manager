def fetch_data():
    #Logic for Task1 
    print("Action: Fetching data from source...")
    return "success"

def process_data():
    #Logic for Task2 
    print("Action: Processing raw data...")
    return "success"

def store_data():
    #Logic for Task3 
    print("Action: Storing processed data in database...")
    return "success"

# Mapping names from JSON to Python functions 
TASK_REGISTRY = {
    "task1": fetch_data,
    "task2": process_data,
    "task3": store_data
}