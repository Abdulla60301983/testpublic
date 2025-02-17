def longest_continuous_substring(s):
    if not s:
        return 0
    
    s = s.lower()
    max_len = 1
    current_len = 1
    
    for i in range(len(s) - 1):
        if ord(s[i]) + 1 == ord(s[i+1]) or (s[i] == 'z' and s[i+1] == 'a'):
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 1
    
    # Check circular condition
    if ord(s[-1]) + 1 == ord(s[0]) or (s[-1] == 'z' and s[0] == 'a'):
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    
    return max_len

# Test cases
print(longest_continuous_substring("aabcdegg"))  # Should return 5
print(longest_continuous_substring("cdefxyzab"))  # Should return 6