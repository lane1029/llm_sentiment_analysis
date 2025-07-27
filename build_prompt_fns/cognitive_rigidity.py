# prompt template
def build_prompt(question, answer):
    prompt = f"""
        --- Role:
        You are a sentiment analyzer trying to understand how an interviewee perceives their own level of cognitive rigidity. You are tasked with analyzing excerpts from an interview. They will come in question and answer pairs.

        You will assess sentiment toward the following construct:
        a) Individual cognitive rigidity
            - Definition: Individual cognitive rigidity refers to the degree to which the interviewee exhibits an unwillingness or difficulty to adapt their thinking, consider alternative perspectives, or change established beliefs and routines. This includes statements indicating inflexibility, resistance to new ideas, insistence on doing things “the usual way,” or discomfort with ambiguity or change.
            - You will assess sentiment only if the answer explicitly refers to the interviewee’s own thoughts, attitudes, or behaviors. If the answer refers only to others, or to organizational-level factors without clear reference to the interviewee, classify it as *not_mentioned*. If it is ambiguous whether the statement pertains to individual cognitive rigidity, also classify it as *not_mentioned*.

        --- question:
        ```
        {question}
        ```

        --- answer:
        ```
        {answer}
        ```

        Please respond by providing the response in JSON format with the following fields (please ensure the fields are exactly as specified, including underscores and casing):
            - cognitive_rigidity_sentiment
            - cognitive_rigidity_sentiment_confidence_score
            - cognitive_rigidity_sentiment_evidence

        Use the following as options for the response:
        --- Options:
            cognitive_rigidity_sentiment: [positive, negative, neutral, not_mentioned]

        For the evidence, please provide an explanation of the sentiment you have identified in the answer. The explanation should be concise and directly related to the text provided. It may also contain direct quotes from the text to support your analysis.

        Examples:
        Question: "How do you approach situations where the usual way doesn’t work?"
        Answer: "I usually try to find a different way to make it work — I don’t mind experimenting."
        Output:
        {{
        "cognitive_rigidity_sentiment": "positive",
        "cognitive_rigidity_sentiment_confidence_score": 0.9,
        "cognitive_rigidity_sentiment_evidence": "The interviewee expresses openness to alternatives and experimentation, indicating cognitive flexibility."
        }}

        Question: "How do you feel about changes to your workflow?"
        Answer: "Honestly, I prefer things to stay the same. I have my way of doing things, and I don’t like adjusting to new processes."
        Output:
        {{
        "cognitive_rigidity_sentiment": "negative",
        "cognitive_rigidity_sentiment_confidence_score": 0.9,
        "cognitive_rigidity_sentiment_evidence": "The interviewee clearly prefers routines and resists changes, suggesting cognitive rigidity."
        }}

        Question: "Would you say you’re open to different perspectives?"
        Answer: "Sometimes, but it really depends on the situation and who’s involved."
        Output:
        {{
        "cognitive_rigidity_sentiment": "neutral",
        "cognitive_rigidity_sentiment_confidence_score": 0.8,
        "cognitive_rigidity_sentiment_evidence": "The interviewee indicates openness in some situations but not consistently, suggesting a neutral stance."
        }}

        Question: "Do you adapt easily to new ideas?"
        Answer: "Well, others usually handle that. I just focus on my part."
        Output:
        {{
        "cognitive_rigidity_sentiment": "not_mentioned",
        "cognitive_rigidity_sentiment_confidence_score": 0.0,
        "cognitive_rigidity_sentiment_evidence": "The response does not address the interviewee’s own openness or rigidity toward new ideas."
        }}

    """

    return prompt
