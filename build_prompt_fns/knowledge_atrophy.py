# prompt template
def build_prompt(question, answer):
    prompt = f"""
        --- Role:
        You are a sentiment analyzer tasked with evaluating the interviewee’s sentiment about the perceived *impact of PROJECT A on their knowledge and skills* — specifically whether they believe it will lead to knowledge atrophy. You are analyzing excerpts from an interview in question and answer pairs.

        You will assess sentiment toward the following construct:
        a) Perceived impact of PROJECT A on knowledge atrophy
            - Definition: This refers to the extent to which the interviewee perceives that using PROJECT A will either help them develop and maintain valuable skills or lead to the erosion and loss of their existing knowledge and abilities. 
            - Options:
                • *Positive*: The interviewee clearly expresses that PROJECT A helps them gain or strengthen valuable skills, supports their learning, or improves their expertise.
                • *Negative*: The interviewee clearly expresses that PROJECT A leads to loss of knowledge, makes their skills less relevant, or reduces their opportunities to learn and grow.
                • *Neutral*: The interviewee expresses a mixed, mild, or indifferent view about its effect on their knowledge and skills.
                • *Not_mentioned*: The answer does not clearly reference PROJECT A’s impact on their knowledge, skills, or professional development.

        --- question:
        ```
        {question}
        ```

        --- answer:
        ```
        {answer}
        ```

        Please respond in JSON format with these fields:
            - knowledge_atrophy_sentiment
            - knowledge_atrophy_sentiment_confidence_score
            - knowledge_atrophy_sentiment_evidence

        Use the following as options:
        --- Options:
            knowledge_atrophy_sentiment: [positive, negative, neutral, not_mentioned]

        For the evidence, provide a concise explanation of your assessment, including direct quotes where appropriate.

        Examples:
        Question: "Do you think PROJECT A affects your ability to keep your skills sharp?"
        Answer: "Absolutely, it helps me learn new things and stay up to date."
        Output:
        {{
        "knowledge_atrophy_sentiment": "positive",
        "knowledge_atrophy_sentiment_confidence_score": 0.95,
        "knowledge_atrophy_sentiment_evidence": "The interviewee says 'helps me learn new things and stay up to date,' indicating perceived skill enhancement."
        }}

        Question: "What do you think about PROJECT A’s effect on your expertise?"
        Answer: "It kind of takes over what I used to do myself, so I feel like I’m losing touch with my skills."
        Output:
        {{
        "knowledge_atrophy_sentiment": "negative",
        "knowledge_atrophy_sentiment_confidence_score": 0.95,
        "knowledge_atrophy_sentiment_evidence": "The interviewee says 'losing touch with my skills,' indicating knowledge atrophy."
        }}

        Question: "Does PROJECT A change how you use your knowledge?"
        Answer: "It automates some parts, but I still use my judgment sometimes."
        Output:
        {{
        "knowledge_atrophy_sentiment": "neutral",
        "knowledge_atrophy_sentiment_confidence_score": 0.9,
        "knowledge_atrophy_sentiment_evidence": "The interviewee mentions both automation and continued use of judgment, suggesting a mixed view."
        }}

        Question: "What do you think of machine learning in general?"
        Answer: "It’s interesting, but I don’t fully trust it yet."
        Output:
        {{
        "knowledge_atrophy_sentiment": "not_mentioned",
        "knowledge_atrophy_sentiment_confidence_score": 0.0,
        "knowledge_atrophy_sentiment_evidence": "The interviewee does not clearly reference PROJECT A’s impact on their knowledge or skills."
        }}
    """

    return prompt
