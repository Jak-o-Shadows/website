# -*- coding: utf-8 -*-
import website



def main(stuff):
    try:
        from Cheetah.Template import Template
        t = Template(website.website, searchList =[stuff])
    except:
        t = website.nonCheetah(stuff["title"], stuff["style"], stuff["contents"], stuff["time"], stuff["first"], stuff["second"])
    return t
    
if __name__ == "__main__" :
    main()
