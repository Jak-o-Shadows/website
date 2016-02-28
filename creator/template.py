# -*- coding: utf-8 -*-
import website



def main(stuff):
    try:
        from Cheetah.Template import Template
        t = Template(website.website, searchList =[stuff])
    except:
        print stuff["title"]
        print stuff["style"]
        print stuff["contents"]
        print stuff["time"]
        t = website.nonCheetah(stuff["title"], stuff["style"], stuff["contents"], stuff["time"])
    return t
    
if __name__ == "__main__" :
    main()
