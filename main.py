import re

def count_char_occurrences(word, char):
    """Counts the occurrences of a character (case-insensitive) in a word."""
    return word.lower().count(char.lower())

def parse_claim(claim_text):
    """
    Parses a claim string to extract the word, character, and claimed count.
    Supports patterns like "Çilekte 42 'R' harfi var" or "Programlama kelimesinde 3 adet 'A' harfi var".
    """
    word = None
    char = None
    claimed_count = None

    # Pattern 1: "Çilekte 42 'R' harfi var" (specific to the article's primary example)
    # Matches 'çilekte', a number, an optional quoted character, and 'harfi var'.
    match_specific = re.search(r"çilekte\s+(\d+)\s+['\"]?([a-zA-Z])['\"]?\s+harfi\s+var", claim_text.lower())
    if match_specific:
        word = "çilek"
        claimed_count = int(match_specific.group(1))
        char = match_specific.group(2)
        return word, char, claimed_count

    # Pattern 2: "X kelimesinde Y adet Z harfi var" (more general pattern)
    # Matches a word, 'kelimesinde', a number, 'adet', an optional quoted character, and 'harfi var'.
    match_general = re.search(r"(\w+)\s+kelimesinde\s+(\d+)\s+adet\s+['\"]?([a-zA-Z])['\"]?\s+harfi\s+var", claim_text.lower())
    if match_general:
        word = match_general.group(1)
        claimed_count = int(match_general.group(2))
        char = match_general.group(3)
        return word, char, claimed_count

    return None, None, None

def validate_and_critique_claim(claim_text):
    """
    Validates a given claim about character counts in a word and provides a critique.
    Demonstrates data validation and critical thinking, as discussed in the article.
    """
    print(f"Analiz edilen iddia: \"{claim_text}\"") # Analyzed claim
    word, char, claimed_count = parse_claim(claim_text)

    # --- Data Validation Step: Check if the claim was successfully parsed ---
    if not all([word, char, claimed_count is not None]):
        print("  [HATA] İddia ayrıştırılamadı. Lütfen 'Çilekte 42 'R' harfi var' veya 'Programlama kelimesinde 3 adet 'A' harfi var' gibi bir format kullanın.") # Error: Claim could not be parsed.
        print("-" * 60)
        return

    actual_count = count_char_occurrences(word, char)

    print(f"  Ayrıştırılan: Kelime='{word}', Karakter='{char}', İddia Edilen Sayı={claimed_count}") # Parsed: Word, Char, Claimed Count
    print(f"  '{word}' kelimesindeki '{char}' karakterinin gerçek sayısı: {actual_count}") # Actual count

    # --- Critical Thinking Step: Compare claimed vs. actual and provide assessment ---
    if actual_count == claimed_count:
        print(f"  [DOĞRU] İddia DOĞRU. '{word}' kelimesinde gerçekten {actual_count} adet '{char}' karakteri bulunmaktadır.") # True: Claim is TRUE
    else:
        print(f"  [YANLIŞ] İddia YANLIŞ.") # False: Claim is FALSE
        print(f"  [ELEŞTİREL DÜŞÜNCE] İddia edilen sayı ({claimed_count}) gerçek sayıyla ({actual_count}) eşleşmiyor.") # Critical Thinking: Claimed count doesn't match actual count.
        print("  Bu durum, bilgiyi olduğu gibi kabul etmek yerine doğrulamanın önemini vurgular.") # This highlights the importance of verifying information.
        print("  Özellikle sıra dışı veya spesifik görünen verileri her zaman doğrulayın.") # Always validate data, especially when it seems unusual or specific.
    print("-" * 60)

if __name__ == "__main__":
    # The primary example from the article: "The '42 R's in Strawberry" Myth
    validate_and_critique_claim("Çilekte 42 'R' harfi var")

    # Another example to show generalization (a true claim)
    validate_and_critique_claim("Programlama kelimesinde 3 adet 'A' harfi var")

    # A true claim
    validate_and_critique_claim("Muz kelimesinde 1 adet 'M' harfi var")

    # A false claim
    validate_and_critique_claim("Elma kelimesinde 2 adet 'L' harfi var")

    # An unparsable claim
    validate_and_critique_claim("Bu cümle anlamsız bir iddia içeriyor")

    # Another false claim with the general pattern
    validate_and_critique_claim("Veri kelimesinde 2 adet 'E' harfi var")
