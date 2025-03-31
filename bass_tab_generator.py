import random

key_maps ={
    "E Major":{
        "E":[0,2,4],
        "A":[0,2,4],
        "D":[1,2,4],
        "G":[1,3,4]
    },
    "A Major":{
        "E":[0,1,4],
        "A":[0,2,4],
        "D":[1,4],
        "G":[0,2,4]
    },
    "G Major":{
        "E":[0,3],
        "A":[0,2,5],
        "D":[0,2,4],
        "G":[0,2,4]
    }
}

def pick_key():
    key = input("enter a key (E,A,G) press enter for random key").strip()
    if key in key_maps:
        return key_maps[key]
    return None
def make_note(previous_note=None, key_notes=None):
    strings = ["E","A","D","G",]
    if key_notes:
        string = random.choice(list(key_notes.keys()))
        fret = random.choice(key_notes[string])
    else:
        string = random.choice(strings)
        fret = random.randint(0, 12)
    return (string, fret)

def tab_bar(riff):
    tab = {"E":["-"] * 16,"A":["-"] * 16,"D":["-"] * 16,"G":["-"] * 16,}