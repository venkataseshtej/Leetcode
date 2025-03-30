class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Pointer to write compressed characters
        i = 0      # Pointer to read through chars
        
        while i < len(chars):
            char = chars[i]
            count = 0
            
            # Count consecutive occurrences
            while i < len(chars) and chars[i] == char:
                count += 1
                i += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # If count > 1, write the digits of the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write  # New length of the compressed array

    
#         c=0
#         for i in len(chars):
#             if 
        

# def compress(chars):
#     write = 0  # Pointer to write compressed characters
#     i = 0      # Pointer to read through chars
    
#     while i < len(chars):
#         char = chars[i]
#         count = 0
        
#         # Count consecutive occurrences
#         while i < len(chars) and chars[i] == char:
#             count += 1
#             i += 1
        
#         # Write the character
#         chars[write] = char
#         write += 1
        
#         # If count > 1, write the digits of the count
#         if count > 1:
#             for digit in str(count):
#                 chars[write] = digit
#                 write += 1
    
#     return write  # New length of the compressed array
