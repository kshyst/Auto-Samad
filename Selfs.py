import requests


def get_self_list(token: str):
    url = "https://setad.dining.sharif.edu/rest/selfs"

    response = requests.get(url, headers={"Authorization": f"Bearer {token}"})

    selfs_list = {}

    if response.status_code == 200:
        response = response.json()
        for self in response['payload']:
            selfs_list.update({self['name']: self['id']})
    else:
        print("Error in fetching selfs list")

    return selfs_list
