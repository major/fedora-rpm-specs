%global soversion 0

Name:           mstore
Version:        0.3.0
Release:        %autorelease
Summary:        Molecular structure store for testing
License:        Apache-2.0
URL:            https://github.com/grimme-lab/mstore
Source0:        https://github.com/grimme-lab/mstore/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-gfortran
BuildRequires:  cmake(mctc-lib)

%description
Molecular structure store for testing

%package devel
Summary:       Development headers for mstore
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for mstore.

%prep
%autosetup

%conf
# TODO: Account for absolute path CMAKE_INSTALL_INCLUDEDIR so we can use %%{_fmoddir}
%cmake \
  -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_lib}/gfortran/modules \
  -Dmstore-module-dir:STRING=mstore

%build
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libmstore.so.%{soversion}{,.*}
%{_bindir}/mstore-info
%{_bindir}/mstore-fortranize

%files devel
%{_libdir}/libmstore.so
%{_fmoddir}/mstore/
%{_libdir}/cmake/mstore/
%{_libdir}/pkgconfig/mstore.pc

%changelog
%autochangelog
