from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from src.state.state import AgentState
from src.nodes.llm_node import llm_node

builder = StateGraph(AgentState)

builder.add_node("llm", llm_node)

builder.add_edge(START, "llm")
builder.add_edge("llm", END)

graph = builder.compile()