import requests
from bs4 import BeautifulSoup

URL = "https://codes.thisisnotawebsitedotcom.com/"
WK_BOUND = "GravityFallsBoundary"


def post(word) -> requests.Response:
    headers = {"content-type": f"multipart/form-data; boundary={WK_BOUND}"}
    raw_data = f'--{WK_BOUND}\r\nContent-Disposition: form-data; name="code"\r\n\r\n{word}\r\n--{WK_BOUND}--\r\n'
    return requests.post(URL, data=raw_data, headers=headers)


def process_response_html(response: requests.Response, word: str):
    soup = BeautifulSoup(response.text, features="html.parser")
    s = soup.find("div")
    if "data-text" in s.attrs:
        response_text = s.attrs["data-text"]
        with open(f"./findings/{word}.html", "w") as f:
            f.write(response_text)
    else:
        with open(f"./findings/{word}.html", "wb") as f:
            f.write(response.content)


def process_response_media(response: requests.Response, word: str):
    ext = response.headers["Content-Type"].split("/")[-1]
    with open(f"./findings/{word}.{ext}", "wb") as fh:
        fh.write(response.content)


def read_file(path):
    words = set()
    with open(path) as f:
        for line in f:
            words.add(line.strip())
    return words


def send_word(word: str):
    result = post(word)
    if result.status_code == 404:
        print(f"Word: {word} is not a valid word")
        return None

    print(f"Word {word} is valid. Writing response")
    content_type = result.headers["Content-Type"]
    if content_type in RESPONSE_TYPES:
        fn = RESPONSE_TYPES[content_type]
        fn(result, word)


def main():
    words = read_file("./dictionary.txt")
    for word in words:
        print("Searching for word", word)
        send_word(word)


if __name__ == "__main__":
    RESPONSE_TYPES = {
        "text/html": process_response_html,
        "image/png": process_response_media,
        "video/mp4": process_response_media,
    }
    main()
