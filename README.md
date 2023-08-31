# Anchored-wire-meshes

## Introduction
This code is the implementation of the meta-model introduced in Boschi et al. (2023) for analysing the response of anchored wire meshes, commonly adopted to stabilize potentially unstable soil slopes and employed either as active or a passive anchoring systems. 
This model was conceived on the basis of the results of a series of 3D large displacement finite element numerical analyses, in which the wire mesh mechanical behaviour is modelled as either an elastic or an elastic-plastic membrane (Boschi et al., 2020; 2021). It is inspired to standard load-displacement curves for shallow foundations and the wire mesh presence is taken into account by suitably modifying the bearing capacity formula. The proposed model predictions was also validated thanks to the comparison with experimental punching test results. 
The use of the model, only requiring the definition of geometry and soil-wire mesh mechanical properties, allows the pre-design of the reinforcement system without performing ad-hoc finite element numerical analyses. 

## Model assumptions


## Input parameters
The input parameters refers to the geometry and soil/wire mesh mechanical properties. 
The input parameters are named as it followed in the provided Python code:





The differential equations are integrated by using an explicit scheme: stability of the numerical scheme depends on the number of steps.





## References

Boschi, K., di Prisco, C., Flessati, L. (2023). An innovative design approach for anchored wire meshes. Acta Geotechnica. 

Boschi, K., di Prisco, C., Flessati, L., & Mazzon, N. (2021). Numerical Analysis of the Mechanical Response of Anchored Wire Meshes. In International Conference of the International Association for Computer Methods and Advances in Geomechanics, pp. 779-785. Springer, Cham. https://doi.org/10.1007/978-3-030-64518-2_92 

Boschi, K., di Prisco, C., Flessati, L., Galli, A. & Tomasin, M. (2020), Punching Tests on Deformable Facing Structures: Numerical Analyses and Mechanical Interpretation. Lecture Notes in Civil Engineering 40, pp 429-437. https://doi.org/10.1007/978-3-030-21359-6_45 
