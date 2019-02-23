package RESTCalls;

import android.os.AsyncTask;
import android.util.Log;

import java.io.InputStream;

public class postImg {
    public String post(final String image) {
        /*AsyncTask<String, String, String> postImgTask =
                new AsyncTask<String, String, String>() {
                    String exceptionMessage = "";
                    @Override
                    protected String doInBackground(String... params) {
                        //return "";
                        String result = "";
                        try {
                            HttpClient httpclient = new DefaultHttpClient();
                            HttpPost httpPost = new HttpPost("http://104.248.237.28:1313/analysisPOST/");
                            String json = "";

                            Gson gsonObject = new Gson();
                            JsonObject jsonObject = new JsonObject();
                            Gson gson = new Gson();
                            JsonElement je = gson.toJsonTree(params[0]);
                            jsonObject.add("Image", je);
                            json = jsonObject.toString();
                            Log.d("json",json);
                            StringEntity se = new StringEntity(json);

                            httpPost.setEntity(se);
                            httpPost.setHeader("Accept", "application/json");
                            httpPost.setHeader("Content-type", "application/json");

                            HttpResponse httpResponse = httpclient.execute(httpPost);

                            InputStream inputStream = httpResponse.getEntity().getContent();
                            if(inputStream != null)
                                result = inputStream.toString();
                            else
                                result = "Did not work!";

                        } catch (Exception e) {
                            Log.d("InputStream", e.getLocalizedMessage());
                        }

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
                    }
                };
        postImgTask.execute(image);
        while (postImgTask.getStatus()!= AsyncTask.Status.FINISHED){
        }
        try {
            return postImgTask.get();
        }
        catch (Exception e){
            Log.d("Error in return get",e.toString());
        }
        return null;*/
        return null;
    }
}
