# Feature toggles: Python bindings disabled by default
# until fixed upstream
%bcond  python 0
# Export is faulty on s390x due to bugs in assimp
%bcond  export 0
%global soversion 3
%global forgeurl https://github.com/elalish/manifold
%global pypiname manifold3d

Version:        3.3.2
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
Source0:        %{forgesource}
# Use cmake build for Python package
# https://github.com/elalish/manifold/pull/1432
Source1:        setup.py
Source2:        pyproject.toml

# Build dependencies
# Manifold requires static files
BuildRequires:  polyclipping2-static
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openvdb-devel >= 11
%if %{with export}
BuildRequires:  pkgconfig(assimp)
%endif
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  python3-devel
%if %{with python}
BuildRequires:  python3-nanobind-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
# Tests
BuildRequires:  python3-pytest
BuildRequires:  python3-trimesh
%endif
# Documentation
BuildRequires:  doxygen
# Remove rpath
BuildRequires:  chrpath

# Only 64 bit architectures
ExcludeArch:    i686

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
Requires:       %{name}%{?_isa}=%{version}-%{release}
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

# Is there a way to use shared nanobind library? Changing
# NB_STATIC to NB_SHARED seems to build a
# Ensure have debuginfo
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
  -DMANIFOLD_DOWNLOADS=OFF \
  -DMANIFOLD_EXPORT=%{?with_export:ON}%{!?with_export:OFF} \
  -DMANIFOLD_OPTIMIZED=ON \
  -DMANIFOLD_PAR=ON \
  -DMANIFOLD_PYBIND=%{?with_python:ON}%{!?with_python:OFF} \
  -DMANIFOLD_STRICT=OFF
%cmake_build
doxygen

%if %{with python}
cp LICENSE %{_vpath_builddir}/bindings/python/
cp README.md %{_vpath_builddir}/bindings/python/
pushd %{_vpath_builddir}
pushd bindings
pushd python
cp %{SOURCE1} .
cp %{SOURCE2} .
chrpath --delete manifold3d*.so
%pyproject_wheel
popd
popd
%endif

%install
%cmake_install

find docs/docbook/ -type f -exec install -pDm0644 "{}" \
  "%{buildroot}%{_datadir}/help/en/%{name}/{}" \;

%if %{with python}
pushd %{_vpath_builddir}
pushd bindings
pushd python
%pyproject_install
popd
popd
popd
%endif

%check
# Test for s390x architecture fails if DMANIFOLD_EXPORT=ON
# due to bugs in dependency assimp, check if can enable when
# updating
# https://github.com/elalish/manifold/issues/1335
%ctest --test-dir %{_vpath_builddir}

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
%files -n python3-manifold3d
%{python3_sitearch}/manifold3d.pyi
%{python3_sitearch}/manifold3d*.so
%{python3_sitearch}/manifold3d-%{version}.dist-info/
%endif


%files doc
%license LICENSE
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/%{name}

%changelog
%autochangelog
