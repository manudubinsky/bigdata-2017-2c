import matplotlib.pyplot as plt

data = [ ("big data", 100, 15), ("Hadoop", 95, 25)]

def text_size(total):
    return 8 + total /200*20


for word,job_popularity,resume_popularity in data:
    plt.text (job_popularity,resume_popularity,word,ha='center',va='center',
              size=text_size(job_popularity + resume_popularity))
plt.xlabel("popularity")
plt.ylabel("popularity resumes")
plt.axis([0,100,0,100])
plt.xticks([])
plt.yticks([])
plt.show()
