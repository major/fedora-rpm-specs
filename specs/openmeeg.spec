# rhbz#2104109
%bcond_with vtk
#

%bcond_without python
%bcond_without hdf5
%bcond_without matio
%bcond_with cgal
%bcond_without doc
%bcond_without check

%bcond_without debug

# This package fails its testsuite with LTO.  Disable LTO for now
%define _lto_cflags %{nil}

## https://github.com/openmeeg/openmeeg/issues/346
ExcludeArch: s390x

#%%global relsuf rc4

Name:    openmeeg
Version: 2.5.15
Release: %autorelease
Summary: Low-frequency bio-electromagnetism solving forward problems in the field of EEG and MEG
License: CeCILL-B
URL:     http://openmeeg.github.io/
Source0: https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:  %{name}-use_builtin_find_blas_lapack.patch
Patch1:  %{name}-fix-cmake4.patch

# Remove newer cmake_policy
Patch2:  %{name}-fix_compatibility_cmake330.patch

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnuplot
BuildRequires: graphviz
BuildRequires: expat-devel
BuildRequires: flexiblas-devel
%{?fedora:BuildRequires: gifticlib-devel}
%{?fedora:BuildRequires: nifticlib-devel}
BuildRequires: zlib-devel
%if %{with hdf5}
BuildRequires: hdf5-devel
%endif
%if %{with matio}
BuildRequires: matio-devel
%endif
%if %{with vtk}
BuildRequires: vtk-devel
%endif
%if %{with cgal}
BuildRequires: CGAL-devel
%endif

# CGAL causes 'memory exhausted' error
%global openmeeg_cmake_options \\\
%if %{with debug} \
        -DCMAKE_BUILD_TYPE=Debug \\\
        -DCMAKE_CXX_FLAGS_DEBUG:STRING="-O0 -g -fPIC" \\\
%else \
        -DCMAKE_BUILD_TYPE=Release \\\
        -DCMAKE_CXX_FLAGS_DEBUG:STRING="%{build_cxxflags}" \\\
%endif \
        -DUSE_PROGRESSBAR=ON \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_OpenMEEG:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_matio:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_zlib:BOOL=ON \\\
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \\\
        -DCMAKE_SKIP_RPATH:BOOL=YES \\\
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \\\
        -DCMAKE_INSTALL_INCLUDEDIR:PATH=include/%{name} \\\
        -DUSE_OMP:BOOL=ON \\\
%if %{with python} \
        -DENABLE_PYTHON:BOOL=ON \\\
        -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \\\
        -DPYTHON_VERSION:STRING=%{python3_version} \\\
        -DPYTHON_INSTALL_RELATIVE:BOOL=OFF \\\
%endif \
%if %{with doc} \
        -DBUILD_DOCUMENTATION:BOOL=ON \\\
%endif \
%if %{with check} \
        -DBUILD_TESTING:BOOL=ON \\\
        -DTEST_HEAD3:BOOL=OFF \\\
%endif \
        -DBUILD_TOOLS:BOOL=ON \\\
        -DENABLE_PACKAGING:BOOL=OFF \\\
        -DSKIP_GITHUB_TESTS:BOOL=ON \\\
%if %{with cgal} \
        -DUSE_CGAL:BOOL=ON \\\
%endif \
        %{?fedora:-DUSE_GIFTI:BOOL=ON} \\\
%if %{with hdf5} \
        -DUSE_SYSTEM_hdf5:BOOL=ON \\\
%endif \
%if %{with matio} \
        -DUSE_SYSTEM_matio:BOOL=ON \\\
%endif \
%if %{with vtk} \
        -DUSE_VTK:BOOL=ON \\\
%endif \
        -DUSE_SYSTEM_zlib:BOOL=ON \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -Wno-dev

%description
The OpenMEEG software is a C++ package for solving the forward
problems of electroencephalography (EEG) and magnetoencephalography (MEG).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use OpenMEEG.

%if %{with python}
%package        -n python3-openmeeg
Summary:        OpenMEEG binding for Python3
%py_provides    python3-%{name}
%py_provides    python3-OpenMEEG

BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:  swig
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       swig
%description    -n python3-openmeeg
OpenMEEG binding for Python3.
%endif

%if %{with doc}
%package        doc
Summary:        Documentation files for OpenMEEG
BuildRequires:  doxygen
BuildArch:      noarch
%description    doc
%{summary}.
%endif

%prep
%autosetup -N -n %{name}-%{version}

%if 0%{?fedora} < 42
%patch -P 2 -p1 -b .backup
%endif

%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .backup

%build
%if %{with debug}
export CXXFLAGS="-O0 -g -fPIC"
export CFLAGS="-O0 -g -fPIC"
%endif

# Force setuptools_scm to set dynamic version of Python OpenMEEG
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%cmake %{openmeeg_cmake_options}
%cmake_build

%install
%cmake_install

%if %{with check}
%check
export FLEXIBLAS=netlib
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export PYTHONPATH=%{buildroot}%{python3_sitearch}/%{name}
%if %{with debug}
export OPENMEEG_DATA_PATH=%{_builddir}/%{name}-%{version}/data
ctest --test-dir %_vpath_builddir -VV --force-new-ctest-process -j1 --output-on-failure --debug -E 'openmeeg_python_test_python2.py|OpenMEEGMathsTest-full|CM2-Head1'
%else
export OPENMEEG_DATA_PATH=%{_builddir}/%{name}-%{version}/data
%ctest -E 'openmeeg_python_test_python2.py|OpenMEEGMathsTest-full|CM2-Head1'
%endif
%endif

%files
%license LICENSE.txt
%{_bindir}/om*
%{_libdir}/libOpenMEEG*.so.1
%{_libdir}/libOpenMEEG*.so.1.1.0

%files devel
%doc coding_guidelines.txt
%{_libdir}/libOpenMEEG*.so
%{_includedir}/%{name}/

%if %{with python}
%files -n python3-openmeeg
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}.dist-info/
%endif

%if %{with doc}
%files doc
%license LICENSE.txt
%{_docdir}/OpenMEEG/
%endif

%changelog
%autochangelog
