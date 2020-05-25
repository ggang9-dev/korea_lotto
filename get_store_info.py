import requests
import json

class LottoStoreCrawler:

    __url = 'https://dhlottery.co.kr/store.do?method=sellerInfo645Result'
    __sido = ['서울', '경기', '부산', '대구', '인천', '대전', '울산', '강원', '충북', '충남', '광주', '전북', '전남', '경북', '경남', '제주', '세종']
   
    def __init__(self):
        self.__store_list = []
        pass

    def main(self):
        for sido in LottoStoreCrawler.__sido:
            self.get_store_list(sido, 1)

    def get_store_list(self, sido, page):
    
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        req_data = {
            'searchType' : 1,
            'nowPage' : page,
            'sltSIDO' : sido,
            'sltGUGUN' : "",
            'rtlrSttus' : "",
        }

        res = requests.post(LottoStoreCrawler.__url, data=req_data, headers=headers).json()    
        print("===== {0} =====".format(page))
        self.add_store_list(res['arr'])

        if page < res['totalPage']:
            page+=1
            self.get_store_list(sido, page)

    def add_store_list(self, store_list):
        for store in store_list:
            print(LottoStore(store))
        
class LottoStore:
    def __init__(self, store_json):
        self.addr_1 = store_json['BPLCLOCPLC1']
        self.addr_2 = store_json['BPLCLOCPLC2']
        self.addr_3 = store_json['BPLCLOCPLC3']
        self.addr_4 = store_json['BPLCLOCPLCDTLADRES']
        self.name = store_json['FIRMNM']
        self.longitude = store_json['LONGITUDE']
        self.latitue = store_json['LATITUDE']
        self.use = store_json['DEAL645'] == 1
        self.id = store_json['RTLRID']
        self.tel = store_json['RTLRSTRTELNO']

    def __repr__(self):
        address = " ".join([addr for addr in [self.addr_1, self.addr_2, self.addr_3, self.addr_4] if addr != None])
        return  "{0}({1}) - {2}({3}, {4})".format(self.name, self.tel, address, self.latitue, self.longitude)

if __name__ == '__main__':
    crawler = LottoStoreCrawler()
    crawler.main()
