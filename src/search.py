def date_range_check(date, range_start_date, range_end_date):
    month, day, year = date.split("/")
    start_month, start_day, start_year = range_start_date.split("/")
    end_month, end_day, end_year = range_end_date.split("/")
    month, day, year = int(month, 10), int(day, 10), int(year, 10)
    start_month, start_day, start_year = int(start_month, 10), int(start_day, 10), int(start_year, 10)
    end_month, end_day, end_year = int(end_month, 10), int(end_day, 10), int(end_year, 10)

    if year < start_year:
        return False
    elif year == start_year:
        if month < start_month:
            return False
        if month == start_month:
            if day < start_day:
                return False

    if year > end_year:
        return False
    elif year == end_year:
        if month > end_month:
            return False
        if month == end_month:
            if day > end_day:
                return False

    return True

def search(editions, keywords = [], authors = [], start_date = "01/01/0001", end_date = "01/01/2100"):
    found_articles = []
    for edition in editions:
        for article in edition['data']:
            # Checks if at least one of the key words is in the article
            if len(keywords) > 0:
                keyword_in_article = False
                for keyword in keywords:
                    if keyword in article['text'] or keyword in article['title']:
                        keyword_in_article = True
                        break
                if not keyword_in_article:
                    continue

            # Checks if the author is in the User's specified list
            if len(authors) > 0:
                author_check = False
                for author in authors:
                    if author in article['author']:
                        author_check = True
                        break
                if not author_check:
                    continue

            # Checks if the date is as specified
            article_date = edition['file_path'].replace("../years/2024-25/", "").replace(".json", "").replace("-", "/") + "/2024"
            if not date_range_check(article_date, start_date, end_date):
                continue

            # Appends the article to the results if it satisfies all of the User's criteria
            found_articles.append(article)

    return found_articles