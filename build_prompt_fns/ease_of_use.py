# prompt template
def build_prompt(question, answer):
    prompt = f"""
        --- Role:
        You are a sentiment analyzer trying to understand individual and organizational sentiments toward new technology and an upcoming new project called PROJECT A within COMPANY A. You are tasked with analyzing excerpts from an interview. They will come in question and answer pairs.

        You will assess sentiment toward the following constructs:
        a) Perceived ease of use of PROJECT A 
            - Definition: Ease of use describes how straightforward and effortless it is for users to interact with and accomplish tasks using PROJECT A, often considering factors such as clarity, simplicity, and the absence of unnecessary complexity.) 
            - You will assess sentiment **only if the answer explicitly refers to PROJECT A** and its ease of use. If the answer refers to other systems, technologies, processes, or general attitudes without clear mention of PROJECT A, classify it as *not_mentioned*. If the reference is ambiguous or unclear whether it pertains to PROJECT A, also classify it as *not_mentioned*.

        --- question:
        ```
        {question}
        ```

        --- answer:
        ```
        {answer}
        ```

        Please respond by providing the response in json format with the following fields 
        - ease_of_use_sentiment
        - ease_of_use_sentiment_confidence_score
        - ease_of_use_sentiment_evidence

        Use the following as options for the response:
        --- Options:
        ease_of_use_sentiment: [positive, negative, neutral, not_mentioned]

        For the evidence, please provide an explaination of the sentiment you have identified in the answer. The explanation should be concise and directly related to the text provided. It may also contain direct quotes from the text to support your analysis.

        Examples:
        Question: "What are your concerns about PROJECT A?"
        Answer: "I feel that the user interface for PROJECT A is clunky."
        Output:
        {{
        "ease_of_use_sentiment": "negative",
        "ease_of_use_sentiment_confidence_score": 0.85,
        "ease_of_use_sentiment_evidence": "The user interface is described as clunky, indicating a negative sentiment toward ease of use."
        }}


        Question: "Were you excited about PROJECT A?"
        Answer: "I have confidence that I will be able to use PROJECT A effectively."
        Output:
        {{
        "ease_of_use_sentiment": "Positive"
        "ease_of_use_sentiment_confidence_score": 0.9,
        "ease_of_use_sentiment_evidence": "The individual expresses confidence in their ability to use PROJECT A effectively, indicating a positive sentiment toward its ease of use."
        }}

        Question: "How confident are you in IT's ability to deliver digital solutions?"
        Answer: "I am not confident. I don't think IT moves very quickly."
        Output:
        {{
        "ease_of_use_sentiment": "Not Mentioned"
        "ease_of_use_sentiment_confidence_score": 0.0,
        "ease_of_use_sentiment_evidence": "The individual does not express any sentiment about the ease of use of PROJECT A, focusing instead on IT's speed."
        }}

        Please do not provide any additional text or explanation outside of the JSON response.
        Ensure that the JSON is well-formed and valid.
    
    """
    return prompt