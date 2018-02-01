
def removeDuplicateLetters( s):
    for c in sorted(set(s)):
        suffix = s[s.index(c):]
        if set(suffix) == set(s):
            return c + removeDuplicateLetters(suffix.replace(c, ''))
    return ''



#so = Solution()

print(removeDuplicateLetters("zcbacdcbc"))