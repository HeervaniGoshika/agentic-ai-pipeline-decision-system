from crewai import Agent

def get_research_agent():
    return Agent(
        role="Research Analyst",
        goal="Understand dataset and define ML problem",
        backstory="Expert in business and data understanding",
        verbose=True
    )