%global upstream_version        1.0.0-rc7

Name:                   libxchange
Version:                1.0.0~rc7
Release:                %autorelease
Summary:                Structured data representation and JSON support for C/C++
License:                Unlicense
URL:                    https://smithsonian.github.io/xchange
Source0:                https://github.com/Smithsonian/xchange/archive/refs/tags/v%{upstream_version}.tar.gz
BuildRequires:          gcc
BuildRequires:          sed
BuildRequires:          doxygen >= 1.9.0

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
%setup -q -n xchange-%{upstream_version}

%build

make %{?_smp_mflags}

%check

make test

%install

make PACKAGE_NAME=%{name} DESTDIR=%{buildroot} libdir=%{_libdir} install

%files
%license LICENSE
%doc CHANGELOG.md
%{_libdir}/%{name}.so.1{,.*}

%files devel
%doc CONTRIBUTING.md
%{_includedir}/*
%{_libdir}/libxchange.so

%files doc
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/xchange.tag
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/example*.c

%changelog
%autochangelog

