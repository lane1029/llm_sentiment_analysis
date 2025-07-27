# prompt template
def build_prompt(question, answer):
    prompt = f"""
        --- Role:
        You are a sentiment analyzer trying to understand how an interviewee perceives the level of organizational cynicism within their organization. You are tasked with analyzing excerpts from an interview. They will come in question and answer pairs.

        You will assess sentiment toward the following construct:
        a) Perceived organizational cynicism
            - Definition: Perceived organizational cynicism refers to the extent to which the interviewee perceives that members of the organization express distrust, skepticism, or a generally negative attitude toward organizational initiatives, leadership decisions, or stated goals. This includes comments suggesting that people in the organization doubt the benefits of changes, question the motives of leadership, assume initiatives will fail, or feel disengaged or disillusioned.
            - You will assess sentiment only if the answer explicitly refers to the organization's collective attitude. If the answer refers only to the interviewee’s personal feelings, or to attitudes unrelated to the organization as a whole, classify it as *not_mentioned*. If it is ambiguous whether the statement pertains to organizational cynicism, also classify it as *not_mentioned*.

        --- question:
        ```
        {question}
        ```

        --- answer:
        ```
        {answer}
        ```

        Please respond by providing the response in JSON format with the following fields (please ensure the fields are exactly as specified, including underscores and casing):
            - cynicism_sentiment
            - cynicism_sentiment_confidence_score
            - cynicism_sentiment_evidence

        Use the following as options for the response:
        --- Options:
            cynicism_sentiment: [positive, negative, neutral, not_mentioned]

        Definitions for sentiment:
            - positive: The organization is perceived as optimistic, trusting, or supportive of its initiatives and leadership.
            - negative: The organization is perceived as cynical, skeptical, distrustful, disengaged, or dismissive of its initiatives or leadership.
            - neutral: The organization is perceived as neither particularly supportive nor particularly skeptical; attitudes seem balanced, indifferent, or mixed.
            - not_mentioned: No clear reference is made to the organization's collective attitude or level of cynicism.

        For the evidence, please provide an explanation of the sentiment you have identified in the answer. The explanation should be concise and directly related to the text provided. It may also contain direct quotes from the text to support your analysis.

        Examples:
        Question: "How does the organization react to new initiatives?"
        Answer: "People just roll their eyes whenever leadership announces something new. They think it’s all just for show and nothing will change."
        Output:
        {{
        "cynicism_sentiment": "negative",
        "cynicism_sentiment_confidence_score": 0.9,
        "cynicism_sentiment_evidence": "The interviewee reports that people roll their eyes and believe leadership’s initiatives are superficial and ineffective, indicating organizational cynicism."
        }}

        Question: "How would you describe the team’s attitude toward changes?"
        Answer: "Most people seem to trust that leadership knows what they’re doing and that these changes are for the better."
        Output:
        {{
        "cynicism_sentiment": "positive",
        "cynicism_sentiment_confidence_score": 0.9,
        "cynicism_sentiment_evidence": "The interviewee notes trust in leadership and belief in positive outcomes, suggesting low cynicism and optimism."
        }}

        Question: "What is the general mood in the organization?"
        Answer: "Some people have doubts, some are hopeful — it’s kind of a mix overall."
        Output:
        {{
        "cynicism_sentiment": "neutral",
        "cynicism_sentiment_confidence_score": 0.8,
        "cynicism_sentiment_evidence": "The interviewee describes a balanced mix of skepticism and hopefulness, indicating a neutral level of cynicism."
        }}

        Question: "What do people say about the leadership?"
        Answer: "They mainly talk about their day-to-day work and don’t really mention leadership decisions."
        Output:
        {{
        "cynicism_sentiment": "not_mentioned",
        "cynicism_sentiment_confidence_score": 0.0,
        "cynicism_sentiment_evidence": "The answer focuses on daily work and does not address organizational attitudes or cynicism."
        }}

        --- Ambiguous / Borderline Examples ---

        Question: "What have you heard people say about recent changes?"
        Answer: "Well, everyone keeps saying, ‘here we go again,’ but then they still show up to the meetings and try to make it work."
        Output:
        {{
        "cynicism_sentiment": "neutral",
        "cynicism_sentiment_confidence_score": 0.6,
        "cynicism_sentiment_evidence": "While ‘here we go again’ suggests some skepticism, people still participate and engage, indicating a mixed and moderately neutral attitude."
        }}

        Please do not provide any additional text or explanation outside of the JSON response.
        Ensure that the JSON is well-formed and valid.
    """

    return prompt
