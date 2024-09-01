system_prompt = """
    You are an expert image recognizer. 
    
    Your task is to recognize the image and return the most relevant information. 
    
    Cover every little detail given in the image in your response.
"""

image_recognizer_prompt_template = [
    ("system", system_prompt),
    (
        "user",
        [
            {
                "type": "image_url",
                "image_url": {"url": "{image_url}"},
            }
        ],
    ),
]
