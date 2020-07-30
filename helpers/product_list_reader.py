if __name__ == '__main__':
    import csv
    with open('products.txt', "r") as p:
        csv_reader = csv.DictReader(p)
        for row in csv_reader:
            del row['title2']
            print(list(dict(row).values()), end=",\n")