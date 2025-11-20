%global singulardir	%{_libdir}/Singular
%global upstreamver	4-4-1
%global downstreamver	%(tr - . <<< %{upstreamver})
#global patchver	p4
%global giturl		https://github.com/Singular/Singular

%bcond python 0

%if %{with python}
# Singular installs python files into nonstandard places
%global _python_bytecompile_extra 0
%endif

# Since qepcad-B requires this package, use this to build when the old version
# of Singular cannot be installed.
%bcond bootstrap 0

# Starting with the 4.3.1p3 release, doc building has become problematic.  The
# s390x build usually fails: while building the examples, Singular eventually
# attempts to fork, gets back ENOMEM, and then doesn't handle the failure well.
# The result is that the build stalls.  To avoid all this, we only build docs
# for aarch64, x86_64, and ppc64le.  If you really need docs for s390x, help me
# figure out how to avoid the problem described above.
%ifarch %{arm64} %{x86_64} %{power64}
%bcond docs 1
%else
%bcond docs 0
%endif

Name:		Singular
Version:	%{downstreamver}%{?patchver}
Release:	%autorelease
Summary:	Computer Algebra System for polynomial computations
# License analysis:
# - The project as a whole is GPL-2.0-only OR GPL-3.0-only
# - GPL-2.0-or-later:
#   - factory/cfNTLzzpEXGCD.{cc,h}
# - GPL-3.0-or-later WITH Bison-exception-2.2:
#   - Singular/grammar.{cc,h}
# - BSD-3-Clause:
#   - Singular/links/ndbm.{cc,h}
#   - Singular/svd
# - Not sure, but similar to HPND and NTP (TODO: check with Legal):
#   - omalloc/omReturn.h
License:	(GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2 AND BSD-3-Clause AND HPND
URL:		https://www.singular.uni-kl.de/
VCS:		git:%{giturl}.git
Source:		%{giturl}/archive/Release-%{upstreamver}%{?patchver}.tar.gz
BuildRequires:	4ti2
BuildRequires:	bison
BuildRequires:	boost-devel
%if %{with python}
BuildRequires:	boost-python2-devel
%endif
BuildRequires:	ccluster-devel
BuildRequires:	cddlib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	emacs
BuildRequires:	environment(modules)
BuildRequires:	flex
BuildRequires:	flint-devel
BuildRequires:	gcc-c++
BuildRequires:	gfan
BuildRequires:	gmp-devel
BuildRequires:	graphviz
BuildRequires:	libgfan-devel
BuildRequires:	libspasm-devel
BuildRequires:	libtool
BuildRequires:	lrcalc
BuildRequires:	make
BuildRequires:	normaliz
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mathicgb)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ntl)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(tbb)
BuildRequires:	pkgconfig(zlib)
%if %{with python}
BuildRequires:	python2-devel
%endif
%if %{without bootstrap}
BuildRequires:	qepcad-B
%endif
# Need uudecode for documentation images in tarball
BuildRequires:	sharutils
BuildRequires:	texinfo-tex
BuildRequires:	tex(latex)
BuildRequires:	TOPCOM
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	environment(modules)
Requires:	less
Requires:	qepcad-B
Requires:	TOPCOM%{_isa}

# The surfex code is no longer distributed with Singular
# This can be removed when F41 reaches EOL
Obsoletes:	Singular-surfex < 4.3.1-1

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

# Support S390(x) architectures
Patch:		%{name}-arches.patch
# Fix overlinking
Patch:		%{name}-link.patch
# Fix the desktop files
Patch:		%{name}-desktop.patch
# Adapt to new template code in NTL 8
Patch:		%{name}-ntl8.patch
# Fix code that can overflow a character buffer with sprintf
Patch:		%{name}-format.patch
# Add missing parentheses that can change code meaning in a macro
Patch:		%{name}-parens.patch
# Unbundle gfanlib
Patch:		%{name}-gfanlib.patch
# Let ESingular read a compressed singular.info file
Patch:		%{name}-emacs.patch
# Fix several "use after free" scenarios due to temporary objects
Patch:		%{name}-use-after-free.patch
# Change little-endian-specific code to endian-agnostic code
Patch:		%{name}-endian.patch
# Disable examples that use the network to avoid hangs on the koji builders
Patch:		%{name}-doc-hang.patch
# Fix an off-by-one error in polymake.lib that leads to failed examples
# https://github.com/Singular/Singular/issues/1210
Patch:		%{name}-polymake-lib.patch
# Adapt to flint 3.3.x
Patch:		%{name}-flint3.3.patch

%description
Singular is a computer algebra system for polynomial computations, with
special emphasis on commutative and non-commutative algebra, algebraic
geometry, and singularity theory.

%package	libs
Summary:	Singular library
Requires:	%{name}-libpolys%{?_isa} = %{version}-%{release}

%description	libs
This package contains the main Singular library.

%package	devel
Summary:	Singular development files
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-libpolys-devel%{?_isa} = %{version}-%{release}

%description	devel
This package contains the Singular development files.

%package	doc
Summary:	Singular documentation files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	doc
This package contains the Singular documentation files.

%package	emacs
Summary:	Emacs interface to Singular
Requires:	emacs-common
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	emacs
Emacs interface to Singular.

%package	-n factory
Summary:	C++ class library for multivariate polynomial data
Requires:	factory-gftables = %{version}-%{release}

%description	-n factory
Factory is a C++ class library that implements a recursive representation of
multivariate polynomial data.  It handles sparse multivariate polynomials over
different coefficient domains, such as Z, Q and GF(q), as well as algebraic
extensions over Q and GF(q) in an efficient way.  Factory includes algorithms
for computing univariate and multivariate gcds, resultants, chinese
remainders, and algorithms to factorize multivariate polynomials and to
compute the absolute factorization of multivariate polynomials with integer
coefficients.

%package	-n factory-devel
Summary:	Development files for the Singular factory
Requires:	factory%{?_isa} = %{version}-%{release}
Requires:	gmp-devel%{?_isa}

%description	-n factory-devel
Development files for the Singular factory.

%package	-n factory-gftables
Summary:	Singular factory addition tables
BuildArch:	noarch

%description	-n factory-gftables
Factory uses addition tables to calculate in GF(p^n) in an efficient way.

%package	libpolys
Summary:	C++ class library for polynomials in Singular
Requires:	factory%{?_isa} = %{version}-%{release}

%description	libpolys
Libpolys contains the data structures and basic algorithms for polynomials in
Singular.

%package	libpolys-devel
Summary:	Development files for libpolys
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	factory-devel%{?_isa} = %{version}-%{release}
Requires:	flint-devel%{?_isa}

%description	libpolys-devel
Development files for libpolys.


%prep
%autosetup -p1 -n %{name}-Release-%{upstreamver}%{?patchver}

%if %{with python}
# Fix the name of the boost_python library
sed -ri 's/(lboost_python)-\$\{PYTHON_VERSION\}/\1%{python2_version_nodots}/' \
    Singular/dyn_modules/python/Makefile.am
%endif

# Do not force the use of c++11, since the polymake code requires c++14
sed -i 's/"-std=c++11"/""/' m4/ntl-check.m4

# Do not add an rpath for ccluster
sed -i 's@ -Wl,-rpath,\${CCLUSTER_HOME}/lib@@' m4/ccluster-check.m4

# Make sure we do not use the bundled gfanlib
rm -fr gfanlib

# Work around a change in normaliz 3.10.5
sed -i '/nmz_multiplicity/d' Singular/LIB/normaliz.lib

# Regenerate configure due to patches
autoreconf -fi

# The file countedref.cc needs to be built without strict aliasing
sed -i '/countedref\.cc/s/\$(CXXFLAGS)/& -fno-strict-aliasing/g' Singular/Makefile.in


%build
export CPPFLAGS='-I%{_includedir}/flint -I%{_includedir}/gfanlib'
%if %{with python}
pyincdir=$(python2 -Esc "import sysconfig; print(sysconfig.get_paths()['include'])")
CPPFLAGS="$CPPFLAGS -I$pyincdir"
%endif
export CFLAGS='%{build_cflags} -fPIC'
export CXXFLAGS='%{build_cxxflags} -fPIC'
# -Wl,-z,now breaks lazy module loading
export LDFLAGS='%{build_ldflags} -Wl,-z,lazy'
module load 4ti2-%{_arch}
module load lrcalc-%{_arch}

%configure \
	--bindir=%{singulardir} \
	--disable-silent-rules \
	--disable-optimizationflags \
	--disable-static \
	--enable-p-procs-dynamic \
	--enable-bigintm-module \
	--enable-gfanlib \
	--enable-gfanlib-module \
	--enable-Order-module \
	--enable-polymake-module \
%if %{with python}
	--enable-python-module \
%else
	--disable-python-module \
%endif
	--enable-sispasm-module \
	--enable-streamio \
	--with-gmp \
	--with-ntl \
	--with-flint \
	--with-mathicgb \
%if %{with python}
	--with-python=%{__python2} \
%else
	--without-python \
%endif
	--with-readline \
%if %{with docs}
	--enable-doc-build \
%endif
	--with-malloc=system

%make_build
%make_build -C dox html


%install
%make_install

# Upstream forgot to move some modules from libexecdir
mv %{buildroot}%{_libexecdir}/singular/MOD/* %{buildroot}%{_libdir}/singular/MOD
rm -fr %{buildroot}%{_libexecdir}

# Validate the desktop files
desktop-file-validate %{buildroot}%{_datadir}/applications/Singular.desktop
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/Singular-manual.desktop

# Remove unnecessary dependencies from the pkgconfig files
sed -i 's/ -lflint.*//;s/Libs\.private.*/& -lflint -lmpfr -lntl -lgmp/' \
  %{buildroot}%{_libdir}/pkgconfig/factory.pc
sed -i 's/ -lflint.*//;s/Libs\.private.*/& -lflint -lmpfr -lgmp/' \
  %{buildroot}%{_libdir}/pkgconfig/libpolys.pc

# Remove files we don't want in the installed tree
rm -f %{buildroot}%{_datadir}/singular/emacs/{ChangeLog,COPYING,NEWS}
rm -fr %{buildroot}%{_docdir}/singular

# Move the config scripts
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{singulardir}/*-config %{buildroot}%{_bindir}

# Install documentation files
mkdir -p %{buildroot}%{_mandir}/man1
for cmd in ESingular Singular TSingular; do
  cp -p Singular/$cmd.man %{buildroot}%{_mandir}/man1/$cmd.1
done
%if %{with docs}
cp -a doc/{html,singular.idx} %{buildroot}%{_datadir}/singular
mkdir -p %{buildroot}%{_infodir}
cp -p doc/singular.info %{buildroot}%{_infodir}
%endif

# remove script that calls surf; we don't ship it
rm -f %{buildroot}%{singulardir}/singularsurf

# create a script also setting SINGULARPATH
cat > %{buildroot}%{_bindir}/Singular << EOF
#!/bin/sh

. /etc/profile.d/modules.sh
export SINGULAR_DATA_DIR=%{_datadir}
exec %{singulardir}/Singular "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/Singular

# TSingular
cat > %{buildroot}%{_bindir}/TSingular << EOF
#!/bin/sh

. /etc/profile.d/modules.sh
exec %{singulardir}/TSingular --singular %{_bindir}/Singular "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/TSingular

# ESingular
cat > %{buildroot}%{_bindir}/ESingular << EOF
#!/bin/sh

. /etc/profile.d/modules.sh
export ESINGULAR_EMACS_DIR=%{_datadir}/singular/emacs
exec %{singulardir}/ESingular --singular %{_bindir}/Singular "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/ESingular

%if %{with python}
# Byte compile the python files
%py_byte_compile %{__python2} %{buildroot}%{_datadir}/singular/LIB
%endif


%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check


%files
%doc README.md
%{_bindir}/Singular
%{_bindir}/TSingular
%{_mandir}/man1/Singular.1*
%{_mandir}/man1/TSingular.1*
%{_datadir}/applications/Singular.desktop
%{_datadir}/icons/Singular.png
%{_datadir}/ml_python/
%{_datadir}/ml_singular/
%if %{with docs}
%{_datadir}/singular/singular.idx
%{_infodir}/singular.info*
%docdir %{_datadir}/singular/html/
%{_datadir}/singular/html/
%{singulardir}/libparse
%endif
%dir %{singulardir}
%{singulardir}/Singular
%{singulardir}/TSingular

%files		libs
%doc libpolys/README
%license COPYING
%license GPL2
%license GPL3
%{_libdir}/libSingular-%{downstreamver}.so
%{_libdir}/singular/
%dir %{_datadir}/singular/
%{_datadir}/singular/LIB/

%files		devel
%{_bindir}/libsingular-config
%{_includedir}/singular/kernel/
%{_includedir}/singular/Singular/
%{_includedir}/singular/singularconfig.h
%{_libdir}/libSingular.so
%{_libdir}/pkgconfig/Singular.pc

%files		doc
%doc dox/html/
%doc dox/*.html
%doc dox/*.png
%doc dox/*.css
%doc dox/tags
%{_datadir}/applications/Singular-manual.desktop

%files		emacs
%license emacs/COPYING
%doc emacs/BUGS
%{_bindir}/ESingular
%{_mandir}/man1/ESingular.1*
%{_datadir}/singular/emacs/
%{singulardir}/ESingular

%files		-n factory
%license factory/COPYING
%doc factory/README
%{_libdir}/libfactory-%{downstreamver}.so
%{_libdir}/libomalloc-0.9.6.so
%{_libdir}/libsingular_resources-%{downstreamver}.so

%files		-n factory-devel
%doc factory/examples
%{_includedir}/factory/
%{_includedir}/omalloc/
%{_includedir}/resources/
%{_libdir}/libfactory.so
%{_libdir}/libomalloc.so
%{_libdir}/libsingular_resources.so
%{_libdir}/pkgconfig/factory.pc
%{_libdir}/pkgconfig/omalloc.pc
%{_libdir}/pkgconfig/singular_resources.pc

%files		-n factory-gftables
%{_datadir}/factory/

%files		libpolys
%license libpolys/COPYING
%doc libpolys/README
%{_libdir}/libpolys-%{downstreamver}.so

%files		libpolys-devel
%{_bindir}/libpolys-config
%dir %{_includedir}/singular/
%{_includedir}/singular/coeffs/
%{_includedir}/singular/libpolysconfig.h
%{_includedir}/singular/misc/
%{_includedir}/singular/polys/
%{_includedir}/singular/reporter/
%{_libdir}/libpolys.so
%{_libdir}/pkgconfig/libpolys.pc


%changelog
%autochangelog
