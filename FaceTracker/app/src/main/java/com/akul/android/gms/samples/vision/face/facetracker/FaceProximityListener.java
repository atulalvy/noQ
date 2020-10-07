package com.akul.android.gms.samples.vision.face.facetracker;

import com.google.android.gms.vision.face.Face;

/**
 * Created by noQTeam
 */
public interface FaceProximityListener {
    void onFaceProximityTrigger(Face face);
}
