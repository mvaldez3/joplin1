/**************** 
 * Joplin1 Test *
 ****************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1, 1, 1]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'joplin1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Welcome_Initializing_ScreenRoutineBegin());
flowScheduler.add(Welcome_Initializing_ScreenRoutineEachFrame());
flowScheduler.add(Welcome_Initializing_ScreenRoutineEnd());
flowScheduler.add(recodeTrainRoutineBegin());
flowScheduler.add(recodeTrainRoutineEachFrame());
flowScheduler.add(recodeTrainRoutineEnd());
const trials_trainLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_trainLoopBegin, trials_trainLoopScheduler);
flowScheduler.add(trials_trainLoopScheduler);
flowScheduler.add(trials_trainLoopEnd);
flowScheduler.add(recodeTestRoutineBegin());
flowScheduler.add(recodeTestRoutineEachFrame());
flowScheduler.add(recodeTestRoutineEnd());
const trials_testLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_testLoopBegin, trials_testLoopScheduler);
flowScheduler.add(trials_testLoopScheduler);
flowScheduler.add(trials_testLoopEnd);
flowScheduler.add(debrief_thankyouRoutineBegin());
flowScheduler.add(debrief_thankyouRoutineEachFrame());
flowScheduler.add(debrief_thankyouRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "Welcome_Initializing_Screen"
  Welcome_Initializing_ScreenClock = new util.Clock();
  import * as sf from 'stim_file_script';
  var random_proto;
  random_proto = sf.randpro_select("/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/Prototype.csv", null);
  
  welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text',
    text: 'Insert welcome text.\n\nPress SPACE to proceed',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  welcome_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "recodeTrain"
  recodeTrainClock = new util.Clock();
  sf.stim_build("/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/dev_train.csv", random_proto);
  os.rename("/Volumes/shares/Cabi/exp/joplin/joplin1/data/_stimfile.csv", (filename + "_stimfile_train.csv"));
  
  // Initialize components for Routine "stimTrain"
  stimTrainClock = new util.Clock();
  train_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'train_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.05), 0.1], size : [0.45, 0.675],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  train_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  batmans_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'batmans_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.35), (- 0.35)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  robins_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'robins_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.35, (- 0.35)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "fix1000"
  fix1000Clock = new util.Clock();
  ITIstim = new visual.ShapeStim ({
    win: psychoJS.window, name: 'ITIstim', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "recodeTest"
  recodeTestClock = new util.Clock();
  // Initialize components for Routine "stimTest"
  stimTestClock = new util.Clock();
  test_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.05), 0.1], size : [0.45, 0.675],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  test_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  batmans_text_test = new visual.TextStim({
    win: psychoJS.window,
    name: 'batmans_text_test',
    text: 'Batmans',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.35), (- 0.35)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  robins_text_test = new visual.TextStim({
    win: psychoJS.window,
    name: 'robins_text_test',
    text: 'Robins',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.35, (- 0.35)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "fix1000"
  fix1000Clock = new util.Clock();
  ITIstim = new visual.ShapeStim ({
    win: psychoJS.window, name: 'ITIstim', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "debrief_thankyou"
  debrief_thankyouClock = new util.Clock();
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: 'Add defbrief/thank you\n\nPress Space to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  end_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function Welcome_Initializing_ScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome_Initializing_Screen'-------
    t = 0;
    Welcome_Initializing_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    welcome_key.keys = undefined;
    welcome_key.rt = undefined;
    _welcome_key_allKeys = [];
    // keep track of which components have finished
    Welcome_Initializing_ScreenComponents = [];
    Welcome_Initializing_ScreenComponents.push(welcome_text);
    Welcome_Initializing_ScreenComponents.push(welcome_key);
    
    Welcome_Initializing_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Welcome_Initializing_ScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome_Initializing_Screen'-------
    // get current time
    t = Welcome_Initializing_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text* updates
    if (t >= 0.0 && welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text.tStart = t;  // (not accounting for frame time here)
      welcome_text.frameNStart = frameN;  // exact frame index
      
      welcome_text.setAutoDraw(true);
    }

    
    // *welcome_key* updates
    if (t >= 1.0 && welcome_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_key.tStart = t;  // (not accounting for frame time here)
      welcome_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_key.clearEvents(); });
    }

    if (welcome_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_key.getKeys({keyList: ['space'], waitRelease: false});
      _welcome_key_allKeys = _welcome_key_allKeys.concat(theseKeys);
      if (_welcome_key_allKeys.length > 0) {
        welcome_key.keys = _welcome_key_allKeys[_welcome_key_allKeys.length - 1].name;  // just the last key pressed
        welcome_key.rt = _welcome_key_allKeys[_welcome_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Welcome_Initializing_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Welcome_Initializing_ScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome_Initializing_Screen'-------
    Welcome_Initializing_ScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('welcome_key.keys', welcome_key.keys);
    if (typeof welcome_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('welcome_key.rt', welcome_key.rt);
        routineTimer.reset();
        }
    
    welcome_key.stop();
    // the Routine "Welcome_Initializing_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function recodeTrainRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'recodeTrain'-------
    t = 0;
    recodeTrainClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    recodeTrainComponents = [];
    
    recodeTrainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function recodeTrainRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'recodeTrain'-------
    // get current time
    t = recodeTrainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    recodeTrainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function recodeTrainRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'recodeTrain'-------
    recodeTrainComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "recodeTrain" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function trials_trainLoopBegin(trials_trainLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_train = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: (filename + "_stimfile_train.csv"),
    seed: undefined, name: 'trials_train'
  });
  psychoJS.experiment.addLoop(trials_train); // add the loop to the experiment
  currentLoop = trials_train;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_train.forEach(function() {
    const snapshot = trials_train.getSnapshot();

    trials_trainLoopScheduler.add(importConditions(snapshot));
    trials_trainLoopScheduler.add(stimTrainRoutineBegin(snapshot));
    trials_trainLoopScheduler.add(stimTrainRoutineEachFrame(snapshot));
    trials_trainLoopScheduler.add(stimTrainRoutineEnd(snapshot));
    trials_trainLoopScheduler.add(feedbackRoutineBegin(snapshot));
    trials_trainLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    trials_trainLoopScheduler.add(feedbackRoutineEnd(snapshot));
    trials_trainLoopScheduler.add(fix1000RoutineBegin(snapshot));
    trials_trainLoopScheduler.add(fix1000RoutineEachFrame(snapshot));
    trials_trainLoopScheduler.add(fix1000RoutineEnd(snapshot));
    trials_trainLoopScheduler.add(endLoopIteration(trials_trainLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}

function trials_trainLoopEnd() {
  psychoJS.experiment.removeLoop(trials_train);

  return Scheduler.Event.NEXT;
}

function trials_testLoopBegin(trials_testLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_test = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: (filename + "_stimfile_test.csv"),
    seed: undefined, name: 'trials_test'
  });
  psychoJS.experiment.addLoop(trials_test); // add the loop to the experiment
  currentLoop = trials_test;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_test.forEach(function() {
    const snapshot = trials_test.getSnapshot();

    trials_testLoopScheduler.add(importConditions(snapshot));
    trials_testLoopScheduler.add(stimTestRoutineBegin(snapshot));
    trials_testLoopScheduler.add(stimTestRoutineEachFrame(snapshot));
    trials_testLoopScheduler.add(stimTestRoutineEnd(snapshot));
    trials_testLoopScheduler.add(fix1000RoutineBegin(snapshot));
    trials_testLoopScheduler.add(fix1000RoutineEachFrame(snapshot));
    trials_testLoopScheduler.add(fix1000RoutineEnd(snapshot));
    trials_testLoopScheduler.add(endLoopIteration(trials_testLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}

function trials_testLoopEnd() {
  psychoJS.experiment.removeLoop(trials_test);

  return Scheduler.Event.NEXT;
}

function stimTrainRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stimTrain'-------
    t = 0;
    stimTrainClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    train_stim = (("/Volumes/shares/Cabi/stimuli/cartoon_animals/Set1/" + stim_id.replace("'", "").toString()) + ".jpg");
    
    train_image.setImage(train_stim);
    train_key.keys = undefined;
    train_key.rt = undefined;
    _train_key_allKeys = [];
    batmans_text.setText('Batmans');
    robins_text.setText('Robins');
    // keep track of which components have finished
    stimTrainComponents = [];
    stimTrainComponents.push(train_image);
    stimTrainComponents.push(train_key);
    stimTrainComponents.push(batmans_text);
    stimTrainComponents.push(robins_text);
    
    stimTrainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function stimTrainRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stimTrain'-------
    // get current time
    t = stimTrainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *train_image* updates
    if (t >= 0.0 && train_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train_image.tStart = t;  // (not accounting for frame time here)
      train_image.frameNStart = frameN;  // exact frame index
      
      train_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train_image.setAutoDraw(false);
    }
    
    // *train_key* updates
    if (t >= 1.0 && train_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train_key.tStart = t;  // (not accounting for frame time here)
      train_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { train_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { train_key.start(); }); // start on screen flip
    }

    frameRemains = 1.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train_key.status = PsychoJS.Status.FINISHED;
  }

    if (train_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = train_key.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _train_key_allKeys = _train_key_allKeys.concat(theseKeys);
      if (_train_key_allKeys.length > 0) {
        train_key.keys = _train_key_allKeys[_train_key_allKeys.length - 1].name;  // just the last key pressed
        train_key.rt = _train_key_allKeys[_train_key_allKeys.length - 1].rt;
        // was this correct?
        if (train_key.keys == correct_key) {
            train_key.corr = 1;
        } else {
            train_key.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *batmans_text* updates
    if (t >= 1.0 && batmans_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      batmans_text.tStart = t;  // (not accounting for frame time here)
      batmans_text.frameNStart = frameN;  // exact frame index
      
      batmans_text.setAutoDraw(true);
    }

    frameRemains = 1.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (batmans_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      batmans_text.setAutoDraw(false);
    }
    
    // *robins_text* updates
    if (t >= 1.0 && robins_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      robins_text.tStart = t;  // (not accounting for frame time here)
      robins_text.frameNStart = frameN;  // exact frame index
      
      robins_text.setAutoDraw(true);
    }

    frameRemains = 1.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (robins_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      robins_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stimTrainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function stimTrainRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stimTrain'-------
    stimTrainComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (train_key.keys === undefined) {
      if (['None','none',undefined].includes(correct_key)) {
         train_key.corr = 1;  // correct non-response
      } else {
         train_key.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('train_key.keys', train_key.keys);
    psychoJS.experiment.addData('train_key.corr', train_key.corr);
    if (typeof train_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('train_key.rt', train_key.rt);
        routineTimer.reset();
        }
    
    train_key.stop();
    return Scheduler.Event.NEXT;
  };
}

function feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    if ((! train_key.keys)) {
        feedback = "Oops...you failed to respond within the alloted time";
    } else {
        if (train_key.corr) {
            feedback = `Correct. It was ${category.upper()}`;
        } else {
            feedback = `Incorrect. It was ${category.upper()}`;
        }
    }
    
    feedback_text.setText(feedback);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedback_text);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text* updates
    if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback'-------
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}

function fix1000RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fix1000'-------
    t = 0;
    fix1000Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fix1000Components = [];
    fix1000Components.push(ITIstim);
    
    fix1000Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function fix1000RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fix1000'-------
    // get current time
    t = fix1000Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ITIstim* updates
    if (t >= 0.0 && ITIstim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ITIstim.tStart = t;  // (not accounting for frame time here)
      ITIstim.frameNStart = frameN;  // exact frame index
      
      ITIstim.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ITIstim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ITIstim.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fix1000Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function fix1000RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fix1000'-------
    fix1000Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}

function recodeTestRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'recodeTest'-------
    t = 0;
    recodeTestClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sf.stim_build("/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/test_stim1.csv", random_proto);
    os.rename("/Volumes/shares/Cabi/exp/joplin/joplin1/data/_stimfile.csv", (filename + "_stimfile_test.csv"));
    
    // keep track of which components have finished
    recodeTestComponents = [];
    
    recodeTestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function recodeTestRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'recodeTest'-------
    // get current time
    t = recodeTestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    recodeTestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function recodeTestRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'recodeTest'-------
    recodeTestComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "recodeTest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function stimTestRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stimTest'-------
    t = 0;
    stimTestClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    stim_test = (("/Volumes/shares/Cabi/stimuli/cartoon_animals/Set1/" + stim_id.replace("'", "").toString()) + ".jpg");
    
    test_image.setImage(stim_test);
    test_key.keys = undefined;
    test_key.rt = undefined;
    _test_key_allKeys = [];
    // keep track of which components have finished
    stimTestComponents = [];
    stimTestComponents.push(test_image);
    stimTestComponents.push(test_key);
    stimTestComponents.push(batmans_text_test);
    stimTestComponents.push(robins_text_test);
    
    stimTestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function stimTestRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stimTest'-------
    // get current time
    t = stimTestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *test_image* updates
    if (t >= 0.0 && test_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test_image.tStart = t;  // (not accounting for frame time here)
      test_image.frameNStart = frameN;  // exact frame index
      
      test_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test_image.setAutoDraw(false);
    }
    
    // *test_key* updates
    if (t >= 1.0 && test_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test_key.tStart = t;  // (not accounting for frame time here)
      test_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { test_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { test_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { test_key.clearEvents(); });
    }

    frameRemains = 1.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test_key.status = PsychoJS.Status.FINISHED;
  }

    if (test_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = test_key.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _test_key_allKeys = _test_key_allKeys.concat(theseKeys);
      if (_test_key_allKeys.length > 0) {
        test_key.keys = _test_key_allKeys[_test_key_allKeys.length - 1].name;  // just the last key pressed
        test_key.rt = _test_key_allKeys[_test_key_allKeys.length - 1].rt;
        // was this correct?
        if (test_key.keys == correct_key) {
            test_key.corr = 1;
        } else {
            test_key.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *batmans_text_test* updates
    if (t >= 1.0 && batmans_text_test.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      batmans_text_test.tStart = t;  // (not accounting for frame time here)
      batmans_text_test.frameNStart = frameN;  // exact frame index
      
      batmans_text_test.setAutoDraw(true);
    }

    frameRemains = 1.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (batmans_text_test.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      batmans_text_test.setAutoDraw(false);
    }
    
    // *robins_text_test* updates
    if (t >= 1.0 && robins_text_test.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      robins_text_test.tStart = t;  // (not accounting for frame time here)
      robins_text_test.frameNStart = frameN;  // exact frame index
      
      robins_text_test.setAutoDraw(true);
    }

    frameRemains = 1.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (robins_text_test.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      robins_text_test.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stimTestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function stimTestRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stimTest'-------
    stimTestComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (test_key.keys === undefined) {
      if (['None','none',undefined].includes(correct_key)) {
         test_key.corr = 1;  // correct non-response
      } else {
         test_key.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('test_key.keys', test_key.keys);
    psychoJS.experiment.addData('test_key.corr', test_key.corr);
    if (typeof test_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('test_key.rt', test_key.rt);
        routineTimer.reset();
        }
    
    test_key.stop();
    return Scheduler.Event.NEXT;
  };
}

function debrief_thankyouRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'debrief_thankyou'-------
    t = 0;
    debrief_thankyouClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    end_key.keys = undefined;
    end_key.rt = undefined;
    _end_key_allKeys = [];
    // keep track of which components have finished
    debrief_thankyouComponents = [];
    debrief_thankyouComponents.push(end_text);
    debrief_thankyouComponents.push(end_key);
    
    debrief_thankyouComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function debrief_thankyouRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'debrief_thankyou'-------
    // get current time
    t = debrief_thankyouClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_text* updates
    if (t >= 0.0 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
    }

    
    // *end_key* updates
    if (t >= 1.0 && end_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_key.tStart = t;  // (not accounting for frame time here)
      end_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_key.clearEvents(); });
    }

    if (end_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_key.getKeys({keyList: ['space'], waitRelease: false});
      _end_key_allKeys = _end_key_allKeys.concat(theseKeys);
      if (_end_key_allKeys.length > 0) {
        end_key.keys = _end_key_allKeys[_end_key_allKeys.length - 1].name;  // just the last key pressed
        end_key.rt = _end_key_allKeys[_end_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    debrief_thankyouComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function debrief_thankyouRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'debrief_thankyou'-------
    debrief_thankyouComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end_key.keys', end_key.keys);
    if (typeof end_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_key.rt', end_key.rt);
        routineTimer.reset();
        }
    
    end_key.stop();
    // the Routine "debrief_thankyou" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  os.remove((filename + "_stimfile_train.csv"));
  os.remove((filename + "_stimfile_test.csv"));
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
