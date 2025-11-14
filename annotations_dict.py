# Map button codes (IDs) to human-readable labels
EVENT_LABELS = {
    # Locatie
    "E-01-02-01": "Livingroom",
    "E-01-02-02": "Hallway",
    "E-01-02-03": "Outside",
    "E-01-02-04": "Bedroom",
    "E-01-02-05": "Bathroom",
    "E-01-02-06": "Stairs",
    "E-XX-XX-XX": "Other (location)",

    # Staat
    "P-00-XX-01": "Sitting",
    "P-00-XX-02": "Standing",
    "P-00-XX-03": "Lying",
    "P-00-XX-04": "Walking",
    "P-00-XX-05": "Sleeping",
    "P-00-XX-06": "Dozing",
    # P-XX-XX-XX aparece em vários grupos; não dá para distinguir no banco
    "P-XX-XX-XX": "Other",

    # Activiteit (ADL)
    "I-01-XX-01": "Using object",
    "I-01-XX-02": "Eating",
    "I-01-XX-03": "Drinking",
    "I-01-XX-04": "Social interaction",
    "I-01-XX-05": "Nursing",
    "I-01-XX-06": "Toileting",
    "I-01-XX-07": "Showering",
    "I-XX-XX-XX": "Other (activity)",

    # Geluid
    "P-01-XX-01": "Shouting",
    "P-01-XX-02": "Laughing",
    "P-01-XX-03": "Singing",
    "P-01-XX-04": "Crying",
    "P-01-XX-05": "Repetitive",

    # Beweging
    "P-01-XX-06": "Clapping",
    "P-01-XX-07": "Rubbing",
    "P-01-XX-08": "Tapping",
    "P-01-XX-09": "Swinging",
    "P-01-XX-10": "Dressing/undressing",
    "P-01-XX-11": "Beating",
    "P-01-XX-12": "Pushing",
    "P-01-XX-13": "Kicking",
    "P-01-XX-14": "Shaking",
    "P-01-XX-15": "Picking",

    # Events
    "E-03-XX-01": "Someone enters",
    "E-03-XX-02": "Someone leaves",
    "E-03-01-01": "Radio on",
    "E-03-01-02": "Radio off",
    "E-03-02-01": "Tv on / Loud noise",  # id duplicado no HTML
    "E-03-02-02": "Tv off",
    "E-03-XX-03": "Changing behaviour (someone else)",

    # Slider (Crisis Ontwikkeling Model – nível)
    "P-00-XX-99": "Crisis level 0",
    "P-00-XX-98": "Crisis level 1",
    "P-00-XX-97": "Crisis level 2",
    "P-00-XX-96": "Crisis level 3",
}
