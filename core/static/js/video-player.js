const video = document.getElementById("myVideo")
const btnPlay = document.getElementById("play")
const btnMute = document.getElementById("mute")
const playlist = ['video1', 'video0', ]
const playname = ['minecraft', 'old video', ]
const playactor = ['Track C418', 'Moe staroe drevnee video', ]
const musicName = document.querySelector('.video__tittle')
const actor = document.querySelector('.video__text')
let number = 0;

function play() {
    if (video.paused) {
        video.play();
        btnPlay.innerHTML = "Pause";
    }
    else {
        video.pause();
        btnPlay.innerHTML = "Play";
    }
}

function mute() {
    if (video.muted) {
        video.muted = false;
        btnMute.innerHTML = "Off";
    }
    else {
        video.muted = true;
        btnMute.innerHTML = "On";
    }
}

function next() {
    if (number < playlist.length - 1) {
        number++; // number = number + 1
    } else {
        number = 0
    }
    video.src = `video/${playlist[number]}.mp4`;
    musicName.innerHTML = playname[number];
    actor.innerHTML = playactor[number];
}

function prev() {
    if (number !=0) {
        number--; // number = number - 1
    } else {
        number = playlist.length - 1;
    }
    video.src = `video/${playlist[number]}.mp4`;
    musicName.innerHTML = playname[number];
    actor.innerHTML = playactor[number];
}