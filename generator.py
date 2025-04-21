import random

# Step 1: Choose a random quote
quotes = [
    "The purpose of our lives is to be happy. – Dalai Lama",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "Get busy living or get busy dying. – Stephen King",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "In the end, we only regret the chances we didn’t take. – Lewis Carroll"
]

selected_quote = random.choice(quotes)

# Step 2: Read the HTML template
with open("template.html", "r", encoding="utf-8") as file:
    template = file.read()

# Step 3: Replace the placeholder with the selected quote
filled_html = template.replace("{{quote}}", selected_quote)

# Step 4: Write the final HTML to output.html

with open("output.html", "w", encoding="utf-8") as file:
    file.write(filled_html)

print("Quote page generated! Open 'output.html' in your browser.")