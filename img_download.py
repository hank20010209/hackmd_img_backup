import glob
import re
import os


# reference: https://gist.github.com/t510599/069d459f928bb4b1622a428a8bbfa66e
def get_urls():
    for md_file in glob.glob("*.md"):
        urls = []
        dir_name = md_file[:-3]
        os.mkdir(dir_name)
        with open(md_file, encoding="utf-8") as md:
            content = md.read()
            urls = re.findall("(https\://i\.imgur\.com/\w+\.(?:png|jpg|gif))", content)
        if urls:
            with open(os.path.join(dir_name, "url.txt"), "w") as wf:
                wf.write("\n".join(urls))


def download_img():
    for ele in os.listdir(os.getcwd()):
        ori_pwd = os.getcwd()
        if os.path.isdir(ele):
            ori_ele = ele
            ele = ele.replace(" ", "\ ")
            command = f'wget -i url.txt'
            os.chdir(ori_ele)
            os.system(command)
            os.chdir(ori_pwd)


if __name__ == '__main__':
    get_urls()
    download_img()