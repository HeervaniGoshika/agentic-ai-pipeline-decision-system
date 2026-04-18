from crewai import Agent

def get_insight_agent():
    return Agent(
        role="Data Analyst",
        goal="Generate insights and visualizations",
        backstory="Expert in analytics",
        verbose=True
    )