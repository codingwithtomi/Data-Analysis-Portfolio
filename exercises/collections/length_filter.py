animals = ["cat", "elephant", "dog", "butterfly", "ant", "giraffe", "duck"]

long_words = [n for n in animals if len(n) > 4]
print(f"Original: {animals}")
print(f"Long words(>4 chars): {long_words}")
