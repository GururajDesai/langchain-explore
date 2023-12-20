import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linked_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import summary_parser, Summary


def llm_exlore_func(name: str) -> Summary:
    linked_in_profile_url = linkedin_lookup_agent(name=name)

    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. one interesting fact about them
        \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },  # which are already available before the chain runs
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linked_profile(linked_in_profile_url)

    res = chain.run(information=linkedin_data)
    return summary_parser.parse(res)


if __name__ == "__main__":
    result = llm_exlore_func("Gururaj Desai")
    print(result)
