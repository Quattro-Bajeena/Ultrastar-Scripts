import subprocess, os
from pathlib import Path
from glob import glob
from subprocess import Popen, PIPE, STDOUT, DEVNULL


song_folders = Path("D:/UltraStarSongsAnimuxDe/")
# song_folders = Path("D:/UltraStarDownloadTest/")
with open("debug.txt", 'w', encoding="utf-8") as f_debug:
    all_folders = [x for x in song_folders.iterdir() if x.is_dir]
    for folder_index, folder in enumerate(all_folders):
        folder_song_downloaded = False
        txt_file = list(folder.glob("*.txt"))[0]
        song_name = folder.name
        print(f"{folder_index}: entering: {song_name}. ", end=' ')
        try:
            with open(txt_file, 'r+', encoding="windows-1252") as f:
                lines = f.read().splitlines()
                video_info_index, video_info = [(i,x) for (i,x) in enumerate(lines) if x.startswith("#VIDEO")][0]

                video_info = video_info[7:]
                video_info = video_info.split(",")
                for info in video_info:
                    info_type = info[0]
                    info_content = info[len(info_type)+1:]
                    if info_type == "v" or info_type == "a":
                        if len(info_content) == 11:
                            yt_dlp_command = f"yt-dlp -o \"{folder}\\{song_name}.mp4\" --remux-video mp4 {info_content}"
                            yt_dlp_download_audio = f"yt-dlp -o \"{folder}\\{song_name}.mp3\" -f bestaudio {info_content}"
                            # extract_audio_command = f"ffmpeg -i \"{folder}\\{song_name}.mp4\" -q:a 0 -map a \"{folder}\\{song_name}.mp3\""
                            # print(yt_dlp_command)
                            # print(yt_dlp_download_audio)
                            # break
                            print("downloading. ", end=" ", flush=True)
                            subprocess.run(yt_dlp_command, stdout=DEVNULL, stderr=STDOUT)
                            print("downloading audio. ", end=" ", flush=True)
                            subprocess.run(yt_dlp_download_audio, stdout=DEVNULL, stderr=STDOUT)

                            new_video_info = f"#VIDEO:{song_name}.mp4"
                            lines[video_info_index] = new_video_info
                            new_thumbnail_info = f"#COVER:{song_name} [CO].jpg"
                            lines.insert(video_info_index, new_thumbnail_info)

                            f.seek(0)
                            f.writelines(line + "\n" for line in lines)
                            f.truncate()
                            folder_song_downloaded = True
                            print("finished.")

                        else:
                            print("\nNot proper format - ", info_content)
            if not folder_song_downloaded:
                print(f"\nSong couldn't be downloaded")
        except Exception as e:
            print(f"\nCouldn't download {song_name}")
            print(e)
            f_debug.write(str(e))