# prompt template
def build_prompt(question, answer):
    prompt = f"""
        --- Role:
        You are a sentiment analyzer trying to understand individual and organizational sentiments toward new technology and an upcoming new project called PROJECT A within COMPANY A. You are tasked with analyzing excerpts from an interview. They will come in question and answer pairs.

        You will assess sentiment toward the following construct:
        a) Perceived increase in workload due to PROJECT A
            - Definition: Perceived increase in workload refers to the extent to which users feel that PROJECT A adds more work, steps, or effort to their tasks compared to their previous workflow. This includes feelings that tasks take longer or require more actions as a result of using PROJECT A.
            - You will assess sentiment **only if the answer explicitly refers to PROJECT A** and its impact on workload. If the answer refers to other systems, technologies, processes, or general attitudes without clear mention of PROJECT A, classify it as *not_mentioned*. If the reference is ambiguous or unclear whether it pertains to PROJECT A, also classify it as *not_mentioned*.

        --- question:
        ```
        {question}
        ```

        --- answer:
        ```
        {answer}
        ```

        Please respond by providing the response in json format with the following fields (please ensure the fields are exactly as specified, including underscores and casing):
        - workload_sentiment
        - workload_sentiment_confidence_score
        - workload_sentiment_evidence

        Use the following as options for the response:
        --- Options:
        workload_sentiment: [positive, negative, neutral, not_mentioned]

        For the evidence, please provide an explanation of the sentiment you have identified in the answer. The explanation should be concise and directly related to the text provided. It may also contain direct quotes from the text to support your analysis.

        Examples:
        Question: "What are your concerns about PROJECT A?"
        Answer: "It’s been really hard, honestly. I thought it would save time, but now I have to enter everything twice and double-check because the system sometimes glitches. Tasks that used to take me an hour now take two."
        Output:
        {{
        "workload_sentiment": "negative",
        "workload_sentiment_confidence_score": 0.9,
        "workload_sentiment_evidence": "The user describes having to enter data twice and longer task times, indicating a perceived increase in workload."
        }}

        Question: "How do you feel about PROJECT A?"
        Answer: "Before, I had to do everything manually, but now it handles most of it for me. I feel like it actually lightened my load. I can finish tasks faster and with fewer steps."
        Output:
        {{
        "workload_sentiment": "positive",
        "workload_sentiment_confidence_score": 0.9,
        "workload_sentiment_evidence": "The individual reports that PROJECT A reduces the amount of work and makes tasks faster, suggesting a decreased workload."
        }}

        Question: "What has your experience been with PROJECT A so far?"
        Answer: "Well, it kind of evens out. Some things are quicker now, but others are more complicated. Overall, it feels about the same as before."
        Output:
        {{
        "workload_sentiment": "neutral",
        "workload_sentiment_confidence_score": 0.8,
        "workload_sentiment_evidence": "The individual mentions both increases and decreases in workload that balance each other out."
        }}

        Question: "What has your experience been with PROJECT A so far?"
        Answer: "Oh, the system? Yeah, I’ve been using it for a few weeks. It looks different and took a while to learn, but I can use it fine now."
        Output:
        {{
        "workload_sentiment": "not_mentioned",
        "workload_sentiment_confidence_score": 0.0,
        "workload_sentiment_evidence": "The individual talks about the system's appearance and learning curve but does not mention its impact on workload."
        }}

        Please do not provide any additional text or explanation outside of the JSON response.
        Ensure that the JSON is well-formed and valid.
    
    """
    return prompt
