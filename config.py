########  GENERAL APP INFORMATION  ##############

APP_TITLE = None
# APP_TITLE = "SC4x | Week 10 | Case Study | ML 2"

APP_INTRO = None
# APP_INTRO = """This app uses an AI API (OpenAI, Gemini, or Claude) to provide feedback on an open response question about machine learning: Which classification algorithm(s) would you use?"""

APP_HOW_IT_WORKS = None
# APP_HOW_IT_WORKS = """ """

SHARED_ASSET = {}
# SHARED_ASSET = {
#     "name":"NAME",
#     "path":"FILE.pdf",
#     "button_text":"Read this PDF first"
# }

HTML_BUTTON = {}

COMPLETION_MESSAGE = "Thank you for submitting a response!"
COMPLETION_CELEBRATION = False

SCORING_DEBUG_MODE = False

 ####### PHASES INFORMATION #########

PHASES = {
    "attempt1": {
        "type": "text_area",
        "height": 200,
        "label": """What classification algorithm(s) would you use?""",
        "instructions": """ The students are using machine learning for a classification problem. They have only learned about these specific algorithms in the course: tree models, random forest, Naïve Bayes, and K-nearest neighbor (kNN). They are asked to briefly describe which machine learning algorithms they would use to predict if an order may be delivered late or not. Evaluate their response and provide feedback about the algorithms they propose within the context of the specific algorithms they have learned (described above). Suggest additional algorithms if they do not mention all four (tree models, random forest, Naïve Bayes, and K-nearest neighbors). This is the student's first submission. They can follow up two more times. """,
        "value": " ",
        "scored_phase": False,
        "rubric": """
            None
        """,
        "minimum_score": 2
    },
    "attempt2": {
        "type": "text_area",
        "height": 200,
        "label": """Do you have any follow up comments or want clarification on the previous feedback?""",
        "instructions": """ The students are using machine learning for a classification problem. They have only learned about these specific algorithms in the course: tree models, random forest, Naïve Bayes, and K-nearest neighbor (kNN). They are asked to briefly describe which machine learning algorithms they would use to predict if an order may be delivered late or not. Evaluate their response and provide feedback about the algorithms they propose within the context of the specific algorithms they have learned (described above). Suggest additional algorithms if they do not mention all four (tree models, random forest, Naïve Bayes, and K-nearest neighbors). This is the student's second submission. They can follow up one more times. """,
        "value": " ",
        "scored_phase": False,
        "rubric": """
            None
        """,
        "minimum_score": 2
    },
    "attempt3": {
        "type": "text_area",
        "height": 200,
        "label": """Do you have any follow up comments or want clarification on the previous feedback?""",
        "instructions": """ The students are using machine learning for a classification problem. They have only learned about these specific algorithms in the course: tree models, random forest, Naïve Bayes, and K-nearest neighbor (kNN). They are asked to briefly describe which machine learning algorithms they would use to predict if an order may be delivered late or not. Evaluate their response and provide feedback about the algorithms they propose within the context of the specific algorithms they have learned (described above). Suggest additional algorithms if they do not mention all four (tree models, random forest, Naïve Bayes, and K-nearest neighbors). This is the student's last submission. They can't ask again. """,
        "value": " ",
        "scored_phase": False,
        "rubric": """
            None
        """,
        "minimum_score": 2
    },
}

######## AI CONFIGURATION #############

########## AI ASSISTANT CONFIGURATION #######
ASSISTANT_NAME = "sc4x_wk10_CaseStudy_ML"
ASSISTANT_INSTRUCTIONS = """ You are an expert in machine learning and the instructor of a course where students are learning the basics of machine learning. """

LLM_CONFIGURATION = {
    "gpt-4-turbo":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-4-turbo",
        "temperature":0,
        "price_per_1k_prompt_tokens":.01,
        "price_per_1k_completion_tokens": .03
    },
    "gpt-4o":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-4o",
        "temperature":0,
        "price_per_1k_prompt_tokens":.0025,
        "price_per_1k_completion_tokens": .010
    },
    "gpt-3.5-turbo":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-3.5-turbo-0125",
        "temperature":0,
        "price_per_1k_prompt_tokens":0.0005,
        "price_per_1k_completion_tokens": 0.0015
    }
}

ASSISTANT_THREAD = ""
ASSISTANT_ID_FILE = "assistant_id.txt"