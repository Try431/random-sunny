import os
import random
import datetime
import uuid

PREPOPULATED_DURATIONS = {
    "South.Park.S24E00.The.Pandemic.Special.REPACK.1080p.WEB.h264-BAE.mkv": 2840.749000
}

def runBash(cmd):
    os.system(cmd)
    
def trim(duration):
    input = random.choice(list(PREPOPULATED_DURATIONS.keys()))
    start_time = calc_random_clip_times(input, duration)
    
    output_filename = f"test_clip-{str(uuid.uuid4())}.mp4"
    
    cmd_string = f"ffmpeg -hide_banner -loglevel error -y -ss {start_time} -i {input} -ss 00:00:02 -t {duration} -c copy static/videos/{output_filename}"
    # print(cmd_string)
    runBash(cmd_string)
    return output_filename
    

def calc_random_clip_times(filename, requested_duration):
    file_duration = PREPOPULATED_DURATIONS.get(filename)
    start_time_in_seconds = random.randrange(int(file_duration) - int(requested_duration) - 2)
    start_time_formatted = datetime.timedelta(seconds=start_time_in_seconds)
    return start_time_formatted

def cleanup():
    for f in os.listdir("static/videos"):
        os.remove(os.path.join("static/videos", f))

    
if __name__ == "__main__":    
    filename = "South.Park.S24E00.The.Pandemic.Special.REPACK.1080p.WEB.h264-BAE.mkv"
    requested_duration = 45
    start_timestamp = calc_random_clip_times("South.Park.S24E00.The.Pandemic.Special.REPACK.1080p.WEB.h264-BAE.mkv", requested_duration)
    if not start_timestamp:
        exit()
    trim(duration=requested_duration)
