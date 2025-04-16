import random

# ✅ Step 1: Markov Chain banana
def build_markov_chain(text):
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in markov_chain:
            markov_chain[current_word] = []

        markov_chain[current_word].append(next_word)
    
    return markov_chain

# ✅ Step 2: Text generate karna using Markov Chain
def generate_text(chain, length=30):
    current_word = random.choice(list(chain.keys()))
    result = [current_word]

    for _ in range(length - 1):
        next_words = chain.get(current_word)
        if not next_words:
            break
        current_word = random.choice(next_words)
        result.append(current_word)

    return ' '.join(result)

# ✅ Step 3: Input text
sample_text = """Faiza is a frontend developer. She loves coding and building web apps. 
Her favorite technologies include JavaScript, Next.js, and Tailwind CSS.
She believes that with code, anything is possible. Code is magical!
"""

# ✅ Step 4: Build chain and generate
chain = build_markov_chain(sample_text)
generated_text = generate_text(chain, length=40)

# ✅ Step 5: Show result
print("\n📝 Generated Text:\n")
print(generated_text)
