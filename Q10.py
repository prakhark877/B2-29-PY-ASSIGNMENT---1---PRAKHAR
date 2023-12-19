def reverse_sentence(input_sentence):
    words = input_sentence.split()

    reversed_sentence = ' '.join(reversed(words))

    return reversed_sentence

input_sentence = "Hello, World! Welcome to Python programming."
output_sentence = reverse_sentence(input_sentence)

print("Input sentence:", input_sentence)
print("Output after reverse:", output_sentence)