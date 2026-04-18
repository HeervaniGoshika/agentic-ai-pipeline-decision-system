from crewai import Agent

def get_data_agent():
    return Agent(
        role="Data Engineer",
        goal="Clean and preprocess data",
        backstory="Expert in data cleaning and feature engineering",
        verbose=True
    )