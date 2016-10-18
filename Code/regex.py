import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 return [word for word in words if re.search(regex, word)]
regex = r"v"
print regex,":",get_matching_words(regex)
regex = r"ss"
print regex,":",get_matching_words(regex)
regex = r"e$"
print regex,":",get_matching_words(regex)
regex = r"b.b"
print regex,":",get_matching_words(regex)
regex = r"b.+b"
print regex,":",get_matching_words(regex)
regex = r"b*.b"
print regex,":",get_matching_words(regex)
regex = r"a.*?e.*?i.*?o.*?u.*?"
print regex,":",get_matching_words(regex)
regex = r"^([regulaxpsion])*$"
print regex,":",get_matching_words(regex)
regex = r"(.)\1"
print regex,":",get_matching_words(regex)
