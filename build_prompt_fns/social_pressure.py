# prompt template
def build_prompt(question, answer):
    prompt = f"""
        --- Role:
        You are a sentiment analyzer tasked with evaluating the direction of social pressure the interviewee perceives from others in the organization regarding technological change **NOT specific to PROJECT A**. You are analyzing excerpts from an interview in question and answer pairs.

        You will assess sentiment toward the following construct:
        a) Direction of perceived social pressure
            - Definition: This refers to whether the interviewee perceives that others in the organization are encouraging them to adopt and embrace technological change (*positive*), discouraging or resisting technological change (*negative*), expressing attitudes that are neither strongly supportive nor resistant (*neutral*), or not mentioning others’ influence (*not_mentioned*). 
            - Options:
                • *Positive*: Others clearly express support, encouragement, or expectations to change.
                • *Negative*: Others clearly express resistance, discouragement, or opposition to change.
                • *Neutral*: Others are mentioned as having mixed, mild, or indifferent views toward change.
                • *Not_mentioned*: The answer does not clearly reference others’ influence or is ambiguous.

        --- question:
        ```
        {question}
        ```

        --- answer:
        ```
        {answer}
        ```

        Please respond in JSON format with these fields:
            - social_pressure_sentiment
            - social_pressure_sentiment_confidence_score
            - social_pressure_sentiment_evidence

        Use the following as options:
        --- Options:
            social_pressure_sentiment: [positive, negative, neutral, not_mentioned]

        For the evidence, provide a concise explanation of your assessment, including direct quotes where appropriate.

        Examples:
        Question: "How do others react to you adopting the new system?"
        Answer: "Everyone keeps telling me I need to use it and stop using the old one."
        Output:
        {{
        "social_pressure_sentiment": "positive",
        "social_pressure_sentiment_confidence_score": 0.95,
        "social_pressure_sentiment_evidence": "The interviewee says 'everyone keeps telling me I need to use it,' indicating supportive social pressure."
        }}

        Question: "Do you feel your coworkers want you to change your methods?"
        Answer: "Actually, they all keep saying the old way was better and that I should just ignore the new system."
        Output:
        {{
        "social_pressure_sentiment": "negative",
        "social_pressure_sentiment_confidence_score": 0.95,
        "social_pressure_sentiment_evidence": "The interviewee reports others saying 'the old way was better,' indicating resistance."
        }}

        Question: "What do you hear from others about changing your approach?"
        Answer: "Some people think it’s great and others say it’s a waste of time."
        Output:
        {{
        "social_pressure_sentiment": "neutral",
        "social_pressure_sentiment_confidence_score": 0.9,
        "social_pressure_sentiment_evidence": "The interviewee mentions both positive and negative opinions, indicating a neutral or mixed sentiment."
        }}

        Question: "Do you feel influenced by others when deciding whether to change?"
        Answer: "I just decide for myself."
        Output:
        {{
        "social_pressure_sentiment": "not_mentioned",
        "social_pressure_sentiment_confidence_score": 0.0,
        "social_pressure_sentiment_evidence": "The interviewee claims independence and does not reference others’ influence."
        }}
    """

    return prompt
