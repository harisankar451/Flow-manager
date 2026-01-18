from app.tasks import TASK_REGISTRY


class FlowManager:
    def __init__(self, flow_config):
        self.flow = flow_config
        #Create a dictionary to quickly find the rule for any task
        self.conditions = {}
        
        #Loop through each condition defined in the JSON
        for condition in self.flow.conditions:
            #Map the task name to its specific success/failure rules
            self.conditions[condition.source_task] = condition
            
        
    def execute(self):
        current_task_name = self.flow.start_task 
        history = []

        while current_task_name and current_task_name != "end":
            
            task_func = TASK_REGISTRY.get(current_task_name)
            if not task_func:
                break
            
            #Execute the actual task logic (fetch, process, or store) 
            result = task_func() 
            history.append({"task": current_task_name, "result": result})
            
            condition = self.conditions.get(current_task_name)
            if not condition:
                #Terminate task with no further conditions 
                break

            #Move to next task or terminate 
            if result == condition.outcome:
                current_task_name = condition.target_task_success 
            else:
                current_task_name = condition.target_task_failure 
        
        return history