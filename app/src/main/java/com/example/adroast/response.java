package com.example.adroast;

import android.content.Intent;
import android.graphics.Color;
import android.graphics.Typeface;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.github.mikephil.charting.animation.Easing;
import com.github.mikephil.charting.charts.BarChart;
import com.github.mikephil.charting.components.Legend;
import com.github.mikephil.charting.components.LegendEntry;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.components.YAxis;
import com.github.mikephil.charting.data.BarData;
import com.github.mikephil.charting.data.BarDataSet;
import com.github.mikephil.charting.data.BarEntry;
import com.github.mikephil.charting.components.AxisBase;
import com.github.mikephil.charting.formatter.IAxisValueFormatter;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.util.ArrayList;
import java.util.List;

public class response extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_response);

        BarChart chart=(BarChart)findViewById(R.id.barChart);
        TextView x=(TextView) findViewById(R.id.xTitle);
        TextView y=(TextView) findViewById(R.id.yTitle);
        TextView title=(TextView) findViewById(R.id.title);
        TextView eval =(TextView) findViewById(R.id.eval);

        JsonParser parser = new JsonParser();
        JsonObject o = parser.parse(getIntent().getStringExtra("Response")).getAsJsonObject();
        String s = o.getAsJsonObject("improvements").toString();
        Log.d("string",s);
        s=s.substring(s.indexOf("[") + 1);
        s=s.substring(0,s.indexOf("]"));
        Log.d("string",s);
        String[] sa = s.split(",");
        eval.setText("Your advertisement received a grade of: "+o.get("grade")+"\nAnalysis: "+sa[2]);
        eval.setTypeface(null, Typeface.BOLD);
        x.setText("Propery Comparison");
        y.setText("Score");
        title.setText("Comparison of Current and Recommended Score");
        List<BarEntry> entries = new ArrayList<BarEntry>();
        entries.add(new BarEntry(0,Integer.parseInt(sa[1])));
        entries.add(new BarEntry(1,Integer.parseInt(sa[0])));
        BarDataSet dataSet = new BarDataSet(entries, "Comparison");
        dataSet.setColors(new int[] {Color.GRAY, Color.RED});
        dataSet.setValueTextColor(Color.BLACK);
        dataSet.setValueTextSize(10f);
        BarData barData = new BarData(dataSet);
        barData.setBarWidth(0.9f);
        chart.setData(barData);

        XAxis xAxis = chart.getXAxis();
        xAxis.setPosition(XAxis.XAxisPosition.BOTTOM);
        xAxis.setTextSize(10f);
        xAxis.setTextColor(Color.BLACK);
        xAxis.setDrawAxisLine(true);
        xAxis.setDrawGridLines(false);
        xAxis.setLabelCount(2);
        final ArrayList<String> xLabel = new ArrayList<>();
        xLabel.add("Current");
        xLabel.add("Potential");
        xAxis.setValueFormatter(new IAxisValueFormatter() {
            @Override
            public String getFormattedValue(float value, AxisBase axis) {
                return xLabel.get((int)value);
            }
        });


        YAxis left = chart.getAxisLeft();
        left.setTextSize(10f);
        left.setTextColor(Color.BLACK);
        left.setDrawLabels(false);
        left.setDrawAxisLine(true);
        left.setDrawGridLines(false);
        left.setDrawZeroLine(true);
        chart.getAxisRight().setEnabled(false);

        chart.animateXY(2000,2000);
        chart.setBackgroundColor(Color.WHITE);
        //chart.setDrawBarShadow(true);
        chart.setFitBars(true);
        chart.getDescription().setEnabled(false);
        chart.getLegend().setEnabled(false);
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
