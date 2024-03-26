import React from "react";
import "../components/changedetection.css"; 

const ChangeDetection = () => {
    return (
        <div className="App">
            <br></br>
            <h1>Upload Two Images</h1>
            <br></br>
            <form action="/images" method="post" enctype="multipart/form-data">
                <label htmlFor="image1">Upload Old Image :</label>
                <input type="file" id="image1" name="image1" accept="image/*" /><br /><br />

                <label htmlFor="image2">Upload New Image :</label>
                <input type="file" id="image2" name="image2" accept="image/*" /><br /><br />

                <input type="submit" value="Upload" />
            </form>
        </div>
    );
};

export default ChangeDetection;