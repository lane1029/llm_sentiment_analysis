# prompt template
def build_prompt(question, answer):
    prompt = f"""
        --- Role:
        You are a sentiment analyzer tasked with evaluating the interviewee’s sentiment about the perceived *ambiguity* of PROJECT A and only PROJECT A. You are analyzing excerpts from an interview in question and answer pairs.

        You will assess sentiment toward the following construct:
        a) Perceived ambiguity of PROJECT A
            - Definition: Ambiguity refers to the extent to which the interviewee perceives PROJECT A as uncertain, unclear, or difficult to understand — specifically in terms of how it works, how it fits into their workflow, and how it may change their roles and responsibilities. This includes whether they feel unsure about its purpose, its processes, or its impact on their day-to-day work.
            - Options:
                • *Positive*: The interviewee clearly expresses that PROJECT A is clear, well-defined, and easy to understand in terms of its operation, integration into workflow, and implications for their role.
                • *Negative*: The interviewee clearly expresses that PROJECT A is ambiguous, confusing, or uncertain in terms of how it works, how it fits, or how it may change their responsibilities.
                • *Neutral*: The interviewee expresses a mixed, mild, or indifferent view about its ambiguity.
                • *Not_mentioned*: The answer does not clearly reference ambiguity, PROJECT A, or is ambiguous itself.

        --- question:
        ```
        {question}
        ```

        --- answer:
        ```
        {answer}
        ```

        Please respond in JSON format with these fields:
            - ambiguity_sentiment
            - ambiguity_sentiment_confidence_score
            - ambiguity_sentiment_evidence

        Use the following as options:
        --- Options:
            ambiguity_sentiment: [positive, negative, neutral, not_mentioned]

        For the evidence, provide a concise explanation of your assessment, including direct quotes where appropriate.

        Examples:
        Question: "Do you feel like you know how PROJECT A will affect your work?"
        Answer: "Yes, it’s clear what it does and how it fits into what I do."
        Output:
        {{
        "ambiguity_sentiment": "positive",
        "ambiguity_sentiment_confidence_score": 0.95,
        "ambiguity_sentiment_evidence": "The interviewee says 'clear what it does and how it fits,' indicating low ambiguity about its operation and impact."
        }}

        Question: "How clear is PROJECT A to you?"
        Answer: "I’m not sure how it’s supposed to fit in with what we already do, and I don’t know what it means for my job."
        Output:
        {{
        "ambiguity_sentiment": "negative",
        "ambiguity_sentiment_confidence_score": 0.95,
        "ambiguity_sentiment_evidence": "The interviewee says 'not sure how it fits' and 'don’t know what it means for my job,' indicating high perceived ambiguity."
        }}

        Question: "Do you feel confident about PROJECT A?"
        Answer: "In some ways it seems straightforward, but I still don’t fully understand how it would change my responsibilities."
        Output:
        {{
        "ambiguity_sentiment": "neutral",
        "ambiguity_sentiment_confidence_score": 0.9,
        "ambiguity_sentiment_evidence": "The interviewee mentions both clarity and uncertainty, suggesting a mixed view on ambiguity."
        }}

        Question: "What do you think of machine learning in general?"
        Answer: "It’s interesting, but I don’t fully trust it yet."
        Output:
        {{
        "ambiguity_sentiment": "not_mentioned",
        "ambiguity_sentiment_confidence_score": 0.0,
        "ambiguity_sentiment_evidence": "The interviewee does not clearly reference PROJECT A."
        }}
    """

    return prompt
