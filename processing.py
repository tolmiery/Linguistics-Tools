import json

def find_common_substring(words):
    #Find the longest common substring shared across all words.
    if not words:
        return ""
    
    base_word = words[0]
    longest_common = ""
    
    for i in range(len(base_word)):
        for j in range(i + 1, len(base_word) + 1):
            candidate = base_word[i:j]
            # Check if this candidate is common to all words
            if all(candidate in word for word in words) and len(candidate) > len(longest_common):
                longest_common = candidate
    
    return longest_common

def extract_prefix_stem_suffix(infinitive, conjugated_forms):
    #Extract prefixes, suffixes, and stem from infinitive and its conjugated forms
    # Find the common stem shared by all conjugated forms
    common_stem = find_common_substring(conjugated_forms)
    
    # Initialize lists for prefixes and suffixes
    prefixes = []
    suffixes = []
    
    for form in conjugated_forms:
        if common_stem in form:
            # Extract the prefix (the part before the common stem)
            prefix = form.split(common_stem)[0]  # Get everything before the common stem
            prefixes.append(prefix)
            
            # Extract the suffix (the part after the common stem)
            suffix = form.split(common_stem)[1]  # Get everything after the common stem
            suffixes.append(suffix)
    
    # Return the prefixes, the common stem, and the suffixes
    return prefixes, common_stem, suffixes

def load_verb_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def analyze_verbs(verb_data):
    verb_analysis = {}
    for infinitive, forms in verb_data.items():
        prefixes, stem, suffixes = extract_prefix_stem_suffix(infinitive, forms)
        verb_analysis[infinitive] = {'prefixes': prefixes, 'stem': stem, 'suffixes': suffixes}
    return verb_analysis

# Load verb data from the external file
verb_data = load_verb_data('verb_data.json')

# Analyzing verb data
verb_analysis = analyze_verbs(verb_data)
print(verb_analysis)
