# -*- coding: UTF-8 -*-
import re

text = r"""
蘋果創辦人賈伯斯（Steve Jobs）逝世10週年，曾經和賈伯斯合作的鴻海創辦人郭台銘7日晚間在臉書Po文提到，當年有機緣參與Steve的葬禮，
送他最後一程，在他逝世10週年後的今天，仍然十分懷念他，郭台銘強調：「Steve Jobs不僅令我景仰，他求精求變，不到最後一刻不放棄的人生，
也激勵著我不斷向前。」

郭台銘回憶，他大約是在2004年間和賈伯斯為了研發iPhone開始接觸。許多人說賈伯斯難相處，而他認為賈伯斯是行事嚴謹，要求極高，
但願意給試錯的機會，一向就事論事，所以在他的感受上，賈伯斯為人和藹可親並不難相處，而且以身作則。賈伯斯2006年因為慶功請團隊吃飯，
他向賈伯斯要名片，對方笑說平常沒有給人名片，但還是給了他一張、還簽了名字。

郭台銘表示，懷念和賈伯斯工作的那些年，他的創新能力無人能及，他的工作態度無人能比，賈伯斯說：「要把每一天都當做人生的最後一天來過」，
說到做到，換了肝後，他仍然堅持每天到公司工作，直至2011年9月3日才被醫生要求必須住進醫院，沒多久就離開大家，留給世人難以超越的成就，
賈伯斯對科技應用的突破與創新，改變了世界。

郭台銘也在臉書貼出當年賈伯斯給他的親筆簽名名片，對此網友紛紛讚嘆：「和賈伯斯共事過的故事真的可以傳家唷！這張一定是傳家寶」、「
美好的相遇，美好的回憶」、「boss眼中的boss」、「跟著世界最頂尖的人一起探索實踐做最棒的事，就算再辛苦困難，回頭看也是值得回味」。
"""


def find_all():
    global text
    # direct match
    res = re.findall(r"[^a-zA-Z]", text)
    print(res)

    # pre-compile
    pat = re.compile(r".伯斯")
    res = pat.findall(text)
    print(res)


def find_all_quantifier():
    import re
    print(re.findall('a?', 'aaaa'))  # ['a', 'a', 'a', 'a', '']
    print(re.findall('a*', 'aaaa'))  # ['aaaa', '']
    print(re.findall('a+', 'aaaa'))  # ['aaaa']
    print(re.findall('a{3}', 'aaaa'))  # ['aaa']
    print(re.findall('a{1,2}', 'aaaa'))  # ['aa', 'aa']

    print(re.findall('a??', 'aaaa'))  # ['', 'a', '', 'a', '', 'a', '', 'a', '']
    print(re.findall('a*?', 'aaaa'))  # ['', 'a', '', 'a', '', 'a', '', 'a', '']
    print(re.findall('a+?', 'aaaa'))  # ['a', 'a', 'a', 'a']
    print(re.findall('a{3}?', 'aaaa'))  # ['aaa']
    print(re.findall('a{1,2}?', 'aaaa'))  # ['a', 'a', 'a', 'a']


def find_all_practice():
    txt = "abaabbbbaabbbbbbbb"
    print(re.findall("ab{3}", txt)) # ['abbb', 'abbb']
    print(re.findall("ab{1,3}", txt))   # ['ab', 'abbb', 'abbb']


if __name__ == '__main__':
    # find_all()
    find_all_quantifier()
    # find_all_practice()