
# Week 2 - Tuesday

## Linux and its Command Line Interface (CLI)
From here on this will be an interactive session, meaning I will go through the topics and execute commands as we go along. At any point you can ask questions or make me try stuff, I'll be your puppet (There will be boundaries though ;-).

### Linux

* Inspired by UNIX
* Linus Torvalds (Douchebag/Git to some, but amazing programmer)
* Open source, free
* File based
* Separates kernel from user interface
* Linux is EVERYWHERE
* Linux is AWESOME


### The Shell

Let's go in and see!

* prompt
* custamizable
* primitive yet very powerful

### The File System

Hierarchical. Root, parents and children. Home directory, relative and absolute paths.

### Users and Permissions

Because UNIX was designed as a multiuser opterating system, it has a notion of users. Each user can have different access levels. There is one so called *root user* which is all powerful! And with great power comes great responsibility.

### Permissions
There are three types of permissions on a file or directory

1. Read
2. Write
3. Execute

There are also three levels of permissions for a file or directory (User, Group, Other). Use chmod to alter permissions. Use chown to change ownership.

### Executing Programs

    /usr/bin
    
Local programs, fg, pid

    #!/usr/bin/env bash
    
    sleep 60

### The Linux Manual

    man chmod
    man chown
    man ls

### Copying, Moving and Removing Files

    cp
    mv
    rm
    ls

### Creating Directories and Files

    mkdir
    rmdir
    touch

### Listing and Killing Processes

    top
    ps
    kill

### Dealing with Textfiles

    cat
    head
    tail
    grep
    wc

What is a byte? kilobyte, kibibyte?

### Glob Patterns

This is where the magic happens...

    * ? [ABC] [0-9] \

### Searching Files

    find
    exec
    find /path/to/directory -name "needle.txt" -exec grep -li "gold" {} \;

### gzip and tar

packing and then packing some more

### Environment Variables

BASH settings

    env
    echo $PATH
    .bashrc
    .bash_profile

### Pipes and Redirects

Controlling the flow

## Assignment
Goto the website and look at week2. You will now have the tools and knowledge to successfully perform the first assignment. Good luck & Have fun!
