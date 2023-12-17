Name:           libsavitar
Version:        5.3.0
Release:        %autorelease
Summary:        C++ implementation of 3mf loading with SIP Python bindings
License:        LGPL-3.0-or-later
URL:            https://github.com/Ultimaker/libSavitar
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Python bits
Source1:        https://github.com/Ultimaker/pySavitar/archive/%{version}.tar.gz#/pySavitar-%{version}.tar.gz

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2:        FindSIP.cmake
Source3:        SIPMacros.cmake
Source4:        CMakeLists.txt
Source5:        SavitarConfig.cmake.in
Source6:        COPYING-CMAKE-SCRIPTS

# Actually export symbols into the shared lib
Patch0:         libsavitar-5.2.2-export-fix.patch

BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pugixml-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sip-devel
BuildRequires:  /usr/bin/sip

# we add a dependency on setuptools to provide the distutils module for FindSIP.cmake
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

%package        devel
Summary:        Development files for libsavitar
Requires:       %{name}%{?_isa} = %{version}-%{release}
# The cmake scripts are BSD
License:        LGPL-3.0-or-later AND BSD-3-Clause

%description    devel
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

Development files.

%package -n     python3-savitar
Summary:        Python 3 libSavitar bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-savitar
Savitar is a C++ implementation of 3mf loading with SIP Python bindings.
3mf is a 3D printing file format.

The Python bindings.

%prep
%autosetup -n libSavitar-%{version} -p1 -S git -a 1

cp -a pySavitar-%{version}/python .
mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE6} cmake/
rm -rf CMakeLists.txt
cp -a %{SOURCE4} %{SOURCE5} .

# Wrong end of line encoding
dos2unix README.md

%build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libSavitar.so.*

%files devel
%license LICENSE cmake/COPYING-CMAKE-SCRIPTS
%{_libdir}/libSavitar.so
%{_includedir}/Savitar
# Own the dir not to depend on cmake:
%{_libdir}/cmake

%files -n python3-savitar
%license LICENSE
%doc README.md
%{python3_sitearch}/pySavitar.so

%changelog
%autochangelog
