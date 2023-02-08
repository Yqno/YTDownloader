import pytube

print(r"""

                                                                                                                                     
,--.   ,--.             ,--------.        ,--.              ,------.                            ,--.                  ,--.               
 \  `.'  /,---. ,--.,--.'--.  .--',--.,--.|  |-.  ,---.     |  .-.  \  ,---. ,--.   ,--.,--,--, |  | ,---.  ,--,--. ,-|  | ,---. ,--.--. 
  '.    /| .-. ||  ||  |   |  |   |  ||  || .-. '| .-. :    |  |  \  :| .-. ||  |.'.|  ||      \|  || .-. |' ,-.  |' .-. || .-. :|  .--' 
    |  | ' '-' ''  ''  '   |  |   '  ''  '| `-' |\   --.    |  '--'  /' '-' '|   .'.   ||  ||  ||  |' '-' '\ '-'  |\ `-' |\   --.|  |    
    `--'  `---'  `----'    `--'    `----'  `---'  `----'    `-------'  `---' '--'   '--'`--''--'`--' `---'  `--`--' `---'  `----'`--'    
                                                                                                                                     
                                                        https://github.com/Yqno

 """)

link = input("Enter your URL: ")
video = pytube.YouTube(link)

# Get a list of all available video formats
available_formats = video.streams.filter(progressive=True, file_extension='mp4')

# Ask the user which format they want to download
for i, stream in enumerate(available_formats):
    print(f"{i+1}. Resolution: {stream.resolution}")

# Convert the user's input into an integer and select the corresponding format
selected_format = int(input("Enter the number of the desired format: ")) - 1
selected_stream = available_formats[selected_format]

# Download the video
selected_stream.download()

print("Video successfully downloaded!")
