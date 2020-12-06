regex_pattern = r'[,.]'
'''
Can also use:
regex_pattern = r'[,.]+'
regex_pattern = r'\D'
regex_pattern = r'\D+'
'''
import re
print("\n".join(re.split(regex_pattern, input())))
