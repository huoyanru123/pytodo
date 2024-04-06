import json
import Events

def SaveEvents(filename,event_list):

    # 编码器
    def EncodeEvent(event):
        ## 周期事件编码
        if isinstance(event, Events.Regular):
            event_data = {
                "type": event.type,
                "date": event.date.strftime("%Y-%m-%d"),
                "content": event.content,
                "circular": event.circular,
                "next_date": event.next.strftime("%Y-%m-%d"),  # 将下次事件日期转换为字符串
                "event":"Regular"
            }
            return event_data
        
        ## DDL事件编码
        elif isinstance(event,Events.DDL):
            event_data = {
                "type": event.type,
                "date": event.date.strftime("%Y-%m-%d"),
                "content": event.content,
                "event":"DDL"
            }
            return event_data
        
        ## BGL事件编码
        elif isinstance(event,Events.BGL):
            event_data = {
                "type": event.type,
                "date": event.date.strftime("%Y-%m-%d"),
                "content": event.content,
                "event":"BGL"
            }
            return event_data

        ## 会议事件编码
        elif isinstance(event,Events.Meeting):
            event_data = {
                "type": event.type,
                "date": event.date.strftime("%Y-%m-%d"),
                "content": event.content,
                "event":"Meeting"
            }
            return event_data
        
        ## 原子事件编码
        elif isinstance(event,Events.AtomEvent):
            event_data = {
                "type": event.type,
                "date": event.date.strftime("%Y-%m-%d"),
                "content": event.content,
                "deadline":event.deadline.strftime("%Y-%m-%d"),
                "event":"AtomEvent"
            }
            return event_data
        
        else:
            return event

    serialized_events = []
    for event in event_list:
        serialized_event = EncodeEvent(event)
        serialized_events.append(serialized_event)
    
    with open(filename, "w") as file:
        json.dump(serialized_events, file, indent=4)

    print("已保存")

def LoadEvents(filename,mode='All'):

    # 字符串转为日期
    def str_to_datetime(date):
        startdate_parts = date.split("-")
        year, month, day = map(int, startdate_parts)
        start_date = Events.date(year, month, day)
        return start_date

    # 解码器
    def DecodeEvent(event_data):
        ## Regular事件解码
        if event_data["event"]=="Regular":
            event_type = event_data["type"]
            event_date = event_data["date"]
            event_content = event_data["content"]
            event_circular = event_data["circular"]

            event = Events.Regular(
                date=str_to_datetime(event_date),
                type=event_type,
                content=event_content,
                circular=event_circular,
            )
            return event
        
        ## DDL事件解码
        elif event_data["event"]=="DDL":
            event_type = event_data["type"]
            event_date = event_data["date"]
            event_content = event_data["content"]

            event = Events.DDL(
                date=str_to_datetime(event_date),
                type=event_type,
                content=event_content,
            )
            return event

        ## BGL事件解码
        elif event_data["event"]=="BGL":
            event_type = event_data["type"]
            event_date = event_data["date"]
            event_content = event_data["content"]

            event = Events.BGL(
                date=str_to_datetime(event_date),
                type=event_type,
                content=event_content,
            )
            return event
        
        ## Meeting事件解码
        elif event_data["event"]=="Meeting":
            event_type = event_data["type"]
            event_date = event_data["date"]
            event_content = event_data["content"]

            # 创建 Regular 事件对象并返回
            event = Events.Meeting(
                date=str_to_datetime(event_date),
                type=event_type,
                content=event_content,
            )
            return event
        
        ## AtomEvent事件解码
        elif event_data["event"]=="AtomEvent":
            event_type = event_data["type"]
            event_date = event_data["date"]
            event_content = event_data["content"]
            event_end=event_data["deadline"]

            event = Events.AtomEvent(
                start=str_to_datetime(event_date),
                end=str_to_datetime(event_end),
                type=event_type,
                content=event_content,
            )
            return event
    
    event_list = []
    regular_list=[]
    ddl_list=[]
    bgl_list=[]
    meeting_list=[]
    atomevent_list=[]
    try:
        with open(filename, "r") as file:
            serialized_events = json.load(file)
            for event_data in serialized_events:
                event = DecodeEvent(event_data)
                event_list.append(event)
                if isinstance(event,Events.Regular):
                    regular_list.append(event)
                elif isinstance(event,Events.DDL):
                    ddl_list.append(event)
                elif isinstance(event,Events.BGL):
                    bgl_list.append(event)
                elif isinstance(event,Events.Meeting):
                    meeting_list.append(event)
                elif isinstance(event,Events.AtomEvent):
                    atomevent_list.append(event)

    except FileNotFoundError:
        print(f"找不到文件：{filename}")
    except json.JSONDecodeError:
        print(f"无法解析 JSON 数据：{filename}")

    if mode=="All":
        return event_list
    elif mode=="Regular":
        return regular_list
    elif mode=="DDL":
        return ddl_list
    elif mode=="BGL":
        return bgl_list
    elif mode=="Meeting":
        return meeting_list
    elif mode=="Atomevent":
        return atomevent_list