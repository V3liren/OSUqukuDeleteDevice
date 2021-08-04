"""
    @ Time : 2021/2/20/020 16:58
    @ Author : V3利刃
"""
import os
import utils

base_dir = os.path.dirname(os.path.abspath(__file__))  # 项目根目录

folderIndex = 0  # 删除的文件夹数量
failFolderName = []  # 删除失败的文件夹名称列表

osuIndex = 0  # 删除的osu文件数量
failOsuName = []  # 删除失败的osu文件名称列表

try:
    print("请确认osu\\Song目录为：", base_dir)
    print("\nOSU!曲库谱面删除器4.0极速版 by V3利刃\n 请将程序放入Songs目录运行~~~\n===== 请输入删除设置（输入：“ok” 以确定）：=====\n")
    print("           +++ Q1 此处删除的是 游戏模式： +++\n0:osu! 1:taiko 2:catch 3:mania")
    ModeList = utils.int_list_input("Mode: ", "请继续输入要删除的 mode数字：")

    print()
    print("          +++ Q2 此处删除的是 mania键数： +++\n1~18k")
    CircleSizeList = utils.int_list_input("CircleSize:", "请继续输入要删除的 mania键数：")
    print("\n正在加载谱子文件，请稍后......")
    MList = ModeList + CircleSizeList
    # print(MList)
    # 获取所有文件列表
    # 判断是否是文件夹
    isdirList, nulldIrList = utils.get_dirList(base_dir)

    #     是文件夹，是否是空文件夹，是就删除
    for nullDir in nulldIrList:
        # 删除空文件夹
        utils.del_dir(base_dir, nullDir, failFolderName)
        folderIndex += 1
        utils.printPath("已删除空文件夹：", nullDir)

    num = len(isdirList)
    print(F"已获取{num}个项目")

    for osuDir in isdirList:
        osuDirList = utils.get_folder_file_list(osuDir)  # 获取文件夹内文件列表
        osuList = utils.get_osu(osuDir, osuDirList)  # 获取.osu文件列表
        # print("osuList: ",osuList)
        if osuList == []:  # 没有.osu文件就返回上一层，删除这个文件夹
            utils.del_dir(base_dir, osuDir, failFolderName)
            folderIndex += 1
        else:  # 存在.osu文件就分析.osu文件
            # 分析 Mode: x 和 CircleSize:x
            # 符合条件就删除这个.osu文件
            osuIndex = utils.delOsu(osuList, MList, osuIndex, failOsuName)
            # 删除完.osu文件就继续获取文件夹内文件列表
            newOsuDirList = utils.get_folder_file_list(osuDir)
            newOsuList = utils.get_osu(osuDir, newOsuDirList)  # 获取.osu文件列表
            #     没有.osu文件就返回上一层，删除这个文件夹
            # print("newOsuList: ", newOsuList)
            if newOsuList == []:
                utils.del_dir(base_dir, osuDir, failFolderName)
                folderIndex += 1
        num -= 1
        print("剩余待分析的项目有：", num, "个")

except BaseException as e:
    print()
    print("error info: ", e)
    print("error file: ", e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
    print("error line: ", e.__traceback__.tb_lineno, "行")  # 发生异常所在的行数
finally:
    print(F"\n执行结束。删除了{osuIndex}个谱面，删除了{folderIndex}个文件夹。")
    print(F"{len(failFolderName)}个文件夹删除失败：{failFolderName}")
    print(F"{len(failOsuName)}个谱面删除失败：{failOsuName}")
    print("by V3利刃")
    while True:
        a = input("\n输入数字0并按回车键结束程序：")
        if a == "0":
            break
        else:
            continue
