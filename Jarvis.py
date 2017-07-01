# This is main module

import Audio_to_text_translator as AudioConverter
import Jarvis_WebPage as JWeb

while(1):
    Audio_Txt=AudioConverter.main()
    print('Audio_Txt -->',Audio_Txt)
    if 'jarvis' in Audio_Txt:
        Audio_list=Audio_Txt.split(' ')
        if 'play' in Audio_list:
            txt=' '.join(Audio_list[2:])
            print('play')
            print(txt)
            JWeb.youtubeSearch(txt)
        elif 'search' in Audio_Txt:
            txt = ' '.join(Audio_list[2:])
            print('search')
            print(txt)
            JWeb.websearch(txt)





