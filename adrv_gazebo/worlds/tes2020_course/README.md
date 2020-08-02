# TES2020_couse

Auto drive RC course in TOYOTA TES Festival 2020 by Gazebo.

-----------------------------------------------------------

## Installation
-----------------------------------------------------------

- ### Environment

  - Ubuntu 18.04
  - ROS (Melodic)
  - Gazebo 9 (version 9.0.0)

- ### Usage

  1. Gazebo Install

    ```bash
    $ sudo apt update
    $ sudo apt install gazebo9
    ```

  2. Gazebo Model Folder Create

    ```bash
    $ cd ~/.gazebo
    $ mkdir models
    ```

  3. Clone Repository

  ```bash
  $ cd ~/.gazebo/models
  $ git clone https://github.com/DaiGuard/TES2020_course.git
  ```

  4. Check Gazebo Model List

    ```bash
    $ gazebo9
    ```

    Gazebo model list

    ![gazebo_list](https://user-images.githubusercontent.com/26181834/87240695-d0f26700-c456-11ea-988b-7f4e6e965fd0.png)

    Gazebo model view
    
    ![gazebo_view](https://user-images.githubusercontent.com/26181834/87240697-d51e8480-c456-11ea-8fbe-393a2446ede6.png)
