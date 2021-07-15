# Logging模块的使用指南
## 三个问题
### Why
在实际应用中，日志文件十分重要，通过日志文件，我们知道程序运行的细节；同时，当程序出问题时，我们也可以通过日志快速定位问题所在。在我们写程序时，也可以借助logging模块的输出信息来调试代码。但是很多人还是在程序中使用print()函数来输出一些信息，比如
### What
logging模块是Python内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级、日志保存路径、日志文件回滚等；相比print，具备如下优点：

可以通过设置不同的日志等级，在release版本中只输出重要信息，而不必显示大量的调试信息；
print将所有信息都输出到标准输出中，严重影响开发者从标准输出中查看其它数据；logging则可以由开发者决定将信息输出到什么地方，以及怎么输出
### How
#### Logging模块使用
##### 2.1、logging模块控制台输出
``` python
import logging
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 声明一个Logger对象
logger = logging.getLogger(__name__)
logger.info("Start print log")
Logger.debug("Do something")
Logger.warning("Something maybe fail.")
Logger.info("Finsh")
# 参数解释
# basicConfig -- 配置了level信息和format信息
# level -- 配置为INFO信息，即只输出INFO级别信息
# format -- 指定了format格式的字符串，包括
# - asctime -- 运行时间
# - name -- 模块名称
# - levelname -- 日志级别
# - message -- 日志内容
```

##### 详细参数解释
**basicConfig** 参数解释
- filename -- 日志输出的文件名，如果指定了这个信息之后，实际上会启用 FileHandler，而不再是 StreamHandler，这样日志信息便会输出到文件中了
- filemode -- 指定日志文件的写入方式
- format -- 指定日志信息的输出格式
%(levelno)s：打印日志级别的数值。
%(levelname)s：打印日志级别的名称。
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]。
%(filename)s：打印当前执行程序名。
%(funcName)s：打印日志的当前函数。
%(lineno)d：打印日志的当前行号。
%(asctime)s：打印日志的时间。
%(thread)d：打印线程ID。
%(threadName)s：打印线程名称。
%(process)d：打印进程ID。
%(processName)s：打印线程名称。
%(module)s：打印模块名称。
%(message)s：打印日志信息。
- datefmt：指定时间的输出格式。

- style：如果 format 参数指定了，这个参数就可以指定格式化时的占位符风格，如 %、{、$ 等。

- level：指定日志输出的类别，程序会输出大于等于此级别的信息。

- stream：在没有指定 filename 的时候会默认使用 StreamHandler，这时 stream 可以指定初始化的文件流。指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；

- handlers：可以指定日志处理时所使用的 Handlers，必须是可迭代的。
