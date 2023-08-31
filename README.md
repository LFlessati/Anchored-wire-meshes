# Anchored-wire-meshes

## Introduction
This code is the implementation of the meta-model introduced in Boschi et al. (2023) for analysing the response of anchored wire meshes, commonly adopted to stabilize potentially unstable soil slopes. 
This model was conceived on the basis of the results of a series of 3D large displacement finite element (FE) numerical analyses, in which the wire mesh mechanical behaviour is modelled as either an elastic or an elastic-plastic membrane (Boschi et al., 2020; 2021). The proposed model predictions was also validated on experimental punching test results. 
The use of the model, only requires the definition of geometry and soil-wire mesh mechanical properties. It allows the pre-design of the reinforcement system without performing any ad-hoc finite element numerical analyses, e.g. to preliminarily choose the geometry of the reinforcing interventions (above all spacing) and the required wire mesh mechanical properties. Indeed, such a tool is suitable for being employed by both producers to optimize the use of their products and designers to reduce the costs of interventions and to increase the sustainability of the retaining system. 

## Model description
The definition and training of the meta-model followed a procedure similar to that used in to machine learning. The only difference is that the functions used to define the model were chosen by critically analysing and mechanically interpreting the local soil-wire mesh interaction processes, detected thanks to the performed FE numerical simulations. The meta-model therefore is not a mere interpolation of the results but it is an interpretative model. 
The followed approach is inspired to the macro-element (ME) theory, commonly employed to analyse different soil-structure interaction problems, and stems from the idea of reproducing a complex system mechanical response via a low number of degrees of freedom and by defining a suitable incremental generalized/upscaled constitutive relationship between the static (in this case soil-retaining system interaction force $F$ and resultant wire mesh tensile force $T$) and kinematic (normal component of the far-field displacement $u$) variables associated with the chosen degrees of freedom. In this sense, the ME approach is an upscaling procedure analogous to the ones commonly adopted in structural engineering. 
The derived differential equations are integrated by using an explicit scheme: stability of the numerical scheme depends on the number of steps.
This ME model is conceived for isotropic wire meshes but, by using average stiffness and strength values, also anisotropic wire meshes can be considered. The wire mesh fragile failure is not accounted for but this is not a severe limitation of the model since in practical applications even the yielding of the mesh, developing before its failure, is not acceptable. The calculation tool refers to horizontal ground surfaces, but ad-hoc numerical results highlighted that the influence of slope inclination plays a minor role. Plate deformability is not accounted for but a simplified approach to analyse its response is suggested in Boschi et al. (2023). 

## Input parameters
The model use requires the definition of 10 input data concerning geometry, basic soil mechanical properties and wire mesh stiffness/strenght and an input variable ($u$), without requiring neither additional FE numerical analyses nor model calibration.
The input parameters are named as it followed in the provided Python code:
1. $B$ [m] plate width
2. $S$ [m] plate spacing
3. $E$ [kPa] soil Young modulus
4. $nu$ [-] soil Poisson’s ratio
5. $c$ [kPa] soil cohesion
6. $phi$ [rad] soil friction angle
7. $psi$ [rad] soil dilatancy angle
8. $gam$ [kN/m$^3$] soil unit weight
9. $J$ [kN/m] wire mesh tensile stiffness
10. $ty$ [kN/m] wire mesh tensile strenght


## References

Boschi, K., di Prisco, C., Flessati, L. (2023). An innovative design approach for anchored wire meshes. Acta Geotechnica. 

Boschi, K., di Prisco, C., Flessati, L., & Mazzon, N. (2021). Numerical Analysis of the Mechanical Response of Anchored Wire Meshes. In International Conference of the International Association for Computer Methods and Advances in Geomechanics, pp. 779-785. Springer, Cham. https://doi.org/10.1007/978-3-030-64518-2_92 

Boschi, K., di Prisco, C., Flessati, L., Galli, A. & Tomasin, M. (2020), Punching Tests on Deformable Facing Structures: Numerical Analyses and Mechanical Interpretation. Lecture Notes in Civil Engineering 40, pp 429-437. https://doi.org/10.1007/978-3-030-21359-6_45
