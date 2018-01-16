import xml.sax
import os

class UnUsedSourceHandler( xml.sax.ContentHandler):
    def __init__(self):
        self.currentTag = ""
        self.file_path = ""
        self.prefix = "C:/zdnuist/loocha_git_ws/Campus/"


    def startElement(self, tag, attributes):
        self.currentTag = tag
        # if tag == "problem":
            # print("**************problem**********")


    def endElement(self, tag) :
        if self.currentTag == "file":
            # print(self.file_path)
            positon = self.file_path.find("LoochaCampus")
            target_path = self.prefix + self.file_path[positon:]
            if os.path.exists(target_path) == True:
                if target_path.endswith(".png") == True:
                    print(target_path)
                    os.remove(target_path)
                    print("delete success")

                if target_path.find("/drawable/") != -1:
                    print(target_path)
                    os.remove(target_path)
                    print("delete success")

                if target_path.find("/anim/") != -1:
                    print(target_path)
                    os.remove(target_path)
                    print("delete success")



                

                



    def characters(self, content) :
        if self.currentTag == "file":
            self.file_path = content

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)

    handler = UnUsedSourceHandler()
    parser.setContentHandler(handler)
    parser.parse("C:\\zdnuist\\temp\\AndroidLintUnusedResources.xml")