import pyshorteners

def compact_url(long_url):
    # Initialize a Shortener object
    s = pyshorteners.Shortener()

    # Shorten the long URL
    short_url = s.tinyurl.short(long_url)

    return short_url

# Example usage to compact a URL:
long_url = "https://www.google.com/search?q=brazil&sca_esv=570204873&sxsrf=AM9HkKnejslcqK1vEZr7fPbMbGqvi6_TSw%3A1696292720313&source=hp&ei=cF8bZc7FEI6f5OUPnaC-wAw&iflsig=AO6bgOgAAAAAZRttgJeVcTUIp97gzszI43xjRlEBS_p4&ved=0ahUKEwjOvZvoztiBAxWOD7kGHR2QD8gQ4dUDCAs&uact=5&oq=brazil&gs_lp=Egdnd3Mtd2l6IgZicmF6aWwyCBAuGLEDGIAEMgsQABiABBixAxiDATILEC4YgAQYxwEYrwEyCxAuGIAEGMcBGK8BMgsQLhiABBjHARivATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgUQABiABDILEC4YgAQYsQMYgwEyCBAAGIAEGLEDSMUVUABYmgtwAHgAkAEAmAGkAaABtwaqAQMwLja4AQPIAQD4AQHCAgcQLhiKBRgnwgIHECMYigUYJ8ICERAuGIAEGLEDGIMBGMcBGNEDwgILEAAYigUYsQMYgwHCAgUQLhiABMICERAuGIMBGMcBGLEDGNEDGIAEwgILEC4YgwEYsQMYgATCAg0QABiABBixAxiDARgK&sclient=gws-wiz"
shortened_url = compact_url(long_url)
print("Shortened URL:", shortened_url)
