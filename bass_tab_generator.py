import random

key_maps ={
    "E Major":{
        "E":[0,2,4,5,7,9,11,12],
        "A":[2,7,9,11],
        "D":[2,9],
        "G":[4,9]
    },
    "A Major":{
        "E":[5,7,9,10],
        "A":[0,2,4,5,7,9,11],
        "D":[7,9,11],
        "G":[2,4,6,11]
    },
    "G Major":{
        "E":[3,7,8,10],
        "A":[2,3,5,10],
        "D":[5,9,10],
        "G":[0,4,5,7,11]
    }
}

def pick_key():
    key = input("enter a key (E,A,G) press enter for random key: ").strip()
    if key in key_maps:
        return key_maps[key]
    return None
def make_note(previous_note=None, key_notes=None):
    strings = ["E","A","D","G",]
    if previous_note:
        prev_string, prev_fret = previous_note

        possible_string = [s for s in strings if abs(strings.index(s) - strings.index(prev_string)) <=2]
        if key_notes:
            possible_frets = [f for f in key_notes.get(prev_string, []) if abs(f - prev_fret) <= 5]
        else:
            possible_frets = [f for f in range(13) if abs(f - prev_fret) <=5]
        string = random.choice(possible_string)
        fret = random.choice(possible_frets) if possible_frets else random.choice(key_notes.get(string, []))
    else:
        string = random.choice(strings)
        if key_notes:
            fret = random.choice(key_notes.get(string, []))
        else:
            fret = random.randint(0, 12)
    return (string, fret)

def tab_bar(riff):
    tab = {"E":["-"] * 16,"A":["-"] * 16,"D":["-"] * 16,"G":["-"] * 16,}

    for i, note in enumerate(riff):
        if i >= 16:
            break
        if len(note) == 2:
            string,fret = note
            if string:
                tab[string][i] = str(fret)

    output = "\n".join(f"{s}|{''.join(f'{n}-' if n != '-' else '--' for n in notes)}|" for s, notes in tab.items())
    return output

def valid_note(prev_note, note, max_fret_distance=5, max_string_distance=2):
    strings = ["E","A","D","G",]
    
    if prev_note:
        prev_string, prev_fret = prev_note
        curr_string, curr_fret = note
        string_distance = abs(strings.index(prev_string) - strings.index(curr_string))
        fret_distance = abs(prev_fret - curr_fret)
        if string_distance > max_string_distance or fret_distance > max_fret_distance:
            return False
        return True

def generate_riff():
    key_notes = pick_key()
    riff = []
    previous_note = None

    for _ in range(12):
        if random.random() < 0.05:
            note1 = make_note(previous_note, key_notes)
            note2 = make_note(note1, key_notes)
            riff.append(note1)
            riff.append(note2)
        else:
            note = make_note(previous_note,key_notes)
            riff.append(note)
            previous_note = note

    print(tab_bar(riff))
generate_riff()