import React from "react";

const Data = ({ data }) => {
  return (
    <>
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          backgroundColor: "white",
          color: "green",
          font: "15px Arial, sans-serif",
          padding: "20px",
          marginTop: "40px",
          flexDirection: "column"
        }}
      >
        <div>
          <h2
            style={{
              lineHeight: "80%",
              fontWeight: "bold",
              margin: "0.3in",
              fontSize: "20px"
            }}
          >
            Soil Color:{data.soil_color}
          </h2>
        </div>
        <div>
          <h2
            style={{
              lineHeight: "80%",
              fontWeight: "bold",
              margin: "0.3in",
              fontSize: "20px"
            }}
          >
            pH Value: {data.pH_value}
          </h2>
        </div>
        <div>
          <h2
            style={{
              lineHeight: "80%",
              fontWeight: "bold",
              margin: "0.3in",
              fontSize: "20px"
            }}
          >
            Soil Type: {data.soil_type}
          </h2>
        </div>
        <div>
          <h2
            style={{
              lineHeight: "80%",
              fontWeight: "bold",
              margin: "0.3in",
              fontSize: "20px"
            }}
          >
            Soil Quality: {data.soil_quality}
          </h2>
        </div>
      </div>
    </>
  );
};

export default Data;