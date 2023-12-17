Name:           libarcus
Version:        5.3.0
Release:        %autorelease
Summary:        Communication library between internal components for Ultimaker software
License:        LGPL-3.0-or-later
URL:            https://github.com/Ultimaker/libArcus
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Python bits
Source1:        https://github.com/Ultimaker/pyArcus/archive/%{version}.tar.gz#/pyArcus-%{version}.tar.gz

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2:        FindSIP.cmake
Source3:        SIPMacros.cmake
Source4:        CMakeLists.txt
Source5:        CPackConfig.cmake
Source6:        ArcusConfig.cmake.in
Source7:        COPYING-CMAKE-SCRIPTS

# https://bugzilla.redhat.com/show_bug.cgi?id=1601917
Patch1:         libArcus-3.10.0-PyQt6.sip.patch

# Actually export symbols
Patch2:         libArcus-5.2.2-actually-export-symbols.patch

BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-protobuf
BuildRequires:  python3-pyqt6-sip
BuildRequires:  python3-sip-devel
BuildRequires:  /usr/bin/sip
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core

# we add a dependency on setuptools to provide the distutils module
# upstream already removed the distutils usage in version 5+
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Arcus library contains C++ code and Python 3 bindings for creating a socket in
a thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

%package        devel

# The cmake scripts are BSD
License:        LGPLv3+ and BSD

Summary:        Development files for libarcus
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Arcus library contains C++ code and Python 3 bindings for creating a socket in
a thread and using this socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

Development files.

%package -n     python3-arcus
Summary:        Python 3 libArcus bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}

%description -n python3-arcus
Arcus Python 3 bindings for creating a socket in a thread and using this
socket to send and receive messages based on the
Protocol Buffers library. It is designed to facilitate the communication
between Cura and its backend and similar code.

%prep
%setup -q -n libArcus-%{version} -a 1

cp -a pyArcus-%{version}/python .
cp -a pyArcus-%{version}/include/pyArcus include
mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE7} cmake/
rm -rf CMakeLists.txt
cp -a %{SOURCE4} %{SOURCE5} %{SOURCE6} .
cp -a pyArcus-%{version}/src/PythonMessage.cpp python/

%patch -P1 -p1
%patch -P2 -p1 -b .export

%build
%cmake -DBUILD_EXAMPLES:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libArcus.so.*

%files devel
%license LICENSE cmake/COPYING-CMAKE-SCRIPTS
%{_libdir}/libArcus.so
%{_includedir}/Arcus
# Own the dir not to depend on cmake:
%{_libdir}/cmake

%files -n python3-arcus
%license LICENSE
%doc README.md
%{python3_sitearch}/pyArcus.so

%changelog
%autochangelog
