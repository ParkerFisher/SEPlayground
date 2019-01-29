from textblob import TextBlob
import requests
import array

test = TextBlob("Shares of Netflix slid 4.1 percent Tuesday, even fucking awful the worst trash disqusting though the streaming  company secured 15 Oscar nominations, including a best picture nod for Roma. The market overall was in the negative Tuesday ven fucking awful the worst trash disqustin amid fears of an economic slowdown, with the tech-heavy Nasdaq Composite Index dropping 1.9 percent. Netflixs ven fucking awful the worst trash disqustinrelatively greater drop seemed surprising on a morning when its films were being celebrated. Netflix received more Oscar nominations than any other studio besides Walt Disney Studios and Fox Searchlight.")
#test2 = TextBlob("company continues increasing emphasis on original content as companies announced they enter market")
#test3 = TextBlob("Netflix said it is becoming less focused on 2nd run programming due to its original content success.")
#test4 = TextBlob("Still, it is not abandoning second-run programming")
#avg = test.sentiment.polarity + test2.sentiment.polarity + test.sentiment.polarity + test.sentiment.polarity
#avg = avg/4


#test5 = TextBlob("Expect Another Big Year for Stock Buybacks, JPMorgan Says")


r = requests.post(
    "https://api.deepai.org/api/sentiment-analysis",
    data={
        'text': 'Shares of Netflix slid 4.1 percent Tuesday, even though the streaming  company secured 15 Oscar nominations, including a best picture nod for "Roma." The market overall was in the negative Tuesday amid fears of an economic slowdown, with the tech-heavy Nasdaq Composite Index dropping 1.9 percent. Netflixs relatively greater drop seemed surprising on a morning when its films were being celebrated. Netflix received more Oscar nominations than any other studio besides Walt Disney Studios and Fox Searchlight.',
    },
    headers={'api-key': '826219d5-9449-4223-aa8b-5af962999bdb'}
)
output = []
output = r.content.splitlines()
print(r.text)
print(output[2])

print("\n")
print(test.sentiment.polarity)

#print(test2.sentiment.polarity)

#print(test3.sentiment.polarity)

#print(test4.sentiment.polarity)

#print(avg)

#def outputparser(str):




