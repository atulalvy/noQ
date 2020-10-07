package com.akul.android.gms.samples.vision.face.facetracker;

import android.app.Application;
import android.speech.tts.TextToSpeech;

import java.util.Locale;

/**
 * Created by noQteam
 */

public class App extends Application {
    public static TextToSpeech ttsObj;

    @Override
    public void onCreate() {
        super.onCreate();
        initializeTTS();
    }

    private void initializeTTS() {
        ttsObj = new TextToSpeech(getApplicationContext(), new TextToSpeech.OnInitListener() {
            @Override
            public void onInit(int status) {
                if (status != TextToSpeech.ERROR) {
                    ttsObj.setLanguage(Locale.UK);
                }
            }
        });
    }
}
