# hhcompamain
一个快速搜集公司域名资产的方便开源工具。A convenient open source tool that helps quickly collect company domain name assets.域名|子域名|公司资产|信息搜集|subdomain|information collection
## 工具特点以及优势
1.方便快捷。命令行输入公司名称即可一键出结果。而且支持模糊匹配记不得公司全名也行。
2.人性化。自动保存输出结果在文件中，不怕误关窗口导致结果丢失。
3.结果全面。集合企查查，天眼查，icp备案查询一个公司的备案域名，结果全面准确率高。
4.开源灵活。可自行更改源码以适应自己的需求。

## 工具环境为python3
使用到的组件为:requests,lxml,urllib

## 注意！！！
使用前请先进入config.txt文件内进行cookie配置：qcccookie为企查查用户登陆后的cook值，tycookie为天眼查用户登陆后的cookie值。
cookie值可抓包获取，也可在浏览器中f12界面的存储功能处查到，文本保存格式为 键1=值1;键2=值2; 例如token=dso24f9328knew;name=admin;

## 配置使用教程：
1.在工具文件下打开cmd

2.python3 -m pip install -r requirements.txt

3.python3 hhcompamain.py -h

4.查看提示后选择想要的参数使用即可
