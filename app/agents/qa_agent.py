from crewai import Agent

def get_qa_agent():
    return Agent(
        role="QA Analyst",
        goal="Validate outputs and ensure correctness",
        backstory="Expert in validation",
        verbose=True
    )