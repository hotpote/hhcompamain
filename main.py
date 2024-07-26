from huoqu import tianyancha,icpbeian,qcc
# from concurrent.futures import ThreadPoolExecutor
import argparse
import re

def get_parser():
    #创建参数总容器
    parser=argparse.ArgumentParser(usage='python3 hhcompamain.py',description='hhcompamain:一款方便快捷的公司域名资产搜集的开源工具')

    #添加参数
    parser.add_argument("-n", "--name",nargs=1,required=True,type=str,help="指定公司名称")
    parser.add_argument('-o',"--output",type=str,help='指定输出文件路径,默认保存在同级目录中的result.txt中')

    #结构化参数
    args=parser.parse_args()

    return args



def main(name:str,addr="result.txt"):
    # 创建线程池
    # executor = ThreadPoolExecutor()

    # name=input('请输入企业名称:\n')
    q=qcc(name[0])
    try:
        result_name,result_dizhi=q.choose()    #调用企查查模糊匹配
    except Exception as e:
        print('请输入正确企业名称或正确企业号数') 
        exit()
    print("\n\n所选公司如下:")
    print(result_name)
    print("接下来逐个查找:\n\n")

    i=0
    for name in result_name:      #依次查找
        # qcc_thread=executor.submit(q.huoqu(name,result_dizhi[i]))
        # result1=qcc_thread.result()
        result1=q.huoqu(name,result_dizhi[i])
        i+=1

        t=tianyancha(name)
        # tian_thread=executor.submit(t.huoqu())
        # result2=tian_thread.result()
        result2=t.huoqu()

        icp=icpbeian(name)
        # icp_thread=executor.submit(icp.huoqu())
        # result3=icp_thread.result()
        result3=icp.huoqu()

        resultt=set()
        result4=result1+result2+result3  #处理结果
        for r in result4:
            rr=r.replace('、','')
            if rr[0:3]=='www':
                resultt.add(rr[4:])       #去重
            else:
                resultt.add(rr)
        
        if addr:
            output(name,resultt,str(addr))   #写入文件
        
        print(f'所以"{name}"的最终结果为:') #输出结果
        for k in resultt:
            print(k)

def output(name,result,addr):
    with open(addr,'a',encoding="utf-8") as f:
        f.write("---------------------------------------------\n")
        f.write(f"'{name}'的最终结果为：\n")
        for i in result:
            f.write(f"{i}\n")

if __name__=="__main__": #本地测试
    args=get_parser()
    # print(args.name,args.output)
    main(args.name,args.output)