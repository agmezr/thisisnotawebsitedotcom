# thisisnotawebsitedotcom

Gravity falls is back with the page [thisisnotawebsitedotcom.com](). As always it's filled with misteries. You can enter a code and get an image, video, small message or redirect. But trying so many codes there is hard and boring so I automated the task with this

# Setup

1. Create a virtual env
```bash
python3 -m venv venv
```
2. Activate and install dependencies
```bash
source venv/bin/activate
pip install -r requirements.txt
```

# How to use?

Add as many codes as you want in the `dictionary.txt` file. One per line. Run the main scrip and see the results in the `findings` directory

### Example

```bash
$ python main.py
Searching for word gravity falls
Word gravity falls is valid. Writing response
Searching for word stanford
Word stanford is valid. Writing response
Searching for word soos
...
```

Ready. Finding folder now contains all responses
```bash
ls -l findings
total 14684
-rw-r--r-- 1 alex alex      44 Aug 23 19:39  README.md
-rw-r--r-- 1 alex alex     114 Aug 23 19:36  alex.html
-rw-r--r-- 1 alex alex    1075 Aug 23 19:36  dipper.html
-rw-r--r-- 1 alex alex 2261222 Aug 23 19:36  dorito.mp4
-rw-r--r-- 1 alex alex 2499683 Aug 23 19:36  ford.png
-rw-r--r-- 1 alex alex      17 Aug 23 19:36 'gravity falls.html'
-rw-r--r-- 1 alex alex      42 Aug 23 19:36  life.html
-rw-r--r-- 1 alex alex    1464 Aug 23 19:36  mabel.html
-rw-r--r-- 1 alex alex 3116292 Aug 23 19:36  mason.png
-rw-r--r-- 1 alex alex 3474173 Aug 23 19:36  soos.html
-rw-r--r-- 1 alex alex 1143315 Aug 23 19:36  stan.html
-rw-r--r-- 1 alex alex 2499683 Aug 23 19:36  stanford.png
```