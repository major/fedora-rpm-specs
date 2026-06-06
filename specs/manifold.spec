%global _without_python 1
%bcond  python 1
%bcond  export 1
%global soversion 3
%global forgeurl https://github.com/elalish/manifold
%global pypiname manifold3d

Version:        3.5.1
%forgemeta
Name:           manifold
Release:        %autorelease
Summary:        Geometry library for topological robustness

# svd.h is under MIT license
# https://github.com/elalish/manifold/blob/master/src/svd.h
# disjoint_sets.h is under Zlib license
# https://github.com/elalish/manifold/blob/master/src/disjoint_sets.h
License:        Apache-2.0 AND MIT AND Zlib
URL:            %{forgeurl}
Source:         %{forgesource}

# Build dependencies
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openvdb-devel >= 11
%if %{with export}
BuildRequires:  pkgconfig(assimp)
%endif
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  polyclipping2-devel
%if %{with python}
BuildRequires:  chrpath
## Tests
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist trimesh}
%endif
# Documentation
BuildRequires:  doxygen
# Remove rpath

# Only 64 bit architectures
ExcludeArch:    %{ix86}

%description
Manifold provides robust operations on watertight triangle meshes
with guaranteed manifold output. Features include parallelized algorithms,
support for arbitrary vertex attributes, and material mapping
for rendering applications.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}, including headers, CMake config,
and pkg-config files.

%if %{with python}
%package -n python3-%{pypiname}
Summary:        Python bindings for %{name}
# The manifold C++ sources are Apache-2.0 AND MIT AND Zlib (see the main
# License field), and we assume that all of these may contribute to the Python
# extension. The Python extension also uses nanobind (python-nanobind), and is
# compiled in part from sources distributed as data inside the nanobind Python
# package. These sources are licensed BSD-3-Clause. The use of nanobind also
# brings in an indirect dependency on the header-only robin-map library, which
# is licensed MIT.
License:        Apache-2.0 AND BSD-3-Clause MIT AND Zlib
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       robin-map-static
Provides:       bundled(libnanobind)

%description -n python3-%{pypiname}
Python interface for %{name} geometry library
%endif

%package doc
Summary:      Documentation for %{name}
%description doc
Docbook documentation for %{name}.

%prep
%forgeautosetup

# Nanobind can only be built statically from sources shipped in its Python
# package; see https://github.com/wjakob/nanobind/issues/1042.
sed -i "s|NB_STATIC|NB_STATIC NOSTRIP|" \
    bindings/python/CMakeLists.txt

# Switch Doxygen to DocBook output
sed -i "s|GENERATE_HTML          = YES|GENERATE_HTML          = NO|" \
   Doxyfile
sed -i "s|GENERATE_DOCBOOK       = NO|GENERATE_DOCBOOK       = YES|" \
   Doxyfile

%if %{with python}
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_SKIP_BUILD_RPATH=ON \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DMANIFOLD_CBIND=ON \
  -DMANIFOLD_CROSS_SECTION=ON \
  -DMANIFOLD_DOWNLOADS=OFF \
  -DMANIFOLD_EXPORT=%{?with_export:ON}%{!?with_export:OFF} \
  -DMANIFOLD_OPTIMIZED=ON \
  -DMANIFOLD_PAR=ON \
  -DMANIFOLD_PYBIND=%{?with_python:ON}%{!?with_python:OFF} \
  -DMANIFOLD_STRICT=OFF
%cmake_build
doxygen

%if %{with python}
%pyproject_wheel
%endif

%install
%cmake_install

find docs/docbook/ -type f -exec install -pDm0644 "{}" \
  "%{buildroot}%{_datadir}/help/en/%{name}/{}" \;

%if %{with python}
%pyproject_install
%pyproject_save_files -L manifold3d
# TODO: Can we prevent this rpath rather than removing it after the fact?
chrpath --delete %{buildroot}%{python3_sitearch}/manifold3d*.so
%endif

%check
# Exclude some failed tests
%ctest --test-dir %{_vpath_builddir} -E "BooleanComplex.InterpolatedNormals|Boolean.Normals|Manifold.GetNormalLegacyContract"

%if %{with python}
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{py3_test_envvars} %{python3} bindings/python/examples/run_all.py -e
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{pytest}
%endif

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libmanifold.so.%{soversion}*
%{_libdir}/libmanifoldc.so.%{soversion}*

%files devel
%doc README.md CONTRIBUTING.md
%{_includedir}/%{name}/
%{_libdir}/libmanifold.so
%{_libdir}/libmanifoldc.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%if %{with python}
%files -n python3-manifold3d -f %{pyproject_files}
%license LICENSE
# bindings/python/README.md is only for developers, not library users
%doc README.md
%endif

%files doc
%license LICENSE
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/%{name}

%changelog
%autochangelog
