**Flow Manager**

# How do the tasks depend on one another? 
There are three tasks in this project with an outcome of either success or failure. The flow manager uses a dictonary created from the JSON conditions. Task2 depends on Task1 returning "success" outcome. Task3 depends on Task2 returning "success" outcome.

# How is the success or failure of a task evaluated? 
The manager captures the return value of each tasks. It then compares this value to the outcome string defined in the JSON configuration. If it is a match, the manager moves to target_task_success ("task3 or task3). Else if Mismatch, he manager moves to target_task_failure ( "end").

# What happens if a task fails or succeeds?
To satisfy the requirement that Task 3 (Store Data) only runs if all previous tasks succeed, the JSON configuration defines the failure path for Task 1 and Task 2 as "end". This ensures the loop terminates immediately upon any failure.

## Installation and Setup
Recommended IDE Visual Studio Code.
1. Download the project from Github
2. Open the Project folder in VSCode
3. Open the terminal in VSCode and create a virtual environment for python.
    python -m venv venv
4. Give the command to activate virtual environment
    venv\Scripts\activate
5. Install the libraries from requirements files using
    pip install -r requirements.txt
6. For testing
    pytest tests/test.py 
7. Run the project
    uvicorn app.main:app --reload
8. API will be available in http://127.0.0.1:8000/flow-manager
    For API documentation http://127.0.0.1:8000/docs 
    Give the sample json in Postman or API Documentation in the request body. In response we can see the task results.
