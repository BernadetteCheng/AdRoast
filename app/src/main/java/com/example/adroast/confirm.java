package com.example.adroast;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.io.ByteArrayOutputStream;
import java.io.InputStream;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class confirm extends AppCompatActivity {

    String r;
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
                RESTCalls.postImg rc = new RESTCalls.postImg();
                r=post(b64img);
                Log.d("ans",r);
                Intent intent = new Intent(confirm.this, response.class);
                intent.putExtra("Response",r);
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
    public String post(final String image) {
        AsyncTask<String, String, String> postImgTask =
                new AsyncTask<String, String, String>() {
                    String exceptionMessage = "";
                    @Override
                    protected String doInBackground(String... params) {
                        //return "";
                        String result = "empty";
                        OkHttpClient client = new OkHttpClient();
                        MediaType MEDIA_TYPE_MARKDOWN
                                = MediaType.parse("text/x-markdown; charset=utf-8");
                        Request request = new Request.Builder()
                                .url("http://104.248.237.28:1313/analysisPOST/")
                                .header("Authorization","oko")
                                .post(RequestBody.create(MEDIA_TYPE_MARKDOWN, params[0]))
                                .build();
                        try {
                            Response response = client.newCall(request).execute();
                            Log.d("here fuck","ok");
                            result = response.body().string();
                        } catch (Exception e) {
                            Log.d("InputStream", e.toString());
                        }
                        Log.d("result",result);
                        return result;
                    }

                    @Override
                    protected void onPreExecute() {
                    }
                    @Override
                    protected void onProgressUpdate(String... progress) {
                        Log.d("progress",progress[0]);
                    }
                    @Override
                    protected void onPostExecute(String result) {
                        Log.d("Detect","done");
                        if(!exceptionMessage.equals("")){
                            Log.d("Error in post detect",exceptionMessage);
                        }
                        if (result == null) return;
                        give(result);
                    }
                };
        postImgTask.execute(image);
        try {
            return postImgTask.get();
        }
        catch (Exception e){
            Log.d("Error in return get",e.toString());
        }
        return null;
    }
    public void give(String ra){
        this.r=ra;
    }
}
