import requests
from lxml import etree
from urllib.parse import quote
import re
requests.packages.urllib3.disable_warnings()
class huoqu():
    def __init__(self) -> str:   #父类模版
        pass
    def huoqu(self):
        pass

class tianyancha(huoqu):

    def __init__(self,company_name) -> str:     #初始化，输入公司名
        self.company_name=company_name
    
    def huoqu(self):
        cookie=open("config.txt","r",encoding="utf-8")   #从配置文件获取cookie
        cookie2=cookie.readlines()
        for cookie3 in cookie2:
            cookie4=cookie3.strip()
            if cookie4[:8]=='tycookie':
                cookiee=cookie4[9:]

        headers={		#以字典形式导入
            'Host':'beian.tianyancha.com',
            'Cookie':cookiee,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate, br',
            'Upgrade-Insecure-Requests':'1',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'none',
            'Sec-Fetch-User':'?1',
            'Te':'trailers',
            'Connection':'close',
        }

        result=[]     #结果数组
        company_name2=quote(self.company_name)  #url编码
        response=requests.get(url=f'https://beian.tianyancha.com/search/{company_name2}',headers=headers,verify=False) #获取结果数据
        response2=response.content.decode('utf-8')  #流数据转化为utf-8编码数据

        html=etree.HTML(response2)
        domain=html.xpath('//*[@class="ranking-ym"]/text()')     #从响应报文匹配网站域名
        print(f'"{self.company_name}"的资产在天眼查的结果为:')    #输出
        for i in domain:
            if i=='网站域名':
                continue
            print(i)
            result.append(i)
        return result

class icpbeian(huoqu):

    def __init__(self,company_name:str):
        self.company_name=company_name
    
    def huoqu(self) -> list:
        cookiee=''
        cookie=open("config.txt","r",encoding="utf-8")
        cookie2=cookie.readlines()
        for cookie3 in cookie2:
            print()
            if cookie3[:9]=='icpcookie':
                cookiee=cookie3[10:]

        headers={		#以字典形式导入
            'Host':'www.beianx.cn',
            'Cookie':cookiee,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate, br',
            'Upgrade-Insecure-Requests':'1',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'none',
            'Sec-Fetch-User':'?1',
            'Te':'trailers',
            'Connection':'close',
        }
        result=[]
        company_name2=quote(self.company_name)  #url编码
        # print(company_name2)
        response=requests.get(url=f'https://www.beianx.cn/search/{company_name2}',headers=headers, verify=False)  #请求数据
        response2=response.content.decode('utf-8')  
        # f=open("test.txt","w")
        # f.write(response2)
        html=etree.HTML(response2)
        domain=html.xpath('//table[@class="table table-sm table-bordered table-hover"]//tr/td[6]//a/text()')  #从响应报文匹配网站域名
        print(f'"{self.company_name}"的资产在icp备案的结果为:') #输出
        for i in domain:
            result.append(i)
            print(i)
        return result
    

class qcc(huoqu):

    def __init__(self,company_name:str):
        self.company_name=company_name
    
    def huoqu(self,result_name,result_dizhi) -> list:
        
        cookie=open("config.txt","r",encoding="utf-8") #获取cookie
        cookie2=cookie.readlines()
        for cookie3 in cookie2:
            cookie4=cookie3.strip()
            if cookie4[:9]=='qcccookie':
                cookiee=cookie4[10:]
        # print(cookiee)
        headers={		#以字典形式导入
            'Host':'www.qcc.com',
            'Cookie':cookiee,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate, br',
            'Referer':'https://www.qcc.com/',
            'Upgrade-Insecure-Requests':'1',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'same-origin',
            'Sec-Fetch-User':'?1',
            'Te':'trailers',
        }

        result=[]
        dizhi2=str(result_dizhi).replace('firm','cassets')
        response_ye=requests.get(url=dizhi2,headers=headers, verify=False) #访问找到的地址来匹配最终的域名
        response_ye2=response_ye.content.decode('utf-8')
        f=open("test.txt","w",encoding="utf-8")
        f.write(response_ye2)
        html_ye=etree.HTML(response_ye2)
        #(//table[@class="ntable app-ntable-expand-all"])[2]/tr/td[4]/div/div/div/div/div/text()
        domain=html_ye.xpath('(//table[@class="ntable app-ntable-expand-all"])[2]/tr/td[4]/div/div/div/div/div/text()') #xpath语句获取域名
        # print(domain)
        print("---------------------------------------------------------------")
        print(f'"{result_name}"的资产在企查查备案的结果为:') #输出
        for i in domain:
            result.append(i)
            print(i)
        return result

    def choose(self)->list:   #模糊匹配选择要查的公司
        cookie=open("config.txt","r",encoding="utf-8")  #获取cook
        cookie2=cookie.readlines()
        for cookie3 in cookie2:
            cookie4=cookie3.strip()
            if cookie4[:9]=='qcccookie':
                cookiee=cookie4[10:]
        # print(cookiee)
        headers={		#以字典形式导入
            'Host':'www.qcc.com',
            'Cookie':cookiee,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate, br',
            'Referer':'https://www.qcc.com/',
            'Upgrade-Insecure-Requests':'1',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'same-origin',
            'Sec-Fetch-User':'?1',
            'Te':'trailers',
        }
        result_name=[]
        result_dizhi=[]
        company_name2=quote(self.company_name)  #url编码
        response=requests.get(url=f'https://www.qcc.com/web/search/?key={company_name2}',headers=headers, verify=False) #请求报文
        response2=response.content.decode('utf-8')
        # f=open("test.txt","w",encoding="utf-8")
        # f.write(response2)
        html=etree.HTML(response2)
        try:
            dizhi=html.xpath('//a[@class="title copy-value"]/@href')     #获取公司详情地址
            i=0
            for dizhi2 in dizhi:
                name_com=html.xpath('//a[@class="title copy-value"]/span')[i]   #获取对应公司名
                name_com2 = etree.tostring(name_com, encoding='utf8', method='html').decode()   
                name_com3= re.sub("(<.*?>)","",name_com2)
                print(f'{i+1}号：')
                print(name_com3)
                # print(dizhi2)
                i+=1                                     
        except Exception as e:
            print('请输入正确公司名')
            exit()
        while True:
            try:
                num=input("请输入要查询的企业号数，可以为多个，用','分割。想退出查询请输入'ok'\n")
                if num=="ok":
                    break
                num2=re.split('[,，]',num)
                for i in num2:
                    name_com=html.xpath('//a[@class="title copy-value"]/span')[int(i)-1]
                    name_com2 = etree.tostring(name_com, encoding='utf8', method='html').decode()   #获取要查询的公司名
                    name_com3= re.sub("(<.*?>)","",name_com2)
                    if name_com3 in result_name:
                        continue
                    result_name.append(name_com3)
                    result_dizhi.append(html.xpath('//a[@class="title copy-value"]/@href')[int(i)-1]) #获取要查询的公司地址
                    print(f"目前已选择公司为：{result_name}")
                    # print(result_dizhi)
            except Exception as e:
                print("请输入正确号数")
                continue

        return result_name,result_dizhi


if __name__=="__main__": #本地测试1
    t=qcc('字节')

    result_name,result_dizhi=t.choose()
    print(result_name)
    print(result_dizhi)
    i=0
    for name in result_name:
        t.huoqu(name,result_dizhi[i])
        i+=1


    # t=tianyancha("优酷")
    # t.huoqu()

    # q=icpbeian('北京抖音信息服务有限公司')
    # q.huoqu()
    