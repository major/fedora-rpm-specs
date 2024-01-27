%global bootstrap 0

Name: mlton
Version: 20210117
Release: 3%{?dist}
Summary: Optimizing compiler for Standard ML

License: MIT
URL: http://mlton.org/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tgz

# Generated sources (non-binary) for bootstrapping.
# See http://mlton.org/PortingMLton#_bootstrap
#Source100: mlton-bootstrap-ppc64le-redhat-linux.tar.gz

BuildRequires: make
BuildRequires: gcc gmp-devel tex(latex)

%if ! 0%{?bootstrap}
BuildRequires: mlton
%endif

Requires: gmp-devel gcc

# Filter out false dependencies.
%global __provides_exclude_from ^(%{_docdir}|%{_libdir}/mlton/sml)/.*$
%global __requires_exclude_from ^(%{_docdir}|%{_libdir}/mlton/sml)/.*$


# Description taken from the Debian package by Stephen Weeks.
%description
MLton is a whole-program optimizing compiler for Standard ML.  MLton
generates standalone executables with excellent runtime performance,
is SML 97 compliant, and has a complete basis library. MLton has
source-level profiling, a fast C FFI, an interface to the GNU
multiprecision library, and lots of useful libraries.


%prep
%autosetup -T -b 0 -p1

# https://fedoraproject.org/wiki/Packaging:Guidelines#Shebang_lines
sed -i -e '1 s;^#! */usr/bin/env *;#!/usr/bin/;' bin/*


%build
%if 0%{?bootstrap}
# Build mlton-compile from the bootstrap sources.
make dirs runtime CFLAGS="$RPM_OPT_FLAGS"

# We need the -O1 here or else RHEL 7 GCC miscompiles the bootstrap source.
for s in mlton/mlton.*.c; do
  gcc $RPM_OPT_FLAGS -O1 -c -Ibuild/lib/mlton/include \
     -Ibuild/lib/mlton/targets/self/include -w "${s}"
done
gcc $RPM_OPT_FLAGS -o build/lib/mlton/mlton-compile \
    -Lbuild/lib/mlton/targets/self \
    -L/usr/local/lib \
    mlton.*.o \
    -lmlton -lgmp -lgdtoa -lm

make basis-no-check script constants libraries tools CFLAGS="$RPM_OPT_FLAGS"

# Install this to a local location and clean. Then continue on with a
# regular build with PATH.
make install PREFIX=$(pwd)/../bootstrap
export PATH=$PATH:$(pwd)/../bootstrap/bin
make clean
%endif

make all docs PREFIX=%{_prefix} libdir=%{_libdir} CFLAGS="$RPM_OPT_FLAGS"


%install
make install-no-strip install-docs PREFIX=%{_prefix} libdir=%{_libdir} \
     docdir=%{_pkgdocdir} DESTDIR=$RPM_BUILD_ROOT

# Remove unnecessary regression test.
rm -rf $RPM_BUILD_ROOT%{_libdir}/mlton/sml/ckit-lib/regression


%files
%doc %{_pkgdocdir}
%license %{_pkgdocdir}/license/*
%{_bindir}/ml*
%{_libdir}/mlton
%{_mandir}/man1/*


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20210117-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20210117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

%autochangelog
