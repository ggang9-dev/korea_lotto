from bs4 import BeautifulSoup
import requests

class LotterWinningStoreCrawler:

    __url = 'https://dhlottery.co.kr/store.do?method=topStore&pageGubun=L645'
    
    def __init__(self, drwNo=""):
        self.__drwNo = drwNo
        self.__first_store = []
        self.__second_store = []

    def request_lotto(self, drwNo, page):
        req_data = {
            'drwNo' : drwNo,
            'nowPage': page,
            'gameNo': 5133
        }
        return requests.post(LotterWinningStoreCrawler.__url, data=req_data)
    
    def main(self):

        res = self.request_lotto(self.__drwNo, 1)
        page_obj = BeautifulSoup(res.text, 'html.parser')

        # 회차
        drwNoList = page_obj.find('select', {'id': 'drwNo'})
        self.__drwNo = drwNoList.find('option', selected=True).get_text(strip=True)

        # 1등 
        self.add_store(page_obj, 1)

        # 2등
        pages_obj = page_obj.find('div', {'class':'paginate_common'}).find_all("a")
        pages = [a_tag.get_text(strip=True) for a_tag in pages_obj]

        for page in pages:
            if page == 1:
                self.add_store(page_obj, 2)
            else:
                temp_res = self.request_lotto(self.__drwNo, page)
                temp_page_obj = BeautifulSoup(temp_res.text, 'html.parser')
                self.add_store(temp_page_obj, 2)

    def add_store(self, obj, rank):
        tables = obj.find_all('table', {'class':'tbl_data_col'})

        if rank == 1:
            table = tables[0]
        else:
            table = tables[-1]
            
        trs = table.select('tbody > tr')
        for tr in trs:
            tds = tr.find_all('td')
            cols = [ele.get_text(strip=True) for ele in tds]
            if cols:
                if rank == 1:
                    self.__first_store.append(LottoStoreCrawler(rank, cols))
                else:
                    self.__second_store.append(LottoStoreCrawler(rank, cols))

    def print(self):
        print("==== {0} 회차 ====".format(self.__drwNo))

        print("\n======== 1등({0}) ========".format(len(self.__first_store)))
        for store in self.__first_store:
            print(store)

        print("\n======== 2등({0}) ========".format(len(self.__second_store)))
        for store in self.__second_store:
            print(store)

class LottoStoreCrawler:
    def __init__(self, rank, cols):
        if rank == 1:
            self.rank = 1
            self.name = cols[1]
            self.method = cols[2]
            self.address = cols[3]
        else:
            self.rank = 2
            self.name = cols[1]
            self.method = '-'
            self.address = cols[2]
     
    def __repr__(self):
        return "{0}등 - {1}, 주소 : {2}, 구분 : {3}".format(self.rank, self.name, self.address, self.method)


if __name__ == "__main__":
    crawler = LotterWinningStoreCrawler()
    crawler.main()
    crawler.print()
