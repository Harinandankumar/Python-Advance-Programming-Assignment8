#!/usr/bin/env python
# coding: utf-8

# 1. Given a sentence as txt, return True if any two adjacent words have this
# property: One word ends with a vowel, while the word immediately after
# begins with a vowel (a e i o u).
# Examples
# vowel_links(&quot;a very large appliance&quot;) ➞ True
# vowel_links(&quot;go to edabit&quot;) ➞ True
# vowel_links(&quot;an open fire&quot;) ➞ False
# vowel_links(&quot;a sudden applause&quot;) ➞ False
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def vowel_links(in_string):
    in_list = in_string.split(" ")
    vowel_list = ['a','e','i','o','u']
    end,start,output = False, False,False
    for ele in range(len(in_list)):
        temp = True if in_list[ele][-1] in vowel_list else False
        start = True if in_list[ele][0] in vowel_list else False
        if start == end == True:
            output=True
            break
        end=temp
    print(f'vowel_links({in_string}) ➞ {output}')
                
vowel_links("a very large appliance")
vowel_links("go to edabit")
vowel_links("an open fire")
vowel_links("a sudden applause")


# 2. You are given three inputs: a string, one letter, and a second letter.
# Write a function that returns True if every instance of the first letter occurs
# before every instance of the second letter.
# Examples
# first_before_second(&quot;a rabbit jumps joyfully&quot;, &quot;a&quot;, &quot;j&quot;) ➞ True
# # Every instance of &quot;a&quot; occurs before every instance of &quot;j&quot;.
# first_before_second(&quot;knaves knew about waterfalls&quot;, &quot;k&quot;, &quot;w&quot;) ➞ True
# first_before_second(&quot;happy birthday&quot;, &quot;a&quot;, &quot;y&quot;) ➞ False
# # The &quot;a&quot; in &quot;birthday&quot; occurs after the &quot;y&quot; in &quot;happy&quot;.
# first_before_second(&quot;precarious kangaroos&quot;, &quot;k&quot;, &quot;a&quot;) ➞ False
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


# Approach 1 Using index() and() rindex() functions
def first_before_second_index(in_string,in_first,in_second):
    last_occur_first = in_string.rindex(in_first)
    first_occur_second = in_string.index(in_second)
    output = True if last_occur_first < first_occur_second else False
    print(f'first_before_second_index({in_string}, {in_first}, {in_second}) ➞ {output}')

# Approach 2 Using find() and() rfind() functions
def first_before_second_find(in_string,in_first,in_second):
    last_occur_first = in_string.rfind(in_first)
    first_occur_second = in_string.find(in_second)
    output = True if last_occur_first < first_occur_second else False
    print(f'first_before_second_find({in_string}, {in_first}, {in_second}) ➞ {output}')

first_before_second_index("a rabbit jumps joyfully", "a", "j")
first_before_second_index("knaves knew about waterfalls", "k", "w")
first_before_second_index("happy birthday", "a", "y")
first_before_second_index("precarious kangaroos", "k", "a")
print()
first_before_second_find("a rabbit jumps joyfully", "a", "j")
first_before_second_find("knaves knew about waterfalls", "k", "w")
first_before_second_find("happy birthday", "a", "y")
first_before_second_find("precarious kangaroos", "k", "a")


# 3. Create a function that returns the characters from a list or string r on odd or
# even positions, depending on the specifier s. The specifier will be &quot;odd&quot; for
# items on odd positions (1, 3, 5, ...) and &quot;even&quot; for items on even positions (2,
# 4, 6, ...).
# Examples
# char_at_pos([2, 4, 6, 8, 10], &quot;even&quot;) ➞ [4, 8]
# # 4 &amp; 8 occupy the 2nd &amp; 4th positions
# char_at_pos(&quot;EDABIT&quot;, &quot;odd&quot;) ➞ &quot;EAI&quot;
# # &quot;E&quot;, &quot;A&quot; and &quot;I&quot; occupy the 1st, 3rd and 5th positions
# 
# char_at_pos([&quot;A&quot;, &quot;R&quot;, &quot;B&quot;, &quot;I&quot;, &quot;T&quot;, &quot;R&quot;, &quot;A&quot;, &quot;R&quot;, &quot;I&quot;, &quot;L&quot;, &quot;Y&quot;], &quot;odd&quot;) ➞ [&quot;A&quot;,
# &quot;B&quot;, &quot;T&quot;, &quot;A&quot;, &quot;I&quot;, &quot;Y&quot;]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def char_at_pos(in_list,mode):
    out_list = []
    for ele in range(len(in_list)):
        if mode == 'even' and (ele+1)%2 == 0:
            out_list.append(in_list[ele])
        elif mode == 'odd' and (ele+1)%2 != 0:
            out_list.append(in_list[ele])            
    print(f'char_at_pos{in_list,mode} ➞ {out_list}')
        
        
char_at_pos([2, 4, 6, 8, 10], "even")
char_at_pos("EDABIT", "odd")
char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd")


# 4. Write a function that returns the greatest common divisor of all list
# elements. If the greatest common divisor is 1, return 1.
# Examples
# GCD([10, 20, 40]) ➞ 10
# GCD([1, 2, 3, 100]) ➞ 1
# GCD([1024, 192, 2048, 512]) ➞ 64
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def GCD(in_list):
    small = min(in_list)
    gcd = -1
    for i in range(1, small+1):
        output = []
        for ele in in_list:
            output.append(ele%i)
        if len(set(output)) == 1 and list(set(output))[0] == 0:
            gcd = i
    print(f'GCD({in_list}) ➞ {gcd}')
    
GCD([10, 20, 40])
GCD([1, 2, 3, 100])
GCD([1024, 192, 2048, 512])


# 5. A number/string is a palindrome if the digits/characters are the same when
# read both forward and backward. Examples include &quot;racecar&quot; and 12321.
# Given a positive number n, check if n or the binary representation of n is
# palindromic. Return the following:
# - &quot;Decimal only.&quot; if only n is a palindrome.
# - &quot;Binary only.&quot; if only the binary representation of n is a palindrome.
# - &quot;Decimal and binary.&quot; if both are palindromes.
# - &quot;Neither!&quot; if neither are palindromes.
# Examples
# palindrome_type(1306031) ➞ &quot;Decimal only.&quot;
# # decimal = 1306031
# # binary = &quot;100111110110110101111&quot;
# palindrome_type(427787) ➞ &quot;Binary only.&quot;
# # decimal = 427787
# # binary = &quot;1101000011100001011&quot;
# palindrome_type(313) ➞ &quot;Decimal and binary.&quot;
# # decimal = 313
# # binary = 100111001
# palindrome_type(934) ➞ &quot;Neither!&quot;
# # decimal = 934
# # binary = &quot;1110100110&quot;
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def palindrome_type(in_num):
    output = None
    if str(in_num) == str(in_num)[::-1] and str(bin(in_num)[2:]) == str(bin(in_num)[2:])[::-1]:
        output = 'Decimal and binary.'
    elif str(in_num) == str(in_num)[::-1] and str(bin(in_num)[2:]) != str(bin(in_num)[2:])[::-1]:
        output = 'Decimal only.'
    elif str(bin(in_num)[2:]) != str(bin(in_num)[2:])[::-1] and str(in_num) == str(in_num)[::-1]:
        output = 'Binary only.'
    else:
        output = 'Neither!'
    print(f'palindrome({in_num}) ➞ {output}')

palindrome_type(1306031)
palindrome_type(427787)
palindrome_type(313)
palindrome_type(934)

