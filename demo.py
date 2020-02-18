"""
docker demo
"""
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.tracking import manual_tracking, to_fxfy
from moviepy.video import fx as vfx

video = VideoFileClip("what-year.mp4")
video.preview()

txy, (fx, fy) = manual_tracking(video, fps=6)
with open("tracking.dat", "w+") as f:
    pickle.dump(txy)

clip_blurred = video.fx( vfx.headblur, fx, fy, 25)

txt_clip = (
    TextClip("sup anyvision?", font="DejaVu-Sans", fontsize=70, color="white")
    .set_position("center")
    .set_duration(2)
)
result = CompositeVideoClip([video.rotate(180), txt_clip])
result.write_videofile("dockered.webm", fps=25)
result.preview()
