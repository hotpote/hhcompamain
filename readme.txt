工具环境为python3
使用到的组件为:requests,lxml,urllib

使用前请先进入config.txt文件内进行cookie配置：qcccookie为企查查用户登陆后的cook值，tycookie为天眼查用户登陆后的cookie值，icpcookie为icp备案查询的cookie值。
        cookie值可登录账号后在浏览器中按f12查看存储功能处查到，保存格式为 键1=值1;键2=值2; 如token=dso24f9328knew;name=admin;

配置使用教程：
1.在工具文件下打开cmd
2.python3 -m pip install -r requirements.txt
3.python3 hhcompamain.py -h
4.查看提示后选择想要的参数使用即可
