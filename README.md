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
