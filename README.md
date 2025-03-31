# Bass-Tab-generator

## Objective
Design a **Random Bass Guitar Tab Generator** that creates playable bass riffs with specific constraints on note selection, key adherence, and fretboard movement. The generator produces a 16-note riff in a standard bass guitar tab format, with an optional key selection feature.

---

## Requirements and Constraints

### Bass Guitar Setup
- **Tuning**: Standard 4-string bass guitar tuning: E (E1), A (A1), D (D2), G (G2).
- **Fretboard Range**: 0 (open string) to 12th fret.

### Riff Length
- Each generated riff must consist of exactly **16 notes** (single notes or two-note combinations).

### Note Plucking Probability
- **95% chance** of plucking only one string per note.
- **5% chance** of plucking two strings simultaneously.
  - When two strings are plucked, the fret distance between the notes must be **2 frets or less** (e.g., E string fret 2 and A string fret 3 is allowed, but E string fret 2 and A string fret 5 is not).

### Key Options
- The generator supports an optional input for selecting a key. If no key is specified, notes can be chosen randomly across all strings and frets (within playability constraints).
- **Supported Keys** (with defined string/fret combinations):
  - **Key of E Major**: Example map:  
    - E: 0, 2, 4  
    - A: 0, 2, 4  
    - D: 1, 2, 4  
    - G: 1, 3, 4  
  - **Key of G Major**: Example map:  
    - E: 0, 3  
    - A: 0, 2, 5  
    - D: 0, 2, 4  
    - G: 0, 2, 4  
  - **Key of A Major**: Example map:  
    - E: 0, 1, 4  
    - A: 0, 2, 4  
    - D: 1, 4  
    - G: 1, 3, 6  
- When a key is selected, only use the string/fret combinations from the corresponding map.

### Playability Constraints
- Maximum distance between consecutive notes:
  - **2 strings apart** (e.g., from E to D is allowed, but E to G is not).
  - **5 frets apart** (e.g., E string fret 2 to A string fret 5 is allowed, but E string fret 2 to A string fret 8 is not).
- For key-specific runs:
  - Filter the string/fret combinations from the key map.
  - Ensure consecutive notes adhere to the 2-string and 5-fret distance limits.

### Output Format
- Use standard bass guitar tablature structure:

G|----------------|
D|----------------|
A|----------------|
E|----------------|

- Each position in the tab represents one of the 16 notes.
- **Single-note example**: `E|-2-` means E string, fret 2.
- **Two-note example**: `A|-2-| D|-3-|` means A string fret 2 and D string fret 3 plucked together.
- Use hyphens (`-`) to maintain spacing and readability (e.g., one note per beat).

---

## Functionality

### Input
- **Optional**: Key selection (E Major, G Major, A Major, or none for random).
- No other user inputs required.

### Logic Flow
1. **If a key is specified**:
 - Load the predefined string/fret combination map for that key.
 - Filter combinations based on playability constraints (2 strings, 5 frets max distance between consecutive notes).
2. **If no key is specified**:
 - Randomly select any string (E, A, D, G) and fret (0–12) for each note, respecting playability constraints.
3. **For each of the 16 notes**:
 - Generate a random number to determine if it’s a single note (95%) or two-note pluck (5%).
 - For single notes: Choose a string/fret combo within constraints.
 - For two-note plucks: Choose two string/fret combos within 2 frets of each other and 2 strings apart.
 - Validate that each note transition respects the 2-string and 5-fret distance limits from the previous note.

### Output
- Generate a 16-note bass riff in standard tab format (as shown above).
- Ensure the tab is visually aligned and playable.

---

## Deliverables
- A detailed description of the generator’s logic (no code).
- A sample output tab for:
- A random riff (no key specified).
- A riff in the key of E Major.
- A riff in the key of G Major.
- A riff in the key of A Major.

---

## Example Output

### Random Riff (No Key Specified)

G|----------------|
D|-----3----------|
A|-2-------5------|
E|---0---2---0-2--|



### Riff in E Major (Example)

G|----------------|
D|-----2-------4--|
A|-2-------4------|
E|---0---2---0----|

---

## Notes
- Prioritize playability and musical coherence within the given constraints.
- Key-specific maps are based on simplified major scale theory for this assignment.
- No image generation is required unless explicitly requested (confirm with the user first).
