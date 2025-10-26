import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-demos!")
    print(os.getenv("OPENAI_API_KEY"))

information = """
    Elon Reeve Musk is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, Twitter, and xAI. Musk has been the wealthiest person in the world since 2021; as of October 2025, Forbes estimates his net worth to be US$500 billion.

    Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he had obtained Canadian citizenship at birth through his Canadian-born mother. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen.

    In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence (AI) research, but later left; growing discontent with the organization's direction and their leadership in the AI boom in the 2020s led him to establish xAI. In 2022, he acquired the social network Twitter, implementing significant changes, and rebranding it as X in 2023. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company the Boring Company, which he founded in 2017.
"""

summary_template = f"""
    Given the information {information} about aperson I want to create:
    1. A shot summary
    2. Two inetresting facts about him/her
"""

summary_prompt_template = PromptTemplate(
    template=summary_template,
    input_variables=["information"]
)

#lm = ChatOpenAI(model="gpt-5", temperature=0)
llm = ChatOllama(model="gemma3:270m")
chain = summary_prompt_template | llm

result = chain.invoke(input={"information": information})
print(result.content)


if __name__ == "__main__":
    main()
