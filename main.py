test_sentence = "As he crossed toward the pharmacy at the corner he involuntarily turned his head because of a burst of light that had ricocheted from his temple, and saw, with that quick smile with which we greet a rainbow or a rose, a blindingly white parallelogram of sky being unloaded from the van—a dresser with mirrors across which, as across a cinema screen, passed a flawlessly clear reflection of boughs sliding and swaying not arboreally, but with a human vacillation, produced by the nature of those who were carrying this sky, these boughs, this gliding façade"

def word_frequency(sentence):
  final_frequency = {}
  for word in sentence.split():
    if word not in final_frequency:
      final_frequency[word] = 1
    else:
      final_frequency[word] += 1
  return final_frequency

print(word_frequency(test_sentence))        