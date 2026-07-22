%global _configure ../configure

Name:		lis
Version:	2.1.11
Release:	%autorelease
Summary:	A library for solving linear equations and eigenvalue problems
License:	BSD-3-Clause
URL:		http://www.ssisc.org/lis/index.en.html
Source0:	http://www.ssisc.org/lis/dl/lis-%{version}.zip
ExcludeArch:	%{ix86}
BuildRequires:	autoconf
BuildRequires:	chrpath
BuildRequires:	gcc
BuildRequires:	gcc-gfortran
BuildRequires:	make

%description
Lis, a Library of Iterative Solvers for linear systems, is a scalable parallel
library for solving systems of linear equations and standard eigenvalue
problems with real sparse matrices using iterative methods.

%package bin
Summary:	lis executables

%description bin
This package contains binaries shipped with the lis library.

%package devel
Summary:	Development headers and library for lis
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Lis, a Library of Iterative Solvers for linear systems, is a scalable parallel
library for solving systems of linear equations and standard eigenvalue
problems with real sparse matrices using iterative methods.

This package contains the development headers and library.

%package doc
Summary:	Developer documentation for lis
BuildArch:  noarch

%description doc
Lis, a Library of Iterative Solvers for linear systems, is a scalable parallel
library for solving systems of linear equations and standard eigenvalue
problems with real sparse matrices using iterative methods.

This package contains the developer documentation for lis.

%prep
%autosetup

%build
export CFLAGS="${CFLAGS} -std=gnu17"
export CC=gcc
autoconf --force

mkdir -p omp
pushd omp
%configure --disable-static --enable-shared \
    --enable-saamg \
    --enable-quad --disable-rpath
%make_build
popd

%install
%make_install -C omp

# Get rid of RPATHs
# https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath
chrpath --delete %{buildroot}%{_bindir}/*

# Get rid of .la file
find %{buildroot} -name "*.la" -delete

# .. and examples
rm -rf %{buildroot}%{_datadir}/examples

%files
%doc AUTHORS
%license COPYING
%{_libdir}/liblis.so.*

%files bin
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/*.h
%{_libdir}/liblis.so

%files doc
%doc doc/*.pdf
%license COPYING
%{_mandir}/man3/lis*.3*

%changelog
%autochangelog
