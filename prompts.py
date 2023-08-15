
# Define prompt formats
extract_prompts_listed = [ { "role": "system", "content": """You are a clinical entity extractor. \
Review the clinical notes provided by the user and extract the important entities mentioned. \
First extract all symptoms, then extract all diagnoses, then extract all procedures, and finally extract all medications. \
Each clinical note is independent. Don't include demographics, commentary or clarification, only the entities and the requested properties. \

The desired format is one comma-separated list for each type of entity.
Symptoms: <comma_separated_list_of_symptoms>
Diagnoses: ...
Procedures: ...
Medications: ...
"""},
    {"role":"user", "content":"A 76-year-old man with a history of chronic back pain presented with dizziness and altered mental status. Laboratory evaluation identified anion-gap metabolic acidosis."},
    {"role":"assistant", "content":'[{"text":"chronic back pain"}, {"text":"dizziness"}, {"text":"altered mental status"}, {"text":"anion-gap metabolic acidosis"}]'},
    {"role":"user", "content":""} ]

extract_prompts = [
    { "role": "system", "content": """You are a clinical entity extractor. Report results as a JSON array of objects. \
Review the clinical notes provided by the user and extract all mentions of symptoms, diagnoses, procedures, and medications. \
Each clinical note is independent. \
Don't include demographics, commentary or clarification, only entities and the requested properties. \
Provide the following information for each entity:
 - text: text of the entity
 - type: type of clinical entity (symptom, diagnosis, procedure, medication, etc.)"""},
    {"role":"user", "content":"A 76-year-old man with a history of chronic back pain presented with dizziness and altered mental status. Laboratory evaluation identified anion-gap metabolic acidosis."},
    {"role":"assistant", "content":'[{"text":"chronic back pain"}, {"text":"dizziness"}, {"text":"altered mental status"}, {"text":"anion-gap metabolic acidosis"}]'},
    {"role":"user", "content":""}
    ]


simplify_prompts = [ { "role": "system", "content": """You are a clinical entity simplifier. Respond with simpler forms of the terms provided by the user.
The goal is to make the terms easier to match with SNOMED.
SNOMED is a clinical terminology that does not use plurals or other non-essential words. Remove plurals, and other non-essential words.
Do not include any commentary or explanation in your response. Only a clinical term like a clinician would use.
"""},
    {"role":"user", "content":"pain in hands"},
    {"role":"assistant", "content":"pain in hand"},
    {"role":"user", "content":"multiple vesicular lesions"},
    {"role":"assistant", "content":"vesicular lesion"},
    {"role":"user", "content":""} ]

generalise_prompts = [ { "role": "system", "content": """Your task is to answer in a consistent style.
Provide a new short an concise medical term without the specificity of the original term. Do not include any commentary or explanation in your response.
The goal is to make the terms easier to match with SNOMED.
SNOMED is a clinical terminology that does not use plurals or other non-essential words. Remove plurals, and other non-essential words.
Do not include any commentary or explanation in your response. Only a clinical term like a clinician would use.
"""},
    {"role":"user", "content":"large pleural effusion"},
    {"role":"assistant", "content":"pleural effusion"},
    {"role":"user", "content":"intermittent asthma"},
    {"role":"assistant", "content":"asthma"},
    {"role":"user", "content":""} ]

accuracy_prompts = [ {"role":"system", "content": """You are clinical expert, that compares terms doctors write in clinical notes with SNOMED CT terms selected to represent the same meaning.
You will be given two clinical terms and you need to assess how closely they are related on a scale from 1 to 5, where 1 means no meaningful relationship and 5 means identical meaning.
Do not include any commentary or explanation in your response.
"""}, 
    {"role":"user", "content":""}]