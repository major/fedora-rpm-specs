# asio only ships headers, so no debuginfo package is needed
%global debug_package %{nil}

Name:           asio
Version:        1.28.1
Release:        %autorelease
Summary:        A cross-platform C++ library for network programming

License:        BSL-1.0
URL:            https://think-async.com
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-generators

%description
The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%package devel
Summary:        Header files for asio
Recommends:     openssl-devel
Recommends:     boost-devel

%description devel
Header files you can use to develop applications with asio.

The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%prep
%autosetup

%build
autoreconf --install
%configure
%make_build

%install
%make_install

%files devel
%doc doc/*
%license LICENSE_1_0.txt
%{_includedir}/asio/
%{_includedir}/asio.hpp
%{_libdir}/pkgconfig/asio.pc

%changelog
%autochangelog
