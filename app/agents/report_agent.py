from crewai import Agent

def get_report_agent():
    return Agent(
        role="Report Writer",
        goal="Generate final business report",
        backstory="Expert in storytelling with data",
        verbose=True
    )