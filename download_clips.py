import subprocess
from pathlib import Path
from glob import glob


# song_folders = Path("D:/UltraStarSongsAnimuxDe/")
song_folders = Path("D:/UltraStarDownloadTest/")
with open("debug.txt", 'w') as f_debug:
    for folder in [x for x in song_folders.iterdir() if x.is_dir]:
        folder_song_downloaded = False
        txt_file = list(folder.glob("*.txt"))[0]
        with open(txt_file) as f:
            lines = f.read().splitlines()
            video_info = [x for x in lines if x.startswith("#VIDEO")][0]
            video_info = video_info[7:]
            video_info = video_info.split(",")
            for info in video_info:
                info_type = info[0]
                # f_debug.write(info + "\n")
                info_content = info[len(info_type)+1:]
                if info_type == "v" or info_type == "a":
                    folder_song_downloaded = True
                    if len(info_content) == 11:
                        # print(folder, info_content)
                        # f_debug.write(info_type + " = " + info_content + "\n")
                        # youtube_link = f"https://www.youtube.com/watch?v={info_content}"

                        video_command = f"yt-dlp -o \"{folder}\\{folder.name}.mp4\" --remux-video mp4 {info_content}"
                        audio_command = f"yt-dlp -o \"{folder}\\{folder.name}.mp4\" --extract-audio --audio-format mp3 {info_content}"
                        # thumbnail_command = f"yt-dlp -o \"{folder}\\{folder.name}.mp4\" --write-thumbnail --skip-download {info_content}"
                        print(video_command)
                        print(audio_command)
                        # print(folder.name)
                        # print(youtube_link)

                        # You have to change line from
                        # #VIDEO:co=https://static.wikia.nocookie.net/love-live/images/b/ba/Bokura_wa_Ima_no_Naka_de_-_Cover.jpg
                        # to
                        # #VIDEO:µ’s - Bokura wa Ima no Naka de.mp4


                        #INSERT cover file [CO] file to txt
                        pass
                    else:
                        pass
                        # print("!!!not proper format - ",folder, info_content)
        if not folder_song_downloaded:
            print("!!!!!!not downloaded - " + str(folder))

        
    