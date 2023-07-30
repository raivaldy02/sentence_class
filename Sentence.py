# Write Python 3 code in this online editor and run it.
from typing import List

class Sentence: 
    def __init__(self, sentence:str): 
        self.sentence = sentence

    def split(self, target:str, count = 0) -> List[str]: 
        sentence = self.sentence[count:len(self.sentence)]
        delimiter_index = sentence.find(target)
        
        if delimiter_index == 0: 
            return [""] + self.split(target, count = count + delimiter_index + len(target))
        elif delimiter_index > 0: 
            return [sentence[0:delimiter_index]] + self.split(target, count = count + delimiter_index + len(target))
        else: 
            return [sentence]
    
    def upper(self, char:chr) -> chr: 
        return chr(ord(char) ^ 32) if ord(char) ^ 32 in range(65, 91) else char
        
    def lower(self, char: chr) -> chr:
        return chr(ord(char) ^ 32) if ord(char) ^ 32 in range(97, 123) else char

    
    def equals(self, operand_1:str, operand_2:str = "") -> bool:
        operand_2 = self.sentence if not operand_2 else operand_2
        return operand_1 == operand_2
        
    def contains(self, target:str) -> bool: 
        target_len = len(target)
        sentence_len = len(self.sentence)
        for x in range(sentence_len - target_len + 1):
            if self.sentence[x:x+target_len] == target:
                return True
        return False
        
    def starts_with(self, target:str) -> bool: 
        start, end = 0, len(target)
        return self.sentence[start:start + end] == target
    
    def ends_with(self, target:str) -> bool: 
        sentence_len = len(self.sentence)
        start, end = sentence_len - len(target), len(target)
        return self.sentence[start:start + end] == target
        
    def capitalize(self) -> str: 
        return " ".join([ self.upper(text[0]) + text[1:len(text)] for text in self.sentence.split()])
        
    def center(self, length:int) -> str: 
        difference = length - len(self.sentence)
        left, right = difference // 2, difference - (difference // 2)
        
        return left * " " + self.sentence + " " * right
        
    def count(self, target:str, iteration:int = 0) -> int: 
        return len(self.sentence.split(target)) - 1
        
        
    def ljust(self, length:int) -> str: 
        return self.sentence + " " * length
        
        
    def rjust(self, length:int) -> str: 
        return " " * length + self.sentence
    
    
if __name__ == "__main__": 
    sentence = Sentence("hello world")
    sentence.contains(" Worl") 
    sentence.starts_with("Hello World")
    sentence.ends_with("rld")
    print(sentence.ljust(20), sentence.rjust(20))
