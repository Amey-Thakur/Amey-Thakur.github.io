---
title: "QuadTree Visualizer"
date: 2022-04-27T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["2D Spatial Partitioning", "Algorithm Visualizer", "Algorithms", "Bounding Volume Hierarchy", "Broad Phase Collision Detection", "Collision Detection", "Computational Geometry", "Computer Graphics", "Computer Vision", "Data Structure Visualization", "Data Structures", "Digital Image Processing", "FPS Optimization", "Game Development", "Game Engine Architecture", "Game Physics", "GIS", "Hit Detection", "Image Compression", "Interactive Simulation", "JavaScript", "K-D Tree", "Location-Based Services", "Narrow Phase Collision Detection", "Nearest Neighbor Search", "Next.js", "Octree", "p5.js", "Performance Optimization", "Physics Engine", "QuadTree", "Quadtree Data Structure", "R-tree", "Range Queries", "React", "Real-time Simulation", "Recursive Subdivision", "Spatial Hash", "Spatial Indexing", "Spatial Partitioning Algorithms", "Tree Data Structure", "TypeScript", "Visualization", "Web Development"]
ShowToc: true
TocOpen: false
summary: "Special thanks to Mega Satish and Hasan Rizvi for their meaningful contributions, support, and wisdom that helped shape this work. We propose to develop a program that can show a QuadTree view and data model architecture. Nowadays, many digital map applications have the need to present large quantities of precise point data on the map."
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

<style>
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

<p class="special-thanks">
Special thanks to <a href="https://scholar.google.com/citations?user=7Ajrr6EAAAAJ&hl=en">Mega Satish</a> and <a href="https://scholar.google.com/citations?user=OJuGq08AAAAJ&hl=en">Hasan Rizvi</a> for their meaningful contributions, support, and wisdom that helped shape this work.
</p>

We propose to develop a program that can show a QuadTree view and data model architecture. Nowadays, many digital map applications have the need to present large quantities of precise point data on the map. Such data can be weather information or the population in towns. With the development of the Internet of Things (IoT), we expect such data will grow at a rapid pace. However, visualizing and searching in such a magnitude of data becomes a problem as it takes a huge amount of time. QuadTrees are data structures that are used to efficiently store point data in a two-dimensional environment. Each node in this tree has a maximum of four children. QuadTrees allow us to visualize the data easily and rapidly compared to other data structures. This project aims to build an application for interactively visualizing such data, using a combination of grid-based clustering and hierarchical clustering, along with QuadTree spatial indexing. This application illustrates the simulation of the working of the QuadTree data structure.

---

## Introduction

The QuadTree is a spatial data structure with a hierarchical structure. It's a tree with each level corresponding to a further refinement of the space in question. Though QuadTrees come in a variety of shapes and sizes, they can be used in a variety of ways. The concept can be applied to any dimension, and it is always a recursive subdivision of space that aids in the storage of information and provides the most vital or interesting details regarding space. In QuadTrees, we begin by adding pointers to its root node, which defines all potential space. The node divides into four child nodes when the number of points in the node reaches a predetermined maximum capacity. When any of those nodes has reached its full point capacity, it splits into four child nodes, and so on. QuadTrees have a range of applications; from internet services handling millions of requests every second, image compression, handling geolocation services, searching for nodes in 2-D areas, collision detection and more.  Collision detection is a crucial feature in the majority of video games. Detecting when two entities collide is critical in both 2D and 3D games, since bad collision detection may lead to some very intriguing effects. Numerous games need the use of collision detection techniques to identify whether two objects have interacted, however, these algorithms are frequently costly procedures that may significantly slow down a system. In this paper, we will be addressing QuadTrees, and how we can use them to speed up collision detection by skipping pairs of objects that are too far apart to collide. We’ll be writing a general-purpose, scalable and re-usable QuadTree library in Typescript and importing it into a visualization tool to depict its internal workings.

This project aims to provide a web application for visualizing the QuadTree structure.  QuadTree. The users should be able to understand the working of the QuadTree and experience the simulation provided on the web application. This Visualizer provides an interactive environment where users can change configurations of the QuadTree and environment conditions at runtime.

---

## Literature Survey

### Brief History of QuadTree

A QuadTree [[1]](#ref-1)[[2]](#ref-2)[[3]](#ref-3) is a tree data structure with zero or four offspring at each node. Its key distinguishing feature is its method of recursively partitioning a flat 2-D [[2]](#ref-2) space into four regions. The data associated with a leaf cell differs depending on the application, but the leaf cell is a "unit of relevant spatial information." The subdivided areas or regions can be square or rectangular or any other form. This data structure was named a QuadTree by Raphael Finkel and J.L. Bentley in 1974.

### Existing Systems

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 1: </span>
    Existing Systems
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center;">Author’s Name</th>
            <th style="padding: 12px; text-align: center;">Title and Year of Publication</th>
            <th style="padding: 12px; text-align: center;">Findings</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Qing Cai, Yimin Zhou</td>
            <td style="padding: 12px; vertical-align: top;">A quadtree-based hierarchical clustering a method for visualizing large point dataset, 2016</td>
            <td style="padding: 12px; vertical-align: top;">This paper introduces a new clustering method with quadtree spatial indexing. It explains a grid-based, partitioning, hierarchical clustering method on quadtree file system storage.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Clifford A. Shaffer, Hanan Samet</td>
            <td style="padding: 12px; vertical-align: top;">Optimal quadtree construction algorithms, 1987</td>
            <td style="padding: 12px; vertical-align: top;">In this paper, an algorithm for constructing a quadtree in time proportionate to the number of blocks in a given picture is described.</td>
        </tr>
        <tr>
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Irene Gargantini</td>
            <td style="padding: 12px; vertical-align: top;">An effective way to represent quadtrees, 1982</td>
            <td style="padding: 12px; vertical-align: top;">This paper proposes a new structure very similar to a quadtree, called a “linear quadtree” and different algorithms used to represent that structure. The linear quadtree saves 66% of the computer storage required by regular quadtrees.</td>
        </tr>
    </tbody>
</table>

</div>

---

## Proposed Methodology

### Brief History of QuadTree

The QuadTree is a data structure for organizing objects based on their locations in a two-dimensional space. By definition, a QuadTree [[2]](#ref-2) is a tree in which each node has at most four children. QuadTree implementations ensure that as points are added to the tree, nodes are rearranged such that none of them has more than four children. Figure 1 below illustrates the general concept of QuadTree data structure.

{{< figure src="QuadTree%20Visualizer/figures/Figure 1%20-%20QuadTree%20Data%20Structure.png" caption="QuadTree Data Structure" align="center" >}}

The QuadTree partitioning strategy divides space [[1]](#ref-1)[[2]](#ref-2) into four quadrants at each level. When a quadrant contains more than one object, the tree subdivides that region into four smaller quadrants, adding a level to the tree. A similar partitioning is also known as a Q-tree. QuadTrees are a way of partitioning space so that it's easy to traverse and search.

### Applications of QuadTree

It is used extensively in computer graphics, image compression and is also used to represent spatial relations. Visualizing data points with a QuadTree [[3]](#ref-3) and checking and detecting collisions. The computer issue of identifying the collision of two or more bodies is known as collision detection. Collision detection [[5]](#ref-5) is a basic problem in computational geometry that has applications in a wide range of computer domains. Figure 2 shows the use case of Quadtree Visualizer.

{{< figure src="QuadTree%20Visualizer/figures/Figure 2 - QuadTree Visualizer.png" caption="QuadTree Visualizer" align="center" >}}

QuadTrees are also implemented for spatial indexing [[3]](#ref-3) while searching a particular point or location in a map. QuadTrees are very efficient as they can sparse through the maps very easily and quickly compared to other methods. Figure 3 shows the use case of QuadTree Spatial Indexing.

{{< figure src="QuadTree%20Visualizer/figures/Figure 3 - QuadTree Spatial Indexing.png" caption="QuadTree Spatial Indexing" align="center" >}}

QuadTrees, for example, can handle a sparse Mario level a billion tiles across, where one of the tiles contains the finishing spot. A QuadTree will split the arrival spot into different cells and still use gigantic cells for the empty spaces. Figure 4 shows the use case of QuadTree in Gaming.

{{< figure src="QuadTree%20Visualizer/figures/Figure 4 - QuadTree in Gaming.png" caption="QuadTree in Gaming" align="center" >}}

### Some possible use cases of QuadTree

#### Hit detection:

For example, as seen in the maps above, there are a lot of points in space. If we wish to discover an arbitrary point P, we can do it inside that set of points. This quickly turns into a frantic process. We could check each and every single point to P, but when there are 1000 points yet none of them are P, we will have to do 1000 comparisons to figure out which point is P.

Alternatively, we may get a very rapid lookup by retaining a matrix (a 2D array) of Booleans for each and every conceivable point in this space. However, suppose the area occupied by these points is 1 million <span style="font-family: 'Times New Roman', serif;">&times;</span> 1 million so we need to keep 1,000,000,000,000 variables.

A QuadTree would seem to be a better choice in this scenario. To find P, the QuadTree [[1]](#ref-1) will determine which quadrant it is in. Then it will determine which quadrant within that quadrant it is in. Even if there are 1000 points in the space, it will only have to execute this seven times for a <span style="font-family: 'Times New Roman', serif;">100 &times; 100</span> space (provided points can have numerical value only). Once it's found that rectangle node, it just needs to test whether any of the four-leaf equals P.

#### Sparse Data using QuadTree:

QuadTrees are ideal for sparse data to search for a particular point. By only performing computations between items in comparable nodes/quads, QuadTrees aid in obtaining knowledge about which collisions in an environment are worth investigating.

QuadTree nodes split into four evenly-sized leaf nodes when the number of objects inside them reaches a certain capacity. Objects are inserted into a fresh QuadTree every iteration, which places each object in its deepest possible node.The QuadTree algorithm improves upon the naive <span style="font-family: 'Times New Roman', serif;"><i>T</i>(<i>n</i>) = &theta;(<i>n</i><sup>2</sup>)</span> algorithm and achieves <span style="font-family: 'Times New Roman', serif;"><i>T</i>(<i>n</i>) = <i>O</i>(<i>n</i><sup>2</sup>)</span>, <span style="font-family: 'Times New Roman', serif;"><i>T</i>(<i>n</i>) = &Omega;(<i>n</i> log <i>n</i>)</span>. Inadvertently, QuadTrees depending on pixels are a sort of trie.

### Limitations of QuadTree

The fundamental drawback of QuadTrees is that comparing two pictures [[4]](#ref-4) that vary only in rotations or translation is nearly difficult. This is due to the fact that the QuadTree depiction of such pictures will be so distinct. The picture rotation methods offered are limited to revolutions of 90 degrees. There is no alternative rotation available, thus there is no translation facility. Figure 5.1 shows the original image and Figure 5.2 shows the rotated images. As we can see, it is not possible to compare two images that are different in terms of rotation.

<figure class="align-center">
    <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
        <div style="flex: 1 1 0; min-width: 45%; text-align: center;">
            <img loading="lazy" src="QuadTree%20Visualizer/figures/Figure 5 - Image Translation in QuadTree (5.1) First Image.png" alt="(5.1) First Image" style="border-radius: 4px; margin: 1rem auto; display: block; width: 100%; height: auto; aspect-ratio: 1.5; object-fit: contain;">
            <p style="color: var(--secondary); font-size: 14px; margin-top: 0px;">(5.1) First Image</p>
        </div>
        <div style="flex: 1 1 0; min-width: 45%; text-align: center;">
            <img loading="lazy" src="QuadTree%20Visualizer/figures/Figure 5 - Image Translation in QuadTree (5.2) Rotated Image.png" alt="(5.2) Rotated Image" style="border-radius: 4px; margin: 1rem auto; display: block; width: 100%; height: auto; aspect-ratio: 1.5; object-fit: contain;">
            <p style="color: var(--secondary); font-size: 14px; margin-top: 0px;">(5.2) Rotated Image</p>
        </div>
    </div>
    <figcaption>
        <p>Image Translation in QuadTree</p>
    </figcaption>
</figure>

### Types of QuadTree

There are three types of QuadTrees:
1.  Point QuadTree
2.  Edge QuadTree
3.  Polygonal Map QuadTree.

Some characteristics are shared by all QuadTrees:
*   They break space down into flexible cells.
*   There is a maximum capacity for each cell (or bucket). When the bucket reaches its full capacity, it separates.
*   The QuadTree's spatial decomposition is followed by the tree directory.

### Working of QuadTree

The Figure 6 below depicts how a QuadTree [[7]](#ref-7) alters as a result of insertion of a point E:
1.  Make four boxes out of the current two-dimensional space.
2.  If a box includes one or more points, make a child object that stores the box's two-dimensional space.
3.  Do not generate a child for a box that does not contain any points.
4.  Repeat with each of the children.

{{< figure src="QuadTree%20Visualizer/figures/Figure 6 - Working of QuadTree.png" caption="Working of QuadTree" align="center" >}}

## Algorithm

Three types of nodes are used in quadtree:
1.  **Point node:** It is used to represent a point. It is always a leaf node.
2.  **Empty node:** It is used as a leaf node to represent that no point exists in the region it represents.
3.  **Region node:** This is always an internal node. It is used to represent a region. A region node always has 4 children nodes that can either be a point node or an empty node.

### Insertion in QuadTree

**Insertion:** A recursive function for storing a point in a QuadTree.
1.  As the current node, begin with the root node.
2.  If the specified point is not within the boundary indicated by the current node, the insertion should be terminated with an error.
3.  Determine the best child node to store the point.
4.  If the child node is empty, it should be replaced with a point node that represents the point. Insertion should be stopped.
5.  Replace the child node with a region code if it is a point node. For the point that was just replaced, use insert. Set the current node to be the region's freshly generated node.
6.  Set the specified child node as the current node if it is a region node. Proceed to step 2.

### Search in QuadTree

**Search:** This is a boolean function that determines whether or not a point exists in 2D space.
1.  As the current node, begin with the root node.
2.  If the specified point is not within the boundary indicated by the current node, the search should be terminated with an error.
3.  Determine the best child node to hold the point in.
4.  Return FALSE if the child node is empty.
5.  Return TRUE if the child node is a point node and matches the specified point, else return FALSE.
6.  Set the current node as the child region node if the child node is a region node. Proceed to step 2.

### Complexity

#### Time complexity:
<div style="display: flex; flex-direction: column; align-items: center; margin: 1rem 0;">

<p style="font-size: 0.9em; margin-bottom: 10px; text-align: center;">
    <span style="user-select: none;">Table 2: </span>
    Time Complexity
</p>

<table style="width: auto; min-width: 200px; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 2px solid #ccc;">
      <th style="text-align: left; padding: 8px;">Operation</th>
      <th style="text-align: left; padding: 8px;">Complexity</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><strong>Find</strong></td>
      <td style="padding: 8px;"><span style="font-family: 'Times New Roman', serif; font-size: 1.1em;"><i>O</i>(log<sub>2</sub><i>N</i>)</span></td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><strong>Insert</strong></td>
      <td style="padding: 8px;"><span style="font-family: 'Times New Roman', serif; font-size: 1.1em;"><i>O</i>(log<sub>2</sub><i>N</i>)</span></td>
    </tr>
    <tr>
      <td style="padding: 8px;"><strong>Search</strong></td>
      <td style="padding: 8px;"><span style="font-family: 'Times New Roman', serif; font-size: 1.1em;"><i>O</i>(log<sub>2</sub><i>N</i>)</span></td>
    </tr>
  </tbody>
</table>

</div>

#### Space complexity:
<span style="font-family: 'Times New Roman', serif; font-size: 1.1em;"><i>O</i>(<i>k</i> log<sub>2</sub><i>N</i>)</span>, where <span style="font-family: 'Times New Roman', serif; font-size: 1.1em;"><i>k</i></span> is the count of points in the space and Space is of dimension <span style="font-family: 'Times New Roman', serif; font-size: 1.1em;"><i>N</i> &times; <i>M</i></span>, <span style="font-family: 'Times New Roman', serif; font-size: 1.1em;"><i>N</i> &ge; <i>M</i></span>.

### Collision in QuadTree

Because the data points in the visualizer are always shifting, collisions are unavoidable. Collision [[5]](#ref-5) is the meeting of two bodies, in this case data points in the shape of circles. The QuadTree visualization is built on top of a 2D Collision System with a restitution coefficient that can be adjusted to differentiate between elastic and inelastic impacts. Collision detection is a costly activity. One method for speeding up collision detection is to use QuadTrees.

### Coefficient of Restitution

The coefficient of restitution [[6]](#ref-6) is the ratio of the final velocity to the starting velocity of two objects after they collide. The restitution coefficient, written as '<span style="font-family: 'Times New Roman', serif;"><i>e</i></span>,' is a unitless quantity with values ranging from 0 to 1.

The coefficient of restitution is a quantity that represents the nature of the colliding materials. The coefficient of restitution informs about the elasticity of the collision. A fully elastic collision is one in which there is no loss of total kinetic energy. The greatest coefficient of restitution for this sort of collision is <span style="font-family: 'Times New Roman', serif;"><i>e</i> = 1</span>. A fully inelastic collision is one in which all of the kinetic energy is wasted. They have a restitution coefficient of <span style="font-family: 'Times New Roman', serif;"><i>e</i> = 0</span>. The majority of real-life crashes occur in the middle. The Coefficient of Restitution mathematical formula is as follows:

<div style="font-family: 'Times New Roman', Times, serif; font-style: italic; font-size: 1.2rem; display: flex; align-items: center; justify-content: center; gap: 15px; background: rgba(128, 128, 128, 0.1); padding: 20px; border-radius: 8px; margin: 2rem 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
    <span style="font-weight: bold;">Coefficient of Restitution (e)</span>
    <span>=</span>
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
        <div style="border-bottom: 2px solid currentColor; padding-bottom: 5px; margin-bottom: 5px;">Relative Speed After Collision</div>
        <div>Relative Speed Before Collision</div>
    </div>
</div>

You can see from the following equation that you always divide the smaller number by a larger number. As a result, the restitution coefficient is always positive.

### Workflow of QuadTree

Figure 7 illustrates the workflow of the QuadTree application. Next.js is responsible for both client and server-side scripting.

{{< figure src="QuadTree%20Visualizer/figures/Figure 7 - Workflow of QuadTree.png" caption="Workflow of QuadTree" align="center" >}}

### Model Architecture

An architectural model is a simplified representation of a system. It is an estimate that captures the various system characteristics. It is a generalized form that has all of the system's critical elements. The process of modelling architecture entails determining the system's features and expressing them as models so that the system may be understood. Architecture models make it possible to see information about the system represented by the model. Figure 8 depicts the web application's model architecture.

{{< figure src="QuadTree%20Visualizer/figures/Figure 8 - Model Architecture of QuadTree.png" caption="Model Architecture of QuadTree" align="center" >}}

---

## Design

### Experimental Setup

*   Since we are using Next.js in our project, we first need to have Node.js.
*   The web application works on http://localhost:3000.
*   To run the application locally, we need to install the packages required using the npm command: `npm install package.json`.
*   Figure 9 shows the command prompt with the packages installed using the npm install commands.

{{< figure src="QuadTree%20Visualizer/figures/Figure 9 - Command-npm install package.json.png" caption="Command: npm install package.json" align="center" >}}

*   After installing all the dependencies, we then run the command: `npm run dev`.
*   After we run the command: `npm run dev`. It will run the developer server.
*   Figure 10 depicts the compilation and running of the server. The server is working on http://localhost:3000.

{{< figure src="QuadTree%20Visualizer/figures/Figure 10 - Compilation & Server Hosting.png" caption="Compilation & Server Hosting" align="center" >}}

---

## Implementation

### Quadtree.ts

<details>
<summary>Show Code</summary>

```typescript
// A QuadNode object must have a way to tell if it is inside a given node's bounds

export interface QuadObject {
  insideRect: (rect: Rect) => boolean // whether the object in fully contained within a Rect
}

// Node of a QuadTree
// carries data about its:
// - bounds
// - depth
// - children
// - containing objects

export class QuadNode {
  public leaves!: Array<QuadNode> | null
  public quadObjects = new Array<QuadObject>()

  constructor(
    public bounds: Rect,
    private depth: number
  ) { }

  // cleanup references down the QuadTree recursively

  clear(): void {
    this.quadObjects = new Array<QuadObject>()
    this.leaves?.forEach((leaf: QuadNode) => leaf.clear())
    this.leaves = null
  }

  // process any updates recursively down the tree

  process(quadNodeProcedure: (quadNode: QuadNode) => void): void {
    quadNodeProcedure(this)
    this.leaves?.forEach((leaf: QuadNode) => leaf.process(quadNodeProcedure))
  }

  // Initialise the sub-quads of the current Node,
  // and test if any object fit into a deeper quad

  subdivide(): void {
    // calculate new bounds of sub-quads
    const midW = this.bounds.w / 2
    const midH = this.bounds.h / 2
    const newDepth = this.depth + 1

    this.leaves = [
      new QuadNode(new Rect(this.bounds.x, this.bounds.y, midW, midH), newDepth),
      new QuadNode(new Rect(this.bounds.x + midW, this.bounds.y, midW, midH), newDepth),
      new QuadNode(new Rect(this.bounds.x, this.bounds.y + midH, midW, midH), newDepth),
      new QuadNode(new Rect(this.bounds.x + midW, this.bounds.y + midH, midW, midH), newDepth)
    ]

    // place current particles into newly created groups
    // removes the object from the current array if it fits into another node

    this.quadObjects.forEach((object: QuadObject) => {
      this.leaves?.forEach((leaf: QuadNode) => {
        if (leaf.insert(object))
          this.quadObjects.splice(this.quadObjects.indexOf(object), 1) // remove from the current level
      })
    })
  }

  // Inserts an object into the deepest point of the QuadTree it belongs
  // returns whether the object fit into the bounds of the currently attempted quadNode

  insert(quadObject: QuadObject): boolean {
    // test if the quad bounds contains the object
    if (!quadObject.insideRect(this.bounds)) return false

    // directly insert if max depth is reached
    if (this.depth >= QuadTree.maxDepth)
      return !!this.quadObjects.push(quadObject) // length should always be non-zero for push -> truthy

    // Node is safe to push object into
    // first try the leaves
    if (this.leaves)
      for (const leaf of this.leaves)
        if (leaf.insert(quadObject)) return true

    // if no leaves, or leaves fail to cover object, push current node
    this.quadObjects.push(quadObject)

    // test if max capacity for the node has been reached
    if (!this.leaves && this.quadObjects.length > QuadTree.capacity)
      this.subdivide() // divide and redistribute

    // object has been placed into an array by this point
    return true
  }
}

// Root Reference for a QuadTree
// primary interface for operations

export class QuadTree {
  static maxDepth = Math.ceil(Math.log2(1000 / 5) / 2) + 1 // default for as small as 5 pixels on a 1000x1000 grid
  static capacity = 5
  public quadRoot: QuadNode

  constructor(
    public bounds: Rect,
    public quadObjects: Array<QuadObject>
  ) {
    this.quadRoot = new QuadNode(bounds, 0)
  }

  // Updates the QuadTree will most recent object positions and then recursively calls a procedure
  // @param quadNodeProcedure function to call on each node of the tree

  process(quadNodeProcedure: (quadNode: QuadNode) => void): void {
    this.quadRoot.clear() // refresh the QuadNodes
    this.quadObjects.forEach((quadObject: QuadObject) => this.quadRoot.insert(quadObject)) // insert updated objects
    this.quadRoot.process(quadNodeProcedure) // call any user-defined, per-node procedure
  }

  // Inserts a QuadObject into the deepest level of the QuadTree it belong
  // @param quadObject object to insert into the QuadTree

  insert(quadObject: QuadObject): void {
    this.quadObjects.push(quadObject) // update master object array
    this.quadRoot.insert(quadObject) // descend object into tree
  }
}
```

</details>

### Package.json (Dependencies used)

<details>
<summary>Show Code</summary>

```json
"dependencies": {
  "@material-ui/core": "^4.11.2",
  "@material-ui/icons": "^4.11.2",
  "next": "10.0.5",
  "react": "17.0.1",
  "react-dom": "17.0.1"
},

"devDependencies": {
  "@types/node": "^14.14.20",
  "@types/react": "^17.0.0",
  "@typescript-eslint/eslint-plugin": "^4.12.0",
  "@typescript-eslint/parser": "^4.12.0",
  "eslint": "^7.17.0",
  "eslint-plugin-react": "^7.22.0",
  "gh-pages": "^3.1.0",
  "sass": "^1.32.2",
  "typescript": "^4.1.3"
}
```

</details>

### Python Implementation

#### QuadTree from Images

The Python implementation demonstrates how to generate a QuadTree from an image and visualize the results. This implementation shows the core algorithm for splitting images into quadrants and calculating mean colors for each section.

The main objective is to generate a quadtree from an image and display it.

**Input:**
```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('./dataset/Filly.jpg')
img.shape
```

**Output:**
```
(1280, 960, 3)
```

**Input:**
```python
plt.imshow(img)
```

**Output:**
```
<matplotlib.image.AxesImage at 0x1d800729ed0>
```

{{< figure src="QuadTree%20Visualizer/Kaggle/dataset/Filly_output.png" caption="Original Image" align="center" >}}

#### Split Image in 4

A big part of how the algorithm works is splitting the image into 4 quarters and calculate the mean color of each part to create a level of the tree. Let's split the image into four parts and calculate the mean color of each quadrant.

**Input:**
```python
from operator import add
from functools import reduce

def split4(image):
    half_split = np.array_split(image, 2)
    res = map(lambda x: np.array_split(x, 2, axis=1), half_split)
    return reduce(add, res)

split_img = split4(img)
split_img[0].shape
```

**Output:**
```
(640, 480, 3)
```

**Input:**
```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].imshow(split_img[0])
axs[0, 1].imshow(split_img[1])
axs[1, 0].imshow(split_img[2])
axs[1, 1].imshow(split_img[3])
```

**Output:**
```
<matplotlib.image.AxesImage at 0x1d8467e38d0>
```

{{< figure src="QuadTree%20Visualizer/Kaggle/dataset/Filly_split.png" caption="Split Quadrants" align="center" >}}

#### Reconstruct The Full Image from The Split
This will be useful when we want to display the image back, as the quadtree will store the images split into 4

**Input:**
```python
def concatenate4(north_west, north_east, south_west, south_east):
    top = np.concatenate((north_west, north_east), axis=1)
    bottom = np.concatenate((south_west, south_east), axis=1)
    return np.concatenate((top, bottom), axis=0)

full_img = concatenate4(split_img[0], split_img[1], split_img[2], split_img[3])
plt.imshow(full_img)
plt.show()
```

**Output:**

{{< figure src="QuadTree%20Visualizer/Kaggle/dataset/Filly_reconstructed.png" caption="Reconstructed Image" align="center" >}}

#### Calculate the mean

Calculate the mean of all the parts of the split.

**Input:**
```python
def calculate_mean(img):
    return np.mean(img, axis=(0, 1))

means = np.array(list(map(lambda x: calculate_mean(x), split_img))).astype(int).reshape(2,2,3)
print(means)
plt.imshow(means)
plt.show()
```

**Output:**
```
[[[123 112 107]
  [159 141 128]]

 [[101  67  76]
  [149 126 101]]]
```

{{< figure src="QuadTree%20Visualizer/Kaggle/dataset/Filly_mean.png" caption="Mean Calculation" align="center" >}}

#### QuadTree Data Structure

Now let's create a data structure that will allow us to construct our quadtree. It's a recursive calculation.

**Input:**
```python
def checkEqual(myList):
    first=myList[0]
    return all((x==first).all() for x in myList)

class QuadTree:

    def insert(self, img, level = 0):
        self.level = level
        self.mean = calculate_mean(img).astype(int)
        self.resolution = (img.shape[0], img.shape[1])
        self.final = True

        if not checkEqual(img):
            split_img = split4(img)

            self.final = False
            self.north_west = QuadTree().insert(split_img[0], level + 1)
            self.north_east = QuadTree().insert(split_img[1], level + 1)
            self.south_west = QuadTree().insert(split_img[2], level + 1)
            self.south_east = QuadTree().insert(split_img[3], level + 1)

        return self

    def get_image(self, level):
        if(self.final or self.level == level):
            return np.tile(self.mean, (self.resolution[0], self.resolution[1], 1))

        return concatenate4(
            self.north_west.get_image(level),
            self.north_east.get_image(level),
            self.south_west.get_image(level),
            self.south_east.get_image(level))
```

```python
img = mpimg.imread('./dataset/Filly.jpg')

quadtree = QuadTree().insert(img)
```

```python
plt.imshow(quadtree.get_image(1))
plt.show()
plt.imshow(quadtree.get_image(3))
plt.show()
plt.imshow(quadtree.get_image(7))
plt.show()
plt.imshow(quadtree.get_image(10))
plt.show()
```

**Output:**

{{< figure src="QuadTree%20Visualizer/Kaggle/dataset/Filly_quadtree.png" caption="QuadTree Data Structure" align="center" >}}

{{< figure src="QuadTree%20Visualizer/Kaggle/dataset/Filly_quadtree_depth_3.png" caption="QuadTree Depth 3" align="center" >}}

{{< figure src="QuadTree%20Visualizer/Kaggle/dataset/Filly_quadtree_depth_7.png" caption="QuadTree Depth 7" align="center" >}}

{{< figure src="QuadTree%20Visualizer/Kaggle/dataset/Filly_quadtree_depth_10.png" caption="QuadTree Depth 10" align="center" >}}

---

## Results

### Homepage

Figure 19 illustrates the homepage of the web application. Here we can visualize a QuadTree with the data points and the different divisions of the QuadTree.

{{< figure src="QuadTree%20Visualizer/figures/Figure 11 - Homepage.png" caption="Homepage" align="center" >}}

### Clear QuadTree

Figure 20 shows a clean QuadTree without the data points. Since there are no points, we can see only the square.

{{< figure src="QuadTree%20Visualizer/figures/Figure 12 - Clear QuadTree.png" caption="Clear QuadTree" align="center" >}}

### Spawn Bodies

Figure 21 depicts the spawn circles in the QuadTree. Here we can see the clear division of the QuadTree.

{{< figure src="QuadTree%20Visualizer/figures/Figure 13 - Spawn Bodies.png" caption="Spawn Bodies" align="center" >}}

### Random Bodies

Figure 22.1 & Figure 22.2 show the random bodies generated randomly in the QuadTree.

<figure class="align-center">
    <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
        <div style="flex: 1 1 0; min-width: 45%; text-align: center;">
            <img loading="lazy" src="QuadTree%20Visualizer/figures/Figure 14.1 - Random Bodies.png" alt="(14.1) Random Bodies" style="border-radius: 4px; margin: 1rem auto; display: block; width: 100%; height: auto; aspect-ratio: 1.5; object-fit: contain;">
            <p style="color: var(--secondary); font-size: 14px; margin-top: 0px;">(22.1) Random Bodies</p>
        </div>
        <div style="flex: 1 1 0; min-width: 45%; text-align: center;">
            <img loading="lazy" src="QuadTree%20Visualizer/figures/Figure 14.2 - Random Bodies.png" alt="(14.2) Random Bodies" style="border-radius: 4px; margin: 1rem auto; display: block; width: 100%; height: auto; aspect-ratio: 1.5; object-fit: contain;">
            <p style="color: var(--secondary); font-size: 14px; margin-top: 0px;">(22.2) Random Bodies</p>
        </div>
    </div>
    <figcaption>
        <p>Random Bodies</p>
    </figcaption>
</figure>

### Random & Spawn Bodies

Figure 23.1 & 23.2 Figure shows the combination of both random and spawn bodies in the QuadTree.

<figure class="align-center">
    <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
        <div style="flex: 1 1 0; min-width: 45%; text-align: center;">
            <img loading="lazy" src="QuadTree%20Visualizer/figures/Figure 15.1 - Random & Spawn Bodies.png" alt="(23.1) Random & Spawn Bodies" style="border-radius: 4px; margin: 1rem auto; display: block; width: 100%; height: auto; aspect-ratio: 1.5; object-fit: contain;">
            <p style="color: var(--secondary); font-size: 14px; margin-top: 0px;">(23.1) Random & Spawn Bodies</p>
        </div>
        <div style="flex: 1 1 0; min-width: 45%; text-align: center;">
            <img loading="lazy" src="QuadTree%20Visualizer/figures/Figure 15.2 - Random & Spawn Bodies.png" alt="(23.2) Random & Spawn Bodies" style="border-radius: 4px; margin: 1rem auto; display: block; width: 100%; height: auto; aspect-ratio: 1.5; object-fit: contain;">
            <p style="color: var(--secondary); font-size: 14px; margin-top: 0px;">(23.2) Random & Spawn Bodies</p>
        </div>
    </div>
    <figcaption>
        <p>Random & Spawn Bodies</p>
    </figcaption>
</figure>

### Control Panel

Figure 24 illustrates the control panel. The control panel here is used to simulate different environments in the QuadTree such as types of bodies, the coefficient of restitution and the frames per second of the movement of the bodies.

{{< figure src="QuadTree%20Visualizer/figures/Figure 16 - Control Panel.png" caption="Control Panel" align="center" >}}

---

## YouTube Demonstration

{{< youtube 8un0Qu8ibNk >}}

---

## Future Scope
Since QuadTrees are a type of tree data structure in which each internal node has exactly four children, they are most often used to partition a two-dimensional space by recursively subdividing it into four quadrants or areas. The areas can be rectangular, square, or any other form. The QuadTree is used as a utility as part of the Maps SDK for iOS Utility Library. They’ve also been heavily used in image compression algorithms and higher-level design of 8-bit games like Mario.

Eventually, we believe that QuadTrees can be used for memory management in a big and hierarchical database. It is one of the most crucial places we can use the QuadTree and it can be used to access varied data points and make searching efficient and fast.

Further work in this project can be to let the user visualize their own QuadTree using their own dataset. Users will have to give a dataset for the input and the visualizer will create a QuadTree based on the given dataset.  Additional features could be added here such as the different color and shapes for different data points. Moreover, this project can be implemented as part of bigger projects such as Geolocation, Collision Detection Systems.

---

## Conclusion

We explored a type of tree data structure named QuadTree, that can be used to represent 2-D spaces. In this process, we learnt how/why they are used in a range of applications from scaling up internet services to handle millions of requests per minute to their ever-present use in geolocation-based services like Maps and how we can build applications/libraries to implement the same in our apps/services. It can be concluded QuadTrees are extremely powerful data structures that are still heavily under-utilized in both the industry and community applications. By the time of completion of this project we’ve learned to develop scalable and reusable codebases for large projects, understood the fundamentals of API build and interaction and understood function in a time-bound manner and collaborate at scale across various tasks and disciplines.

---

## Presentation

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; margin-bottom: 20px;">
    <iframe src="QuadTree%20Visualizer/25-04-2022/Final%20Presentation.pdf" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
</div>

---

## Additional Resources

### Project Source, Research & Visualizations
Access the complete source code, full research paper, video demonstrations, and related engineering materials via the repositories below:
<div style="display: flex; flex-direction: column; gap: 10px;">
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/QUADTREE-VISUALIZER" target="_blank">QuadTree Visualizer Project Repository</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/8un0Qu8ibNk" target="_blank">YouTube Demonstration</a>
  </div>
  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://www.researchgate.net/publication/360242672_QuadTree_Visualizer" target="_blank">Full Paper (IJERT)</a>
  </div>
  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://github.com/Amey-Thakur/QUADTREE-VISUALIZER/blob/main/BlackBook/BlackBook-Amey_Mahendra_Thakur-TU3F1819127.pdf" target="_blank">BlackBook (PDF)</a>
  </div>
  <div>
    <!-- Kaggle Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" fill="currentColor" stroke="none" style="vertical-align: middle; margin-right: 8px;">
        <path transform="matrix(.527027 0 0 .527027 -30.632288 -22.45559)"
            d="M105.75 102.968c-.06.238-.298.357-.713.357H97.1c-.477 0-.89-.208-1.248-.625L82.746 86.028l-3.655 3.477v12.93c0 .595-.298.892-.892.892h-6.152c-.595 0-.892-.297-.892-.892V43.5c0-.593.297-.89.892-.89H78.2c.594 0 .892.298.892.89v36.288l15.692-15.87c.416-.415.832-.624 1.248-.624h8.204c.356 0 .593.15.713.445.12.357.09.624-.09.803L88.274 80.588l17.297 21.488c.237.238.297.535.18.892" />
    </svg>
    <a href="https://www.kaggle.com/code/ameythakur20/quadtree" target="_blank">Kaggle Notebook</a>
  </div>
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/QUADTREE-VISUALIZER/tree/main/Source_Code/quadtree-visualizer" target="_blank">Source Code</a>
  </div>
  <div>
    <!-- Graduation Cap Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
    <a href="https://github.com/Amey-Thakur/COMPUTER-ENGINEERING" target="_blank">Computer Engineering Resources</a>
  </div>
</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "QuadTree Visualizer: Spatial Indexing for Collision Detection". AmeyArc (Apr 2022). https://amey-thakur.github.io/posts/2022-04-27-quadtree-visualizer/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2022quadtree,
  title   = "QuadTree Visualizer: Spatial Indexing for Collision Detection",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2022",
  month   = "Apr",
  url     = "https://amey-thakur.github.io/posts/2022-04-27-quadtree-visualizer/"
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
    <span class="reference-text"><a id="ref-1"></a><b>I. Gargantini</b>, “An effective way to represent quadtrees”, <i>Communications of the ACM</i>, vol. 25, no. 12, pp. 905–910, Dec. 1982, DOI: <a href="https://doi.org/10.1145/358728.358741">10.1145/358728.358741</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>Q. Cai and Y. Zhou</b>, “A quadtree-based hierarchical clustering method for visualizing large point dataset”, <i>2016 Sixth International Conference on Information Science and Technology (ICIST)</i>, 2016, pp. 372-375, DOI: <a href="https://doi.org/10.1109/ICIST.2016.7483441">10.1109/ICIST.2016.7483441</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>C. A. Shaffer and H. Samet</b>, “Optimal quadtree construction algorithms”, <i>Computer Vision, Graphics, and Image Processing</i>, vol. 37, no. 3, pp. 402–419, Mar. 1987, DOI: <a href="https://doi.org/10.1016/0734-189X(87)90045-4">10.1016/0734-189X(87)90045-4</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>Gary J. Sullivan and Richard L. Baker</b>, "Efficient quadtree coding of images and video," <i>IEEE Transactions on image processing</i>, vol. 3, no. 3, pp. 327-331, 1994, DOI: <a href="https://doi.org/10.1109/83.287030">10.1109/83.287030</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>Mark de Berg, Marcel Roeloffzen, and Bettina Speckmann</b>, "Kinetic compressed quadtrees in the black-box model with applications to collision detection for low-density scenes," in <i>European Symposium on Algorithms</i>, pp. 383-394, Springer, Berlin, Heidelberg, 2012, DOI: <a href="https://doi.org/10.1007/978-3-642-33090-2_34">10.1007/978-3-642-33090-2_34</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>Praveen K. Sharma and Harish N. Dixit</b>, "Energetics of a bouncing drop: Coefficient of restitution, bubble entrapment, and escape," <i>Physics of Fluids</i>, vol. 32, no. 11, 112107, 2020, DOI: <a href="https://doi.org/10.1063/5.0029484">10.1063/5.0029484</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>Reji Mathew and David S. Taubman</b>, "Quad-tree motion modeling with leaf merging," <i>IEEE Transactions on Circuits and Systems for Video Technology</i>, vol. 20, no. 10, pp. 1331-1345, 2010, DOI: <a href="https://doi.org/10.1109/TCSVT.2010.2077480">10.1109/TCSVT.2010.2077480</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>Stefan Tilkov and Steve Vinoski</b>, "Node.js: Using JavaScript to build high-performance network programs," <i>IEEE Internet Computing</i>, vol. 14, no. 6, pp. 80-83, 2010, DOI: <a href="https://doi.org/10.1109/MIC.2010.145">10.1109/MIC.2010.145</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>Steve Fenton</b>, <i>Pro TypeScript</i>, Apress, 2014, <a href="https://www.apress.com/gp/book/9781484232484">https://www.apress.com/gp/book/9781484232484</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>Mike Cantelon, Marc Harter, T. J. Holowaychuk, and Nathan Rajlich</b>, <i>Node.js in action</i>, Greenwich: Manning, 2014, DOI: <a href="https://dl.acm.org/doi/10.5555/2601501">10.5555/2601501</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>Robin Wieruch</b>, <i>The road to react: Your journey to master plain yet pragmatic react.js</i>, Robin Wieruch, 2017, <a href="https://www.roadtoreact.com">https://www.roadtoreact.com</a> [Accessed: Apr. 27, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>Mohit Thakkar</b>, "Next.js," in <i>Building React Apps with Server-Side Rendering</i>, pp. 93-137, Apress, Berkeley, CA, 2022, DOI: <a href="https://doi.org/10.1007/978-1-4842-5869-9">10.1007/978-1-4842-5869-9</a> [Accessed: Apr. 27, 2022].</span>
</div>

</div>
