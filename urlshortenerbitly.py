import pyshorteners

longUrl = input("Enter URL to shorten: ")


typingBitly = pyshorteners.Shortener(api_key='')

shortUrl = typingBitly.bitly.short(longUrl)

print("Your short URL is: " + shortUrl)