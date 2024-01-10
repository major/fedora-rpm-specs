Name: libparserutils
Version: 0.2.5
Release: %autorelease
Summary: A library for building efficient parsers

License: MIT
URL: http://www.netsurf-browser.org/projects/libparserutils/
Source: http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz

BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: netsurf-buildsystem
BuildRequires: pkgconfig(check)
BuildRequires: make

%description
LibParserUtils is a library for building efficient parsers, written in
C. It was developed as part of the NetSurf project.

Features:
* No mandatory dependencies (iconv() implementation optional for
  enhanced charset support)
* A number of built-in character set converters
* Mapping of character set names to/from MIB enum values
* UTF-8 and UTF-16 (host endian) support functions
* Various simple data structures (resizeable buffer, stack, vector)
* A UTF-8 input stream
* Simple C API
* Portable

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%global make_vars COMPONENT_TYPE=lib-shared PREFIX=/usr LIBDIR=%{_lib} DOXYCONF=build/Doxyfile Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"

%prep
%autosetup -n %{name}-%{version} -p1

sed -i -e s@-Werror@@ Makefile

%build
make %{?_smp_mflags} %{make_vars} %{build_vars}
make %{?_smp_mflags} docs %{make_vars}

%install
make install DESTDIR=%{buildroot} %{make_vars}

%check
make %{?_smp_mflags} test %{make_vars} %{build_vars}

%files
%doc README
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/parserutils
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license COPYING
%doc build/docs/html

%changelog
%autochangelog
