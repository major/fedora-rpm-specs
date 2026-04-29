%global upstream_version        1.1.2

Name:            libxchange
Version:         1.1.2
Release:         %autorelease
Summary:         Structured data representation and JSON support for C/C++
License:         Unlicense
URL:             https://sigmyne.github.io/xchange
Source0:         https://github.com/Sigmyne/xchange/archive/refs/tags/v%{upstream_version}.tar.gz
BuildRequires:   gcc
BuildRequires:   cmake
BuildRequires:   sed
BuildRequires:   doxygen >= 1.13.0
Patch0:          install-examples.patch

%description

The xchange library provides a free framework for structured data 
representation in C/C++ (C99 or later), and includes JSON parsing and 
emitting functions. It is free to use, in any way you like, without 
licensing restrictions.

%package devel
Summary:                C development files for the xchange C/C++ library
Requires:               %{name}%{_isa} = %{version}-%{release}

%description devel
This sub-package provides C headers and non-versioned shared library symbolic 
links for the xchange C/C++ library.

%package doc
Summary:                Documentation for the xchange C/C++ library
BuildArch:              noarch

%description doc
This package provides HTML documentation and examples for the xchange C/C++ 
library. The HTML API documentation can also be used with the Eclipse IDE.

%prep
%autosetup -p1 -n xchange-%{upstream_version}

%build

%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_DOC=ON

%cmake_build

%install

%cmake_install

# Rename documentation directory to package name
mv %{buildroot}/%{_docdir}/xchange %{buildroot}/%{_docdir}/%{name}

%check

%ctest

%files
%license LICENSE
%doc CHANGELOG.md
%{_libdir}/libxchange.so.1{,.*}

%files devel
%{_includedir}/xchange.h
%{_includedir}/xjson.h
%{_libdir}/libxchange.so
%{_libdir}/cmake
%{_libdir}/pkgconfig
%doc %{_docdir}/%{name}/*.md
%doc %{_docdir}/%{name}/examples

%files doc
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/xchange.tag
%doc %{_docdir}/%{name}/html

%changelog
%autochangelog

