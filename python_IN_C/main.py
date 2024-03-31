import random

# def isPalindrome(x: int) -> bool:
#     first_list = []
#     second_list = []
    
#     for el in str(x):
#         first_list.append(el)


#     for el in str(x)[::-1]:
#         second_list.append(el)

#     print(first_list == second_list)

# isPalindrome(x= "")


# def romanToInt(s: str) -> int:
#     if s == None:
#         return 0
    
#     final_int = 0
    
#     for el in s:
#         if el == 'I':
#             final_int += 1
#         elif el == "V":
#             final_int += 5
#         elif el == "X":
#             final_int += 10
#         elif el == "L":
#             final_int += 50
#         elif el == "C":
#             final_int += 100
#         elif el == "D":
#             final_int += 500
#         elif el == "M":
#             final_int += 1000

#     return final_int

# romanToInt(s= "III")

# print(romanToInt(s= "III"))
# print(romanToInt(s= "LVIII"))
# print(romanToInt(s= "MCMXCIV"))


# def romanToInt(s: str) -> int:
#     m = {
#                 'I': 1,
#                 'V': 5,
#                 'X': 10,
#                 'L': 50,
#                 'C': 100,
#                 'D': 500,
#                 'M': 1000
#             }
    
#     total_cost = 0

#     for i in range(len(s)):
#         if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
#             total_cost -= m[s[i]]
#         else:
#             total_cost += m[s[i]]
    
#     return total_cost

# print(romanToInt(s="MCMXCIV"))

# nums1 = [1,1,2,2]
# nums2 = [0,0,1,1,1,2,2,3,3,4]

# def removeDuplicates(nums) -> int:
#     main_list = []
#     for i in range(len(nums) - 1):
#         if nums[i] != nums[i + 1]:
#             main_list.append(nums[i])
    
#     main_list.append(nums[-1])

#     return main_list


# print(removeDuplicates(nums=nums2))


# st = ["flower","flow","flight"]
# s = ["dog","racecar","car"]

# def longestCommonPrefix(strs) -> str:
#     if not strs:
#         return ""
    
#     for i in range(len(strs[0])):
#         for srtring in strs[1:]:
#             if i >= len(srtring) or srtring[i] != strs[0][i]:
#                 return strs[0][:i]

#     return strs[0]

# longestCommonPrefix(st)

# longestCommonPrefix(s)

# nums1 = [1,3,5,6,8,10]

# def searchInsert(nums: list, target: int) -> int:

#     if target not in nums:
#         nums.append(target)
#         nums.sort()
#         return nums.index(target)
#     else:
#         return nums.index(target)




# searchInsert(nums=nums1, target=7)

# print(nums1)


# Пример 1:

# s1 = "()"
# #  Вывод: true
# # Пример 2:

# s2 = "()[]{}"
# #  Вывод: true
# # Пример 3:

# s3 = "(]"
# #  Вывод: ложь

# s4 = "{[]}"


# def isValid( s: str) -> bool:
#     for el in range(len(s)):
#         if s[el] == "(" and s[el+1] != ")":
#             return False
#         elif s[el] == "[" and s[el+1] != "]":
#             return False
#         elif s[el] == "{" and s[el+1] != "}":
#             return False
#         else:
#             return True

#     s = sorted(s)
#     s = ''.join(s)

#     for el in range(len(s)):
#         if s[el] == "(" and s[el+1] == ")":
#             return True
#         elif s[el] == "[" and s[el+1] == "]":
#             return True
#         elif s[el] == "{" and s[el+1] == "}":
#             return True
#         else:
#             return False
        

        # if s[el] == simbol_list[1] and s[el+1] == simbol_list[2]:
        #     print('Verno')
        # if s[el] == simbol_list[3] and s[el+1] == simbol_list[4]:
        #     print('Verno')
        # if s[el] == simbol_list[5] and s[el+1] == simbol_list[6]:
        #     print('Verno')

        
       
# print(sorted('{[]}'))
# print(sorted("()[]{}"))
# print(sorted(s3))

# isValid(s=s1)
# isValid(s=s2)
# isValid(s=s3)
# isValid(s=s4)

# simbol_list = {
#         1: "(",
#         2: ")",
#         3: "[",
#         4: "]",
#         5: "}",
#         6: "{",
#     }

# print(simbol_list[1] != simbol_list[2])



# def twoSum( nums: int, target: int):
#         hash = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hash:
#                 return [i, hash[complement]]
#             hash[nums[i]] = i


# twoSum([1,2,5,3,6,3,6,2,7,11,15], 9)

# test_str = "luffy is still joyboy"

# def lengthOfLastWord(s: str) -> int:
#     is_open = True
#     sum_el = 0
#     for el in s[::-1]:
#         if el == " " and is_open:
#             continue
#         if el.isalpha():
#             sum_el += len(el)
#             is_open = False
#         elif el == " ":
#             break
            
#     return sum_el

# lengthOfLastWord(test_str)
# print(lengthOfLastWord(test_str))


# def strStr(haystack: str, needle: str) -> int:
#     if needle in haystack:
#         index_ellement = haystack.find(needle)
#         return index_ellement
#     else:
#         return -1

# strStr(haystack="hello", needle="ll")

# Входные данные: кандидаты = [2,3,6,7], цель = 7
#  Выходные данные: [[2,2,3],[7]]

# Входные данные: кандидаты = [2,3,5], цель = 8
#  Выходные данные: [[2,2,2,2],[2,3,3],[3,5]]


def combinationSum(candidates: int, target: int):
    all_combinations = []
    for el in range(len(candidates)):
        return
    

# Ввод: числа = [2,0,2,1,1,0]
# Вывод: [0,0,1,1,2,2]



# nums = [1,2,3,4,5,6,7,8,9,0]

# def permute(nums):
     
#      result_stack = []
#      combination_stack = 0

#      i = 0
#      while(i < len(nums)):      
#         combination_stack += len(nums) * len(nums) - i
#         i += 1

#      combination_stack = combination_stack/len(nums) - 3
#      while(combination_stack >= len(result_stack)):
#         randol_ellement = nums[:]
#         random.shuffle(randol_ellement)
#         if randol_ellement not in result_stack:
#             result_stack.append(randol_ellement)
    
#      return result_stack


# print(permute(nums))


# nums = [1,2,3]

# def permute(nums):
#     def backtrack(nums, path):
#         if not nums:
#             result.append(path)
#             return
#     for i in range(len(nums)):
#         backtrack(nums[:i] + nums[i+1], path + nums[i])
#         result = []
#         backtrack(nums, [])
#         return result


# permute(nums)


# def count_vowels(any_srt: str) -> int:
#     vowels = ["A", "E", "I", "O", "U", "Y"] 
#     vowels_count = 0
    
#     for i in any_srt.upper():
#         if i in vowels:
#             vowels_count += 1
    
#     print(vowels_count)


# count_vowels('Hello! My neighbor')


# def sum_of_digits(integer: int) -> int:

#     if integer == 0:
#         return 0
#     elif isinstance(integer, float):
#         return print('Function working with round number')
#     elif integer < 0:
#         print('This value negitive meaning')
#         return  
#     else:
#         count = 0
#         for i in str(integer):
#             count += int(i)
        
#         return count

    
# print(sum_of_digits(-123))
    

# list_arr = [1,2,3,4]

# def plusOne(digits: list):
#     all_numbers = int(''.join(str(item) for item in digits))
#     all_numbers += 1 
#     all_numbers = str(all_numbers)
#     result = []
#     for i in all_numbers:
#         i = int(i)
#         result.append(i)
    
#     return result

# print(plusOne(digits=list_arr))

ls_1 = [1,2,3,0,0,0]
ls_2 = [2,5,6]

# def merge(list_1, list_2):
#
#     for i, el in enumerate(list_1):
#         print(f"i{i}= element {el}")
#         if el == el in list_1:
#             list_1.remove(el)
#
#     print(list_1)
#
#     result = list_1 + list_2
#
#
#
# merge(list_1=ls_1, list_2=ls_2)


ls1 = [1,2,3,4,5,6,7,8,9,10]
def sorts_int(ls: list) -> list:
    result = ls.sort()
    return result

print(sorts_int(ls1))

print('Return Def')
print('I have new project')

