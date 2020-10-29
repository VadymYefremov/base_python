""" Example of use lambda, map & filter function in list  """

# py = list(filter(lambda x: x.endswith('.json'), data)) # п1 Домашнего задания 12


data = ['this', 'free', 'online', 'Tool', 'easy', '1234', 'need',
        'copy', 'paste', 'into', 'generator', 'choose', 'appropriate',
        'either', 'Each', 'entry', 'separated', 'line', 'number', 'random',
        'entries', 'you', 'want', '34displayed', '2click', 'Button', 'randomly',
        'appear', 'from', 'inserted', 'really', 'here', 'some', 'common', 'ways',
        '8756', 'homework', 'memorize', 'perfect', 'study', 'example', 'part',
        'science', 'periodic', 'table', 'chemical', 'element', 'practice', 'atomic', 'school']


result1_1 = list(filter(lambda x: len(x) == 5, data))
result1_2 = list(filter(lambda x: x.istitle(), data))
result1_3 = list(filter(lambda x: x.isdigit(), data))


print(result1_1)
print(result1_2)
print(result1_3)


result2_1 = list(map(lambda x: len(x), data))
result2_2 = list(map(lambda x: x.istitle(), data))
result2_3 = list(map(lambda x: x.isdigit(), data))


print(result2_1)
print(result2_2)
print(result2_3)
