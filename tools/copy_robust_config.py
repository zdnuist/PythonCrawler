import os
import shutil

os.chdir("C:\\zdnuist\\loocha_git_ws\\Campus\LoochaCampus")

src = "C:/zdnuist/loocha_git_ws/Campus/LoochaCampus/build/outputs/mapping/college/release/mapping.txt"
des = "C:/zdnuist/loocha_git_ws/Campus/LoochaCampus/robust/mapping.txt"
shutil.copyfile(src , des)

src = "C:/zdnuist/loocha_git_ws/Campus/LoochaCampus/build/outputs/robust/methodsMap.robust"
des = "C:/zdnuist/loocha_git_ws/Campus/LoochaCampus/robust/methodsMap.robust"
shutil.copyfile(src , des)

