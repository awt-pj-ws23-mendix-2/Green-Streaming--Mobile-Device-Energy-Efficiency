# Green-Streaming--Mobile-Device-Energy-Efficiency

## Installation
### Pre-requisite
During the test following versions were used 

* Python version(pip3) : 3.12 [official documentation](https://www.python.org/downloads/)
* ffmpeg : 6.0  [official documentation](https://www.ffmpeg.org/download.html)



Make sure python is installed and correctly configured on the mac OS. Take a look at the [official python documentation](https://www.python.org/downloads/macos/), to make sure paths are correctly configured.

To install all the required imports , execute this in the terminal (Use another pip command if another python verison is installed)
```
pip3 install -r Requirements.txt
```

### Configure settings

* In `/src/configuration.config.template` for sudo_password add your Mac user sudo password

* The **output_path** is the path, where raw data/metadata will be stored.

* The **csv_output_path** is the path, where generated csv files by extractor class will be saved.


# Software working design

![Untitled Diagram drawio](https://github.com/awt-pj-ws23-mendix-2/Green-Streaming--Mobile-Device-Energy-Efficiency/assets/74930393/c4023896-8be3-4e0c-a206-42a9614029fb)

   Python served as the primary programming language for our implementation, offering versatility and compatibility with various libraries and platforms. Integration of components was achieved using associated Python libraries. OpenCV played a vital role in gathering video frame data such as frames per second (fps) and brightness, facilitating essential information for analysis. Ffplay was employed for local video streaming, circumventing potential compatibility issues with other integrated players or browsers on macOS. Powermetrics provided crucial energy consumption metrics in real-time, allowing for monitoring and analysis during video playback and processing.
    
   Multiprocessing played a pivotal role in our implementation, facilitating parallel task execution to boost system performance and efficiency. This was especially advantageous for concurrently running multiple processes, ensuring that the power results remained unaffected by external tasks running on the system. In summary, our carefully designed system architecture, powered by Python and its related libraries, was thoughtfully engineered and rigorously tested to guarantee resilience and functionality. This framework served as the cornerstone for our sustainable streaming experimentation and analysis.


## Project description:

As digital technologies continue to evolve and permeate every aspect of modern life, there is a growing awareness of the environmental impact associated with digital activities, including streaming. This study investigates the energy efficiency of different playback settings during streaming on laptops, with a focus on promoting sustainable streaming practices. Utilizing a system architecture comprised of OpenCV, FFmpeg, FFplayer, multiprocessing, and power metrics monitoring on the macOS M1/M2 platform, we examine the energy consumption associated with various playback configurations. Through data collection and analysis, we explore the impact of factors such as resolution, fps, screen brightness, and codec on energy usage during streaming. Our findings reveal insights into optimal settings that balance energy efficiency with user experience, paving the way for recommendations to optimize streaming settings for sustainability.






## Project structure:
* `./main.py` : The main file for running the application.For IDE, one can execute the file by clicking on the run button in the gutter.
  * in main.py  three variables are configurable,
    * `local_execution` : boolean (change the variable to "True", to execute the files from `./testfolder`).
    * `number_of_files`: Number (represents how many files from the testfolder or online video links should be player).
    * `repeat_per_file`: Number (represents how many times a single video should be played)
* `./video_links.txt` : all the video links to be streamed or player over the internet can be saved there. (Make sure to change the `local_execution` variable in main.py)
* `./src` : contains all the main classes used in the project
* `./src/configuration.config` : contains all the configuration related information for running commands on terminal. It also configures where the data is stored after processing.
* `./src/configuration.config.template` : It is a template for configuration.config file in case it is lost.
* `./src/csv_storage`: contains the processed metadata in .CSV format.
* `./src/temp_data`: contains the metadata for different processes like powermetrics, brightness, fps, resolution etc.
* `./src/graph`: the graphs created will be saved directly in the graph folder.

### For local video execution:

To play videos which are stored on the device locally without the influence of internet,
create a folder named **testfolder** in the root folder and add all the videos to generate the videos content. In test folder 
it can be present in different folder or directly in testfolder itself. The application is able to extract all **.mp4** videos from testfolder by itself.

* change the varibale `local_execution` to True.

### For online video streaming:

To play videos over the internet, save all the links in the file `./video_links.txt` make sure each link
is saved in new line. 

* change the varibale `local_execution` to False.


