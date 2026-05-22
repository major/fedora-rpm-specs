%global sover 1.5
# skip solvertest due to unstable behavior for that architecture
%global ctest_extra_args -E solvertest

Name:       orocos-kdl
Version:    1.5.3
Release:    %autorelease
Summary:    A framework for modeling and computation of kinematic chains
ExcludeArch: %{ix86}

License:    LGPL-2.0-or-later
URL:        http://www.orocos.org/kdl.html
Source0:    https://github.com/orocos/orocos_kinematics_dynamics/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:     0-cmake-eigen3.patch

BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  python3-psutil

Requires:   eigen3

%description
The Kinematics and Dynamics Library (KDL) develops an application independent 
framework for modeling and computation of kinematic chains, such as robots, 
bio-mechanical human models, computer-animated figures, machine tools, etc. 
It provides class libraries for geometrical objects (point, frame, line,... ), 
kinematic chains of various families (serial, humanoid, parallel, mobile,... ),
and their motion specification and interpolation.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation for %{name}.

%package     -n python%{python3_pkgversion}-pykdl
Summary:        Python module for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pybind11
%{?python_provide:%python_provide python%{python3_pkgversion}-pykdl}

%description -n python%{python3_pkgversion}-pykdl
The python%{python3_pkgversion}-pykdl package contains the Python module
for %{name}.


%prep
%autosetup -p 1 -n orocos_kinematics_dynamics-%{version}


%build
pushd orocos_kdl
%cmake \
  -DENABLE_TESTS:BOOL=ON
%cmake_build
%cmake_build --target docs
# remove doxygen tag file, it is faulty and we do not need it
rm %{_vpath_builddir}/doc/kdl.tag

popd

pushd python_orocos_kdl
mkdir -p %{_vpath_builddir}/include/kdl
cp -a ../orocos_kdl/src/* %{_vpath_builddir}/include/kdl
cp -a ../orocos_kdl/%{_vpath_builddir}/src/* %{_vpath_builddir}/include/kdl
ln -s ../../../orocos_kdl/src %{_vpath_builddir}/include/kdl
CXXFLAGS="${CXXFLAGS:-%optflags} -Iinclude" \
  %cmake \
  -DPYTHON_SITE_PACKAGES_INSTALL_DIR=%{python3_sitearch} \
  -DPYTHON_VERSION=3
%cmake_build
popd

%install
pushd orocos_kdl
%cmake_install
popd

pushd python_orocos_kdl
%cmake_install
popd


%check
pushd orocos_kdl
%ctest -- --test-dir %{_vpath_builddir}/tests %{ctest_extra_args}
popd

pushd python_orocos_kdl
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
%{py3_test_envvars} %{python3} tests/PyKDLtest.py
popd


%files
%doc README.md
%license orocos_kdl/COPYING
%{_libdir}/liborocos-kdl.so.%{sover}
%{_libdir}/liborocos-kdl.so.%{version}

%files devel
%{_includedir}/kdl/
%{_libdir}/liborocos-kdl.so
%{_libdir}/pkgconfig/orocos-kdl.pc
%{_libdir}/pkgconfig/orocos_kdl.pc
%{_datadir}/orocos_kdl/

%files doc
%doc orocos_kdl/%{_vpath_builddir}/doc/api/html

%files -n python%{python3_pkgversion}-pykdl

%ifarch ppc64le
    %{python3_sitearch}/PyKDL.cpython-%{python3_version_nodots}-powerpc64le-linux-gnu.so
%else
    %{python3_sitearch}/PyKDL.cpython-%{python3_version_nodots}-%{_arch}-linux-gnu.so
%endif

%changelog
%autochangelog
