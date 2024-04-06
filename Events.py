from datetime import date, timedelta
from abc import ABC
from abc import abstractmethod

# 事件类型定义

### 事件基类
class Event(ABC):
    @abstractmethod
    def __init__(self) -> None:
        '''
        __date表示事件时间，__type表示事件类型,__content表示事件内容
        '''
        self.__date=date(2004,8,4)
        self.__type=""
        self.__content=""

    @abstractmethod
    def Print(self):
        '''
        说明date
        '''

### 周期事件类
class Regular(Event):
    '''
    Regularly需要提供事件发生的频次circular
    '''

    #### 初始化函数
    def __init__(self,date,type,content,circular) -> None:
        super().__init__()
        self.__date=date
        self.__type=type
        self.__content=content
        self.__circular=circular
        self.__next=timedelta(days=self.__circular)+self.__date
    
    #### 读写器
    @property
    def date(self):
        return self.__date
    @property
    def type(self):
        return self.__type
    @property
    def content(self):
        return self.__content
    @property
    def circular(self):
        return self.__circular
    @property
    def next(self):
        return self.__next

    #### 更新函数
    def Update(self):
        '''
        如果今天是作此事的日期，则更新其日期属性为今天
        '''
        if date.today==self.__next:
            self.__date=date.today()
            self.__next=timedelta(days=self.__circular)+self.__date

    #### 打印函数
    def Print(self):
        print("{0}\n{1}\n上次做是在:{2}\n下次做是在:{3}\n每{4}天一次\n".format(self.__type, self.__content, self.__date, self.__next, self.__circular))

#### 创建周期事件
def CreateRegular():
    input_data = input("创建一个周期事件：按格式：类型 内容 起始时间 周期输入\n").split(" ")
    event_type = input_data[0]
    event_content = input_data[1]
    startdate_parts = input_data[2].split("-")
    year, month, day = map(int, startdate_parts)
    circular = int(input_data[3])
    start_date = date(year, month, day)
    return Regular(date=start_date, type=event_type, content=event_content, circular=circular)


### 截止日期类
class DDL(Event):
    #### 初始化函数
    def __init__(self,date,type,content) -> None:
        super().__init__()
        self.__date=date    #截止日期
        self.__type=type
        self.__content=content

    # 读写器
    @property
    def date(self):
        return self.__date
    @property
    def type(self):
        return self.__type
    @property
    def content(self):
        return self.__content

    #### 打印函数
    def Print(self):
        print("{0}\n{2}\nDDL为{1}\n".format(self.__type,self.__date,self.__content))

#### 创建截止日期事件
def CreateDDL():
    input_data = input("创建一个DDL事件：按格式：类型 内容 截止时间输入\n").split(" ")
    event_type = input_data[0]
    event_content = input_data[1]
    startdate_parts = input_data[2].split("-")
    year, month, day = map(int, startdate_parts)
    end_date = date(year, month, day)
    return DDL(date=end_date, type=event_type, content=event_content)

### 开始日期类
class BGL(Event):

    #### 初始化函数
    def __init__(self,date,type,content) -> None:
        super().__init__()
        self.__date=date    #开始日期
        self.__type=type
        self.__content=content

    # 读写器
    @property
    def date(self):
        return self.__date
    @property
    def type(self):
        return self.__type
    @property
    def content(self):
        return self.__content

    #### 打印函数
    def Print(self):
        print("{0}\n{2}\nBGL为{1}\n".format(self.__type,self.__date,self.__content))

#### 创建开始日期事件
def CreateBGL():
    input_data = input("创建一个BGL事件：按格式：类型 内容 开始时间输入\n").split(" ")
    event_type = input_data[0]
    event_content = input_data[1]
    startdate_parts = input_data[2].split("-")
    year, month, day = map(int, startdate_parts)
    start_date = date(year, month, day)
    return BGL(date=start_date, type=event_type, content=event_content)

### 会议类
class Meeting(Event):
    '''
    会议类是指在具体的某一天的一次性事件
    '''
    #### 初始化函数
    def __init__(self,date,type,content) -> None:
        super().__init__()
        self.__date=date    #会议日期
        self.__type=type
        self.__content=content

    # 读写器
    @property
    def date(self):
        return self.__date
    @property
    def type(self):
        return self.__type
    @property
    def content(self):
        return self.__content

    #### 打印函数
    def Print(self):
        print("{0}\n{2}\n{1}做\n".format(self.__type,self.__date,self.__content))

#### 创建会议事件
def CreateMeeting():
    input_data = input("创建一个会议事件：按格式：类型 内容 时间输入\n").split(" ")
    event_type = input_data[0]
    event_content = input_data[1]
    startdate_parts = input_data[2].split("-")
    year, month, day = map(int, startdate_parts)
    start_date = date(year, month, day)
    return Meeting(date=start_date, type=event_type, content=event_content)

### 原子事件
'''
原子事件代指有开始日期和截止日期的事件，用来构建链
'''
class AtomEvent(Event):
    #### 初始化函数
    def __init__(self,start,end,type,content) -> None:
        super().__init__()
        self.__date=start    #开始日期
        self.__type=type
        self.__content=content
        self.__deadline=end     #结束日期

    # 读写器
    @property
    def date(self):
        return self.__date
    @property
    def type(self):
        return self.__type
    @property
    def content(self):
        return self.__content
    @property
    def deadline(self):
        return self.__deadline

    #### 打印函数
    def Print(self):
        print("{0}\n{2}\nBGL为{1}\nDDL为{3}\n".format(self.__type,self.__date,self.__content,self.__deadline))

#### 创建原子事件
def CreateAtom():
    input_data = input("创建一个原子事件：按格式：类型 内容 起始时间 截止时间输入\n").split(" ")
    event_type = input_data[0]
    event_content = input_data[1]
    startdate_parts = input_data[2].split("-")
    year1, month1, day1 = map(int, startdate_parts)
    start_date = date(year1, month1, day1)
    enddate_parts=input_data[3].split("-")
    year2, month2, day2 = map(int, enddate_parts)
    end_date = date(year2, month2, day2)
    return AtomEvent(start=start_date,end=end_date,type=event_type, content=event_content)