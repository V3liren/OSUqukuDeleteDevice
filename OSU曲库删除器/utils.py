"""
    @ Time : 2021/2/20/020 17:18
    @ Author : V3利刃
"""
import os
import shutil


def get_dirList(path):
    """
    获取文件夹内文件列表
    :param path:文件夹路径
    :return:
    """
    os.chdir(path)  # 切换或进入路径
    dirList = os.listdir(path)  # 获取路径下所有的文件和文件夹
    isdirList = []
    nulldIrList = []
    for file in dirList:
        isDirPath = path + os.sep + file  # 组合成路径
        if os.path.isdir(isDirPath) and os.listdir(isDirPath):  # 如果是文件夹，并且不是空文件夹
            isdirList.append(isDirPath)  # 添加进列表
        if os.path.isdir(isDirPath) and not os.listdir(isDirPath):  # 如果是文件夹，并且是空文件夹
            nulldIrList.append(isDirPath)
    return isdirList, nulldIrList  # 返回文件列表


def pathName(path):
    # 获取路径最后的一段
    FName = os.path.basename(path)
    return FName


def printPath(print_txt, path):
    # 打印路径最后的一段
    FName = os.path.basename(path)
    print(print_txt, FName)


def del_dir(base_dir, dirpath, failFolderName):
    """
    删除文件夹
    :param base_dir:
    :param dirpath:
    :return:
    """
    try:
        os.chdir(base_dir)  # 切换或进入路径
        shutil.rmtree(dirpath)  # 删除文件夹
        printPath("已删除没有谱子的文件夹：", dirpath)
    except BaseException as e:
        print("\n删除这个文件夹时错误：", pathName(dirpath))
        print("错误信息：", e)
        failFolderName.append(pathName(dirpath))


#     不是空文件夹，进入文件夹
def get_folder_file_list(osuDir):
    # 获取文件夹内文件列表
    os.chdir(osuDir)  # 切换或进入路径
    osuDirList = os.listdir(osuDir)  # 获取路径下所有的文件和文件夹
    return osuDirList


def get_osu(osuDir, osuDirList):
    # 筛选.osu文件
    # 获取.osu文件列表
    osuList = []
    for osuFilePath in osuDirList:
        if (osuFilePath.lower().endswith((".osu"))):
            osuList.append(osuDir + os.sep + osuFilePath)
    return osuList


def delOsu(osuList, MList, osuIndex, failOsuName):
    # 读取.osu文件
    for osuFile in osuList:
        try:
            with open(osuFile, "r", encoding="utf-8") as f:
                osuTxt = f.read()
            for MC in MList:
                # 分析 Mode: x 和 CircleSize:x
                # 符合条件就删除这个.osu文件
                if ("Mode: " in MC) and (MC in osuTxt):  # 删除各种模式
                    os.remove(osuFile)
                    printPath("已删除谱子：", osuFile)
                    osuIndex += 1
                    continue
                elif ("CircleSize:" in MC) and (MC in osuTxt) and ("Mode: 3\n" in osuTxt):  # 删除mania模式键数
                    os.remove(osuFile)
                    printPath("已删除谱子：", osuFile)
                    osuIndex += 1
                    continue
        except BaseException as e:
            print("\n读取或分析这个.osu文件时错误：", pathName(osuFile))
            print("错误信息：", e)
            failOsuName.append(pathName(osuFile))
    return osuIndex


def int_list_input(M, input_info):
    my_list = []
    while True:
        try:
            my_int = input(input_info)
            if my_int == "ok":
                break
            if my_int == "":
                continue
            my_int = int(my_int)
            my_list.append(M + str(my_int) + "\n")
        except BaseException as e:
            print("=====>请输入数字！\n")
    return my_list
