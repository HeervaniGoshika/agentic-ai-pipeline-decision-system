from crewai import Agent

def get_ml_agent():
    return Agent(
        role="ML Engineer",
        goal="Train and evaluate models",
        backstory="Expert in machine learning",
        verbose=True
    )