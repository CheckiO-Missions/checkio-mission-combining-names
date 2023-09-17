"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["brad", "angelina"],
            "answer": "brangelina",
        },
        {
            "input": ["angelina", "brad"],
            "answer": "angelad",
        },
        {
            "input": ["sheldon", "amy"],
            "answer": "shamy",
        },
    ],
    "Extra": [
        {
            "input": ["amy", "sheldon"],
            "answer": "eldon",
        },
        {
            "input": ["frank", "ava"],
            "answer": "frava",
        },
        {
            "input": ["britain", "exit"],
            "answer": "brexit",
        },
    ]
}
