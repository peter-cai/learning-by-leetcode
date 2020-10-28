# solution by Python3

# solution 1 by regular expression
'''
1. *用于解包，*[a,b,c] 即为 a, b, c
2. 由于正则表达式输出是list，所以需要解包
3. 当匹配不成功，则正则表达式输出是空，int()无输入情况下，输出为0
4. .lstrip用来跳过字符串左边的空格
5. 正则表达式常见符号匹配：
-------------------------------------------------------------------------------------------
. # 点可代表一切字符     \ # 起转义作用                     [...] # 指代方括号中的任意字符
\d # 指代数字0-9        \D # 指代非数字                    \s # 指代一切空格，包括tab制表符、空格、换行等
\S # 指代非空格         \w # 指代大小写字母、数字和下划线    \W # 指代非大小写字母、数字和下划线
* # 匹配前面字符 >=0 次  + # 匹配前面字符1次及以上           ? # 匹配前面字符0次或1次
{m} # 匹配m次           {m,n} # 匹配m到n次                 {m,} # 至少匹配m次
-------------------------------------------------------------------------------------------
6. 正则表达式常见函数
re.match(pattern, string, flags=0)：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
re.search(pattern, string, flags=0)：扫描整个字符串并返回第一个成功的匹配。
re.sub(pattern, repl, string, count=0, flags=0)： 用于替换字符串中的匹配项。
re.compile(pattern[, flags])：用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search()使用。
re.findall(pattern, string, flags=0)或pattern.findall(string[, pos[, endpos]])：在字符串中找到正则表达式所匹配的所有子串，
        并返回一个列表，如果没有找到匹配的，则返回空列表。
pattern.groups(): 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+',s.lstrip())), 2**31-1), -2**31)




