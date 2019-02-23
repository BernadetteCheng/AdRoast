package com.example.adroast;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.io.ByteArrayOutputStream;

public class confirm extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_confirm);

        ImageView imageCont = (ImageView) findViewById(R.id.imageView);
        final byte[] imgByteArray = getIntent().getByteArrayExtra("Image");
        imageCont.setImageBitmap(BitmapFactory.decodeByteArray(imgByteArray,0,imgByteArray.length));

        Button btn = (Button) findViewById(R.id.button5);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
                    startActivityForResult(takePictureIntent, 1);
                }
            }
        });
        Button cont = (Button) findViewById(R.id.button6);
        cont.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String b64img = Base64.encodeToString(imgByteArray, Base64.DEFAULT);
                Intent intent = new Intent(confirm.this, response.class);
                startActivity(intent);
            }
        });
    }
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 1 && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            Bitmap imageBitmap = (Bitmap) extras.get("data");

            ByteArrayOutputStream outStream = new ByteArrayOutputStream();
            imageBitmap.compress(Bitmap.CompressFormat.PNG,100,outStream);
            byte[] imgByteArray = outStream.toByteArray();

            Intent intent = new Intent(confirm.this, confirm.class);
            intent.putExtra("Image",imgByteArray);
            startActivity(intent);
        }
    }
}
