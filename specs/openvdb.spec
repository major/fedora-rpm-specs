# Use soversion
%global soversion 11.0

# Set to 1 to enable testsuite. Fails everywhere with GCC 8+.
%bcond tests 0

# Optional supports
%bcond openexr 1
%bcond ax      0
%bcond nanovdb 0
%bcond python  %{?fedora}
%bcond imath   %{?fedora} || %{?rhel} >= 9
%bcond docs    0

# ax currently incompatible with newer llvm versions
%global llvm_compat 15

%global _description %{expand:
OpenVDB is an Academy Award-winning open-source C++ library comprising a novel
hierarchical data structure and a suite of tools for the efficient storage and
manipulation of sparse volumetric data discretized on three-dimensional grids.
It is developed and maintained by Academy Software Foundation for use in
volumetric applications typically encountered in feature film production.}

Name:           openvdb
Version:        11.0.0
Release:        %autorelease
Summary:        C++ library for sparse volumetric data discretized on three-dimensional grids
License:        MPL-2.0
URL:            https://www.openvdb.org/

Source0:        https://github.com/AcademySoftwareFoundation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# OpenVDB no longer builds on 32bits with latest TBB due to OOM.
ExcludeArch:    %{ix86}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  boost-devel >= 1.61
# boost-python3-devel merged in boost-devel for Fedora 33+
# https://src.fedoraproject.org/rpms/boost/c/1f2e448e099a867f9da62b9da009d3dec5e1ad64?branch=master
%if 0%{?rhel}
BuildRequires:  boost-python3-devel
%endif
BuildRequires:  cmake >= 2.8
%if %{with docs}
BuildRequires:  doxygen >= 1.8.11
%endif
#BuildRequires:  epydoc
BuildRequires:  gcc-c++
BuildRequires:  ghostscript >= 8.70
BuildRequires:  findutils
BuildRequires:  sed
BuildRequires:  libstdc++-devel
%if %{with ax}
BuildRequires:  llvm%{?llvm_compat}-devel
BuildRequires:	pkgconfig(libffi)
%endif
BuildRequires:  pkgconfig(blosc) >= 1.5.0
BuildRequires:  pkgconfig(cppunit) >= 1.10
# RHEL and CentOS only have that build requirement for x86_64
%if 0%{?rhel}
%ifarch x86_64
BuildRequires:  glfw-devel >= 2.7
%endif
%else
BuildRequires:  pkgconfig(glfw3) >= 2.7
%endif
%if %{with imath}
BuildRequires:  pkgconfig(Imath)
%endif
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(log4cplus) >= 1.0
BuildRequires:  cmake(pybind11)
%if %{with openexr}
BuildRequires:  pkgconfig(OpenEXR) >= 3.0
%endif
# Requires v2020.3 in adherence to VFX Reference Platform guideline
# https://vfxplatform.com/
BuildRequires:  cmake(tbb) = 2020.3
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(zlib) > 1.2.7

%description    %{_description}

This package contains some graphical tools.

%package        libs
Summary:        Core OpenVDB libraries

%description    libs %{_description}

%package        devel
Summary:        Development files for %{name}
%if %{with docs}
BuildRequires:  texlive-latex
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# Requires v2020.3 in adherence to VFX Reference Platform guideline
# https://vfxplatform.com/
Requires:       cmake(tbb) >= 2020.3
Requires:       pkgconfig(zlib) > 1.2.7
Obsoletes:      %{name}-doc < 6.1.0-1
%if %{with docs}
Provides:       %{name}-doc = %{version}-%{release}
%endif

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%if %{with python}
%package        -n python3-%{name}
Summary:        OpenVDB Python module
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-python3 < 6.2.0
Obsoletes:      %{name}-python2 < 5.1.0-1
Provides:       %{name}-python2 = %{version}-%{release}

%description    -n python3-%{name} %{_description}

This package contains the Python module.
%endif


%prep
%autosetup -p1

# Hardcoded values
sed -i \
    -e 's|lib$|%{_lib}|g' \
    %{name}/%{name}/CMakeLists.txt %{name}/%{name}/python/CMakeLists.txt


%build
%ifarch ppc64le
%undefine _smp_mflags
%endif 
export CXXFLAGS="%{build_cxxflags} -Wl,--as-needed"

# Ignore versions (python 3, etc.)
# Set ABI version to address blender compatibility for
# Fedora 40 and onward
%cmake \
    -DCMAKE_NO_SYSTEM_FROM_IMPORTED=TRUE \
    -DDISABLE_DEPENDENCY_VERSION_CHECKS=ON \
%if %{with docs}
    -DOPENVDB_BUILD_DOCS=ON \
%endif
%if %{with python}
    -DOPENVDB_BUILD_PYTHON_MODULE=ON \
%endif
%if 0%{?rhel}
    -DCONCURRENT_MALLOC=None \
%endif
    -DOPENVDB_BUILD_UNITTESTS=OFF \
    -DOPENVDB_ENABLE_RPATH=OFF \
    -DPYOPENVDB_INSTALL_DIRECTORY=%{python3_sitearch} \
%if %{with ax}
    -DHAVE_FFI_CALL=ON \
    -DUSE_AX=ON \
    -DLLVM_STATIC=0 \
    -DLLVM_CONFIG=$(which llvm-config%{?llvm_compat:-%{llvm_compat}}) \
    -DLLVM=%{_bindir} \
%endif
%if %{with openexr}
    -DUSE_EXR=ON \
%endif
%if %{with nanovdb}
    -DUSE_NANOVDB=ON \
    -DNANOVDB_USE_OPENVDB=ON \
%endif
%if %{with imath}
    -DUSE_IMATH_HALF=ON \
%endif
    %{nil}
# Increase memory reserve to 12GB per build thread for a successful build on
# ppc64le and s390x.
%cmake_build %limit_build -m 12288

%if %{with tests}
%check
%ctest test
%endif

%install
%cmake_install

%if %{with docs}
# Let RPM pick up html documents in the files section
mv %{buildroot}%{_docdir}/OpenVDB/html .
rm -fr %{buildroot}%{_datadir}/doc
%endif

find %{buildroot} -name '*.a' -delete

%files
%{_bindir}/vdb_print
%if %{with nanovdb}
%{_bindir}/nanovdb_{convert,print,validate}
%endif

%files libs
%license LICENSE
%doc README.md CHANGES
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.%{soversion}

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/py%{name}.cpython-*.so
%endif

%files devel
%if %{with docs}
%doc html
%endif
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/OpenVDB/

%changelog
%autochangelog
