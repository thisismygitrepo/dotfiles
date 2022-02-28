

import crocodile.toolbox as tb
import platform

system = platform.system()

os = tb.os
P = tb.P
L = tb.List

DotFiles = P.home().joinpath("dotfiles")

UserProfile = P(tmp) if (tmp := os.getenv("USERPROFILE")) else None
OneDriveConsumer = P(tmp) if (tmp := os.getenv("OneDriveConsumer")) else None
OneDriveCommercial = P(tmp) if (tmp := os.getenv("OneDriveCommercial")) else None
OneDrive = P(tmp) if (tmp := os.getenv("OneDrive")) else None

LocalAppData = P(tmp) if (tmp := os.getenv("LOCALAPPDATA")) else None  # C:\Users\username\AppData\Local
AppData = P(tmp) if (tmp := os.getenv("APPDATA")) else None  # C:\Users\username\AppData\Roaming

ProgramData = P(tmp) if (tmp := os.getenv("PROGRAMDATA")) else None  # C:\ProgramData

ProgramFiles = P(tmp) if (tmp := os.getenv("ProgramFiles")) else None  # C:\Program Files
ProgramFilesX86 = P(tmp) if (tmp := os.getenv("ProgramFiles(x86)")) else None  # C:\Program Files (x86)
ProgramW6432 = P(tmp) if (tmp := os.getenv("ProgramW6432")) else None  # C:\Program Files

CommonProgramFiles = P(tmp) if (tmp := os.getenv("CommonProgramFiles")) else None  # C:\Program Files\Common Files
CommonProgramFilesX86 = P(tmp) if (tmp := os.getenv("CommonProgramFiles(x86)")) else None  # C:\Program Files (x86)\Common Files
CommonProgramW6432 = P(tmp) if (tmp := os.getenv("CommonProgramW6432")) else None  # C:\Program Files\Common Files

Tmp = P(tmp) if (tmp := os.getenv("TMP")) else None  # C:\Users\usernrame\AppData\Local\Temp
Temp = Tmp

Path = L(os.getenv("PATH").split(";")).apply(P)
PSPath = L(os.getenv("PSModulePath").split(";")).apply(P)

HostName = os.getenv("COMPUTERNAME")
UserDomain = os.getenv("USERDOMAIN")
UserName = os.getenv("USERNAME")
OS = os.getenv("OS")  # Windows_NT
Public = P(tmp) if (tmp := os.getenv("PUBLIC")) else None


def construct_path(path_list):
    from functools import reduce
    return reduce(lambda x, y: x + ";" + y, tb.L(tb.pd.unique(path_list)).apply(str))


if __name__ == '__main__':
    pass
