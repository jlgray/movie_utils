import os
import sys

import moviepy.editor as mpy

FPS = 60

if __name__ == "__main__":

    args = sys.argv
    if (len(args) < 2):
        print("Usage is: $>python3 makegif.py <dirname> [outname]")
    else:
        d = args[1]
        if (not os.path.isdir(d)):
            print(d, "is not a valid directory")
        else:
            files = [os.path.join(d, x) for x in os.listdir(d) if x.endswith(".png")]
            
            if len(args) > 2:
                outname = args[2]
                out_fmt = outname.split(".")[-1]
            else:
                outname = d + ".gif"
                out_fmt = "gif"

            if out_fmt == "gif":
                clip = mpy.ImageSequenceClip(files, fps=FPS)
                clip.write_gif(outname, fps=FPS)
                
            elif out_fmt == "mp4":
                clip = mpy.ImageSequenceClip(files, fps=FPS)
                clip.write_videofile(outname, fps=FPS)


