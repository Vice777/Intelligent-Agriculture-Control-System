import { Component } from "react";
import output from "../img/output.png";
import analysis from "../img/analysis.png";
import upload from "../img/upload.png";

class CardBar extends Component {
  render() {
    return (
      <section className="body__section py-10">
        <div className="bg-[#219653] inPhone py-20">
        <div className="grid place-items-center mt-5">
          <p className="text-3xl font-bold text-center text-gray-900 uppercase mb-2">
            HOW Sakha HELPS
          </p>
          <p className="text-xl font-medium text-center text-gray-500 ">

          </p>
        </div>
        <div className="grid place-items-center mt-14 mb-20">
          <div className="inline-flex space-x-36 items-center justify-end">
            <div className="w-1/4 h-full">
              <div className="inline-flex flex-col space-y-6 items-center justify-end flex-1 h-full pl-9 pr-8 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
                <img className="w-1/5 h-12 rounded-lg" src={upload} alt="help" />
                <p className="w-56 h-7 text-lg font-semibold text-gray-900 text-center">
                  Step:1
                </p>
                <p className="opacity-70 w-56 h-1/5 text-base text-center">
                  Upload your images
                </p>
              </div>
            </div>
            <div className="w-1/4 h-full">
              <div className="inline-flex flex-col space-y-6 items-center justify-end flex-1 h-full pl-9 pr-8 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
                <img className="w-14 h-14 rounded-lg" src={analysis} alt="SMS" />
                <p className="w-56 h-7 text-lg font-semibold text-gray-900 text-center">
                  Step:2
                </p>
                <p className="opacity-70 w-56 h-1/5 text-base text-center">
                  Wait for analysis
                </p>
              </div>
            </div>
            <div className="w-1/4 h-full">
              <div className="inline-flex flex-col space-y-6 items-center justify-end flex-1 h-full pl-9 pr-8 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
                <img
                  src={output}
                  className="w-14 h-14 rounded-lg"
                  alt="voice assistance"
                />
                <p className="w-56 h-7 text-lg font-semibold text-gray-900 text-center">
                  Step:3
                </p>
                <p className="opacity-70 w-56 h-1/5 text-base text-center">
                  Get your result
                </p>
              </div>
            </div>
          </div>
        </div>
        </div>
      </section>
    );
  }
}

export default CardBar;
