import requests
import json

mock_response_url = ""


def scrape_linked_profile(linkedin_profile_url: str):
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
