Name:           robotraconteur
Version:        1.2.8
Release:        1%{?dist}
Summary:        Robot Raconteur is a communication framework for Robotics and Automation

License:        Apache-2.0
URL:            https://github.com/robotraconteur/robotraconteur
Source0:        %{url}/releases/download/v%{version}/RobotRaconteur-%{version}-Source.tar.gz
Source1:        %{url}/releases/download/v%{version}/robotraconteur.rpmlintrc
Patch0:         https://patch-diff.githubusercontent.com/raw/robotraconteur/robotraconteur/pull/456.patch
Patch1:         https://patch-diff.githubusercontent.com/raw/robotraconteur/robotraconteur/pull/458.patch
Patch2:         https://patch-diff.githubusercontent.com/raw/robotraconteur/robotraconteur/pull/470.patch
ExcludeArch:    s390x

%global rpmlintrc %{SOURCE1}

BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  dbus-devel
BuildRequires:  openssl-devel
BuildRequires:  libusb1-devel
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  gtest-devel
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  swig
BuildRequires:  fdupes
# Documentation
BuildRequires:  doxygen
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-tabs)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  texinfo

%description
Robot Raconteur is a communication framework for Robotics and Automation.

%package -n librobotraconteurcore1
Summary:        Robot Raconteur runtime library

%description -n librobotraconteurcore1
This package provides the run-time library of Robot Raconteur.

%package -n librobotraconteur-devel
Summary:        Robot Raconteur development files
Requires:       librobotraconteurcore1%{?_isa} = %{version}-%{release}
Requires:       robotraconteurgen%{?_isa} = %{version}-%{release}
Requires:       boost-devel

%description -n librobotraconteur-devel
This package provides development files for Robot Raconteur.

%package -n python3-robotraconteur
Summary:        Robot Raconteur Python 3 module
Requires:       librobotraconteurcore1%{?_isa} = %{version}-%{release}
Requires:       python3-numpy
Requires:       python3

%description -n python3-robotraconteur
Robot Raconteur Python module. Use with python 3.

%package -n robotraconteurgen
Summary:        Robot Raconteur code generator tool
Requires:       librobotraconteurcore1%{?_isa} = %{version}-%{release}

%description -n robotraconteurgen
This package provides the Robot Raconteur code generator tool.

%package -n librobotraconteur-devel-doc
Summary: Documentation for the Robot Raconteur
BuildArch: noarch

%description -n librobotraconteur-devel-doc
Documentation for the Robot Raconteur Core C++ Library and Getting Started Guide

%package -n python3-robotraconteur-doc
Summary: Documentation for the Robot Raconteur Python Core Library
BuildArch: noarch

%description -n python3-robotraconteur-doc
Documentation for the Robot Raconteur Python Core Library

%prep
%autosetup -n RobotRaconteur-%{version}-Source -p1

%build
%cmake \
   -DBUILD_GEN=ON \
   -DBUILD_PYTHON=OFF \
   -DBUILD_PYTHON3=ON \
   -DUSE_PREGENERATED_SOURCE=OFF \
   -DPYTHON3_EXECUTABLE=%{__python3} \
   -DINSTALL_PYTHON3_PIP=ON \
   -DBUILD_DOCUMENTATION=ON \
   -DBUILD_SHARED_LIBS=ON \
   -DROBOTRACONTEURCORE_SOVERSION_MAJOR_ONLY=ON \
   -DROBOTRACONTEUR_SKIP_RPATH=ON \
   -DROBOTRACONTEUR_TESTING_DISABLE_DISCOVERY_LOOPBACK=ON \
   -DCMAKE_GTEST_DISCOVER_TESTS_DISCOVERY_MODE=PRE_TEST \
   -DBUILD_TESTING=ON \
   -DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON \
   -DINSTALL_PYTHON3_PIP_EXTRA_ARGS="--compile --no-build-isolation \
      --no-deps --root-user-action=ignore"

export LD_LIBRARY_PATH=%{_builddir}/%{?buildsubdir}/%{_vpath_builddir}/out/lib:$LD_LIBRARY_PATH
%cmake_build
%cmake_build --target RobotRaconteurCore_doc
%cmake_build --target RobotRaconteurPython3_doc
%cmake_build --target RobotRaconteurGettingStarted_doc

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/librobotraconteur-devel-doc
cp -a %{_vpath_builddir}/docs/cpp %{buildroot}%{_docdir}/librobotraconteur-devel-doc/
cp -a %{_vpath_builddir}/docs/getting_started %{buildroot}%{_docdir}/librobotraconteur-devel-doc/

mkdir -p %{buildroot}%{_docdir}/python3-robotraconteur-doc
cp -a %{_vpath_builddir}/docs/python3 %{buildroot}%{_docdir}/python3-robotraconteur-doc/

find %{buildroot}%{_docdir} -name ".buildinfo" -delete
find %{buildroot}%{_docdir} -name ".doctrees" -type d -exec rm -rf {} +

%fdupes %{buildroot}%{_docdir}

%check
%ctest -j1

# Move files to match Fedora packaging guidelines if needed

%files -n librobotraconteurcore1
%license LICENSE.txt
%{_libdir}/libRobotRaconteurCore.so.1{,.*}

%files -n librobotraconteur-devel
%license LICENSE.txt
%{_includedir}/RobotRaconteur.h
%{_includedir}/RobotRaconteur/
%{_libdir}/libRobotRaconteurCore.so
%{_libdir}/cmake/RobotRaconteur

%files -n python3-robotraconteur
%license LICENSE.txt
%doc RobotRaconteurPython/README.md
%{python3_sitearch}/RobotRaconteur/
%{python3_sitearch}/robotraconteur-*.dist-info/

%files -n robotraconteurgen
%license LICENSE.txt
%{_bindir}/RobotRaconteurGen
%{_mandir}/man1/robotraconteurgen.1*

%files -n librobotraconteur-devel-doc
%license LICENSE.txt
%{_docdir}/librobotraconteur-devel-doc/

%files -n python3-robotraconteur-doc
%license LICENSE.txt
%{_docdir}/python3-robotraconteur-doc/

%changelog
* Fri May 22 2026 John Wason <wason@wasontech.com> - 1.2.8-1
- Update to upstream version 1.2.8

* Thu Dec 18 2025 John Wason <wason@wasontech.com> - 1.2.7-1
- Update to upstream version 1.2.7

* Sun Aug 31 2025 John Wason <wason@wasontech.com> - 1.2.6-1
- Test RPM Build
