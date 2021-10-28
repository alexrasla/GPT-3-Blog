

- Introduction
    - Novelty
        - a 175 billion parameter autoregressive language model, same model as GPT2
        - larger batch size and smaller learning rate
        - trained on Common Crawl dataset, 1 trillion words, but filtered to prevent redundancy and make sure text was human curated to prevent data contamination
        - does not overfit to common crawl (contamination is likely, but not as harmful)
        - tested using fine tuning, few shot, one shot, zero shot (amount of demonstrations used for in context analysis)
            - no gradient updates or fine tuning in shots, just demonstrations 
                - these methods best simulate actual human learning and behavior, not just training to do a specific task
                - humans have wide knowledge of language and need ot know when and how to apply it
                - few shot advantage is major reduction need for tast specific data
                - one shot is most is most sysnonymous to human like learning
                - zero shot is most convenient

- Use cases
    - a plethory of use cases
        - each use case tested on zero, one, and few shot 
        - i will focus on few shot since that is the novelty in this paper
    - completing a word, sentence or paragraph
        - 86.4% accuracy in few shot, over 18% increase in accuracy
    - translation, trained on 93% english 7% other, show graph and bleu score
        - trained by mixing many natural languages blended together on a word sentence adn document levle
        - translation into english was more accurate and stronger than other way
        - outperforms previous supervised nmt work by 5 blue 
    - news article generation
        - given human written articles and reliably generated short articles in the news genre
        - human ability to detect model generated text decreased as model size increased
    
    - learning andu utilizig new words
        - qualitative analysis shows correct or plausible usage of the word 
    - computational reasoning, reocgnizing a novel pattern
        - SAT style questions, analogies achieved 65.2% (whereas college applicants was 57% )
        - performs well on 2 to 3 digit computation, but rapidly declines with more operations

       - answering questions about some facts
        - 71.2% accuracy 
    - common sense reasoning, reading comprehension, knowledge question answering
        - 82.8%, 79.4% accuracy prior state-of-the-art 

    - which word a pronoun refers to
        - 88.6%, just a few points below state of the art
    - natural language inference, ability to understand the relationship between two sentences
        - only largest version performs better than random 56%

- Case Study
    - translate english into slovak?

    - Limitations/Future work
    - Text synthesis is gramatically sounds and readable, but is sometimes repetivite, incorehert, and contradictory
        - Could be solved by biderectinoality, re-reading 
             - Bidirectionaly models could be promising future study on large scale models like GPT3
        - Ambuiguity if few-shot actually learns new tasks at inference time, or just recognizes tasks from trainnig period
        - Expensive to perform inference on such large scale models
            - Distillation to managable size for specific tasks
- Conclusion
    - Potentially harmful
        - anything that uses text generation can be very harmful (social hacking), phishing
            - as models get better this get more dangerous
        - bais, gender discrimination, race discrimination
    - impriving pretraining sample efficiency
    
    
- still lacking in comprehension and meaning
