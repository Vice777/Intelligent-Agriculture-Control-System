import React, { useState , useEffect} from "react";
import PreHeader from "../../components/preheader/preheader";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/footer";
import axios from "axios";
import Data from "../../components/data/data";

const Soil = () => {
  const [photo, setPhoto] = useState([]);
  const [load, setLoad] = useState(false);
  const [prediction, setPrediction] = useState("");
  const [lang, setLang] = useState("en");
  const [soil, setSoil] = useState({});

  const getData = async (e) => {
    e?.preventDefault();
    if(document.getElementById('image').files.length > 0){
      try {
        const data = new FormData();
        data.append('image', document.getElementById('image').files[0]);
        const res = await axios.post("http://localhost:3001/soil", data);
        setSoil(res.data);
      } catch (error) {
        console.log(error.data);
      }
    }else{
      alert("No image uploaded!");
    }
  }  

  return (
    <>
      <PreHeader />
      <Header />
      <section className="">
        <div className="grid place-items-center my-14  ">
          <div className="container bg-gray-100  p-10 grid place-items-center my-14 ">
            <p className="text-2xl font-medium text-green-600 my-12">
              Upload your image to get the Soil Quality
              <br />
            </p>
            <div className="flex flex-row space-x-3 my-10">
              <div></div>
              <div className="ml-16 "></div>
              <div className="ml-16"></div>
              <div className="ml-16 "></div>
            </div>
            <p className="title">Select Image:</p>
            <div className=" m-6">
              <input
                type="file"
                id="image"   
                />
            </div>
            <button
              onClick={(e)=>getData(e)}
              type="button"
              className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
              >
              Get Upload
            </button>
            {soil?.pH_value && <Data data={soil}/> }
            <p className="title" style={{ marginTop: 30 }}>
              Uploaded Image:
            </p>
          </div>
        </div>

        <div>
          {load ? (
            <div className="grid place-items-center my-14  ">loading </div>
          ) : (
            <div></div>
          )}
          {prediction !== "" ? (
            <div className="grid place-items-center my-14 text-center ">
              <p className="font-bold my-3">
                Soil Quality From Image Predicted:{" "}
              </p>
              {prediction}
            </div>
          ) : (
            <div></div>
          )}
        </div>
      </section>
      <Footer />
    </>
  );
};

export default Soil;
