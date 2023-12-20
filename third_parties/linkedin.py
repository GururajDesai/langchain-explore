import requests
import json
import os

mock_response_url = ""

def mock_scrape_linked_profile(linkedin_profile_url: str):
    """
    scrape information from linkedin profiles.
    Manually scrape the information from the linkedIn profile
    """
    data = None
    with open("./third_parties/eden_marco_mock.json") as json_data:
        data = json.load(json_data)

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", " ", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


def scrape_linked_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
