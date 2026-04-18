from crewai import Crew
from app.agents.research_agent import get_research_agent
from app.agents.data_agent import get_data_agent
from app.agents.ml_agent import get_ml_agent
from app.agents.insight_agent import get_insight_agent
from app.agents.report_agent import get_report_agent
from app.agents.qa_agent import get_qa_agent
from app.tasks.pipeline import create_tasks

def run_pipeline():

    research = get_research_agent()
    data = get_data_agent()
    ml = get_ml_agent()
    insight = get_insight_agent()
    report = get_report_agent()
    qa = get_qa_agent()

    agents = [research, data, ml, insight, report, qa]

    tasks = create_tasks(agents)

    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    return result