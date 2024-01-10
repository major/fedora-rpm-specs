Name: libhubbub
Version: 0.3.8
Release: %autorelease
Summary: An HTML5 compliant parsing library

License: MIT
URL: http://www.netsurf-browser.org/projects/hubbub/
Source: http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz

BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gperf
BuildRequires: netsurf-buildsystem
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libparserutils)
BuildRequires: make

%description
Hubbub is an HTML5 compliant parsing library, written in C. It was
developed as part of the NetSurf project.

The HTML5 specification defines a parsing algorithm, based on the
behavior of mainstream browsers, which provides instructions for how to
parse all markup, both valid and invalid. As a result, Hubbub parses web
content well.

Features:
* Parses HTML, good and bad
* Simple C API
* Fast
* Character encoding detection
* Well-tested (~90% test coverage)
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

%global make_vars COMPONENT_TYPE=lib-shared PREFIX=/usr LIBDIR=%{_lib} Q=
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
%{_includedir}/hubbub
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license COPYING
%doc docs/Architecture docs/Macros docs/Todo docs/Treebuilder docs/Updated
%doc docs/html

%changelog
%autochangelog
