from crewai import Task

def create_tasks(agents):

    research, data, ml, insight, report, qa = agents

    task1 = Task(
        description="Analyze dataset and define problem",
        agent=research
    )

    task2 = Task(
        description="Clean and preprocess dataset",
        agent=data
    )

    task3 = Task(
        description="Train ML model and evaluate performance",
        agent=ml
    )

    task4 = Task(
        description="Generate insights and visualizations",
        agent=insight
    )

    task5 = Task(
        description="Write final report",
        agent=report
    )

    task6 = Task(
        description="Validate all outputs",
        agent=qa
    )

    return [task1, task2, task3, task4, task5, task6]