import requests
from datetime import datetime, timezone

# Replace with your Notion API token and database ID
notion_token = "secret_hbwVzTdYwHVM4AwWrNQaBfwSGLkxhZqagzOKJ63cjL6"
database_id = "d8b09fc5ed2841adb8c999082f2910f3"

# Headers for the Notion API request
headers = {
    'Authorization': 'Bearer ' + notion_token,
    'accept': 'application/json',
    'Notion-Version': '2022-06-28',
    'content-type': 'application/json'
}

# Function to get pages from the Notion database
def get_page():
    url = f'https://api.notion.com/v1/databases/{database_id}/query'

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
    data = response.json()
    
    import json
    # Save the response data to a JSON file
    with open("LC.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    return results

# Function to create a new page in the Notion database
def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": database_id}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    print(res.status_code)
    return res


# Define values for data
time = datetime.now().isoformat()
question_type = "Linked List"
lc_url = "https://leetcode.com/problems/add-two-numbers/description/"
diff = "Medium"
S_no = "32"
practice_time = 1
my_expertise = "Couldn't Solve"
title = "2. Add Two Numbers"
remark = "easy question simple logic"

# Define data to be used for creating a new page
data = {
    "Tag": {
        "multi_select": [
            {
                "name": question_type
            }
        ]
    },

    "Question Link": {
        "url": lc_url
    },

    "Level": {
        "select": {
            "name": diff
        }
    },

    "S No.": {
        "rich_text": [
            {
                "text": {
                    "content": S_no
                }
            }
        ]
    },

    "No. of times practiced": {
        "number": practice_time
    },

    "My Expertise": {
        "select": {
            "name": my_expertise
        }
    },

    "Remark": {
        "rich_text":[
            {
                "text": {
                    "content": remark
                }
            }
        ]
    },

    "Question": {
        "title": [
            {
                "text": {
                    "content": title
                }
            }
        ]
    }
}

# Call the create_page function with the defined data
create_page(data)
