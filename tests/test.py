import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.tasks import TASK_REGISTRY

client = TestClient(app)

# fixture to provide the JSON flow given in example
@pytest.fixture
def flow_payload():
    return {
        
  "flow": {
    "id": "flow123",
    "name": "Data processing flow",
    "start_task": "task1",
    "tasks": [
      {
        "name": "task1",
        "description": "Fetch data"
      },
      {
        "name": "task2",
        "description": "Process data"
      },
      {
        "name": "task3",
        "description": "Store data"
      }
    ],
    "conditions": [
      {
        "name": "condition_task1_result",
        "description": "Evaluate the result of task1. If successful, proceed to task2; otherwise, end the flow.",
        "source_task": "task1",
        "outcome": "success",
        "target_task_success": "task2",
        "target_task_failure": "end"
      },
      {
        "name": "condition_task2_result",
        "description": "Evaluate the result of task2. If successful, proceed to task3; otherwise, end the flow.",
        "source_task": "task2",
        "outcome": "success",
        "target_task_success": "task3",
        "target_task_failure": "end"
      }
    ]
  }
}
    
#Function to verify success path
def test_success_path(flow_payload, monkeypatch):
    # Simply force all tasks to return success
    monkeypatch.setitem(TASK_REGISTRY, "task1", lambda: "success")
    monkeypatch.setitem(TASK_REGISTRY, "task2", lambda: "success")

    response = client.post("/run-flow", json=flow_payload)
    assert len(response.json()["execution_history"]) == 3
    assert response.json()["execution_history"][-1]["task"] == "task3"

#Function to verify failure path
def test_failure_path(flow_payload, monkeypatch):
    #Force task1 to fail
    monkeypatch.setitem(TASK_REGISTRY, "task1", lambda: "failed")

    response = client.post("/run-flow", json=flow_payload)
    history = response.json()["execution_history"]
    
    #Task3 should not be in history
    assert len(history) == 1
    assert "task3" not in [item["task"] for item in history]