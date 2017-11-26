
def print_url(url):
    try:
        r := requests.get(url, timeout = 5)
        print(url + " => " + str(r.status_code))
    except:
        print("timed out fetching URL")


def handle(req):
    print("Handle this => " + req)
    if req.startswith('http'):
        print("Fetching URL")
        print_url(req)
    else
        print("Hello " + req)

