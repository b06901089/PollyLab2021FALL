### Crawling pictures from unsplash.com
### command usage:
### python unsplash.py -w unsplash -q [query] -o [output directory] -p [number of pages - 4]

### command expamples:
### python unsplash.py -w unsplash -q temple -o . -p 15
### output expamples:
### ../
###   unsplash.py
###   temple/
###     pic1.jpg
###     pic2.jpg
###     (19 pages of pictures)

### command expamples:
### python unsplash.py -w unsplash -q temple -o ./Temple -p 10
### output expamples:
### ../
###   unsplash.py
###   temple/
###     Temple/
###       pic1.jpg
###       pic2.jpg
###       (14 pages of pictures)

### Reference:
### https://blog.paperspace.com/building-computer-vision-datasets/

# import argparse, urllib3, os, requests
# from tqdm import trange,tqdm
# from concurrent.futures import ProcessPoolExecutor,as_completed

# page = 1
# website  = "https://www.unsplash.com"
# session  = requests.Session()
# search   = 'building'
# # base_url = website + "/napi/search/photos?query={0}&xp=&per_page=20&page={1}".format(search, page)
# base_url = website + "/napi/search/photos?query={0}&xp=&per_page=20&".format(search)
# response = session.get(base_url)
# # print(response.json())
# urls=[]
# if response.status_code == 200 :
#     results = response.json()['results']
#     total_pages = response.json()['total_pages']
#     print(total_pages)
#     urls    = urls + [(url['id'], url['urls']['regular']) for url in results]
#     # raw -> full -> regular -> small -> thumb
# print(len(urls))
# # urllib3.request.urlretrieve(urls[0][1],'./'+urls[0][0]+'.jpg')




import argparse, urllib, os, requests
from tqdm import trange,tqdm
from concurrent.futures import ProcessPoolExecutor,as_completed

class _unsplash(object):

    def __init__(self):
        self.website = "https://www.unsplash.com"
        self.session = requests.Session()

    def __call__(self, search, pages=None):

        base_url = self.website + "/napi/search/photos?query={0}&xp=&per_page=20&".format(search)

        total_pages = self.session.get(base_url).json()['total_pages']
        print('total_pages : ', total_pages)
        if not pages: pages = total_pages

        urls=[]

        for page in trange(1, pages+5 ,desc="Downloading image URLs"):
            print(page)
            search_url = self.website + "/napi/search/photos?query={0}&xp=&per_page=20&page={1}".format(search, page)
            response = self.session.get(search_url)
            if response.status_code == 200 :
                results = response.json()['results']
                urls = urls + [(url['id'],url['urls']['regular']) for url in results]
                # picture resolution paramters
                # raw -> full -> regular -> small -> thumb

        # print(urls)
        # print(len(urls))
        # print(len(list(set(urls))))
        
        return list(set(urls))

unsplash = _unsplash()

class _download_imgs(object):

    def __init__(self, output_dir, query):
        self.query = query
        self.directory = output_dir + '/' + query
        if not os.path.isdir(self.directory) : os.makedirs(self.directory)

    def __call__(self, urls):
        with ProcessPoolExecutor() as pool:
            downloads = [pool.submit(urllib.request.urlretrieve, url[1], self.directory+'/'+url[0]+'.jpg') for url in urls]
            for download in tqdm(as_completed(downloads), total=len(downloads), desc='Downloading '+self.query+" images...."):
                pass

class _scrape(object):

    def __call__(self, args):

        if args.w.lower() == 'unsplash' : urls = unsplash(args.q.lower(), args.p)
        download_imgs = _download_imgs(args.o, args.q.lower())
        download_imgs(urls)

scrape=_scrape()

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Web Scraping')

    parser.add_argument('-w', default = 'unsplash', choices = ['unsplash'], metavar = 'website', required = False, type = str,
                        help = 'name of the website that you want to scrape data from, example: unsplash')
    parser.add_argument('-q', metavar = 'query', required = True, type = str,
                        help = 'search term for query, example: mushroom')
    parser.add_argument('-o', metavar = 'output directory', required = True, type = str,
                        help = 'Path to the folder where you want the data to be stored, the directory will be created if not present')
    parser.add_argument('-p', metavar = 'no of pages', type = int, help = 'Number of pages to scrape')

    args = parser.parse_args()
    scrape(args)