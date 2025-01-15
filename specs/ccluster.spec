Name:           ccluster
Version:        1.1.7
Release:        %autorelease
Summary:        Cluster the roots of a univariate polynomial

License:        LGPL-2.1-or-later
URL:            https://github.com/rimbach/Ccluster
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix use of XOR where exponentiation was intended
Patch:          https://github.com/rimbach/Ccluster/pull/74.patch
# Prevent multiple definition errors when linking
Patch:          https://github.com/rimbach/Ccluster/pull/75.patch
# Adapt to flint 3.x
Patch:          %{name}-flint3.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  flint-devel
BuildRequires:  gcc
BuildRequires:  make

%description
Ccluster is a C library implementing an algorithm for local clustering
of the complex roots of a univariate polynomial whose coefficients are
complex numbers.

The inputs of the clustering algorithm are a polynomial P, a square
complex box B and a rational number eps.

It outputs a set of eps-natural clusters of roots together with the sum
of multiplicities of the roots in each cluster.  An eps-cluster is a
complex disc D of radius at most eps containing at least one root, and
it is natural when 3D contains the same roots as D.  Each root of P in B
is in exactly one cluster of the output, and clusters may contain roots
of P in 2B.

The implemented algorithm is described here:
https://dl.acm.org/citation.cfm?id=2930939.

Please cite https://link.springer.com/chapter/10.1007/978-3-319-96418-8_28
if you use it in your research.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       flint-devel%{?_isa}

%description    devel
This package contains header files and library links for developing
applications that use %{name}.

%prep
%autosetup -n Ccluster-%{version} -p1

%conf
# Install in the right place on 64-bit platforms
if [ "%{_lib}" != lib ]; then
  sed -i 's,^\(LIBDIR=\)lib,\1%{_lib},' Makefile.in
fi

%build
CFLAGS='%{build_cflags} -I%{_includedir}/flint'
CXXFLAGS='%{build_cxxflags} -I%{_includedir}/flint'
# Use Fedora link flags and add an soname
major=$(echo %{version} | cut -d. -f1)
sed -i "s|-shared|& %{build_ldflags} -Wl,-h,libccluster.so.${major}|" Makefile.in
# This is NOT an autoconf-generated configure script; do not use %%configure
./configure --prefix=%{_prefix} --disable-static
%make_build library bins AT= QUIET_CC= QUIET_AR=

%install
%make_install

%check
PATH=$PATH:$PWD/test
%make_build testMignotte testMandelbrot

%files
%doc README.md README
%license LICENSE
%{_libdir}/libccluster.so.1*

%files devel
%{_includedir}/ccluster/
%{_libdir}/libccluster.so

%changelog
%autochangelog
