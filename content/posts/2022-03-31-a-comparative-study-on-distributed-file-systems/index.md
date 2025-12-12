---
title: "A Comparative Study on Distributed File Systems"
date: 2022-03-31T00:00:00-05:00
draft: false
author: "Amey Thakur"
summary: "Special thanks to Mega Satish and Hasan Rizvi for their meaningful contributions, support, and wisdom that helped shape this work. Distributed File Systems form the backbone of large-scale data storage. Systems like the Hadoop File System, Google File System, and Network File System have changed how data is managed across servers."
tags: ["Andrew File System", "Architecture", "Big Data", "Client-Server Model", "Cloud Storage", "Data Engineering", "Distributed File Systems", "Distributed Systems", "Fault Tolerance", "File System Architecture", "File Systems", "GFS", "Google File System", "Hadoop", "Hadoop Distributed File System", "HDFS", "High-Performance Computing", "MapReduce", "NFS", "Network File System", "Scalability", "System Design"]
ShowToc: true
TocOpen: false
---

<style>
/* Make images transparent on light backgrounds */
.post-content img {
    mix-blend-mode: multiply;
}

/* Dark mode: Show original images with transparent backgrounds */
[data-theme="dark"] .post-content img {
    filter: none;
    mix-blend-mode: normal;
    border-radius: 8px;
    opacity: 0.95; /* Slightly reduce glare while maintaining contrast */
}

/* General hover effect for all links in post content */
.post-content a {
    transition: all 0.3s ease;
}
.post-content a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}

/* Dark mode hover effect (same color) */
[data-theme="dark"] .post-content a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}
</style>

<style>
.special-thanks {
    font-size: 0.9rem;
    color: #1a73e8; /* Standard Blue for Light Mode */
    margin-bottom: 1.5rem;
}

.special-thanks a {
    color: #1a73e8;
    text-decoration: underline;
    border: none;
    background-image: none;
    box-shadow: none;
    text-underline-offset: 3px;
    transition: all 0.3s ease;
}

.special-thanks a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676; /* Subtle glow/bolding effect without lift */
}

[data-theme="dark"] .special-thanks {
    color: #64b5f6; /* Lighter Blue for Dark Mode readability */
}

[data-theme="dark"] .special-thanks a {
    color: #64b5f6;
}

[data-theme="dark"] .special-thanks a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}
</style>

<p class="special-thanks">
Special thanks to <a href="https://scholar.google.com/citations?user=7Ajrr6EAAAAJ&hl=en">Mega Satish</a> and <a href="https://scholar.google.com/citations?user=OJuGq08AAAAJ&hl=en">Hasan Rizvi</a> for their meaningful contributions, support, and wisdom that helped shape this work.
</p>

Distributed File Systems form the backbone of large-scale data storage. Systems like the **Hadoop File System**, **Google File System**, and **Network File System** have changed how data is managed across servers. Each of these systems brings its own strengths and limitations when it comes to performance, fault tolerance, consistency, scalability, and availability.

This study compares these file systems and outlines a simple criterion for choosing the right one based on specific needs. It also highlights the key advantages and drawbacks of each system.

## Introduction

A Distributed File System is a client–server model that lets clients access and process data stored across multiple servers as if it were on a local machine. It brings files from different servers together into a single global directory, creating a unified view of the system.

To ensure clients always receive the latest version of the data, the system includes mechanisms to prevent conflicts and manage updates effectively.

When designing such systems, several factors must be considered: transparency, flexibility, reliability, performance, scalability, and security. Key design aspects also include architecture, processes, communication, naming, synchronization, caching and replication, and fault-tolerance techniques.

---

## Literature Survey

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 1: </span>
    Key Research in Distributed File Systems
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center; width: 10%;">Year</th>
            <th style="padding: 12px; text-align: center; width: 30%;">Paper Title</th>
            <th style="padding: 12px; text-align: center; width: 25%;">Authors</th>
            <th style="padding: 12px; text-align: center;">Key Contribution</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; text-align: center; vertical-align: top;">2017</td>
            <td style="padding: 12px; vertical-align: top;">"An Efficient Cache Management Scheme for Accessing Small Files in Distributed File Systems"</td>
            <td style="padding: 12px; vertical-align: top;">Kyuongsoo Bok, Hyunkyo Oh, Jongtae Lim, and Jaesoo Yoo</td>
            <td style="padding: 12px; vertical-align: top;">Introduced a distributed cache management scheme for the Hadoop Distributed File System (HDFS). The approach focuses on storing and caching small files efficiently to improve retrieval performance.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; text-align: center; vertical-align: top;">2019</td>
            <td style="padding: 12px; vertical-align: top;">"An Efficient Ring-Based Metadata Management Policy for Large-Scale Distributed File Systems"</td>
            <td style="padding: 12px; vertical-align: top;">Yuanning Gao, Xiaochun Yang, Jiaxi Liu, and Guihai Chen</td>
            <td style="padding: 12px; vertical-align: top;">Proposed AngleCut, a new hashing-based technique for partitioning metadata namespace trees. The method improves metadata handling in large-scale distributed storage systems by offering better balance and efficiency.</td>
        </tr>
    </tbody>
</table>

</div>

---

## The Library Analogy

How do you manage a library so big it doesn't fit in one building?

### The Analogy: The Inter-Library Loan

*   **Centralized (Your Laptop)**: All books are in one room. Easy to find, but if the room burns down, everything is gone.
*   **Distributed (DFS)**:
    *   **Transparency**: You search the catalog for "Harry Potter". The system tells you it's on Shelf 3. You don't need to know that Shelf 3 is actually in a warehouse in another city. To you, it feels like the book is right next to you.
    *   **Caching (AFS)**: When you borrow the book, you take it home (Local Cache). You read it there. Only when you return it (Close File) does the library update its records. This reduces traffic to the warehouse.
    *   **Direct Access (NFS)**: You read the book at the library counter. Every page turn is a request to the librarian. It's chattier but ensures you have the absolute latest version.

---

## Network File System (NFS)

Network File System (NFS) is a mechanism for storing and accessing files over a network. It is a distributed file system that lets users access files and directories located on remote machines and use them as if they were on a local system. Users can create, remove, read, write, and modify file attributes on remote directories through standard operating system commands, making the interaction seamless.

### Architecture of NFS

The diagram shows the client–server structure of the Network File System (NFS). It highlights how communication flows between the client machine and the server machine over the network.

{{< figure src="A%20Comparative%20Study%20on%20Distributed%20File%20Systems/figures/Architecture%20of%20NFS.png" caption="Architecture of NFS" align="center" >}}

#### Client Side

*   **System Call Layer**: Receives file operation requests from applications (open, read, write).
*   **Virtual File System (VFS) Layer**: Decides whether the request is for the local file system or a remote NFS-mounted directory.
*   **Local File System Interface**: Handles local disk operations when needed.
*   **NFS Client**: Converts VFS calls into NFS operations.
*   **RPC Client Stub**: Sends these NFS requests to the remote server using Remote Procedure Calls.

#### Server Side

*   **System Call Layer**: Handles incoming file-related system calls.
*   **VFS Layer**: Routes operations to the correct file system.
*   **Local File System Interface**: Interacts with the server's local storage.
*   **NFS Server**: Processes NFS requests coming from clients.
*   **RPC Server Stub**: Receives RPC calls and forwards them to the NFS server component.

#### Overall Flow

The client makes a file request → NFS client converts it → RPC sends it → NFS server processes it → response returns via RPC. This makes remote files appear local to the user.

### Features of NFS

{{< figure src="A%20Comparative%20Study%20on%20Distributed%20File%20Systems/figures/Features%20of%20NFS.png" caption="Features of NFS" align="center" >}}

*   Lets multiple machines access the same files, so everyone on the network works with the same data.
*   Cuts down storage costs by allowing systems to share applications instead of installing them locally on every device.
*   Ensures consistency and reliability because all users read from a single, unified file set.
*   Makes mounting file systems seamless, with no extra steps needed from the user.
*   Keeps remote file access completely transparent, so using a remote file feels the same as using a local one.
*   Works smoothly in a heterogeneous environment with different platforms and systems.
*   Lowers system administration work by centralizing file management.

---

## Andrew File System (AFS)

Andrew File System started as part of the larger Andrew project. It was originally called "Vice" and was developed at Carnegie Mellon University. AFS was mainly designed for systems running BSD, UNIX, or the Mach operating system.

Today, AFS development continues through the OpenAFS project. This version is cross-platform and works on Linux, macOS, Sun Solaris, and even Microsoft Windows NT.

### Structure of AFS

The diagram shows how the Andrew File System (AFS) operates using a client–server model. It highlights how file requests move between the client machine and the server machine.

{{< figure src="A%20Comparative%20Study%20on%20Distributed%20File%20Systems/figures/Structure%20of%20AFS.png" caption="Structure of AFS - Venus/Vice Components" align="center" >}}

#### Client Machine

**Application Program**
The user application makes normal file system calls (open, read, write).

**System Call Interception**
Instead of sending these calls directly to the local file system, AFS intercepts them. This allows AFS to decide whether the requested file is local or remote.

**AFS Client ("Venus")**
Venus handles all AFS-related operations on the client side. It does two main things:
*   Communicates with the AFS server using RPC.
*   Manages local caching so frequently accessed files don't require repeated remote requests.

**Local File System**
Acts as the cache storage. Files fetched from the server are stored locally to improve performance.

#### Server Machine

**AFS Server ("Vice")**
Vice stores the actual file data and metadata. When a client requests a file not in its cache, Venus contacts Vice via RPC.

**Local File System (on server)**
Stores the authoritative version of all files and directories managed by AFS.

#### Communication via RPC

*   The client's Venus component sends Remote Procedure Calls to the server's Vice component.
*   Vice returns the requested file or metadata.
*   The client caches the received data in the local file system.

#### Overall Flow

1. Application makes a file request.
2. Venus intercepts the call.
3. If file is cached → serve locally.
4. If not cached → request from Vice via RPC.
5. Vice sends file → client saves it in local cache.
6. Application gets seamless access.

### Vice and Venus Components

{{< figure src="A%20Comparative%20Study%20on%20Distributed%20File%20Systems/figures/AFS%20-%20Vice%20_%20Venus.png" caption="AFS - Vice & Venus Components" align="center" >}}

#### Vice (Server)

*   Provides files to the client, called Venus.
*   Consists of a set of trusted servers collectively called Vice.
*   Runs a dedicated process on the server side.
*   Each Venus client has a dedicated Vice process.

#### Venus (Client)

*   Caches files from Vice locally.
*   Contacts Vice only when a file is opened or closed.
*   All reading and writing is done on the local cached copy.

### Features of AFS

{{< figure src="A%20Comparative%20Study%20on%20Distributed%20File%20Systems/figures/Features%20of%20AFS.png" caption="Features of AFS" align="center" >}}

*   **File Backups**: AFS data files are backed up every night, with backups stored on-site for six months.
*   **File Security**: Data is protected using the Kerberos authentication system.
*   **Physical Security**: Files are stored on servers in the UCSC data center.
*   **Reliability and Availability**: Servers and storage run on redundant hardware to ensure continuous access.
*   **Authentication**: Kerberos handles authentication. Accounts are automatically created for all UCSC students, faculty, and staff, using the CruzID 'blue' password.

---

## Google File System (GFS)

### Architecture of GFS

Google File System is organized into groups containing many storage servers. These servers are built using cost-effective hardware and operate in a cluster-based setup. Files are stored in tree-like structures, and each file has a unique path name to identify it.

{{< figure src="A%20Comparative%20Study%20on%20Distributed%20File%20Systems/figures/Architecture%20of%20GFS.png" caption="Architecture of GFS" align="center" >}}

This diagram shows how the Google File System (GFS) handles files using a master–chunkserver model.

#### 1. Client/Application

*   The application requests a file using a filename and chunk index.
*   The GFS client communicates with the GFS master to locate the required chunk.

#### 2. GFS Master

*   Stores the entire file namespace (directory tree and metadata).
*   Maintains chunk handles, chunk locations, and metadata about each file.
*   Sends control instructions to chunkservers (e.g., replication, lease management).
*   Tracks the state of each chunkserver.

#### 3. GFS Chunkservers

*   Store file data in fixed-size chunks on their local disks.
*   Chunkservers send the actual chunk data directly to the client.
*   They follow the master's instructions for replication and updates.

#### 4. Message Flow

**Control Messages (thin arrows):**
Between client ↔ master and master ↔ chunkservers. These include metadata lookup, chunk locations, and instructions.

**Data Messages (thick arrows):**
Client ↔ chunkservers. These carry the actual file data read or written.

#### Overall Flow

Client requests chunk info from master → master returns chunk metadata → client directly reads/writes data from chunkservers → chunkservers update master when needed.

### Characteristics of GFS

{{< figure src="A%20Comparative%20Study%20on%20Distributed%20File%20Systems/figures/Google%20File%20System%20Characteristics.png" caption="Google File System Characteristics" align="center" >}}

*   **Error Tolerance**: GFS can handle faults without losing data.
*   **Data Replication**: Important data is automatically copied across multiple servers.
*   **Backup and Recovery**: Supports self-reliant data backup and recovery.
*   **High Productivity**: Optimized for large-scale data processing.
*   **Efficient Communication**: Minimizes communication between primary and secondary servers through block management.
*   **Identification and Authorization**: Provides mechanisms to identify and authorize users.
*   **High Availability**: Reliable system with minimal downtime.

GFS clusters with over 1,000 nodes and 300 TB of storage can serve hundreds of clients continuously, making them extremely powerful.

---

## Hadoop Distributed File System (HDFS)

HDFS is an open-source version of the Google File System, designed to handle large datasets efficiently. It is widely used by web companies like Facebook, eBay, LinkedIn, and Twitter for big data storage and analytics.

### Hadoop Master-Slave Architecture (HDFS + YARN)

{{< figure src="A%20Comparative%20Study%20on%20Distributed%20File%20Systems/figures/Architecture%20of%20HDFS.png" caption="Hadoop Master-Slave Architecture (HDFS + YARN)" align="center" >}}

Hadoop 2.x clusters combine storage (HDFS) and resource management (YARN). The architecture has two main levels:

#### 1. Master Node (The "Brain")

Manages cluster health, metadata, and job scheduling. It does not store actual data.

**NameNode (HDFS):**
*   Stores metadata like filenames, permissions, and locations of data blocks.
*   Knows which Slave Node holds which part of a file but does not store file contents.

**ResourceManager (YARN):**
*   Manages cluster resources (CPU, RAM).
*   Accepts user job submissions and allocates resources to Slave Nodes.

#### 2. Slave Nodes (The "Workers")

Hundreds or thousands of standard servers performing storage and computation.

**DataNode (HDFS):**
*   Stores actual data blocks.
*   Sends heartbeats to NameNode and reports stored blocks.

**NodeManager (YARN):**
*   Manages processes (containers) on the node.
*   Executes instructions from ResourceManager.

**Map / Reduce (Processing):**
*   Map processes chunks of data; Reduce aggregates results.
*   Running computation on the same node where data is stored improves efficiency (Data Locality).

#### Workflow Summary

**Storage:** NameNode directs clients where to store data; DataNodes hold it.

**Processing:** ResourceManager assigns jobs; NodeManagers execute MapReduce tasks on Slave Nodes.

---

## File System Comparison

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 2: </span>
    Comparative Analysis of Distributed File Systems
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9em;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 10px; text-align: left;">File System</th>
            <th style="padding: 10px; text-align: left;">Performance</th>
            <th style="padding: 10px; text-align: left;">Scalability</th>
            <th style="padding: 10px; text-align: left;">Availability</th>
            <th style="padding: 10px; text-align: left;">Fault Tolerance</th>
            <th style="padding: 10px; text-align: left;">Data Flow</th>
            <th style="padding: 10px; text-align: left;">Reliability</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">NFS</td>
            <td style="padding: 10px;">Average one-way latencies: 0.027 ms, 6.87 ms, 13.9 ms</td>
            <td style="padding: 10px;">Scalable with pNFS (supports parallel storage)</td>
            <td style="padding: 10px;">Supports small and large files (100 MB to 5 GB)</td>
            <td style="padding: 10px;">Can tolerate CPU failure; state maintained in /var/lib/nfs</td>
            <td style="padding: 10px;">Transmission via TCP & UDP</td>
            <td style="padding: 10px;">Early versions were less reliable; improved in NFS v4</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">HDFS</td>
            <td style="padding: 10px;">Average two-way latency: 175 s for files up to 50 GB</td>
            <td style="padding: 10px;">Nodes can be added or removed dynamically</td>
            <td style="padding: 10px;">High availability in Hadoop 2.x to prevent single points of failure</td>
            <td style="padding: 10px;">Creates replicas across different nodes/clusters</td>
            <td style="padding: 10px;">Uses MapReduce for data transfer</td>
            <td style="padding: 10px;">Data replicated across multiple machines for reliability</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">GFS</td>
            <td style="padding: 10px;">Fixed chunk size (64 KB); each block has 32-bit checksum</td>
            <td style="padding: 10px;">Minimizes master involvement to avoid hotspots</td>
            <td style="padding: 10px;">High availability using partitioned memory (BigTable)</td>
            <td style="padding: 10px;">Chunks stored in Linux systems and replicated across sites</td>
            <td style="padding: 10px;">Pipelining over TCP for high-bandwidth transfer</td>
            <td style="padding: 10px;">Controls multiple replicas across locations for reliability</td>
        </tr>
        <tr>
            <td style="padding: 10px; font-weight: bold;">OpenAFS</td>
            <td style="padding: 10px;">Cannot do parallel processing; average 1024 MB per unit time</td>
            <td style="padding: 10px;">Scales up to petabytes (1 GB per user; 1 PB for 1 million users)</td>
            <td style="padding: 10px;">4-bit releases from secure endpoints; some stability issues</td>
            <td style="padding: 10px;">Replication doesn’t happen; uses multiple read-only servers</td>
            <td style="padding: 10px;">Supports read/write or read-only; can create 11 replicas of read-only data</td>
            <td style="padding: 10px;">Ensured via read-only replication and client-side caching</td>
        </tr>
    </tbody>
</table>

</div>

---

## What We Learnt From This Study

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 3: </span>
    Summary of Learnings: GFS vs NFS vs AFS
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9em;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 10px; text-align: left;">Feature</th>
            <th style="padding: 10px; text-align: left;">GFS</th>
            <th style="padding: 10px; text-align: left;">NFS</th>
            <th style="padding: 10px; text-align: left;">AFS</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Architecture</td>
            <td style="padding: 10px;">Cluster-based</td>
            <td style="padding: 10px;">Client-Server</td>
            <td style="padding: 10px;">Cluster-based</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Caching</td>
            <td style="padding: 10px;">No caching</td>
            <td style="padding: 10px;">Client and server caching</td>
            <td style="padding: 10px;">Client caching</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Similarity to Unix</td>
            <td style="padding: 10px;">Not similar</td>
            <td style="padding: 10px;">Similar</td>
            <td style="padding: 10px;">Similar</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Data Storage / Reads</td>
            <td style="padding: 10px;">File data stored across different chunk servers; reads come from multiple servers</td>
            <td style="padding: 10px;">Reads come from the same server</td>
            <td style="padding: 10px;">Reads come from the same server</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Server Replication</td>
            <td style="padding: 10px;">No replication</td>
            <td style="padding: 10px;">Server replication</td>
            <td style="padding: 10px;">Server replication</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Namespace</td>
            <td style="padding: 10px;">Location-independent</td>
            <td style="padding: 10px;">Not location-independent</td>
            <td style="padding: 10px;">Location-independent</td>
        </tr>
        <tr>
            <td style="padding: 10px; font-weight: bold;">Locking</td>
            <td style="padding: 10px;">Lease-based locking</td>
            <td style="padding: 10px;">Lease-based locking</td>
            <td style="padding: 10px;">Lease-based locking</td>
        </tr>
    </tbody>
</table>

</div>

---

## Conclusion

This study compared several file systems, including NFS, AFS, GFS, and HDFS. Among these, HDFS stands out as the most preferred option due to its high performance, strong availability, and robust file replication, which provides excellent fault tolerance. GFS follows closely because of its scalability and use of data chunks that enable efficient pipelined transmission over TCP channels. NFS remains popular as a well-established system, trusted for its reliability, while OpenAFS offers several user-friendly features, including client-side caching and high scalability.

---

## Presentation

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; margin-bottom: 20px;">
    <iframe src="A%20Comparative%20Study%20on%20Distributed%20File%20Systems/PRESENTATION%20-%20A%20COMPARATIVE%20STUDY%20ON%20DISTRIBUTED%20FILE%20SYSTEMS.pdf" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
</div>

---

## Additional Resources

#### Project Source & Engineering Materials
Access the complete presentation and related computational engineering materials via the links below:

<div style="display: flex; flex-direction: column; gap: 8px;">
  

<div>
    <!-- Globe/DOI Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
    <a href="https://doi.org/10.13140/RG.2.2.31450.82887" target="_blank">ResearchGate Record (DOI)</a>
  </div>

<div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB" target="_blank">Distributed Computing</a>
  </div>

<div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/COMPUTER-ENGINEERING" target="_blank">Computer Engineering Resources</a>
  </div>

</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "A Comparative Study on Distributed File Systems". AmeyArc (Mar 2022). https://amey-thakur.github.io/posts/2022-03-31-a-comparative-study-on-distributed-file-systems/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2022dfs,
  title   = "A Comparative Study on Distributed File Systems",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2022",
  month   = "Mar",
  url     = "https://amey-thakur.github.io/posts/2022-03-31-a-comparative-study-on-distributed-file-systems/"
}
```

---

## References

<style>
.reference-container {
    padding-left: 0;
}
.reference-item {
    display: flex;
    margin-bottom: 0.8rem;
}
.reference-num {
    flex: 0 0 45px; /* Fixed width for the number column */
    font-weight: bold;
    color: inherit;
}
.reference-text {
    flex: 1; /* Takes remaining space */
}
</style>

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">[1]</span>
    <span class="reference-text"><a id="ref-1"></a><b>S. De and M. Panjwani</b>, "A Comparative Study on Distributed File Systems," in <i>Modern Approaches in Machine Learning and Cognitive Science: A Walkthrough, Latest Trends in AI, Volume 2</i>, Springer, Cham, pp. 43-51, 2021, DOI: <a href="https://doi.org/10.1007/978-3-030-68291-0_5">10.1007/978-3-030-68291-0_5</a> [Accessed: Mar. 31, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>Y. Gao, X. Gao, X. Yang, J. Liu, and G. Chen</b>, "An Efficient Ring-Based Metadata Management Policy for Large-Scale Distributed File Systems," <i>IEEE Transactions on Parallel and Distributed Systems</i>, vol. 30, no. 9, pp. 1962-1974, Sep. 2019, DOI: <a href="https://doi.org/10.1109/TPDS.2019.2901883">10.1109/TPDS.2019.2901883</a> [Accessed: Mar. 31, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>K. Bok, J. Lim, H. Oh, and J. Yoo</b>, "An efficient cache management scheme for accessing small files in Distributed File Systems," <i>2017 IEEE International Conference on Big Data and Smart Computing (BigComp)</i>, Jeju, South Korea, pp. 151-155, Feb. 2017, DOI: <a href="https://doi.org/10.1109/BIGCOMP.2017.7881731">10.1109/BIGCOMP.2017.7881731</a> [Accessed: Mar. 31, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>M. Nithya and N. U. Maheshwari</b>, "Load rebalancing for Hadoop Distributed File System using distributed hash table," <i>2017 International Conference on Intelligent Sustainable Systems (ICISS)</i>, Palladam, India, pp. 939-943, Dec. 2017, DOI: <a href="https://doi.org/10.1109/ISS1.2017.8389317">10.1109/ISS1.2017.8389317</a> [Accessed: Mar. 31, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>L. S. Rani, K. Sudhakar, and S. V. Kumar</b>, "Distributed File Systems: A Survey," <i>International Journal of Computer Science and Information Technologies</i>, vol. 5, no. 3, pp. 3716-3721, 2014, <a href="https://www.ijcsit.com/docs/Volume%205/vol5issue03/ijcsit20140503234.pdf">https://www.ijcsit.com/docs/Volume%205/vol5issue03/ijcsit20140503234.pdf</a> [Accessed: Mar. 31, 2022].</span>
</div>

</div>
