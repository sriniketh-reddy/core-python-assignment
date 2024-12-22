def percentage_of_positive_rating(rating):
    return (rating.count(5)+rating.count(4)) / len(rating) * 100

ratings  = list(map(int,input("Enter the Ratings (1-5) separated by space: ").split()))
if ratings:
    positive_rating_percentage = percentage_of_positive_rating(ratings)
    print("Percentage of postive ratings: ",positive_rating_percentage)
else: 
    print("No ratings provided.")