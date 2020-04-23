from spiderman.spiders.helpers import urls_according_keywords

if __name__ == '__main__':
    out = urls_according_keywords(total_pages=8)
    print(len(out))
    for o in out:
        print(o)
