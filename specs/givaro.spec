# Use packaged autotools to re-generate the configure script?
%bcond autoreconf 1

Name:           givaro
Version:        4.2.0
%global so_version 9
Release:        %autorelease
Summary:        C++ library for arithmetic and algebraic computations

# The entire source is CECILL-B except for src/kernel/recint/reclonglong.h,
# which is LGPL-3.0-or-later, and various Autotools build-system files, which
# do not contribute to the licenses of the binary RPMs.
License:        CECILL-B AND LGPL-3.0-or-later
# FSFAP-no-warranty-disclaimer:
#   - macros/ax_cxx_compile_stdcxx_11.m4
# FSFUL AND FSFULLR AND GPL-2.0-or-later WITH Libtool-exception:
#   - macros/libtool.m4
# FSFUL AND GPL-2.0-or-later WITH Libtool-exception AND CECILL-B:
#   (CECILL-B from configure.ac)
#   - configure
# FSFULLR:
#   - aclocal.m4
#   - macros/ltoptions.m4
#   - macros/ltsugar.m4
#   - macros/ltversion.m4
#   - macros/lt~obsolete.m4
# FSFULLR AND CECILL-B:
#   (CECILL-B from each corresponding Makefile.am)
#   - macros/Makefile.in
#   - examples/FiniteField/Makefile.in
#   - examples/Integer/Makefile.in
#   - examples/Matrix/Makefile.in
#   - examples/Polynomial/Makefile.in
#   - examples/Rational/Makefile.in
#   - examples/RecInt/Makefile.in
# GPL-2.0-or-later WITH Autoconf-exception-generic:
#   - build-aux/ar-lib
#   - build-aux/compile
#   - build-aux/depcomp
#   - build-aux/missing
#   - build-aux/test-driver
# GPL-2.0-or-later WITH Libtool-exception:
#   - build-aux/ltmain.sh
# GPL-3.0-or-later WITH Autoconf-exception-generic:
#   - build-aux/config.guess
#   - build-aux/config.sub
# X11:
#   - build-aux/install-sh
SourceLicense:  %{shrink:
                %{license} AND
                FSFAP-no-warranty-disclaimer AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                GPL-2.0-or-later WITH Libtool-exception AND
                X11
                }
URL:            https://casys.gricad-pages.univ-grenoble-alpes.fr/givaro/
%global forgeurl https://github.com/linbox-team/givaro
Source:         %{forgeurl}/releases/download/v%{version}/givaro-%{version}.tar.gz

# Add missing #include <cstdint> for (u)int64_t
# Fixes failure to compile on GCC 13.
# https://github.com/linbox-team/givaro/pull/218
Patch:          %{forgeurl}/pull/218.patch
# Temporary GCC 14 workaround
#
# Fixes https://github.com/linbox-team/givaro/issues/226 “GCC 14: No match
# for operator= for Givaro::ZRing<Givaro::Integer>”
#
# Recommended in
# https://github.com/linbox-team/givaro/issues/226#issuecomment-1908853755
Patch:          0001-Temporary-GCC-14-workaround.patch
# Fix build using GCC 15
# https://github.com/linbox-team/givaro/pull/233
#
# Fixes:
#
# Build failure with GCC-15
# https://github.com/linbox-team/givaro/issues/232
Patch:          %{forgeurl}/pull/233.patch

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  gmp-devel

%description
Givaro is a C++ library for arithmetic and algebraic computations. Its main
features are implementations of the basic arithmetic of many mathematical
entities: Prime fields, Extension Fields, Finite Fields, Finite Rings,
Polynomials, Algebraic numbers, Arbitrary precision integers and rationals (C++
wrappers over gmp). It also provides data-structures and templated classes for
the manipulation of basic algebraic objects, such as vectors, matrices (dense,
sparse, structured), and univariate polynomials (and therefore recursive
multivariate).


%package        devel
Summary:        Files useful for givaro development

Requires:       givaro%{?_isa} = %{version}-%{release}

Obsoletes:      givaro-devel-doc < 4.1.1-15

%description    devel
The libraries and header files for using givaro for development.


# The static library is required by Macaulay2. See its spec file for a full
# explanation; the essential justification is excerpted below:
#
#   We have to use the static version of the libfplll and givaro library. They
#   have global objects whose constructors run before GC is initialized. If we
#   allow the shared libraries to be unloaded, which happens as a normal part
#   of Macaulay2's functioning, then GC tries to free objects it did not
#   allocate, which leads to a segfault.
%package        static
Summary:        Static library for givaro

Requires:       givaro-devel%{?_isa} = %{version}-%{release}

%description    static
A static library for givaro.


%prep
%autosetup -p1


%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif

%ifarch %{ix86}
# Excess precision leads to test failures
%global optflags %optflags -ffloat-store
%endif
%ifarch s390x
%global optflags %optflags -ffp-contract=off
%endif

%configure --without-archnative

# Get rid of undesirable hardcoded rpaths, and workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool


%build
%make_build


%install
%make_install

# We don't want libtool archives
rm -f %{buildroot}%{_libdir}/libgivaro.la


%check
export LD_LIBRARY_PATH="${PWD}/src/.libs"
%make_build check


%files
%license COPYING
%license COPYRIGHT
%license Licence_CeCILL-B_V1-en.txt
%license Licence_CeCILL-B_V1-fr.txt

%doc AUTHORS
%doc ChangeLog
%doc README.md

%{_libdir}/libgivaro.so.%{so_version}{,.*}


%files devel
%{_bindir}/givaro-config

%dir %{_datadir}/givaro
%{_datadir}/givaro/givaro-makefile

%{_includedir}/givaro/
%{_includedir}/gmp++/
%{_includedir}/recint/
%{_includedir}/givaro-config.h

%{_libdir}/libgivaro.so

%{_libdir}/pkgconfig/givaro.pc


%files static
%{_libdir}/libgivaro.a


%changelog
%autochangelog
