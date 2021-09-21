#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:36:42 2021

@author: tomasic
"""

import numpy as np
import plotly.graph_objects as go

#Triangle
triangle = np.array([[0, 0.5, 1.5], [2, 0.5, 1.5], [1, 1, 1.5]])

#AABB (voxel cell)
box_center = np.array([1,1,1])
box_extents = np.array([0.5,0.5,0.5])
X, Y, Z = 0, 1, 2

#  Moving coordinate system origin to center of AABB
v0 = triangle[0] - box_center
v1 = triangle[1] - box_center
v2 = triangle[2] - box_center

# Edge vectors for triangle
f0 = triangle[1] - triangle[0]
f1 = triangle[2] - triangle[1]
f2 = triangle[0] - triangle[2]

# Collision tests
for l in range (0,1):
                      
    ## Test - 1st category of separating axes
    # Test axis a00
    a00 = np.array([0, -f0[Z], f0[Y]])
    p0 = np.dot(v0, a00)
    p1 = np.dot(v1, a00)
    p2 = np.dot(v2, a00)
    r = box_extents[Y] * abs(f0[Z]) + box_extents[Z] * abs(f0[Y])
    if abs(r)>0 and (max(-max(p0, p1, p2), min(p0, p1, p2))) >= r:
        print(False)
        collision = False
        break
    
    # Test axis a01
    a01 = np.array([0, -f1[Z], f1[Y]])
    p0 = np.dot(v0, a01)
    p1 = np.dot(v1, a01)
    p2 = np.dot(v2, a01)
    r = box_extents[Y] * abs(f1[Z]) + box_extents[Z] * abs(f1[Y])
    if abs(r)>0 and (max(-max(p0, p1, p2), min(p0, p1, p2))) >= r:
        print(False)
        collision = False
        break
    
    # Test axis a02
    a02 = np.array([0, -f2[Z], f2[Y]])
    p0 = np.dot(v0, a02)
    p1 = np.dot(v1, a02)
    p2 = np.dot(v2, a02)
    r = box_extents[Y] * abs(f2[Z]) + box_extents[Z] * abs(f2[Y])
    if abs(r)>0 and (max(-max(p0, p1, p2), min(p0, p1, p2))) >= r:
        print(False)
        collision = False
        break
    
    # Test axis a10
    a10 = np.array([f0[Z], 0, -f0[X]])
    p0 = np.dot(v0, a10)
    p1 = np.dot(v1, a10)
    p2 = np.dot(v2, a10)
    r = box_extents[X] * abs(f0[Z]) + box_extents[Z] * abs(f0[X])
    if abs(r)>0 and (max(-max(p0, p1, p2), min(p0, p1, p2))) >= r:
        print(False)
        collision = False
        break
    
    # Test axis a11
    a11 = np.array([f1[Z], 0, -f1[X]])
    p0 = np.dot(v0, a11)
    p1 = np.dot(v1, a11)
    p2 = np.dot(v2, a11)
    r = box_extents[X] * abs(f1[Z]) + box_extents[Z] * abs(f1[X])
    if abs(r)>0 and (max(-max(p0, p1, p2), min(p0, p1, p2))) >= r:
        print(False)
        collision = False
        break
    
    # Test axis a12
    a12 = np.array([f2[Z], 0, -f2[X]])
    p0 = np.dot(v0, a12)
    p1 = np.dot(v1, a12)
    p2 = np.dot(v2, a12)
    r = box_extents[X] * abs(f2[Z]) + box_extents[Z] * abs(f2[X])
    if abs(r)>0 and (max(-max(p0, p1, p2), min(p0, p1, p2))) >= r:
        print(False)
        collision = False
        break
    
    # Test axis a20
    a20 = np.array([-f0[Y], f0[X], 0])
    p0 = np.dot(v0, a20)
    p1 = np.dot(v1, a20)
    p2 = np.dot(v2, a20)
    r = box_extents[X] * abs(f0[Y]) + box_extents[Y] * abs(f0[X])
    if abs(r)>0 and (max(-max(p0, p1, p2), min(p0, p1, p2))) >= r:
        print(False)
        collision = False
        break
    
    # Test axis a21
    a21 = np.array([-f1[Y], f1[X], 0])
    p0 = np.dot(v0, a21)
    p1 = np.dot(v1, a21)
    p2 = np.dot(v2, a21)
    r = box_extents[X] * abs(f1[Y]) + box_extents[Y] * abs(f1[X])
    if abs(r)>0 and (max(-max(p0, p1, p2), min(p0, p1, p2))) >= r:
        print(False)
        collision = False
        break
    
    # Test axis a22
    a22 = np.array([-f2[Y], f2[X], 0])
    p0 = np.dot(v0, a22)
    p1 = np.dot(v1, a22)
    p2 = np.dot(v2, a22)
    r = box_extents[X] * abs(f2[Y]) + box_extents[Y] * abs(f2[X])
    if abs(r)>0 and (max(-max(p0, p1, p2), min(p0, p1, p2))) >= r:
        print(False)
        collision = False
        break
    
    
    ## Test - 2nd category of separating axes
    # Test axis X
    if max(v0[X], v1[X], v2[X]) <= -box_extents[X] or min(v0[X], v1[X], v2[X]) >= box_extents[X]:
        print(False)
        collision = False
        break
    
    # Test axis Y
    if max(v0[Y], v1[Y], v2[Y]) <= -box_extents[Y] or min(v0[Y], v1[Y], v2[Y]) >= box_extents[Y]:
        print(False)
        collision = False
        break
    
    # Test axis Z
    if max(v0[Z], v1[Z], v2[Z]) <= -box_extents[Z] or min(v0[Z], v1[Z], v2[Z]) >= box_extents[Z]:
        print(False)
        collision = False
        break
    
                      
    ## Test - 3rd category of separating axes
    # Test axis corresponding to triangle face normal
    plane_normal = np.cross(f0, f1)
    plane_distance = np.dot(plane_normal, v0)
    r = box_extents[X] * abs(plane_normal[X]) + box_extents[Y] * abs(plane_normal[Y]) + box_extents[Z] * abs(plane_normal[Z])
    if plane_distance > r:
        print(False)
        collision = False
        break
    

    
    print(True)
    collision = True
    break
    ## End of testing
                      
## Plotting                      
x, y, z = triangle.T

r1 = [box_center[0] - box_extents[0], box_center[0] + box_extents[0]]
r2 = [box_center[1] - box_extents[1], box_center[1] + box_extents[1]]
r3 = [box_center[2] - box_extents[2], box_center[2] + box_extents[2]]

x1=[r1[0], r1[0], r1[1], r1[1], r1[0], r1[0], r1[1], r1[1]]
y1=[r2[0], r2[1], r2[1], r2[0], r2[0], r2[1], r2[1], r2[0]]
z1=[r3[0], r3[0], r3[0], r3[0], r3[1], r3[1], r3[1], r3[1]]

i= [7, 0, 0, 0, 4, 4, 6, 1, 4, 0, 3, 6]
j= [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3]
k= [0, 7, 2, 3, 6, 7, 1, 6, 5, 5, 7, 2]

square3dmesh = go.Mesh3d(x=x1,y=y1,z=z1, i=i, j=j, k=k,color='red', opacity=0.6, name='y')
triangle3dmesh = go.Mesh3d(x=x, y=y, z=z, color='green', opacity=1)

fig = go.Figure(data=[triangle3dmesh, square3dmesh])

#fig.update_layout(title=collision, scene_aspectmode='auto')


fig.show()
