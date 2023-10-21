%bcond bundled_thread_pool 0

Name:           libfplll
Version:        5.4.5
%global so_version 8
Release:        %autorelease
Summary:        Lattice algorithms using floating-point arithmetic

# The entire source is LGPL-2.1-or-later, except:
#
#   - The contents of fplll/enum-parallel/ are MIT
#
# The header-only libraries are unbundled; since header-only libraries are
# treated as static libraries, their licenses still contribute to the licenses
# of the binary RPMs
#   - cr-marcstevens-snippets-thread_pool-static is MIT; it replaces
#     fplll/io/thread_pool.hpp
#   - json-static is is MIT AND CC0-1.0 (the latter because it includes
#     Hedley); it replaces fplll/io/json.hpp
#
# Additionally, a number of autoconf build system sources, which do not
# contribute to the binary RPM license because they are neither installed nor
# linked into any installed file, are under various other permissible licenses:
#
#   - INSTALL, {,fplll/,tests/}Makefile.in, aclocal.m4, compile, config.guess,
#     config.sub, configure, depcomp, install-sh, ltmain.sh, missing,
#     test-driver, */Makefile.in, m4/*.m4
License:        LGPL-2.1-or-later AND MIT AND CC0-1.0
URL:            https://fplll.github.io/fplll/
Source0:        https://github.com/fplll/fplll/releases/download/%{version}/fplll-%{version}.tar.gz
# Man pages hand-written for Fedora in groff_man(7) format based on --help
# output and README.md:
Source1:        fplll.1
Source2:        latticegen.1

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(qd)
# BR on *-static required for tracking header-only libraries
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  json-static

# The contents of fplll/enum-parallel/ are based on, but heavily modified from,
# https://github.com/cr-marcstevens/fplll-extenum. We do not treat this as a
# bundled dependency because the separate fplll-extenum library was integrated
# into fplll and is no longer separately developed.

%if %{without bundled_thread_pool}
BuildRequires:  cr-marcstevens-snippets-thread_pool-devel
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  cr-marcstevens-snippets-thread_pool-static
%else
# The file fplll/io/thread_pool.hpp is a copy of cxxheaderonly/thread_pool.hpp
# from commit e01ae885cdbef3af265341110a434f6fa7b8e8ac (or, equivalently, a
# number of earlier commits that did not modify that file) of
# https://github.com/cr-marcstevens/snippets/.
Provides:       bundled(cr-marcstevens-snippets-thread_pool-devel) = 0^20210722gite01ae88
%endif

%description
fplll contains implementations of several lattice algorithms. The
implementation relies on floating-point orthogonalization, and LLL is central
to the code, hence the name.

It includes implementations of floating-point LLL reduction algorithms,
offering different speed/guarantees ratios. It contains a 'wrapper' choosing
the estimated best sequence of variants in order to provide a guaranteed output
as fast as possible. In the case of the wrapper, the succession of variants is
oblivious to the user.

It includes an implementation of the BKZ reduction algorithm, including the
BKZ-2.0 improvements (extreme enumeration pruning, pre-processing of blocks,
early termination). Additionally, Slide reduction and self dual BKZ are
supported.

It also includes a floating-point implementation of the Kannan-Fincke-Pohst
algorithm that finds a shortest non-zero lattice vector. Finally, it contains a
variant of the enumeration algorithm that computes a lattice vector closest to
a given vector belonging to the real span of the lattice.


%package        devel
Summary:        Development files for libfplll

Requires:       libfplll%{?_isa} = %{version}-%{release}
Requires:       qd-devel%{?_isa}

%if %{without bundled_thread_pool}
# We unbundled this; the API header now references the system copy of the
# header, so dependent packages need it installed. (Technically, they should
# also explicitly BR the -static package, since they are indirectly using the
# header-only library.)
Requires:       cr-marcstevens-snippets-thread_pool-devel
Requires:       cr-marcstevens-snippets-thread_pool-static
%endif

%description    devel
The libfplll-devel package contains libraries and header files for
developing applications that use libfplll.


# The static library is required by Macaulay2. See its spec file for a full
# explanation; the essential justification is excerpted below:
#
#   We have to use the static version of the libfplll and givaro library. They
#   have global objects whose constructors run before GC is initialized. If we
#   allow the shared libraries to be unloaded, which happens as a normal part
#   of Macaulay2's functioning, then GC tries to free objects it did not
#   allocate, which leads to a segfault.
%package        static
Summary:        Static library for libfplll

Requires:       libfplll-devel%{?_isa} = %{version}-%{release}

%description    static
The libfplll-static package contains a static library for libfplll.


%package        tools
Summary:        Command line tools that use libfplll

Requires:       libfplll%{?_isa} = %{version}-%{release}

%description    tools
The libfplll-tools package contains command-line tools that expose
the functionality of libfplll.


%prep
%autosetup -n fplll-%{version}
# Unbundle “JSON for Modern C++”:
echo '#include <nlohmann/json.hpp>' > fplll/io/json.hpp
%if %{without bundled_thread_pool}
# Unbundle cr-marcstevens-snippets-thread_pool-devel
sed -r -i 's@io/thread_pool\.hpp@@' fplll/Makefile.am
sed -r -i 's@fplll/io(/thread_pool\.hpp)@cr-marcstevens\1@' fplll/threadpool.h
%endif


%build
autoreconf --install --force --verbose

# This is a formality; no extra flags are required in practice:
export CFLAGS="${CFLAGS-} $(pkgconf --cflags nlohmann_json)"
export LDFLAGS="${LDFLAGS-} $(pkgconf --libs nlohmann_json)"

%configure --disable-silent-rules

# Eliminate hardcoded rpaths, and work around libtool moving all -Wl options
# after the libraries to be linked
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-nostdlib|-Wl,--as-needed &|' \
    -i libtool

%make_build


%install
%make_install
find '%{buildroot}' -type f -name '*.la' -print -delete

install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p \
    '%{SOURCE1}' '%{SOURCE2}'


%check
LD_LIBRARY_PATH="${PWD}/src/.libs" %make_build check


%files
%doc NEWS README.md
%license COPYING
%{_libdir}/libfplll.so.%{so_version}{,.*}
%{_datadir}/fplll/


%files devel
%{_includedir}/fplll.h
%{_includedir}/fplll/
%{_libdir}/libfplll.so
%{_libdir}/pkgconfig/fplll.pc


%files static
%{_libdir}/libfplll.a


%files tools
%{_bindir}/fplll
%{_bindir}/latticegen
%{_mandir}/man1/fplll.1*
%{_mandir}/man1/latticegen.1*


%changelog
%autochangelog
