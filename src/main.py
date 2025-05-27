
if __name__ == "__main__":
    from get_db import get_editions
    from search import search

    editions = get_editions()

    # Collecting User field inputs to feed into search
    print("Please input the following search terms to find your desired article: keyword(s) (comma-seperated), author(s) (also comma seperated), and your date range (eg. 01/21/2024-10/12/2024)")
    keywords_input = input("Keyword(s): ")
    keywords = keywords_input.lower().strip().split(",")

    authors_input = input("Author(s): ")
    authors = authors_input.lower().strip().split(",")

    date_range_input = input("Date Range: ").strip()
    start_date = date_range_input.split("-")[0]
    end_date = date_range_input.split("-")[1]

    # Outputting the titles of the articles that satisfy the User's inputs
    found_articles = search(editions, keywords, authors, start_date, end_date) # Todo: make it so that the articles are ranked by relevance
    for article in found_articles:
        print(article['title'])