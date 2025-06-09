import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "deepseek/deepseek-r1-0528:free",
        "messages": [
        {
            "role": "user",
            "content": "What is the meaning of life?"
        }
        ],
        
    })
)
print(response.json())