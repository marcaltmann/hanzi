from thefuzz import fuzz


print(fuzz.ratio("verhindern", "hindern"))
print(fuzz.ratio("abnehmen", "abnehmen"))
