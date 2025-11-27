from string_utils import reverse_string,to_lower,to_upper,count_vowels

if __name__ == "__main__":
    sample ="Hello world"
    
    
    print("original:",sample)
    print("Reverse:",reverse_string(sample))
    print("uppercase:",to_upper(sample))
    print("lowercase",to_lower(sample))
    print("vowel count",count_vowels(sample))