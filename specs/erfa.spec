Name: erfa
Version: 2.0.1
Release: %autorelease
Summary: Essential Routines for Fundamental Astronomy

License: BSD-3-Clause
URL: https://github.com/liberfa/erfa
Source0: https://github.com/liberfa/erfa/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires: meson
BuildRequires: gcc

%description
ERFA is a C library containing key algorithms for astronomy, and is 
based on the SOFA library published by the International Astronomical 
Union (IAU).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup 

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%doc README.rst INFO
%license LICENSE
%{_libdir}/liberfa.so.*

%files devel
%{_libdir}/liberfa.so
%{_includedir}/erfa*.h
%{_libdir}/pkgconfig/erfa.pc

%changelog
%autochangelog
