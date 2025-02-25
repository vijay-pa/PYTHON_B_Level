from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()

#NEWS Agent

news_agent = Agent(
    name= "News Agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["search the latest financial news about Nvidia Stocks",
                    "Summarize the top5 news articles",
                    "Provide Key insights in markdown format for read"],
    markdown = True,
    show_tool_calls = True,
    debug_mode = True
)

news_agent.print_response("what is the latest news about Nvidia Stocks",
                        stream = True)  # stream = True will print the output as it comes in)