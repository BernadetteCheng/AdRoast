package com.example.adroast;

import android.content.Intent;
import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.github.mikephil.charting.charts.BarChart;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.components.YAxis;
import com.github.mikephil.charting.data.BarData;
import com.github.mikephil.charting.data.BarDataSet;
import com.github.mikephil.charting.data.BarEntry;
import com.github.mikephil.charting.components.AxisBase;

import java.util.ArrayList;
import java.util.List;

public class response extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_response);

        BarChart chart=(BarChart)findViewById(R.id.barChart);

        List<BarEntry> entries = new ArrayList<BarEntry>();
        entries.add(new BarEntry(1,4));
        entries.add(new BarEntry(2,20));
        BarDataSet dataSet = new BarDataSet(entries, "Label");
        dataSet.setColor(1,700);
        dataSet.setValueTextColor(Color.BLUE);
        BarData barData = new BarData(dataSet);
        chart.setData(barData);
        chart.setDrawGridBackground(false);
        chart.setGridBackgroundColor(Color.WHITE);
        XAxis xAxis = chart.getXAxis();
        xAxis.setPosition(XAxis.XAxisPosition.BOTTOM);
        xAxis.setTextSize(10f);
        xAxis.setTextColor(Color.WHITE);
        xAxis.setDrawAxisLine(true);
        xAxis.setDrawGridLines(false);
        YAxis left = chart.getAxisLeft();
        
        left.setDrawLabels(false);
        left.setDrawAxisLine(false);
        left.setDrawGridLines(false);
        left.setDrawZeroLine(true);
        chart.getAxisRight().setEnabled(false);
        left.setTextColor(Color.WHITE);
        chart.invalidate();

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
