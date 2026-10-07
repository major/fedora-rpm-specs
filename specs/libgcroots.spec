Name:		libgcroots
Version:	0.3.4
Release:	%autorelease
License:	Boehm-GC
URL:		https://github.com/uim/libgcroots

Source0:	https://github.com/uim/libgcroots/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	gcc-c++
BuildRequires: make

Summary:	Roots acquisition library for Garbage Collector

%description
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.
This library encourages to have own GC such as for small-footprint,
some application-specific optimizations, just learning or to test
experimental ideas.

%package devel
Summary:	Development files for libgcroots
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.

This package contains a header file and development library to help you
to develop any own GC.

%prep
%autosetup -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Remove unnecessary files
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc README
%license COPYING
%{_libdir}/libgcroots.so.0*

%files devel
%doc README
%license COPYING
%{_includedir}/gcroots.h
%{_libdir}/libgcroots.so
%{_libdir}/pkgconfig/gcroots.pc

%changelog
%autochangelog
