# nijigasaki-bot
A twitter bot that posts every frame of the Nijigasaki Anime in order.
Frames extracted at 1.5 FPS, tweeted every 10 minutes.

* [Twitter Account](https://twitter.com/NijigasakiBot)

![Frame 30, Episode 1](https://i.imgur.com/ohxajgP.jpg)

## Rules for removing useless frames

* All **opening credits** to be removed.
    * Including Sunrise, Funimation credits.
* All **OP** and **ED** themes to be removed.
    * Unless animation is different.
* All **next-episode previews** to be removed.
* All **mid-episode transitions** to be removed.
* All **completely white** or **black** frames to be removed.

## ffmpeg frame extraction command

`ffmpeg -i video.mkv -r 1.5 -qscale:v 2 %04d.jpg`

## Episode folder naming scheme

`./ep#/` e.g. `./ep1/`, `./ep12/`
