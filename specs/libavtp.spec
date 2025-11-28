Name:		libavtp
Version:	0.2.0
Release:	%autorelease
Summary:	An AVTP protocol implementation

License:	BSD-3-Clause
URL:		https://github.com/Avnu/libavtp
Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	libcmocka-devel
BuildRequires:	meson

%description
An open source implementation of Audio Video Transport
Protocol (AVTP) specified in IEEE 1722-2016 spec.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%{_libdir}/libavtp.so.*

%files devel
%doc CONTRIBUTING.md HACKING.md
%{_includedir}/avtp*
%{_libdir}/libavtp.so
%{_libdir}/pkgconfig/avtp.pc


%changelog
%autochangelog
