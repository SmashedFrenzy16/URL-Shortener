import pyshorteners

longUrl = input("Enter URL to shorten: ")

typingTiny = pyshorteners.Shortener()

shortUrl = typingTiny.tinyurl.short(longUrl)

print("Your short URL is: " + shortUrl)