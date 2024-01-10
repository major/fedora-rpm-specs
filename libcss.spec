Name: libcss
Version: 0.9.2
Release: %autorelease
Summary: A CSS parser and selection engine

License: MIT
URL: http://www.netsurf-browser.org/projects/libcss/
Source: http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz

BuildRequires: gcc
BuildRequires: netsurf-buildsystem
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(libparserutils)
BuildRequires: pkgconfig(libwapcaplet)
BuildRequires: make

%description
LibCSS is a CSS (Cascading Style Sheet) parser and selection engine,
written in C. It was developed as part of the NetSurf project. For
further details, see README.

Features:
* Parses CSS, good and bad
* Simple C API
* Low memory usage
* Fast selection engine
* Portable

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%global make_vars COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"

%prep
%autosetup -n %{name}-%{version} -p1

sed -i -e s@-Werror@@ Makefile

%build
make %{?_smp_mflags} %{make_vars} %{build_vars}

%install
make install DESTDIR=%{buildroot} %{make_vars}

%check
make %{?_smp_mflags} test %{make_vars} %{build_vars}

%files
%doc README
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%doc docs/*
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
