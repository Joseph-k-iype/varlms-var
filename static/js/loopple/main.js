
//following defines the custom controls html.  note the first two divs are not standard, but are included to take advantage of the control hiding
var controls = ["<div class='title'>",
    "This is some text",
    "</div>",
    "<div class='button'>",
    "<button type='button' class='btn btn-secondary'>This is a button</button>",
    "</div>",
    "<div class='plyr__controls'>",
    "<button type='button' data-plyr='play'>",
    "<svg><use xlink:href='#plyr-play'></use></svg>",
    "<span class='plyr__sr-only'>Play</span>",
    "</button>",
    "<button type='button' data-plyr='pause'>",
    "<svg><use xlink:href='#plyr-pause'></use></svg>",
    "<span class='plyr__sr-only'>Pause</span>",
    "</button>",
    "<span class='plyr__time'>",
    "<span class='plyr__sr-only'>Current time</span>",
    "<span class='plyr__time--current'>00:00</span>",
    "</span>",
    "<span class='plyr__progress'>",
    "<label for='seek{id}' class='plyr__sr-only'>Seek</label>",
    "<input id='seek{id}' class='plyr__progress--seek' type='range' min='0' max='100' step='0.1' value='0' data-plyr='seek'>",
    "<progress class='plyr__progress--played' max='100' value='0' role='presentation'></progress>",
    "<progress class='plyr__progress--buffer' max='100' value='0'>",
    "<span>0</span>% buffered",
    "</progress>",
    "<span class='plyr__tooltip'>00:00</span>",
    "</span>",
    "<span class='plyr__time'>",
    "<span class='plyr__sr-only'>Duration</span>",
    "<span class='plyr__time--duration'>00:00</span>",
    "</span>",
    "<button type='button' data-plyr='mute'>",
    "<svg class='icon--muted'><use xlink:href='#plyr-muted'></use></svg>",
    "<svg><use xlink:href='#plyr-volume'></use></svg>",
    "<span class='plyr__sr-only'>Toggle Mute</span>",
    "</button>",
    "<span class='plyr__volume'>",
    "<label for='volume{id}' class='plyr__sr-only'>Volume</label>",
    "<input id='volume{id}' class='plyr__volume--input' type='range' min='0' max='10' value='5' data-plyr='volume'>",
    "<progress class='plyr__volume--display' max='10' value='0' role='presentation'></progress>",
    "</span>",
    "<button type='button' data-plyr='captions'>",
    "<svg class='icon--captions-on'><use xlink:href='#plyr-captions-on'></use></svg>",
    "<svg><use xlink:href='#plyr-captions-off'></use></svg>",
    "<span class='plyr__sr-only'>Toggle Captions</span>",
    "</button>",
    "<button type='button' data-plyr='fullscreen'>",
    "<svg class='icon--exit-fullscreen'><use xlink:href='#plyr-exit-fullscreen'></use></svg>",
    "<svg><use xlink:href='#plyr-enter-fullscreen'></use></svg>",
    "<span class='plyr__sr-only'>Toggle Fullscreen</span>",
    "</button>",
    "</div>"].join("");

(function () {
    // pass the controls variable to the html config attribute
    var instances = plyr.setup({
        html: controls
    });
})();


function loadContent(lesson) {
    // console.log(lesson);
    lesson = lesson.replace(/'/g, '"');
    lesson = JSON.parse(lesson);
    console.log(lesson.video);
    const video = lesson.video;
    const ab = document.getElementById('player');
    console.log(ab);
    ab.src = 'http://127.0.0.1:8000/videos/' + video;
    ab.play()
    console.log(lesson);
    document.getElementById("lesson-desc").innerHTML = lesson.description;
    const question = document.getElementById("quiz-ques");
    question.innerHTML = '';
    question.innerHTML = lesson.quiz[0].question;
    console.log(lesson.quiz[0].question);

    var container = document.getElementById("quiz-ans");
    //get length of lesson.quiz
    var len = lesson.quiz.length;
    console.log(len);
    // 
    var htmlElements = "";

    for (var i = 0; i < lesson.quiz.length; i++) {
        // print the question
        console.log(lesson.quiz[i].question);

        document.getElementById("abc").innerHTML += '<div class="col-lg-12" id = "question-title">' + lesson.quiz[i].question +'</div>';
        //console.log(document.getElementById("question+title").innerHTML = '<div class="col-lg-12" id = "question-title">' +lesson.quiz[i].question+ '</div>');
    }


    
    //onclick add event listerner to change video source
    //refresh the video element using the new source
    // var ab =  document.getElementById('videoid').src = 'http://127.0.0.1:8000/videos/'+video;
    // console.log(ab);
    // //pass videoid to the src
}