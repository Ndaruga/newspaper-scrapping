from newspaper import Article


#Assign the url you want to extract the article from.
#mine is a BBC News article "Why remote working leaves us vulnerable to cyber-attacks"
url = "https://www.bbc.com/news/business-57847652"

#Lets extract the web data now

newsData = Article(url, language = "en")
newsData.download()
newsData.parse()

print(newsData.text)