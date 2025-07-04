from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd
import os

os.environ["OPENAI_API_KEY"] = "your-api-key"

df = pd.read_csv("cleaned_retail_data.csv")
llm = OpenAI(temperature=0)

agent = create_pandas_dataframe_agent(llm, df, verbose=True)

query = "What are the top 5 cities by total profit?"
response = agent.run(query)

print(response)
