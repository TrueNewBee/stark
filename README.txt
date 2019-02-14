Strak组件!
2019-2-14 16:24:43
功能简介:
	1. 使用方法和Django的admin一样,需要在strak里面注册,详情看crm/stark.py和配置stark_demo.py
	2. 实现了对不同表的url的各级分发
	3. 用户可以自定义配置表的现实信息 详情可以看crm/stark.py和配置stark_demo.py
	4. 实现了对表添加数据pop的功能!
	5. 最强大就是,你可以拿去直接用,和admin一样,而且不需要超级用户
	2333333333333333333333333333333
使用方法:
	1. 把所有文件都放到新建stark文件夹中,并拷贝到项目根目录
	2. 在settings里面app注册一下!
	3. 在项目app中新建一个stark.py 然后参考stark_demo.py自定义配置一下就好啦!
	4. 然后和admin的打开方式一样!