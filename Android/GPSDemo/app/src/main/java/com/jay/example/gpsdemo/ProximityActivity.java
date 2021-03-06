package com.jay.example.gpsdemo;

import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;

/**
 * Created by Jay on 2015/11/21 0021.
 */
public class ProximityActivity extends AppCompatActivity {

    private LocationManager lm;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_proximity);
        lm = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        //定义固定点的经纬度
        double longitude = 113.56843;
        double latitude = 22.374937;
        float radius = 10;     //定义半径，米
        Intent intent = new Intent(this, ProximityReceiver.class);
        PendingIntent pi = PendingIntent.getBroadcast(this, -1, intent, 0);
        lm.addProximityAlert(latitude, longitude, radius, -1, pi);
    }
}
