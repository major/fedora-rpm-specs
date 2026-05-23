# Enable OpenMP multithreading? Upstream default is no.
%bcond openmp 1
# Support elliptic curve L-functions with PARI? Upstream default is no.
%bcond pari 1

# Use high-precision arithmetic? Upstream default is double.
# Options: double, double-double, quad-double, multiple.
# - OpenMP doesn’t work with double-double or quad-double precision
#   https://gitlab.com/sagemath/lcalc/-/work_items/13
# - Multiple precision would require the bundled “MPFR C++” (mpreal),
#   src/libLfunction/mpreal.h, which we should package separately if we
#   actually use it. As a header-only library, it would also add its license to
#   the licenses of the binary RPMs (“AND GPL-3.0-or-later”).
%global precision double

Name:           lcalc
Version:        2.2.1
%global so_version 2
Release:        %autorelease
# @PACKAGE_DESCRIPTION@, from configure.ac
Summary:        Command-line utility and library for L-function computations

# The entire source is GPL-2.0-or-later, except that src/libLfunction/mpreal.h,
# a bundled copy of “MPFR C++” (mpreal) removed in %%prep, is GPL-3.0-or-later.
License:        GPL-2.0-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later
URL:            https://gitlab.com/sagemath/lcalc
VCS:            git:%{url}.git
Source:         %{url}/-/archive/%{version}/lcalc-%{version}.tar.bz2

# Address GCC “may be used uninitialized” warnings
# https://gitlab.com/sagemath/lcalc/-/merge_requests/9
Patch:          %{url}/-/merge_requests/9.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  make

%if %{with pari}
BuildRequires:  pari-devel
%endif
%if "%{precision}" == "double-double" || "%{precision}" == "quad-double"
BuildRequires:  qd-devel
%endif

Requires:       libLfunction%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

# Renamed from L-function in Fedora 45. Since we have a Provides for the old
# name, and people may still depend on it, we keep the upgrade path
# indefinitely. We also provide an upgrade path for L-function-devel.
Provides:       L-function = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      L-function < 2.0.5-15

%description
%{summary}.


%package -n libLfunction
Summary:        C++ library for working with L-functions

%description -n libLfunction
%{summary}.


%package -n libLfunction-devel
Summary:        Headers and libraries for development with libLfunction

Requires:       libLfunction%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Provides:       L-function-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      L-function-devel < 2.0.5-15

%description -n libLfunction-devel
%{summary}.


%package -n libLfunction-doc
Summary:        Documentation and examples for libLfunction

BuildArch:      noarch

%description -n libLfunction-doc
%{summary}.


%prep
%autosetup -p1

# Remove a bundled copy “MPFR C++” (mpreal), which would be used only in a
# multiple-precision build.
rm src/libLfunction/mpreal.h


%conf
autoreconf --force --install --verbose

%configure \
    --with-pari=%{?with_pari:yes}%{?!with_pari:no} \
    --enable-openmp=%{?with_openmp:yes}%{?!with_openmp:no} \
    --enable-precision=%{precision}

# Get rid of undesirable hardcoded rpaths; work around libtool reordering
# -Wl,--as-needed after all the libraries.
sed --regexp-extended --in-place \
    --expression 's/^(hardcode_libdir_flag_spec=).*/\1""/g' \
    --expression 's/^(runpath_var=)LD_RUN_PATH/\1DIE_RPATH_DIE/g' \
    --expression 's/(CC="g..)"/\1 -Wl,--as-needed"/' \
    libtool


%build
%make_build


%install
%make_install

# We don’t want the entire contents of doc/; we package particular
# documentation files selectively.
rm --recursive --verbose '%{buildroot}%{_docdir}/lcalc'


%check
%make_build check

%if %{with pari}
# Suggested in: add tests for using pari and for openmp
# https://gitlab.com/sagemath/lcalc/-/work_items/19
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' PATH='%{buildroot}%{_bindir}' \
    lcalc -e --a1=0 --a2=0 --a3=1 --a4=-79 --a6=342 --rank-verify=5 \
    > _output.txt
expected=''
[ "$(cat _output.txt)" = "${expected}" ]
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' PATH='%{buildroot}%{_bindir}' \
    lcalc -e --a1=0 --a2=0 --a3=1 --a4=-79 --a6=342 --rank-verify=4 \
    > _output.txt
expected='given rank 4 is different than computed analytic rank 5'
[ "$(cat _output.txt)" = "${expected}" ]
%endif


%files
%{_bindir}/lcalc
%{_mandir}/man1/lcalc.1*


%files -n libLfunction
%license doc/COPYING
%doc README.md
%{_libdir}/libLfunction.so.%{so_version}{,.*}


%files -n libLfunction-devel
%{_includedir}/lcalc/
%{_libdir}/libLfunction.so
%{_libdir}/pkgconfig/lcalc.pc


%files -n libLfunction-doc
%license doc/COPYING
%doc README.md
%doc doc/ChangeLog
%doc doc/CONTRIBUTORS
%doc doc/examples/


%changelog
%autochangelog
