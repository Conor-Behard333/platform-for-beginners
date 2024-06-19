- install wsl (ubuntu)/setup wsl user

- explain basics of Ubuntu (sudo)
    - The concept that "everything is a file" is a fundamental principle in Linux operating systems. This means that various system components, including hardware devices, processes, and inter-process communication mechanisms, are represented as files or file-like objects
        - Regular files (document.txt, image.jpg, etc.)
        - directories (/home/username, etc.)
        - device files (Represent devices that handle data one character at a time)
        - process files (Running processes are represented by files in the /proc directory. Each process has a directory with its process ID (PID) as its name, containing information about the process)

    - sudo (This command allows you to run commands with superuser (admin) privileges.)
    - apt packages (This is the package handling utility)
    - cd (how to move around)
    - ls
    - touch
    - vim
    - rm 
    - cp
    - mv
    - Home Directory:
        - Each user has a home directory (/home/username), where you have full permissions to create and modify files.
    - Root Directory:
        - The root directory (/) is the top level of the filesystem hierarchy.

- useful linux cheat sheet https://www.guru99.com/linux-commands-cheat-sheet.html

- install needed dependencies via the apt repository: 
    - python (hint: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
    
- make a basic web server in python (hint: https://reintech.io/blog/how-to-create-a-simple-web-server-with-python)

- add more advanced features to web server code (index.html, different routes)
    - https://medium.com/@andrewklatzke/creating-a-python3-webserver-from-the-ground-up-4ff8933ecb96

- containerise web-server
    - why containerise? (solves "but it works on my computer" problem, ensures it's repeatable, more portable, etc.) (https://medium.com/@stefan.paladuta17/introduction-to-containerization-a-beginners-walkthrough-f5dc2508e16f)
EXTRA:
    - try and containerise the web server (use https://medium.com/@kalyanasundaramthivaharan/docker-for-dummies-a-beginners-guide-to-containerization-d02082d593df for help)
    
- move code into a git repository:
    - install git in wsl (hint: https://github.com/git-guides/install-git)
    - create github account (use personal email if that is ok)
    - create repository (repo) called web-server
    - git clone the web-server from wsl (hint: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    - add the files in wsl
    - git commit/push to the github repo

- deploy container via k3s
    - install k3s
    - deploy web-server via k3s
