Name:           udns
Version:        0.7
Release:        %autorelease
Summary:        DNS resolver library for both synchronous and asynchronous DNS queries
License:        LGPL-2.1-or-later
URL:            http://www.corpit.ru/mjt/udns.html
Source:         http://www.corpit.ru/mjt/udns/udns-%{version}.tar.gz

# Provide autoconf-style fake prototype for socket to avoid implicit function declarations.
Patch0: udns-configure-c99.patch

BuildRequires: make
BuildRequires: gcc

%description
udns is a resolver library for C (and C++) programs, and a collection
of useful DNS resolver utilities.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%autosetup -p1

%build
CFLAGS="%{optflags}" ./configure --enable-ipv6
%{__make} %{?_smp_mflags} all sharedlib

%install
%{__install} -Dp -m0755 libudns.so.0 %{buildroot}%{_libdir}/libudns.so.0
%{__ln_s} -f libudns.so.0 %{buildroot}%{_libdir}/libudns.so
%{__install} -Dp -m0755 dnsget %{buildroot}%{_bindir}/dnsget
%{__install} -Dp -m0444 dnsget.1 %{buildroot}%{_mandir}/man1/dnsget.1

%{__install} -Dp -m0444 udns.3 %{buildroot}%{_mandir}/man3/udns.3
%{__install} -Dp -m0644 udns.h %{buildroot}%{_includedir}/udns.h

%files
%doc COPYING.LGPL NEWS NOTES TODO
%doc %{_mandir}/man1/dnsget.1*
%{_bindir}/dnsget
%{_libdir}/libudns.so.*

%files devel
%doc %{_mandir}/man3/udns.3*
%{_includedir}/udns.h
%{_libdir}/libudns.so

%changelog
%autochangelog
