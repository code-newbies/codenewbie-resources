import requests

num = "12345"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"

for x in range(401):
    num_url = url.format(num)

    print("{0} {1}".format(x, num_url))

    result = requests.get(num_url)

    if result.status_code == 200:
        num = result.text[-5:]
        print(result.text)

print(result.url)


