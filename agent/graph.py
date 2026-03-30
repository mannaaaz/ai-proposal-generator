from langchain_openai import ChatOpenAI
from agent.prompts import PROPOSAL_PROMPT
from agent.tools import update

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o")

def generate_proposal(template, project_description, client_problem, your_solution, timeline, your_experience, tone):
    
    prompt = PROPOSAL_PROMPT.format(
        template=template,
        project_description=project_description,
        client_problem=client_problem,
        your_solution=your_solution,
        timeline=timeline,
        your_experience=your_experience,
        tone=tone
    )

    response = model.invoke(prompt)

    return update.invoke(response.content)