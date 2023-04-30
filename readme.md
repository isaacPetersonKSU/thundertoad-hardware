# thundertoad hardware
This repo contains hardware designs related to
[thundertoad](https://github.com/ksu-cs-projects-2022-2023/spring2023-isaacPetersonKSU),
a climate-control and data-logging system for small-scale mushroom growing. All
models are built in [freeCAD](https://www.freecad.org/). 

Submodules are used so that the SBCs thundertoad runs on can clone the main
repo without being burdened with storing bulky CAD files. 

# exporting files
When changes are made to freecad files, export.sh should be invoked. This will
invoke freecad's cli to export all cad files as STL models in /stl.


# under construction: view models

```stl
solid Mesh
  facet normal 0.999689 0.024931 -0.000000
    outer loop
      vertex 48.607750 0.000000 0.000000
      vertex 48.547325 2.422896 0.000000
      vertex 48.607750 0.000000 10.000000
    endloop
  endfacet
  facet normal 0.999689 0.024931 0.000000
    outer loop
      vertex 48.607750 0.000000 10.000000
      vertex 48.547325 2.422896 0.000000
      vertex 48.547325 2.422896 10.000000
    endloop
  endfacet
  facet normal 0.997204 0.074729 0.000000
    outer loop
      vertex 48.547325 2.422896 10.000000
      vertex 48.366207 4.839769 0.000000
      vertex 48.366207 4.839769 10.000000
    endloop
  endfacet
  facet normal 0.992239 0.124343 0.000000
    outer loop
      vertex 48.366207 4.839769 10.000000
      vertex 48.366207 4.839769 0.000000
      vertex 48.064842 7.244609 10.000000
    endloop
  endfacet
  facet normal 0.997204 0.074729 -0.000000
    outer loop
      vertex 48.547325 2.422896 0.000000
      vertex 48.366207 4.839769 0.000000
      vertex 48.547325 2.422896 10.000000
    endloop
  endfacet
  facet normal 0.992239 0.124343 0.000000
    outer loop
      vertex 48.366207 4.839769 0.000000
      vertex 48.064842 7.244609 0.000000
      vertex 48.064842 7.244609 10.000000
    endloop
  endfacet
  facet normal 0.984808 0.173649 0.000000
    outer loop
      vertex 48.064842 7.244609 10.000000
      vertex 47.643978 9.631438 0.000000
      vertex 47.643978 9.631438 10.000000
    endloop
  endfacet
  facet normal 0.974928 0.222520 0.000000
    outer loop
      vertex 47.643978 9.631438 10.000000
      vertex 47.643978 9.631438 0.000000
      vertex 47.104668 11.994322 10.000000
    endloop
  endfacet
  facet normal 0.984808 0.173649 -0.000000
    outer loop
      vertex 48.064842 7.244609 0.000000
      vertex 47.643978 9.631438 0.000000
      vertex 48.064842 7.244609 10.000000
    endloop
  endfacet
  facet normal 0.974928 0.222520 0.000000
    outer loop
      vertex 47.643978 9.631438 0.000000
      vertex 47.104668 11.994322 0.000000
      vertex 47.104668 11.994322 10.000000
    endloop
  endfacet
  facet normal 0.962624 0.270842 0.000000
    outer loop
      vertex 47.104668 11.994322 10.000000
      vertex 46.448242 14.327386 0.000000
      vertex 46.448242 14.327386 10.000000
    endloop
  endfacet
  facet normal 0.962624 0.270842 -0.000000
    outer loop
      vertex 47.104668 11.994322 0.000000
      vertex 46.448242 14.327386 0.000000
      vertex 47.104668 11.994322 10.000000
    endloop
  endfacet
  facet normal 0.947928 0.318485 0.000000
    outer loop
      vertex 46.448242 14.327386 10.000000
      vertex 45.676346 16.624830 0.000000
      vertex 45.676346 16.624830 10.000000
    endloop
  endfacet
  facet normal 0.930874 0.365342 0.000000
    outer loop
      vertex 45.676346 16.624830 10.000000
      vertex 45.676346 16.624830 0.000000
      vertex 44.790886 18.880941 10.000000
    endloop
  endfacet
endsolid Mesh
```
