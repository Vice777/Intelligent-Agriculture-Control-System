import { Component } from "react";
import SMS from "../img/sms.png";
import Help from "../img/help-desk.png";
import Call from "../img/phone-call.png";

class HelpCard extends Component {
  render() {
    return (
      <section className="">
        {/* <div className="grid place-items-center mt-14 ">
          <p className="text-3xl font-bold text-center text-gray-900 uppercase mb-2">
            
          </p>
          <p className="text-xl font-medium text-center text-gray-500 ">
            
          </p>
        </div>
        <div className="grid place-items-center mt-14 mb-20">
          <div className="flex space-x-20">
            <div className="flex flex-row m-2">
             
              <div className="flex flex-column flex-wrap w-40">
                <p className=""> </p>
                <p className="text-green-600"></p>
              </div>
            </div>
            <div className="flex flex-row m-2">
             
              <div className="flex flex-column flex-wrap w-40">
                <p className=""> </p>
                <p
                  className="text-green-600 cursor-pointer"
                  onClick={() => {
                    window.location.href = "/sms";
                  }}
                >
                  
                </p>
              </div>
            </div>
            <div className="flex flex-row m-2">
              
              <div className="flex flex-column flex-wrap w-40">
                <p className=""></p>
                <p
                  className="text-green-600 cursor-pointer"
                  onClick={() => {
                    window.location.href = "/voice";
                  }}
                >
                  
                </p>
              </div>
            </div>
          </div>
        </div> */}
      </section>
    );
  }
}

export default HelpCard;
