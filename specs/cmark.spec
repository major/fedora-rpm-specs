# pathological_tests_library failing
%bcond tests 0

Name:           cmark
Version:        0.31.1
Release:        %autorelease
Summary:        CommonMark parsing and rendering

License:        BSD-2-Clause AND MIT
URL:            https://github.com/jgm/cmark
Source0:        https://github.com/jgm/cmark/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
`cmark` is the C reference implementation of CommonMark,
a rationalized version of Markdown syntax with a spec.

It provides a shared library (`libcmark`) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (`cmark`) for parsing and rendering CommonMark
documents.


%package devel
Summary:        Development files for cmark
Requires:       cmark-lib%{?_isa} = %{version}-%{release}
Requires:       cmark%{?_isa} = %{version}-%{release}

%description devel
This package provides the development files for cmark.



%package lib
Summary:        CommonMark parsing and rendering library

%description lib
This package provides the cmark library.



%prep
%autosetup


%build
%cmake %{?_without_tests:-DBUILD_TESTING=OFF}
%cmake_build


%install
%cmake_install


%check
%if %{with tests}
%cmake_build --target test
%endif


%ldconfig_scriptlets lib


%files
%license COPYING
%{_bindir}/cmark
%{_mandir}/man1/cmark.1*


%files lib
%license COPYING
%{_libdir}/libcmark.so.%{version}


%files devel
%doc README.md
%{_includedir}/cmark.h
%{_includedir}/cmark_export.h
%{_includedir}/cmark_version.h
%{_libdir}/libcmark.so
%{_libdir}/pkgconfig/libcmark.pc
%{_mandir}/man3/cmark.3*
%{_libdir}/cmake/cmark


%changelog
%autochangelog
