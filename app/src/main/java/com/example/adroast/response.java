package com.example.adroast;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.db.chart.animation.Animation;
import com.db.chart.model.Bar;
import com.db.chart.model.BarSet;
import com.db.chart.view.BarChartView;
import com.db.chart.animation.Animation;
import com.db.chart.view.ChartView;

public class response extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_response);

        BarChartView chart=(BarChartView)findViewById(R.id.barChart);

        BarSet dataSet=new BarSet();
        dataSet.addBar(new Bar("first", 5));  //or whatever data you have
        dataSet.addBar(new Bar("second",7));
        dataSet.addBar(new Bar("third", 4));
        dataSet.addBar(new Bar("forth", 3));
        chart.addData(dataSet);

        Animation anim = new Animation(6000);
        anim.fromAlpha(4).fromColor(4);//.setEasing(new LinearEase());     //choose your animation here
        chart.show(anim);

        Button cont = (Button) findViewById(R.id.button7);
        cont.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(response.this, profile.class);
                startActivity(intent);
            }
        });
    }
}
