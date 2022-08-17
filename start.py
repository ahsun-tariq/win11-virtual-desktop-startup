import ctypes, time, json, subprocess, os

with open("apps.json") as jsonFile:
    apps = json.load(jsonFile)

def launch_apps(desktops=4,apps=apps):

    os.add_dll_directory(os.getcwd())
    virtual_desktop_accessor = ctypes.WinDLL("VirtualDesktopAccessor.dll")

    for i in range(0,desktops):
        apps_to_start = []
        print(f'Starting {apps_to_start} on desktop {i}')
        sleep_time = 0
        for app, item in apps.items():
            if item['desktop'] == i:
                apps_to_start.append(app)
        if len(apps_to_start)<1:
            sleep_time = 0
        else:
            for app in apps_to_start:
                if apps[app]['time'] > sleep_time:
                    sleep_time = apps[app]['time']
        virtual_desktop_accessor.GoToDesktopNumber(i)
        for app in apps_to_start:
            p = subprocess.Popen(apps[app]['path'])
        time.sleep(sleep_time)
    virtual_desktop_accessor.GoToDesktopNumber(0) 

launch_apps()