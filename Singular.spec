%global singulardir	%{_libdir}/Singular
%global upstreamver	4-3-1
%global downstreamver	%(tr - . <<< %{upstreamver})
%global patchver	p1

%bcond_with python

%if %{with python}
# Singular installs python files into nonstandard places
%global _python_bytecompile_extra 0
%endif

# Since qepcad-B requires this package, use this to build when the old version
# of Singular cannot be installed.
%bcond_with bootstrap

Name:		Singular
Version:	%{downstreamver}%{?patchver}
Release:	2%{?dist}
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
Source0:        https://www.singular.uni-kl.de/ftp/pub/Math/Singular/SOURCES/%{upstreamver}/singular-%{version}.tar.gz
URL:		https://www.singular.uni-kl.de/
BuildRequires:	4ti2
BuildRequires:	bison
BuildRequires:	boost-devel
%if %{with python}
BuildRequires:	boost-python2-devel
%endif
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
%ifarch %{java_arches}
BuildRequires:	java-devel
BuildRequires:	javapackages-tools
%endif
BuildRequires:	libgfan-devel
BuildRequires:	libnormaliz-devel
BuildRequires:	libtool
BuildRequires:	lrcalc
BuildRequires:	make
BuildRequires:	normaliz
BuildRequires:	ntl-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mathicgb)
BuildRequires:	pkgconfig(ncurses)
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
BuildRequires:	surf-geometry
BuildRequires:	texinfo-tex
BuildRequires:	tex(latex)
BuildRequires:	TOPCOM
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	environment(modules)
Requires:	less
Requires:	qepcad-B
Requires:	surf-geometry
Requires:	TOPCOM%{_isa}

# This can be removed when Fedora 38 reaches EOL
Obsoletes:      Singular-polymake < 4.2.0-1
Provides:       Singular-polymake = %{version}-%{release}

# The surfex code is no longer distributed with Singular
# This can be removed when F41 reaches EOL
Obsoletes:      Singular-surfex < 4.3.1-1

# Support S390(x) architectures
Patch0:		%{name}-arches.patch
# Fix both underlinking and overlinking
Patch1:		%{name}-link.patch
# Fix the desktop files
Patch2:		%{name}-desktop.patch
# Adapt to new template code in NTL 8
Patch3:		%{name}-ntl8.patch
# Fix code that can overflow a character buffer with sprintf
Patch4:		%{name}-format.patch
# Add missing parentheses that can change code meaning in a macro
Patch5:		%{name}-parens.patch
# Unbundle gfanlib
Patch6:		%{name}-gfanlib.patch
# Fix code that violates the strict aliasing rules
Patch7:		%{name}-alias.patch
# Let ESingular read a compressed singular.info file
Patch8:		%{name}-emacs.patch
# Fix a sequence point error
Patch9:		%{name}-sequence-point.patch
# Avoid an unnecessary array comparison
Patch10:	%{name}-array-compare.patch
# Fix several "use after free" scenarios due to temporary objects
Patch11:	%{name}-use-after-free.patch
# Fix mismatched type declarations
Patch12:	%{name}-type-mismatch.patch
# Change little-endian-specific code to endian-agnostic code
Patch13:	%{name}-endian.patch
# Disable examples that use the network to avoid hangs on the koji builders
Patch14:	%{name}-doc-hang.patch

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
Factory is a C++ class library that implements a recursive
representation of multivariate polynomial data.  It handles sparse
multivariate polynomials over different coefficient domains, such as Z,
Q and GF(q), as well as algebraic extensions over Q and GF(q) in an
efficient way.  Factory includes algorithms for computing univariate and
multivariate gcds, resultants, chinese remainders, and algorithms to
factorize multivariate polynomials and to compute the absolute
factorization of multivariate polynomials with integer coefficients.

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
Libpolys contains the data structures and basic algorithms for
polynomials in Singular.

%package	libpolys-devel
Summary:	Development files for libpolys
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	factory-devel%{?_isa} = %{version}-%{release}
Requires:	flint-devel%{?_isa}

%description	libpolys-devel
Development files for libpolys.


%prep
%autosetup -n singular-%{downstreamver} -p1

%if %{with python}
# Fix the name of the boost_python library
sed -ri 's/(lboost_python)-\$\{PYTHON_VERSION\}/\1%{python2_version_nodots}/' \
    Singular/dyn_modules/python/Makefile.am
%endif

# Do not force the use of c++11, since the polymake code requires c++14
sed -i 's/-std=c++11//' m4/ntl-check.m4

# Regenerate configure due to patches 0, 1, and 6
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
# Cannot use RPM_LD_FLAGS, as -Wl,-z,now breaks lazy module loading
export LDFLAGS='-Wl,--as-needed -Wl,-z,relro'
module load 4ti2-%{_arch}
module load lrcalc-%{_arch}

%configure \
	--bindir=%{singulardir} \
	--disable-silent-rules \
	--disable-optimizationflags \
	--disable-static \
	--enable-p-procs-dynamic \
	--enable-bigintm-module \
	--enable-gfanlib-module \
	--enable-Order-module \
%if %{with polymake}
	--enable-polymake-module \
%else
	--disable-polymake-module \
%endif
%if %{with python}
	--enable-python-module \
%else
	--disable-python-module \
%endif
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
	--enable-doc \
	--with-malloc=system

%make_build
%make_build -C dox html
%make_build -C Singular libparse
make -C doc -j1 -f Makefile-docbuild singular.idx
make -C doc -j1 all-local


%install
%make_install

# Do not install gfanlib; it is packaged separately
rm -fr %{buildroot}%{_includedir}/gfanlib
rm -f %{buildroot}%{_libdir}/libgfan*

# Validate the desktop files
desktop-file-validate %{buildroot}%{_datadir}/applications/Singular.desktop
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/Singular-manual.desktop

# Remove unnecessary dependencies from the pkgconfig files
sed -i 's/ -lflint.*//;s/Libs\.private.*/& -lflint -lmpfr -lntl -lgmp/' \
  %{buildroot}%{_libdir}/pkgconfig/factory.pc
sed -i 's/ -lflint.*//;s/Libs\.private.*/& -lflint -lmpfr -lgmp/' \
  %{buildroot}%{_libdir}/pkgconfig/libpolys.pc

# We don't want the libtool files
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libexecdir}/singular/MOD/*.la

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
cp -a doc/{html,singular.idx} %{buildroot}%{_datadir}/singular
mkdir -p %{buildroot}%{_infodir}
cp -p doc/singular.info %{buildroot}%{_infodir}

# remove script that calls surf; we don't ship it
rm -f %{buildroot}%{singulardir}/singularsurf

# create a script also setting SINGULARPATH
cat > %{buildroot}%{_bindir}/Singular << EOF
#!/bin/sh

. /etc/profile.d/modules.sh
module load surf-geometry-%{_arch}
export SINGULAR_DATA_DIR=%{_datadir}
exec %{singulardir}/Singular "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/Singular

# TSingular
cat > %{buildroot}%{_bindir}/TSingular << EOF
#!/bin/sh

. /etc/profile.d/modules.sh
module load surf-geometry-%{_arch}
exec %{singulardir}/TSingular --singular %{_bindir}/Singular "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/TSingular

# ESingular
cat > %{buildroot}%{_bindir}/ESingular << EOF
#!/bin/sh

. /etc/profile.d/modules.sh
module load surf-geometry-%{_arch}
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
%{_infodir}/singular.info*
%{_mandir}/man1/Singular.1*
%{_mandir}/man1/TSingular.1*
%{_datadir}/applications/Singular.desktop
%{_datadir}/icons/Singular.png
%{_datadir}/ml_python/
%{_datadir}/ml_singular/
%{_datadir}/singular/singular.idx
%docdir %{_datadir}/singular/html/
%{_datadir}/singular/html/
%dir %{singulardir}
%{singulardir}/Singular
%{singulardir}/TSingular

%files		libs
%doc libpolys/README
%license COPYING
%license GPL2
%license GPL3
%{_libdir}/libSingular-%{downstreamver}.so
%{_libexecdir}/singular/
%dir %{_datadir}/singular/
%{_datadir}/singular/LIB/
%ifarch %{java_arches}
%endif

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
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Jerry James <loganjerry@gmail.com> - 4.3.1p1-1
- Version 4.3.1p1
- Remove the surfex subpackage
- Drop upstreamed -format-specifier and -gcc12 patches
- Drop obsolete -javac patch
- Convert License tags to SPDX
- Reenable building the index on ppc64le

* Mon Jul 25 2022 Jerry James <loganjerry@gmail.com> - 4.2.1p3-3
- Do not build surfex for i686 (rhbz#2104103)
- Add patches to fix code errors: -sequence-point, -array-compare,
  -use-after-free, -format-specifier, -type-mismatch
- Add -endian patch to fix oddities on s390x

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1p3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 4.2.1p3-2
- Rebuild for flint 2.9.0
- Add bootstrap build mode that excludes qepcad-B

* Thu Mar 17 2022 Jerry James <loganjerry@gmail.com> - 4.2.1p3-1
- Version 4.2.1p3
- Add patch for GCC 12
- Build documentation with -j1 to avoid OOM on the koji builders
- Do not build the index on ppc64le due to lack of memory

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 4.2.0p3-3
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0p3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 27 2021 Jerry James <loganjerry@gmail.com> - 4.2.0p3-1
- Version 4.2.0p3

* Wed Aug 25 2021 Jerry James <loganjerry@gmail.com> - 4.2.0p2-5
- Rebuild for flint 2.8.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0p2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Jerry James <loganjerry@gmail.com> - 4.2.0p2-3
- Rebuild for flint 2.7.1
- Build with support for 4ti2, gfan, graphviz, lrcal, normaliz, and TOPCOM

* Tue Jun 29 2021 Jerry James <loganjerry@gmail.com> - 4.2.0p2-2
- Rebuild for ntl 11.5.1

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 4.2.0p2-1
- Version 4.2.0p2
- Drop the -polymake subpackage; the polymake library is no longer linked
- Drop the -polymake and -flint patches

* Wed Feb 17 2021 Jerry James <loganjerry@gmail.com> - 4.1.1p3-24
- Rebuild for normaliz 3.8.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1p3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Jerry James <loganjerry@gmail.com> - 4.1.1p3-22
- Rebuild for polymake 4.3

* Wed Sep 30 2020 Jerry James <loganjerry@gmail.com> - 4.1.1p3-21
- Rebuild for normaliz 3.8.9

* Thu Sep 24 2020 Jerry James <loganjerry@gmail.com> - 4.1.1p3-20
- Rebuild for polymake 4.2

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 4.1.1p3-19
- Rebuild for normaliz 3.8.8

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1p3-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1p3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jerry James <loganjerry@gmail.com> - 4.1.1p3-16
- Add -javac patch for better JDK 11 support

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 4.1.1p3-15
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jul  9 2020 Jerry James <loganjerry@gmail.com> - 4.1.1p3-14
- Rebuild with polymake support

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 4.1.1p3-13.1
- Rebuild for flint 2.6.0 and normaliz 3.8.6 without polymake support
- Add -flint patch

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 4.1.1p3-13
- Rebuild for polymake 4.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1p3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 4.1.1p3-11
- Rebuild for ntl 11.4.3

* Mon Dec  2 2019 Jerry James <loganjerry@gmail.com> - 4.1.1p3-10
- Rebuild for polymake 3.6

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 4.1.1p3-9
- Rebuild for mpfr 4

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 4.1.1p3-8
- Rebuild for ntl 11.3.4

* Fri Sep  6 2019 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.1.1p3-7
- Disable the python interface (#1741426)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1p3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Jerry James <loganjerry@gmail.com> - 4.1.1p3-5
- Add -polymake patch to fix polymake plugin

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.1p3-4
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1p3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 4.1.1p3-2
- Rebuilt for Boost 1.69

* Wed Oct 24 2018 Jerry James <loganjerry@gmail.com> - 4.1.1p3-1
- New upstream version
- Drop upstreamed -polymake, -sagemath, and -python patches

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 4.1.0p3-15
- Rebuild for ntl 11.3.0 and cddlib 0.94j

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 4.1.0p3-14
- Rebuild with polymake support

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 4.1.0p3-13
- Rebuild for ntl 11.2.1, without polymake support to bootstrap

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0p3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 4.1.0p3-11
- Rebuild with polymake support

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 4.1.0p3-10.1
- Rebuild for ntl 11.1.0 without polymake support
- Remove scriptlets that call install-info
- Follow new packaging guidelines for python files in nonstandard places

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 4.1.0p3-10
- Rebuild with polymake support

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 4.1.0p3-9.1
- Rebuild for ntl 11.0.0
- Unbundle gfanlib
- Bootstrap without polymake support

* Tue May 01 2018 Jonathan Wakely <jwakely@redhat.com> - 4.1.0p3-9
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Wed Feb 14 2018 Jerry James <loganjerry@gmail.com> - 4.1.0p3-8
- Add -python patch to adapt to changed boost python interface

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0p3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jerry James <loganjerry@gmail.com> - 4.1.0p3-7
- Rebuild for cddlib and ntl 10.5.0
- Break gfanlib out as a separate package for use by the gfan package

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0p3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0p3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 4.1.0p3-4
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 4.1.0p3-3
- Rebuilt for Boost 1.64

* Tue May 23 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.1.0p3-2
- Revert a function changed to static in p3 due to sagemath requiring it

* Mon May  1 2017 Jerry James <loganjerry@gmail.com> - 4.1.0p3-1
- New upstream version
- Add -emacs patch to fix ESingular
- Build and install surfex.jar

* Tue Apr 18 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.1.0p2-2
- Correct Singular script
- Correct path of Singular lib files

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 4.1.0p2-1
- New upstream version (bz 1181772, 1321077)
- Drop upstreamed patches: -destdir, -headers, -doc, -builddid, -undefined,
  and -semaphore
- Add patches: -desktop, -format, -parens, -sequence-point, -alias, -polymake
- libpolys subpackage replaces libfac
- Rework the Emacs support

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.1.7-11
- Rebuild for readline 7.x

* Wed Nov  9 2016 Paul Howarth <paul@city-fan.org> - 3.1.7-10
- Bootstrap build for ppc64

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 3.1.7-9
- Rebuild for ntl 10.1.0

* Mon Sep  5 2016 Jerry James <loganjerry@gmail.com> - 3.1.7-8
- Rebuild for ntl 9.11.0

* Tue Jul 26 2016 Jerry James <loganjerry@gmail.com> - 3.1.7-7
- Rebuild with polymake support

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 3.1.7-6
- Rebuild for ntl 9.10.0

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 3.1.7-5
- Rebuild for ntl 9.9.1

* Fri Apr 29 2016 Jerry James <loganjerry@gmail.com> - 3.1.7-4
- Rebuild for ntl 9.8.0

* Tue Apr 12 2016 Jerry James <loganjerry@gmail.com> - 3.1.7-3
- Rebuild for polymake 3.0r1

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 3.1.7-2
- Rebuild for ntl 9.7.0

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 3.1.7-1
- Update to 3.1.7; fixes FTBFS (bz 1307301)
- Drop upstreamed -flint24 and -gcc5 patches
- Add -boolean patch to fix a malformed boolean expression

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 3.1.6-20
- Rebuild for ntl 9.6.2
- Drop obsolete ntl6 patch

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 3.1.6-19
- Rebuild for ntl 9.4.0

* Sat Oct  3 2015 Jerry James <loganjerry@gmail.com> - 3.1.6-18
- Rebuild with polymake support

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 3.1.6-17
- Rebuild for flint 2.5.2 and ntl 9.3.0

* Sun Jul 19 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.6-16
- Disable polymake due to broken dependency cycle
- Correct previous perl warning that is now an error
- Use interactive bash on wrappers to work with other login shells (#1243580)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 3.1.6-14
- Rebuild for ntl 9.1.1 and cddlib-094h

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 3.1.6-13
- Rebuild for ntl 9.1.0

* Sun Apr 26 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.6-12
- Update arches patch to support aarch64 (#1213484)

* Thu Apr  2 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.6-11
- Rebuild for rawhide gcc5 and c++ string and list abi

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 3.1.6-10
- Rebuild for ntl 8.1.2

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 3.1.6-9
- Rebuild for ntl 8.1.0
- Add Singular-ntl8.patch to adapt

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 3.1.6-8
- Rebuild for ntl 6.2.1

* Thu Sep 11 2014 Jerry James <loganjerry@gmail.com> - 3.1.6-7
- Rebuild for polymake -2.13-8.git20140811

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Jerry James <loganjerry@gmail.com> - 3.1.6-5
- Update Singular-ntl6.patch to instantiate more missing functions

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Jerry James <loganjerry@gmail.com> - 3.1.6-3
- Rebuild with polymake support
- Fix libsingular.h permissions

* Sun May 18 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.6-2
- Merge with RFE 3.1.6 update (#1074590)
- Remove patches applied upstream
- Disable polymake to allow interface rebootstrap

* Tue Apr 29 2014 Jerry James <loganjerry@gmail.com> - 3.1.5-14
- Rebuild for polymake-2.13

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 3.1.5-13
- Rebuild for polymake-2.12-15.svn20140326

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 3.1.5-12
- Rebuild for NTL 6.1.0
- Fix default paths
- Add ability to rebuild without polymake

* Mon Mar 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 3.1.6-1
- 3.1.6

* Mon Mar 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 3.1.5-11
- fix/workaround char=unsigned char assumptions
- (more) consistently use RPM_OPT_FLAGS
- --with-flint --with-polymake

* Tue Jan 14 2014 Jerry James <loganjerry@gmail.com> - 3.1.5-10
- Update normaliz interface for normaliz 2.8 and later

* Mon Nov 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.1.5-9
- ExclusiveArch: %%ix86 x86_64

* Fri Aug 16 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.5-8
- Correct underlink problem (#991920#c1)

* Thu Aug 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.1.5-7
- rebuild

* Tue May 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.1.5-6
- factory-gftables.noarch subpkg (#965655)

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 3.1.5-5
- Rebuild for ntl 6.0.0
- Fix semaphore code
- Fix underlinked library

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 11 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.5-3
- Rebuild to have factory include path patch in rawhide package

* Tue Aug 7 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.5-2
- Do not build conflicts with factory-devel neither libfac-devel (#842407)

* Sat Aug 4 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.5-1
- Update to Singular 3.1.5, based on sagemath trac ticket #13237
- Remove already applied patches from sagemath Singular spkg
- Rediff Fedora rpm build patches
- Rediff factory and libfac patches for Macaulay2

* Thu Jul 19 2012 Rex Dieter <rdieter@fedoraproject.org> - 3.1.3-8
- macaulay2 patches for libfac/factory
- omit duplicate %%description sections

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.3-6
- Update license field to match valid values.
- Provide newer libfac-devel matching Singular version (#819264).
- Provide newer factory-devel matching Singular version (#819264).
- Remove platform specific factoryconf.h file as only platform specific
  contents it has is "#define INT64 long long int" what is not really correct,
  neither completely wrong...

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.3-5
- Do not conflict Singular-devel with libfac-devel.

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.3-4
- Update license information to match COPYING information.

* Wed May 9 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.3-3
- Correct unresolved mmInit symbol in libsingular.so.

* Sun May 6 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.3-2
- Install singular factory headers in singular devel directory.
- Tag singular-doc files as documentation.

* Sat May 5 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.1.3-1
- Initial Singular spec.
