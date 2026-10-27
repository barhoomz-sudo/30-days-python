# import numpy
# import webbrowser
import requests # type: ignore

# print(numpy.version.version)

# lst = [1,2,3,4,5]
# np_arr = numpy.array(lst)
# print(np_arr)
# print(len(np_arr))
# print(np_arr * 2)

# url_lists = [
#     'https://studiestimer.com/',
#     'https://cs50.harvard.edu/python',
#     'https://github.com/Asabeneh/30-Days-Of-Python'
# ]

# for url in url_lists:
#     webbrowser.open_new_tab(url)

# url = 'https://cs50.harvard.edu/python/psets/7/'
# response = requests.get(url)
# print(response)
# print(response.status_code)
# # print(response.headers)
# print(response.text)

# url = 'https://api.restcountries.com/countries/v5'
# response = requests.get(url, headers={'Authorization': 'Bearer rc_live_056f8a0573ee4a5681a4e981501bbbfb'})
# data = response.json()
# print(type(data))

from my_package import arith
print(arith.add_numbers(99,1))

from my_package import greet
print(greet.greet_person("Ibrahim", "Hussain"))