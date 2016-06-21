##功能
快速给自己的命令行添加自动补全功能,只需写一个json文件


## 使用说明
1. 初始化
git clone https://github.com/chenzhongtao/cli_completion.git  
cd cli_completion  
mkdir /etc/mycompletion  
cp  completion.py  /etc/mycompletion  
chmod +x /etc/mycompletion/completion.py 
cp completion.sh /etc/bash_completion.d/  
. /etc/bash_completion.d/completion.sh  
2. 添加命令行相关的json文件  
cp example/mycli.json  /etc/mycompletion/  
echo "complete -F __cmd_completion mycli" >> /etc/bash_completion.d/completion.sh  
. /etc/bash_completion.d/completion.sh  

假如你的命令行就做mycli,有两个一级命令,cmd1,cmd2,每个一级命令有两个二级命令sub11,sub12等,然后二级命令有些可选参数.
具体可以看example/mycli.json文件,命令用字典表示,参数用列表表示. 跟cmd1,cmd2同级的还有个--conf,表示全局参数.  

如何你的命令行名字为hadoop, 先在/etc/mycompletion/下创建一个hadoop.json文件,规则可以参考mycli.json,然后执行  
echo "complete -F __cmd_completion hadoop" >> /etc/bash_completion.d/completion.sh   
. /etc/bash_completion.d/completion.sh   
