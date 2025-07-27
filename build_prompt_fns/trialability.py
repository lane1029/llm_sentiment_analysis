# prompt template
def build_prompt(question, answer):
    prompt = f"""
        --- Role:
        You are a sentiment analyzer tasked with evaluating the interviewee’s sentiment about the perceived *trialability* of PROJECT A. You are analyzing excerpts from an interview in question and answer pairs.

        You will assess sentiment toward the following construct:
        a) Perceived trialability of PROJECT A
            - Definition: Trialability refers to the extent to which PROJECT A can be experimented with, tested, or tried on a limited basis before full adoption. This includes whether the interviewee feels they (or others) have the opportunity to test, pilot, or explore PROJECT A in a low-risk way before committing to full use.
            - Options:
                • *Positive*: The interviewee clearly expresses that PROJECT A is easy to try out, test, or experiment with before full adoption.
                • *Negative*: The interviewee clearly expresses that it is difficult, impossible, or risky to test or experiment with PROJECT A.
                • *Neutral*: The interviewee expresses a mixed, mild, or indifferent view about trialability.
                • *Not_mentioned*: The answer does not clearly reference trialability or is ambiguous.

        --- question:
        ```
        {question}
        ```

        --- answer:
        ```
        {answer}
        ```

        Please respond in JSON format with these fields:
            - trialability_sentiment
            - trialability_sentiment_confidence_score
            - trialability_sentiment_evidence

        Use the following as options:
        --- Options:
            trialability_sentiment: [positive, negative, neutral, not_mentioned]

        For the evidence, provide a concise explanation of your assessment, including direct quotes where appropriate.

        Examples:
        Question: "Were you able to test PROJECT A before fully switching?"
        Answer: "Yes, they let us try it for a few weeks alongside the old system before deciding."
        Output:
        {{
        "trialability_sentiment": "positive",
        "trialability_sentiment_confidence_score": 0.95,
        "trialability_sentiment_evidence": "The interviewee says 'they let us try it for a few weeks,' indicating positive trialability."
        }}

        Question: "Did you feel like you could test PROJECT A before committing?"
        Answer: "Not really, we had to start using it immediately without any kind of pilot."
        Output:
        {{
        "trialability_sentiment": "negative",
        "trialability_sentiment_confidence_score": 0.95,
        "trialability_sentiment_evidence": "The interviewee states 'we had to start using it immediately,' indicating poor trialability."
        }}

        Question: "How much opportunity was there to test PROJECT A?"
        Answer: "Some parts we could test, but others we just had to jump in."
        Output:
        {{
        "trialability_sentiment": "neutral",
        "trialability_sentiment_confidence_score": 0.9,
        "trialability_sentiment_evidence": "The interviewee mentions both testing and immediate use, suggesting mixed trialability."
        }}

        Question: "Was there a chance to try PROJECT A before full rollout?"
        Answer: "I’m not sure, I just started using it when they told me to."
        Output:
        {{
        "trialability_sentiment": "not_mentioned",
        "trialability_sentiment_confidence_score": 0.0,
        "trialability_sentiment_evidence": "The interviewee does not clearly reference trialability."
        }}
    """

    return prompt
