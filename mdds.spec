# header-only library
%global debug_package %{nil}

%global apiversion 2.1

Name: mdds
Version: 2.1.1
Release: %autorelease
Summary: A collection of multi-dimensional data structures and indexing algorithms

License: MIT
URL: https://gitlab.com/mdds/mdds
Source0: http://kohei.us/files/%{name}/src/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: autoconf

%description
%{name} is a collection of multi-dimensional data structures and
indexing algorithms.

%package devel
Summary: Headers for %{name}
BuildArch: noarch
Requires: boost-devel
Provides: %{name}-static = %{version}-%{release}

%description devel
%{name} is a collection of multi-dimensional data structures and
indexing algorithms.
 
It implements the following data structures:
* segment tree
* flat segment tree 
* rectangle set
* point quad tree
* multi type matrix
* multi type vector

See README.md for a brief description of the structures.

%prep
%autosetup -p1

%build
autoconf
%configure

%install
%make_install
rm -rf %{buildroot}%{_docdir}/%{name}

%check
make check %{?_smp_mflags}

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_datadir}/pkgconfig/%{name}-%{apiversion}.pc
%doc AUTHORS README.md
%license LICENSE

%changelog
%autochangelog
