%global libversion 4.0

Name:       urdfdom
Version:    4.0.2
Release:    3%{?dist}
Summary:    U-Robot Description Format Document Object Model

License:    BSD-3-Clause
URL:        http://ros.org/wiki/urdf
Source0:    https://github.com/ros/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  console-bridge-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  tinyxml2-devel
BuildRequires:  urdfdom-headers-static

%description
The URDF (U-Robot Description Format) library
provides core data structures and a simple XML parser
for populating the class data structures from an URDF file

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   tinyxml2-devel
Requires:   urdfdom-headers-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_bindir}/urdf_mem_test


%files
%license LICENSE
%{_bindir}/*
%{_libdir}/*.so.%{libversion}
%{_datadir}/%{name}

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}
%{_includedir}/%{name}

%changelog
%autochangelog
