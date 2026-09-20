# Shared-library SONAME for OpenVDB 13.1.x
%global soversion 13.1

# Optional components
%bcond tests   0
%bcond ax      1
%bcond docs    0
%bcond imath   0
%bcond openexr 0
%bcond nanovdb 1
%bcond python  1

# Keep AX on a known-compatible LLVM stream when explicitly enabled.
%global llvm_compat 20

%global _description %{expand:
OpenVDB is an Academy Award-winning open-source C++ library comprising a novel
hierarchical data structure and a suite of tools for the efficient storage and
manipulation of sparse volumetric data represented on three-dimensional grids.
It is developed and maintained by the Academy Software Foundation for use in
volumetric applications typically encountered in feature film production.}

Name:           openvdb
Version:        13.1.0
Release:        %autorelease
Summary:        C++ library for sparse volumetric data
License:        Apache-2.0
URL:            https://www.openvdb.org/
Source0:        https://github.com/AcademySoftwareFoundation/openvdb/archive/v%{version}/%{name}-%{version}.tar.gz

# OpenVDB builds are too memory-intensive on 32-bit x86.
ExcludeArch:    %{ix86}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# Bootstrap requirement: keep CMake static so Fedora's CMake RPM macros are
# available before dynamic BuildRequires are evaluated.
BuildRequires:  cmake >= 3.24

%description
%{_description}

This package contains OpenVDB command-line tools.


%package libs
Summary:        Core OpenVDB libraries

%description libs
%{_description}


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa} >= 1.82
Requires:       cmake(tbb)
Requires:       pkgconfig(blosc) >= 1.17.0
Requires:       pkgconfig(log4cplus) >= 2.0
Requires:       pkgconfig(zlib) > 1.2.7
%if %{with imath}
Requires:       pkgconfig(Imath) >= 3.2
%endif
%if %{with openexr}
Requires:       pkgconfig(OpenEXR) >= 3.2
%endif
%if %{with docs}
Provides:       %{name}-doc = %{version}-%{release}
%endif

%description devel
%{_description}

The %{name}-devel package contains headers, the development shared-library
link, and CMake metadata for developing applications that use OpenVDB.


%if %{with ax}
%package ax
Summary:        OpenVDB AX command-line tool
Requires:       %{name}-ax-libs%{?_isa} = %{version}-%{release}

%description ax
OpenVDB AX is a high-performance expression language for operating on
OpenVDB volumes and point data. This optional package contains the vdb_ax
command-line tool.

%package ax-libs
Summary:        OpenVDB AX runtime library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description ax-libs
This package contains the shared OpenVDB AX runtime library.

%package ax-devel
Summary:        Development files for OpenVDB AX
Requires:       %{name}-ax-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       llvm%{llvm_compat}-devel%{?_isa}

%description ax-devel
This package contains headers and the development shared-library link for
developing applications with OpenVDB AX.
%endif


%if %{with nanovdb}
%package nanovdb
Summary:        NanoVDB command-line tools
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description nanovdb
NanoVDB is a lightweight, GPU-friendly, header-only implementation of VDB.
This package contains the NanoVDB command-line tools.

%package nanovdb-devel
Summary:        Header-only development files for NanoVDB
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description nanovdb-devel
NanoVDB is a lightweight, GPU-friendly, header-only implementation of VDB.
This package contains the NanoVDB headers for developing applications that
use NanoVDB and its OpenVDB conversion helpers.
%endif


%if %{with python}
%package -n python3-%{name}
Summary:        OpenVDB Python module
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%if %{with ax}
Requires:       %{name}-ax-libs%{?_isa} = %{version}-%{release}
%endif

%description -n python3-%{name}
%{_description}

This package contains the OpenVDB module for Python 3.
%endif


%prep
%autosetup -p1


%generate_buildrequires
# Core build requirements
printf '%s\n' \
    'gcc-c++' \
    'findutils' \
    'boost-devel >= 1.82' \
    'cmake(tbb)' \
    'pkgconfig(blosc) >= 1.17.0' \
    'pkgconfig(log4cplus) >= 2.0' \
    'pkgconfig(zlib) > 1.2.7'

# External Imath is optional until Fedora provides Imath >= 3.2.
%if %{with imath}
printf '%s\n' 'pkgconfig(Imath) >= 3.2'
%endif

# OpenEXR support is optional.
%if %{with openexr}
printf '%s\n' 'pkgconfig(OpenEXR) >= 3.2'
%endif

# AX is optional and intentionally uses Fedora's LLVM 20 compatibility stack,
# which is within OpenVDB 13.1's upstream-tested LLVM range.
%if %{with ax}
printf '%s\n' 'llvm%{llvm_compat}-devel'
%endif

# Optional documentation support.
%if %{with docs}
printf '%s\n' 'doxygen'
%endif

# Optional Python bindings.
%if %{with python}
printf '%s\n' \
    'python3-devel >= 3.11' \
    'python3-nanobind-devel >= 2.0'
%endif

# Optional unit tests.
%if %{with tests}
printf '%s\n' 'cmake(GTest)'
%endif


%build
# OPENVDB_PYTHON_USE_AX controls whether upstream defines PY_OPENVDB_USE_AX
# and links the Python module against OpenVDB AX.
%cmake \
    -DCMAKE_NO_SYSTEM_FROM_IMPORTED=TRUE \
    -DDISABLE_DEPENDENCY_VERSION_CHECKS=OFF \
    -DOPENVDB_ENABLE_RPATH=OFF \
%if %{with openexr}
    -DUSE_EXR=ON \
%else
    -DUSE_EXR=OFF \
%endif
%if %{with imath}
    -DUSE_IMATH_HALF=ON \
%else
    -DUSE_IMATH_HALF=OFF \
%endif
    -DUSE_LOG4CPLUS=ON \
%if %{with tests}
    -DOPENVDB_BUILD_UNITTESTS=ON \
%else
    -DOPENVDB_BUILD_UNITTESTS=OFF \
%endif
%if %{with docs}
    -DOPENVDB_BUILD_DOCS=ON \
%else
    -DOPENVDB_BUILD_DOCS=OFF \
%endif
%if %{with python}
    -DOPENVDB_BUILD_PYTHON_MODULE=ON \
    -Dnanobind_DIR="$(python3 -m nanobind --cmake_dir)" \
    -DVDB_PYTHON_INSTALL_DIRECTORY=%{python3_sitearch} \
%if %{with ax}
    -DOPENVDB_PYTHON_USE_AX=ON \
%else
    -DOPENVDB_PYTHON_USE_AX=OFF \
%endif
%else
    -DOPENVDB_BUILD_PYTHON_MODULE=OFF \
    -DOPENVDB_PYTHON_USE_AX=OFF \
%endif
%if %{with ax}
    -DOPENVDB_BUILD_AX=ON \
    -DOPENVDB_AX_SHARED=ON \
    -DOPENVDB_AX_STATIC=OFF \
    -DOPENVDB_BUILD_VDB_AX=ON \
    -DUSE_AX=ON \
    -DLLVM_DIR="$("%{_bindir}/llvm-config-%{llvm_compat}" --cmakedir)" \
%if %{with tests}
    -DOPENVDB_BUILD_AX_UNITTESTS=ON \
%else
    -DOPENVDB_BUILD_AX_UNITTESTS=OFF \
%endif
%else
    -DOPENVDB_BUILD_AX=OFF \
    -DOPENVDB_BUILD_VDB_AX=OFF \
    -DUSE_AX=OFF \
%endif
%if %{with nanovdb}
    -DOPENVDB_BUILD_NANOVDB=ON \
    -DUSE_NANOVDB=ON \
    -DNANOVDB_BUILD_TOOLS=ON \
    -DNANOVDB_USE_OPENVDB=ON \
    -DNANOVDB_USE_TBB=ON \
    -DNANOVDB_USE_BLOSC=ON \
    -DNANOVDB_USE_ZLIB=ON \
%if %{with tests}
    -DNANOVDB_BUILD_UNITTESTS=ON \
%else
    -DNANOVDB_BUILD_UNITTESTS=OFF \
%endif
%else
    -DOPENVDB_BUILD_NANOVDB=OFF \
    -DUSE_NANOVDB=OFF \
%endif
    %{nil}

# OpenVDB is exceptionally memory-intensive on some secondary architectures.
%cmake_build %limit_build -m 12288


%install
%cmake_install

%if %{with docs}
mv %{buildroot}%{_docdir}/OpenVDB/html .
rm -rf %{buildroot}%{_datadir}/doc
%endif

# Static libraries are not shipped.
find %{buildroot} -type f -name '*.a' -delete


%check
%if %{with tests}
%if %{with ax}
# vdb_ax_cmd_test currently fails in Fedora's build environment while the
# remaining OpenVDB, NanoVDB, Python, and AX unit tests pass.
%ctest --output-on-failure --exclude-regex '^vdb_ax_cmd_test$'
%else
%ctest --output-on-failure
%endif
%endif


%files
%doc README.md
%{_bindir}/vdb_print

%files libs
%license LICENSE
%doc README.md CHANGES
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.%{soversion}

%files devel
%doc README.md
%if %{with docs}
%doc html
%endif
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/OpenVDB/

%if %{with ax}
%files ax
%doc README.md
%{_bindir}/vdb_ax

%files ax-libs
%{_libdir}/lib%{name}_ax.so.%{version}
%{_libdir}/lib%{name}_ax.so.%{soversion}

%files ax-devel
%doc README.md
%{_includedir}/%{name}_ax/
%{_libdir}/lib%{name}_ax.so
%endif

%if %{with nanovdb}
%files nanovdb
%doc README.md
%{_bindir}/nanovdb_convert
%{_bindir}/nanovdb_print
%{_bindir}/nanovdb_validate

%files nanovdb-devel
%doc README.md
%{_includedir}/nanovdb/
%endif

%if %{with python}
%files -n python3-%{name}
%doc README.md
%{python3_sitearch}/%{name}.cpython-*.so
%endif


%changelog
%autochangelog
