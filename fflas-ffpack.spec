# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We can enable the Doxygen PDF documentation as a substitute.
%bcond doc 1

# This package is arch-specific, because it computes properties of the system
# (such as endianness) and stores them in generated header files. Hence, the
# files DO vary by platform. However, there is no actual compiled code, so turn
# off debuginfo generation.
%global debug_package %{nil}

Name:           fflas-ffpack
Version:        2.5.0
Release:        %autorelease
Summary:        Finite field linear algebra subroutines

# The entire source is LGPL-2.1-or-later, except:
#   - fflas-ffpack/fflas-ffpack-config.h is LGPL-2.0-or-later
#
# Certain build system files that do not contribute to the license of the
# binary RPMs are also distributed under other licenses:
#   - INSTALL and macros/ax_cxx_compile_stdcxx_11.m4 are FSFAP
#   - aclocal.m4 and macros/libtool.m4 are (FSFULLR AND GPL-2.0-or-later)
#   - configure is FSFUL, or, more likely (FSFUL AND LGPL-2.1-or-later)
#   - build-aux/compile, build-aux/depcomp, build-aux/ltmain.sh,
#     build-aux/missing, and build-aux/test-driver are GPL-2.0-or-later
#   - macros/instr_set.m4 is CECILL-B
#   - macros/ltoptions.m4, macros/ltsugar.m4, macros/ltversion.m4, and
#     macros/lt~obsolete.m4 are FSFULLR
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:            https://linbox-team.github.io/fflas-ffpack/
%global forgeurl https://github.com/linbox-team/fflas-ffpack
Source0:        %{forgeurl}/releases/download/v%{version}/fflas_ffpack-%{version}.tar.bz2
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        fflas-ffpack-config.1

# fix perf publisher
# https://github.com/linbox-team/fflas-ffpack/commit/833bb2fa4e87e51e3f7fa1d97f3b4372c1ee4200
#
# This is not only useful for perf/benchmarks; it fixes OpenMP detection in the
# configure script.
#
# Rebased on 2.5.0 (which lacks benchmarks/benchmark-sss.C).
Patch:          0001-fix-perf-publisher.patch

# Give cblas_ssyrk a return type
# https://github.com/linbox-team/fflas-ffpack/pull/384
Patch:          %{forgeurl}/pull/384.patch

# Fix a couple of apparent typos in config-blas.h
# https://github.com/linbox-team/fflas-ffpack/pull/385
Patch:          %{forgeurl}/pull/385.patch

# Do not use _mm_permute_ps for simd128_float as it requires AVX. Fix #378
# https://github.com/linbox-team/fflas-ffpack/pull/379
#
# Fixes:
#
# bad usage of AVX2 instruction without checking availability of the
# instruction set
# https://github.com/linbox-team/fflas-ffpack/issues/378
Patch:          %{forgeurl}/pull/379.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(givaro)
BuildRequires:  gmp-devel

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
BuildRequires:  make
BuildRequires:  tex(stmaryrd.sty)
# Default font for graphviz/dot
BuildRequires:  font(freesans)
%endif

# Although there are references to linbox-devel files in this package,
# linbox-devel Requires fflas-ffpack-devel, not the other way around.

%global common_description %{expand: \
The FFLAS-FFPACK library provides a set of basic routines for linear algebra
over a finite field or the ring of integers with dense and sparse matrices.}

%description
%{common_description}


%package devel
Summary:        Header files for developing with fflas-ffpack

Requires:       givaro-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       flexiblas-devel%{?_isa}

Provides:       fflas-ffpack-static = %{version}-%{release}

%description devel
%{common_description}

This package provides the header files for developing applications that use
FFLAS-FFPACK.


%if %{with doc}
%package doc
Summary:        API documentation for fflas-ffpack

BuildArch:      noarch

%description doc
%{common_description}

This package provides API documentation for fflas-ffpack.
%endif


%prep
%autosetup -n fflas_ffpack-%{version} -p1
# Skip test-echelon for now due to failures.
# See https://github.com/linbox-team/fflas-ffpack/issues/282
sed -i '/^[[:blank:]]*test-echelon/d' tests/Makefile.am

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_shebang_lines
sed -i 's,%{_bindir}/env bash,%{_bindir}/bash,' fflas-ffpack-config.in

# Remove parts of the configure script that select non-default architectures
# and ABIs. On x86_64, we could rely on up to SSE2, but there are no explicit
# SIMD routines below SSE4.1 in the library, so it is not worth worrying about.
sed -i '/INSTR_SET/,/fabi-version/d' configure.ac

%if %{with doc}
# We enable the Doxygen PDF documentation as a substitute. We must enable
# GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and should
# already be set as we like them. We also disable GENERATE_HTML, since we will
# not use it.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP|GENERATE_HTML)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    doc/Doxyfile doc/DoxyfileDev
%endif


%build
# Regenerate configure after monkeying with configure.ac
autoreconf --force --install --verbose

# We define __FFLASFFPACK_HAVE_CBLAS to bypass CBLAS detection so that the
# configure script detects USER LAPACK. Ideally, this would be reported
# upstream, but it’s difficult to describe the problem precisely.
%configure \
  %{?with_doc:--enable-doc --docdir='%{_docdir}/fflas-ffpack'} \
  --disable-static \
  --enable-openmp \
  --without-archnative \
  --with-blas-cflags="$(pkgconf --cflags flexiblas) -D__FFLASFFPACK_HAVE_CBLAS=1" \
  --with-blas-libs="$(pkgconf --libs flexiblas)"
chmod -v a+x fflas-ffpack-config
%make_build

%if %{with doc}
%make_build -C doc/latex
mv -v doc/latex/refman.pdf doc/fflas-ffpack.pdf
# Build the developer documentation, too.
rm -rf doc/latex
%make_build -C doc docs_dev
%make_build -C doc/latex
mv -v doc/latex/refman.pdf doc/fflas-ffpack-dev.pdf
%endif


%install
%make_install
rm -vrf '%{buildroot}%{_prefix}/docs'
install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p '%{SOURCE1}'


%check
# https://docs.fedoraproject.org/en-US/packaging-guidelines/BLAS_LAPACK/#_tests
export FLEXIBLAS=netlib
%make_build check


%files devel
%license COPYING COPYING.LESSER
%if %{without doc}
%doc AUTHORS ChangeLog README.md TODO
%endif

%{_bindir}/fflas-ffpack-config
%{_mandir}/man1/fflas-ffpack-config.1*

%{_includedir}/fflas-ffpack/

%{_libdir}/pkgconfig/fflas-ffpack.pc


%if %{with doc}
%files doc
%license COPYING COPYING.LESSER
%doc AUTHORS ChangeLog README.md TODO
%doc doc/fflas-ffpack.pdf
%doc doc/fflas-ffpack-dev.pdf
%endif


%changelog
%autochangelog
