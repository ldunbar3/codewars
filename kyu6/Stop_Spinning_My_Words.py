def spin_words(str):
  return " ".join(x[::-1] if len(x) >= 5 else x for x in str.split())