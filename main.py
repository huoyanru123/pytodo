import Events
import LoadSave
import sys
import os
import datetime
import json
from datetime import date

def EventHelp():
    os.system('cls')
    print('''
            ***********************************************************************
            *                       备忘录(事件类型的说明)                        *
            *                                                                     *
            *              周期事件指代每隔一定时间要做的事                       *
            *                                                                     *
            *              截止日期事件指代要在指定日期前做的事                   *
            *                                                                     *
            *              开始日期事件指代要在指定日期之后做的事                 *
            *                                                                     *
            *              会议事件指代要在指定日期当日做的事                     *
            *                                                                     *
            *              原子事件指代要在有起始日期和截止日期的事,可用于创建链  * 
            *                                                                     *
            *                                                                     *
            *                                                                     *
            *                                                                     *
            *                                                                     *
            *                                                                     *
            *                                                                     *
            *                                                                     *
            *                                                                     *
            *                                                                     *
            ***********************************************************************
            ''')
    if input("\n输入back以返回\n")=="back":
        return

def AddMenus():

    print('''
        ***********************************************************************
        *                       备忘录(添加事件)                              *
        *                                                                     *
        *                 1. 创建周期事件                                     *
        *                                                                     *
        *                 2. 创建截止日期事件                                 *
        *                                                                     *
        *                 3. 创建开始日期事件                                 * 
        *                                                                     *
        *                 4. 创建会议事件                                     *
        *                                                                     *
        *                 5. 创建原子事件                                     *
        *                                                                     *
        *                 6. 返回                                             *
        *                                                                     *
        *                 7. 帮助                                             *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        ***********************************************************************
        ''')
    
    events=LoadSave.LoadEvents("history.json")

    while True:
        choice = input("请输入命令：\n").strip()
        if choice == "1":
            event = Events.CreateRegular()
            events.append(event)
        elif choice == "2":
            event = Events.CreateDDL()
            events.append(event)
        elif choice == "3":
            event = Events.CreateBGL()
            events.append(event)
        elif choice == "4":
            event = Events.CreateMeeting()
            events.append(event)
        elif choice == "5":
            event = Events.CreateAtom()
            events.append(event)
        elif choice == "6":
            break
        elif choice == "7":
            EventHelp()
            return
        else:
            print("无效命令,请重试\n")
            choice=input()
            os.system('cls')
    if len(events)>0: 
        LoadSave.SaveEvents("history.json",events)

def Help():
    print('''
        ***********************************************************************
        *                        备忘录(指令说明)                             *
        *                                                                     *
        *              使用add指令以增加事件                                  *
        *                                                                     *
        *              使用help指令以查看指令功能                             *
        *                                                                     *
        *              使用done指令以删除事件                                 *
        *                                                                     *
        *              使用show指令以显示当前备忘录中所有事件                 *
        *                                                                     *
        *              使用today指令以显示今日要做                            * 
        *                                                                     *
        *              使用future指令以显示未来要做                           *
        *                                                                     *
        *              使用quit指令退出本程序                                 *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        ***********************************************************************
        ''')
    if input("\n输入back以返回\n")=="back":
        return

def DoneMenus():
    os.system('cls')

    print(
        '''
        ***********************************************************************
        *                            备忘录(已做)                             *
        *                                                                     *
        *                 1.所有事件                                          *
        *                                                                     *
        *                 2.部分事件                                          *
        *                                                                     *
        *                 3.帮助                                              *
        *                                                                     *
        *                 4.返回                                              *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        ***********************************************************************
        '''
    )

    cmd=input()
    while(True):
        # 输入命令跳转指定界面
        if cmd=="1":
            os.system('cls')
            with open("history.json", "w") as file:
                json.dump([], file, indent=4)
            return

        elif cmd=="2":
            os.system('cls')
            events=LoadSave.LoadEvents("history.json")
            new_events=[]
            length=len(events)
            if length>0:
                for event in events:
                    event.Print()
                done_things=[int(x)-1 for x in input("请选择已做事项序号(以空格隔开)：\n").split(" ") if int(x) <length]
                for i in range(0,length-1):
                    if i not in done_things:
                        new_events.append(events[i])
                LoadSave.SaveEvents("history.json",new_events)
                return                
            else:
                print("备忘录无事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="4":
            return
        
        elif cmd=="3":
            EventHelp()
            return
        else:
            print("无效命令，请重试")
            cmd=input()
            os.system('cls')

def Show():
    os.system('cls')

    print(
        '''
        ***********************************************************************
        *                           备忘录(展示事项)                          *
        *                                                                     *
        *                 1.所有事件                                          *
        *                                                                     *
        *                 2.周期事件                                          *
        *                                                                     *
        *                 3.DLL事件                                           *
        *                                                                     *
        *                 4.BGL事件                                           *
        *                                                                     *
        *                 5.会议事件                                          *
        *                                                                     *
        *                 6.原子事件                                          *
        *                                                                     *
        *                 7.返回                                              *
        *                                                                     *
        *                 8.帮助                                              *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        ***********************************************************************
        '''
    )

    cmd=input()
    while(True):
        # 输入命令跳转指定界面
        if cmd=="1":
            os.system('cls')
            events=LoadSave.LoadEvents("history.json")
            if len(events)>0:
                for event in events:
                    event.Print()
            else:
                print("备忘录无事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="2":
            os.system('cls')
            events=LoadSave.LoadEvents("history.json","Regular")
            if len(events)>0:
                for event in events:
                    event.Print()
            else:
                print("备忘录无周期事项")
            if input("\n输入back以返回\n")=="back":
                return
        
        elif cmd=="3":
            os.system('cls')
            events=LoadSave.LoadEvents("history.json","DDL")
            if len(events)>0:
                for event in events:
                    event.Print()
            else:
                print("备忘录无DDL事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="4":
            os.system('cls')
            events=LoadSave.LoadEvents("history.json","BGL")
            if len(events)>0:
                for event in events:
                    event.Print()
            else:
                print("备忘录无BGL事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="5":
            os.system('cls')
            events=LoadSave.LoadEvents("history.json","Meeting")
            if len(events)>0:
                for event in events:
                    event.Print()
            else:
                print("备忘录无会议事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="6":
            os.system('cls')
            events=LoadSave.LoadEvents("history.json","Atomevent")
            if len(events)>0:
                for event in events:
                    event.Print()
            else:
                print("备忘录无原子事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="7":
            return
        
        elif cmd=="8":
            EventHelp()
            return
        else:
            print("无效命令，请重试")
            cmd=input()
            os.system('cls')

def Today():
    
    print(
        '''
        ***********************************************************************
        *                           备忘录(今日事项)                          *
        *                                                                     *
        *                 1.所有事件                                          *
        *                                                                     *
        *                 2.周期事件                                          *
        *                                                                     *
        *                 3.DLL事件                                           *
        *                                                                     *
        *                 4.BGL事件                                           *
        *                                                                     *
        *                 5.会议事件                                          *
        *                                                                     *
        *                 6.原子事件                                          *
        *                                                                     *
        *                 7.返回                                              *
        *                                                                     *
        *                 8.帮助                                              *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        ***********************************************************************
        '''
    )
    events=LoadSave.LoadEvents("history.json")
    today_events=[]
    cmd=input()
    for event in events:
        if isinstance(event,Events.Regular) and event.next==date.today():
            today_events.append(event)
        elif isinstance(event,Events.DDL) and event.date>=date.today():
            today_events.append(event)
        elif isinstance(event,Events.BGL) and event.date<=date.today():
            today_events.append(event)
        elif isinstance(event,Events.Meeting) and event.date==date.today():
            today_events.append(event)
        elif isinstance(event,Events.AtomEvent) and event.deadline>=date.today() and event.date<=date.today():
            today_events.append(event)
    # 输入命令跳转指定界面
    while(True):
        if cmd=="1":
            os.system('cls')
            if len(events)>0:
                for event in today_events:
                    event.Print()
            else:
                print("今日无事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="2":
            os.system('cls')
            regular_events=[event for event in today_events if isinstance(event,Events.Regular)]
            if len(regular_events)>0:
                for regular_event in regular_events:
                    regular_event.Print()
            else:
                print("备忘录无周期事项")
            if input("\n输入back以返回\n")=="back":
                return
        
        elif cmd=="3":
            os.system('cls')
            DDL_events=[event for event in today_events if isinstance(event,Events.DDL)]
            if len(DDL_events)>0:
                for DDL_event in DDL_events:
                    DDL_event.Print()
            else:
                print("备忘录无DDL事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="4":
            os.system('cls')
            BGL_events=[event for event in today_events if isinstance(event,Events.BGL)]
            if len(BGL_events)>0:
                for BGL_event in BGL_events:
                    BGL_event.Print()
            else:
                print("备忘录无BGL事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="5":
            os.system('cls')
            Meeting_events=[event for event in today_events if isinstance(event,Events.Meeting)]
            if len(Meeting_events)>0:
                for Meeting_event in Meeting_events:
                    Meeting_event.Print()
            else:
                print("备忘录无会议事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="6":
            os.system('cls')
            Atom_events=[event for event in today_events if isinstance(event,Events.AtomEvent)]
            if len(Atom_events)>0:
                for atom_event in Atom_events:
                    atom_event.Print()
            else:
                print("备忘录无原子事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="7":
            return
        
        elif cmd=="8":
            EventHelp()
            return

        else:
            print("无效命令，请重试")
            cmd=input()
            os.system('cls')

def FutureMenus(n=3):
    print(
        '''
        ***********************************************************************
        *                       备忘录(未来{0}天的事项)                         *
        *                                                                     *
        *                 1.所有事件                                          *
        *                                                                     *
        *                 2.周期事件                                          *
        *                                                                     *
        *                 3.DLL事件                                           *
        *                                                                     *
        *                 4.BGL事件                                           *
        *                                                                     *
        *                 5.会议事件                                          *
        *                                                                     *
        *                 6.原子事件                                          *
        *                                                                     *
        *                 7.返回                                              *
        *                                                                     *
        *                 8.帮助                                              *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        ***********************************************************************
        '''
    .format(n))
    events=LoadSave.LoadEvents("history.json")
    future_day=date.today()+datetime.timedelta(days=n)
    today_events=[]
    cmd=input()
    for event in events:
        if isinstance(event,Events.Regular) and event.next==future_day:
            today_events.append(event)
        elif isinstance(event,Events.DDL) and event.date>=future_day:
            today_events.append(event)
        elif isinstance(event,Events.BGL) and event.date<=future_day:
            today_events.append(event)
        elif isinstance(event,Events.Meeting) and event.date==future_day:
            today_events.append(event)
        elif isinstance(event,Events.AtomEvent) and event.date<=future_day and event.date>=future_day:
            today_events.append(event)
    # 输入命令跳转指定界面
    while(True):
        if cmd=="1":
            os.system('cls')
            if len(events)>0:
                for event in today_events:
                    event.Print()
            else:
                print("今日无事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="2":
            os.system('cls')
            regular_events=[event for event in today_events if isinstance(event,Events.Regular)]
            if len(regular_events)>0:
                for regular_event in regular_events:
                    regular_event.Print()
            else:
                print("备忘录无周期事项")
            if input("\n输入back以返回\n")=="back":
                return
        
        elif cmd=="3":
            os.system('cls')
            DDL_events=[event for event in today_events if isinstance(event,Events.DDL)]
            if len(DDL_events)>0:
                for DDL_event in DDL_events:
                    DDL_event.Print()
            else:
                print("备忘录无DDL事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="4":
            os.system('cls')
            BGL_events=[event for event in today_events if isinstance(event,Events.BGL)]
            if len(BGL_events)>0:
                for BGL_event in BGL_events:
                    BGL_event.Print()
            else:
                print("备忘录无BGL事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="5":
            os.system('cls')
            Meeting_events=[event for event in today_events if isinstance(event,Events.Meeting)]
            if len(Meeting_events)>0:
                for Meeting_event in Meeting_events:
                    Meeting_event.Print()
            else:
                print("备忘录无会议事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="6":
            os.system('cls')
            Atom_events=[event for event in today_events if isinstance(event,Events.AtomEvent)]
            if len(Atom_events)>0:
                for atom_event in Atom_events:
                    atom_event.Print()
            else:
                print("备忘录无原子事项")
            if input("\n输入back以返回\n")=="back":
                return

        elif cmd=="7":
            return
        
        elif cmd=="8":
            EventHelp()
            return

        else:
            print("无效命令，请重试")
            cmd=input()
            os.system('cls')

def Quit():
    os.system('cls')
    sys.exit(0)

def MainMenus():
    os.system('cls')
    print(
        '''
        ***********************************************************************
        *                             备忘录                                  *
        *                                                                     *
        *                 add                                                 *
        *                                                                     *
        *                 help                                                *
        *                                                                     *
        *                 done                                                *
        *                                                                     *
        *                 show                                                *
        *                                                                     *
        *                 today                                               *
        *                                                                     *
        *                 future                                              *
        *                                                                     *
        *                 quit                                                *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        *                                                                     *
        ***********************************************************************
        '''
    )
    cmd=input()
    # 输入命令跳转指定界面
    if cmd=="add":
        os.system('cls')
        AddMenus()

    elif cmd=="help":
        os.system('cls')
        Help()
    
    elif cmd=="done":
        os.system('cls')
        DoneMenus()

    elif cmd=="show":
        os.system('cls')
        Show()

    elif cmd=="today":
        os.system('cls')
        Today()

    elif cmd.startswith("future "):  # 检查命令是否以 "future " 开头
        os.system('cls')
        n = int(cmd.split(" ")[1])  # 提取参数 n
        FutureMenus(n)

    elif cmd=="quit":
        Quit()
    
    else:
        print("无效命令，请重试")
        cmd=input()
        os.system('cls')

while(1):
    MainMenus()

