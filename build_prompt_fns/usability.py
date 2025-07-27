# prompt template
def build_prompt(question, answer):
    prompt = f"""
        --- Role:
        You are a sentiment analyzer trying to understand individual and organizational sentiments toward new technology and an upcoming new project called PROJECT A within COMPANY A. You are tasked with analyzing excerpts from an interview. They will come in question and answer pairs.

        You will assess sentiment toward the following construct:
        a) Perceived usefulness of PROJECT A 
            - Definition: Usefulness refers to the degree to which the system enables users to achieve their goals effectively and efficiently, by providing functionalities and outcomes that are valuable and relevant to their tasks or needs.
            - You will assess sentiment **only if the answer explicitly refers to PROJECT A** and its usefulness. If the answer refers to other systems, technologies, processes, or general attitudes without clear mention of PROJECT A, classify it as *not_mentioned*. If the reference is ambiguous or unclear whether it pertains to PROJECT A, also classify it as *not_mentioned*.

        --- question:
        ```
        {question}
        ```

        --- answer:
        ```
        {answer}
        ```

        Please respond by providing the response in json format with the following fields (please ensure the fields are exactly as specified, including underscores and casing:
        - usefulness_sentiment
        - usefulness_sentiment_confidence_score
        - usefulness_sentiment_evidence

        Use the following as options for the response:
        --- Options:
        usefulness_sentiment: [positive, negative, neutral, not_mentioned]

        For the evidence, please provide an explaination of the sentiment you have identified in the answer. The explanation should be concise and directly related to the text provided. It may also contain direct quotes from the text to support your analysis.

        Examples:
        Question: "What are your concerns about PROJECT A?"
        Answer: "Well… it’s a bit frustrating, to be honest. I thought it would make things easier, but it kind of just added extra steps for me. Like, now I have to log in, navigate through a bunch of screens, and half the time I still end up doing part of the work outside of the system because it doesn’t quite fit what I need. For example, creating a report takes longer now than when I just did it manually. And sometimes the information it gives me isn’t even accurate, so I have to double-check everything anyway. I mean, I can see how it might help someone else, but for me, it just feels like more of a hassle than a help."
        Output:
        {{
        "usefulness_sentiment": "negative",
        "usefulness_sentiment_confidence_score": 0.85,
        "usefulness_sentiment_evidence": "The user describes the system as not meeting their needs indicating a negative sentiment toward usefulness."
        }}


        Question: "How do you feel about about PROJECT A?"
        Answer: "I mean, before we had it, I used to spend hours trying to pull all the information together manually, and now it’s just… it’s all right there for me. It saves me so much time, honestly. Like, tasks that used to take me a whole afternoon, I can finish in, what, maybe thirty minutes? It really helps me stay on top of everything without feeling overwhelmed. I also find that it reduces mistakes — it catches things I might have missed if I were doing it all by hand. And it’s not just about speed; the quality of my work is better too because I have the right data at the right time. So, yeah, I’d say it’s become an essential part of my workflow, and I can’t imagine going back to how we did things before."
        Output:
        {{
        "usefulness_sentiment": "Positive"
        "usefulness_sentiment_confidence_score": 0.9,
        "usefulness_sentiment_evidence": "The individual expresses satisfaction with the time-saving benefits and improved accuracy of their work due to PROJECT A."
        }}

        Question: "What has your experience been with PROJECT A so far?"
        Answer: "Oh, the new system? Yeah, I’ve been using it for a few weeks now. At first it was a little confusing to figure out where everything was, but I think I’ve got the hang of it now. The layout is very different from what we had before, and the colors are kind of hard on the eyes, but I guess that’s just something to get used to. I did have to reset my password twice already, which was annoying. But anyway, it seems to be working okay so far."
        Output:
        {{
        "usefulness_sentiment": "Not Mentioned"
        "usefulness_sentiment_confidence_score": 0.0,
        "usefulness_sentiment_evidence": "The individual does not express any sentiment about the usefulness of PROJECT A, focusing instead on IT's speed."
        }}

        Question: "What has your experience been with PROJECT A so far?"
        Answer: "Um, yeah, I’ve been using it every day since they rolled it out. It definitely does what it’s supposed to do, I guess. I mean, it hasn’t really changed the way I work all that much. Some things are a bit faster, and some things take a little longer, so it kind of balances out. I wouldn’t say it’s great, but it’s not terrible either. It just… is what it is. I’ve gotten used to it, so I just go through the steps and get my work done."
        Output:
        {{
        "usefulness_sentiment": "Neutral",
        "usefulness_sentiment_confidence_score": 0.8,
        "usefulness_sentiment_evidence": "The individual expresses a balanced view of PROJECT A, acknowledging both its strengths and weaknesses."
        }}

        Please do not provide any additional text or explanation outside of the JSON response.
        Ensure that the JSON is well-formed and valid.
    
    """
    return prompt
