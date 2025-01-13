# Features in Fedora/Free Electronic Lab
#	What else does this build do aside compiling ngspice ?
#	- Ensures interoperability with xcircuit via Tcl
#	- Ensures interoperability with mot-adms
#	- Provides tclspice capabilities
# Chitlesh Goorah

%global	userelease	1
%global	usegitbare	0

%if 0%{?usegitbare} < 1
# force
%global	userelease	1
%endif

%global	majorver	44
%global	minorver	2
%global	docver	44
%undefine	prever
%global	prerpmver	%(echo "%{?prever}" | sed -e 's|-||g')

%global	baserelease	1

%if 0%{?usegitbare} >= 1
# pre-master-42
%global	gitcommit	c87df54f24969de0c9d503c349258d9953ae208a
%global	gitdate	20231111
%global	shortcommit	%(c=%{gitcommit}; echo ${c:0:7})

%global	tarballdate	20231112
%global	tarballtime	1636
%endif

%if	0%{?userelease} >= 1
%global	fedoraver		%{majorver}%{?minorver:.%minorver}
%endif
%if	0%{?usegitbare} >= 1
%global	fedoraver		%{majorver}%{?minorver:.%minorver}^%{gitdate}git%{shortcommit}
%endif

%global	use_gcc_strict_sanitize	0

%global	flagrel	%{nil}
%if		0%{?use_gcc_strict_sanitize} >= 1
%global	flagrel	%{flagrel}.san
%endif

%bcond_with	adms

%undefine       _changelog_trimtime

Name:			ngspice
Version:		%{fedoraver}
Release:		%{baserelease}%{?dist}%{flagrel}
Summary:		A mixed level/signal circuit simulator

# ngspice-42-manual.pdf	CC-BY-SA-4.0 AND BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:		LicenseRef-Callaway-BSD
URL:			http://ngspice.sourceforge.net

%if 0%{?userelease} >= 1
Source0:		https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{majorver}%{?minorver:.%minorver}/ngspice-%{majorver}%{?minorver:.%minorver}.tar.gz
%endif
%if 0%{?usegitbare} >= 1
Source0:       	ngspice-%{tarballdate}T%{tarballtime}.tar.gz
%endif
Source1:		https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{majorver}/ngspice-%{docver}-manual.pdf
%if %{with adms}
Source2:		https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{majorver}/ngspice-adms-va.7z
%endif
Source10:		create-ngspice-git-bare-tarball.sh


# Link libspice.so with -lBLT or -lBLIlite, depending on whether in tk mode or
# not (bug 1047056, debian bug 737279)
Patch0:		ngspice-37-blt-linkage-workaround.patch


BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gcc-c++
%if 0%{?use_gcc_strict_sanitize}
BuildRequires:	libasan
BuildRequires:	libubsan
%endif
BuildRequires:	p7zip

BuildRequires:	readline-devel
BuildRequires:	libXext-devel
BuildRequires:	libpng-devel
BuildRequires:	libICE-devel
BuildRequires:	libXaw-devel
BuildRequires:	libGL-devel
BuildRequires:	libXt-devel
# From ngspice 32
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libXft-devel
BuildRequires:	libXrender-devel

BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex

BuildRequires:	ImageMagick
BuildRequires:	mot-adms

BuildRequires:	xorg-x11-server-Xvfb
BuildRequires:	git

Requires:	%{name}-codemodel%{?_isa} = %{version}-%{release}
Obsoletes:	ngspice-doc < 20-4.cvs20100619
Provides:	ngspice-doc = %{version}-%{release}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Ngspice is a general-purpose circuit simulator program.
It implements three classes of analysis:
- Nonlinear DC analyses
- Nonlinear Transient analyses
- Linear AC analyses

Ngspice implements the usual circuits elements, like resistors, capacitors,
inductors (single or mutual), transmission lines and a growing number of
semiconductor devices like diodes, bipolar transistors, mosfets (both bulk
and SOI), mesfets, jfet and HFET. Ngspice implements the EKV model but it
cannot be distributed with the package since its license does not allow to
redistribute EKV source code.

Ngspice integrates Xspice, a mixed-mode simulator built upon spice3c1 (and
then some tweak is necessary merge it with spice3f5). Xspice provides a
codemodel interface and an event-driven simulation algorithm. Users can
develop their own models for devices using the codemodel interface.

It can be used for VLSI simulations as well.


%package -n	tclspice
Summary:	Tcl/Tk interface for ngspice
BuildRequires:	tk-devel
BuildRequires:	blt-devel

%description -n	tclspice
TclSpice is an improved version of Berkeley Spice designed to be used with
the Tcl/Tk scripting language. The project is based upon the NG-Spice source
code base with many improvements.

%package	codemodel
Summary:	ngspice codemodel and some script files

%description	codemodel
This package contains ngspice codemodel and some script files.

%package	-n libngspice
Summary:	Shared library version of ngspice
Requires:	%{name}-codemodel%{?_isa} = %{version}-%{release}

%description	-n libngspice
This package contains shared library version of ngspice.

%package	-n libngspice-devel
Summary:	Development files for libngspice
Requires:	libngspice%{?isa} = %{version}-%{release}

%description	-n libngspice-devel
This package contains libraries and header files for
developing applications that use libngspice.


%prep
%if 0%{?userelease} >= 1
%setup -q -n %{name}-%{majorver}%{?minorver:.%minorver}
git init
git config user.name "%{name} maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"
git add .
git commit -m "base" -q -a
%endif

%if 0%{?usegitbare} >= 1
%setup -q -c -n %{name}-%{majorver}%{?minorver:.%minorver}-%{gitdate}git%{shortcommit} -T -a 0
git clone ./%{name}.git/
cd %{name}
git config user.name "%{name} maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"

git checkout -b %{name}-%{majorver}-fedora %{gitcommit}
%endif

%if %{with adms}
pushd src/spicelib/devices/adms
%if 0%{?userelease} >= 1
7za x %{SOURCE2}
%endif
%if 0%{?usegitbare} >= 1
# Check if some adms va files exist
for f in \
	bsimbulk/admsva/bsimbulk.va \
	bsimcmg/admsva/bsimcmg.va \
	ekv/admsva/ekv.va \
	%{nil}
do
	test -f $f || exit 1
done
%endif

popd
%endif

%patch -P0 -p2 -b .link
git commit -m "Link libspice.so with -lBLT or -lBLIlite, depending on whether in tk mode or not" -a

# make sure the examples are UTF-8...
for nonUTF8 in \
	examples/tclspice/tcl-testbench4/selectfromlist.tcl \
	examples/tclspice/tcl-testbench1/testCapa.cir \
	examples/tclspice/tcl-testbench1/capa.cir \
	ChangeLog \
	%{nil}
do
	%{_bindir}/iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
	%{__mv} -f $nonUTF8.conv $nonUTF8
done
git commit -m "Change files to UTF8" -a

# rpmlint warnings
find examples/ -type f -name ".cvsignore" -exec rm -rf {} ';'
find src/ -type f -name "*.c" -exec chmod -x {} ';'
find src/ -type f -name "*.h" -exec chmod -x {} ';'
find src/ -type f -name "*.l" -exec chmod -x {} ';'
find src/ -type f -name "*.y" -exec chmod -x {} ';'
git commit -m "Fix permission" -a || :

# Move spinit directory to arch-dependent
sed -i configure.ac -e '\@AC_DEFINE_UNQUOTED.*NGSPICEDATADIR@s|echo .dprefix/share/ngspice|echo %{_libdir}/ngspice|'
sed -i configure.ac -e '\@AC_DEFINE_UNQUOTED.*NGSPICELIBDIR@s|echo .dprefix/share/ngspice|echo %{_libdir}/ngspice|'
sed -i src/misc/ivars.c -e 's|\(["/]\)share/ngspice|\1%_lib/ngspice|'
sed -i src/misc/ivars.c -e 's|\(["/]\)lib/ngspice|\1%_lib/ngspice|'
grep -rl "(pkgdatadir)/" . | xargs sed -i -e 's|(pkgdatadir)/|(pkglibdir)/|'
git commit -m "move spinit directory to arch-dependent" -a

# Fix Tclspice's examples
sed -i \
	's|load "../../../src/.libs/libspice.so"|lappend auto_path "%{_libdir}/tclspice"\npackage require spice|' \
	examples/tclspice/*/*.{tcl,sh}
sed -i \
	's|load ../../../src/.libs/libspice.so|lappend auto_path "%{_libdir}/tclspice"\npackage require spice|' \
	examples/tclspice/*/*.{tcl,sh}
sed -i \
	's|spice::codemodel [\./][\./]*src/xspice/icm/spice2poly/|spice::codemodel %{_libdir}/tclspice/ngspice/|' \
	examples/tclspice/tcl-testbench*/tcl-testbench*.sh
git commit -m "Fix Tclspice's examples" -a

# Fixed minor CVS build
sed -i \
	"s|AM_CPPFLAGS =|AM_CPPFLAGS = -I\$(top_srcdir)/src/maths/ni |" \
	src/spicelib/analysis/Makefile.am
git commit -m "Fix include path" -a

export ACLOCAL_FLAGS=-Im4
./autogen.sh \
%if %{with adms}
	--adms \
%endif
	%{nil}
git commit -m "Execute autogen" -a || :

chmod +x configure

%build
%set_build_flags
%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"

export ASAN_OPTIONS=detect_leaks=0
%endif

%if 0%{?usegitbare} >= 1
cd %{name}
%endif

# ---- Tclspice ----------------------------------------------------------------
# Adding BLT support
export CFLAGS="%{optflags} -I%{_includedir}/blt"

# Make builddir for tclspice
%{__mkdir} -p tclspice
%{__cp} -Rl `ls . | grep -v tclspice` tclspice

# Configure tclspice
cd tclspice
sed -i configure* \
	-e 's|\#define NGSPICEDATADIR "\`echo %{_libdir}/ngspice\`"|\#define NGSPICEDATADIR "\`echo %{_libdir}/tclspice/ngspice\`"|'
sed -i src/misc/ivars.c -e 's|/%_libdir/ngspice|/%_lib/tclspice/ngspice|'

# direct access to Tcl_Interp->result deprecated in tcl8.6,
# remaining usage cannot be replaced by Tcl_SetResult
export CPPFLAGS=-DUSE_INTERP_RESULT

# comment by Mamoru TASAKA (20170330)
# Looking at the actually source code, --enable-newpred does not seem to
# make sense, and it seems to cause calculation error (bug 844100, bug 1429130)
#
# (20190120) Remove some obsolete or dangerous configure option
# by the request from the upstream
%configure \
	--disable-silent-rules \
%if %{with adms}
	--enable-adms \
%endif
	--enable-xspice \
	--enable-klu \
	--enable-osdi \
	--enable-maintainer-mode \
	--enable-dependency-tracking \
	--enable-cider \
%if 0
	--enable-newpred \
%endif
	--enable-openmp \
	--enable-predictor \
	--enable-shared \
	--with-readline=yes \
	--with-tcl=%{_libdir}/ \
	--libdir=%{_libdir}/tclspice \
	%{nil}

%{__make} -k
# Once install to the temp dir
rm -rf $(pwd)/../INST-TCLSPICE
%{__make} INSTALL="install -p" install DESTDIR=$(pwd)/../INST-TCLSPICE
cd ..
# ------------------------------------------------------------------------------

for opt in SHARED NOSHARED
do
	SHARED_OPT=""
	if test x$opt == xSHARED
	then
		SHARED_OPT="$SHARED_OPT --with-ngshared"
		# bug 1927628
		SHARED_OPT="$SHARED_OPT --with-readline=no"
	else
		SHARED_OPT="$SHARED_OPT --without-ngshared"
		SHARED_OPT="$SHARED_OPT --with-readline=yes"
	fi
%configure \
	--disable-silent-rules \
	${SHARED_OPT} \
%if %{with adms}
	--enable-adms \
%endif
	--enable-xspice \
	--enable-osdi \
	--enable-klu \
	--enable-maintainer-mode \
	--enable-dependency-tracking \
	--enable-cider \
%if 0
	# bug 844100, bug 1429130
	--enable-newpred \
%endif
	--enable-openmp \
	--enable-predictor \
	--enable-shared \
	--libdir=%{_libdir} \
	%{nil}

%{__make} clean
# No parallel make
%{__make} -k
# Once install to the temp dir
rm -rf $(pwd)/INST-NGSPICE-${opt}
%{__make} INSTALL="install -p" install DESTDIR=$(pwd)/INST-NGSPICE-${opt}
find $(pwd)/INST-NGSPICE-${opt} -type f | sort

done

%install
%if 0%{?usegitbare} >= 1
cp -p %{name}/COPYING .
cd %{name}
%endif

# ---- Tclspice ----------------------------------------------------------------

# Clean up unneeded / duplicate files also installed from ngspice
pushd INST-TCLSPICE
rm -rf ./%{_libdir}/ngspice/include/
# see bug 1311869
rm -f ./%{_libdir}/tclspice/ngspice/scripts/spinit
# binary differ
# for --short-circuit
if [ -f .%{_bindir}/cmpp ] ; then
  mv .%{_bindir}/cmpp{,-tclspice}
fi
popd

# Install
# ref: https://sourceforge.net/p/ngspice/support-requests/34/
# For codemodel files, install non-shared version
# so, first, install ngshared version, then non-shared version
for opt in SHARED NOSHARED
do
	cp -a INST-NGSPICE-${opt}/* %{buildroot}
done
cp -a INST-TCLSPICE/* %{buildroot}

%{__rm} -rf \
	%{buildroot}%{_libdir}/tclspice/libspice.la \
	%{buildroot}%{_libdir}/tclspice/libspicelite.la \
	%{buildroot}%{_libdir}/libngspice.la \
	%{buildroot}%{_includedir}/config.h \
	%{nil}
# ------------------------------------------------------------------------------

# ADMS support
# It seems that the below is not needed, compiled into binary already
# (mtasaka, 20160628)
%if 0
cp -pr ./src/spicelib/devices/adms/ %{buildroot}%{_libdir}/%{name}
%endif

# Ensuring that all docs are under %%{_pkgdocdir}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr examples/ %{buildroot}%{_pkgdocdir}
install -cpm 0644 %{SOURCE1} %{buildroot}%{_pkgdocdir}/%{name}-%{majorver}.pdf

cp -a \
	Stuarts_Poly_Notes \
	FAQ \
	DEVICES \
	ANALYSES \
	%{buildroot}%{_pkgdocdir}
cp -a \
	AUTHORS \
	README* \
	BUGS \
	ChangeLog \
	NEWS \
	%{buildroot}%{_pkgdocdir}

# pull as debuginfo
chmod +x %{buildroot}%{_libdir}/ngspice/*.cm
chmod +x %{buildroot}%{_libdir}/tclspice/ngspice/*.cm

%check
export ASAN_OPTIONS=detect_leaks=0

%if 0%{?usegitbare} >= 1
cd %{name}
%endif

pushd tests

# See https://sourceforge.net/p/ngspice/bugs/544/
rm -rf USERPROFILE
mkdir USERPROFILE
echo "set ngbehavior=mc" > USERPROFILE/spice.rc
export USERPROFILE=$(pwd)/USERPROFILE

xvfb-run \
	-s "-screen 0 640x480x24" \
	make check

popd

%files
%{_bindir}/*
%{_libdir}/%{name}/ivlng.*
%{_mandir}/man1/*
%doc	%{_pkgdocdir}
%license COPYING

%files	-n tclspice
%doc	%{_pkgdocdir}/examples/tclspice
%dir	%{_libdir}/tclspice/
%dir	%{_libdir}/tclspice/%{name}
%{_libdir}/tclspice/libspice*.so*
%{_libdir}/tclspice/%{name}/*.cm
%{_libdir}/tclspice/%{name}/*.tcl
%{_libdir}/tclspice/%{name}/ivlng.*
%{_libdir}/tclspice/%{name}/scripts/

%files	codemodel
%dir	%{_libdir}/%{name}/
%{_libdir}/%{name}/*.cm
%{_libdir}/%{name}/scripts/

%files	-n libngspice
%{_libdir}/libngspice.so.0*

%files	-n libngspice-devel
%{_libdir}/pkgconfig/ngspice.pc
%{_libdir}/libngspice.so
%{_includedir}/ngspice/

%changelog
* Sun Jan 12 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 44.2-1
- Update to 44.2

* Mon Dec 30 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 44-1
- Update to 44

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 43-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 43-2
- Apply upstream patch for fixing one byte ahead access in string manipulation

* Sun Jul 14 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 43-1
- Update to 43

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 42-2
- Fix compilation with -Werror=incompatible-pointer-types

* Fri Dec 29 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 42-1
- Update to 42
- Kill --with-adms
- Enable --with-klu

* Wed Aug 16 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 41-1
- Update to 41

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 40-1
- Update to 40

* Fri Feb  3 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 39.3-1
- Update to 39.3

* Wed Feb  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 39.2-1
- Update to 39.2

* Wed Feb  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 39-1
- Update to 39

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 38-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 29 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 38-1
- Update to 38

* Wed Oct 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 37-2
- Split out codemodel files, and make ngspice, libngspice require codemodel
- Move scripts to %%_libdir, they were arch-dependent actually

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 37-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 37-1
- Update to 37

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 36-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 36-1
- Update to 36

* Mon Aug  9 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 35-1
- Update to 35

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 34-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 34-2
- build --with-ngshared with --with-readline=no to aviod missing
  symbol for history_file, requested by the upstream

* Tue Feb  2 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 34-1
- Update to 34
  - Don't enable --enable-oldapps
  - cmpp not installed any more
  - header file inclusion change

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 33-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 33-1
- Update to 33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32.2-1.2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May  6 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 32.2-1
- 32.2 tagged

* Tue May  5 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 32-1.D20200505gitbbe81ca
- Update to 32
- Use upstream git to use some upstream fixes since release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 31-4.respin2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct  7 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 31-3.respin2
- 31 tarball again respun

* Sun Sep 29 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 31-2.respin1
- 31 tarball respun

* Wed Sep 25 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 31-1
- Update to 31

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 30-4
- Rebuild for readline 8.0

* Tue Feb 05 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 30-3
- F-30: mass rebuild

* Sun Jan 20 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 30-2
- Remove some obsolete or dangerous configure options by
  the request from the upstream (and ref: bug 1666505)

* Tue Jan  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 30-1
- Update to 30

* Mon Dec 31 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 29-2
- Build shared library (bug 1440904 and so on)

* Sun Dec 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 29-1
- Update to 29

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 28-1
- Update to 28 (bug 1591460)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 27-1
- Update to 27

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 26-8
- Disable newpred mode (bug 844100, bug 1429130)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 26-6
- Rebuild for readline 7.x

* Sun Jul  3 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 26-5
- Link libspice.so with -lBLT or -lBLTlite, depending on whether in tk mode or
  not (bug 1047056, debian bug 737279)

* Tue Jun 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 26-4
- Don't get ngspice files overwritten by files from tclspice side
  (bug 1311869)
- rearrange files entries between ngspice / tclspice
  - move tclspinit into tclspice
  - rename tclspice side cmpp
  - also don't overwrite ngspice header files by tclspice side

* Mon Jun 27 2016 Mamoru TASAKA <mtasaka@fedoraproject.org>
- spec file clean up
- Don't install adms source and compiled .o objects, they are
  already linked into ngspice and tclspice shared library

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Eduardo Mayorga <mayorga@fedoraproject.org> - 26-2
- Use %%global instead of %%define

* Thu Oct 08 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 26-1
- Update to 26 release.
- use licence tag
- use configure macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 23-8
- Fix FTBFS with tcl-8.6 (#1106295)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 23-6
- Introduce %%_pkgdocdir (RHBZ #994004).
- Fix bogus changelog date.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 23-1
- New upstream sources with various bug fixes
- Upstream added #include <ftedev.h> to src/include/tclspice.h

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-6.cvs20101113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-5.cvs20101113
- new upstream sources with various bug fixes

* Sat Aug 21 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-4.cvs20100821
- enabling adms support

* Sun Aug 01 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-3.cvs20100719
- new fixes from development trunk

* Sun Jul 11 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-2.cvs20100620
- added bison and byacc as BR

* Thu Jul 01 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-1.cvs20100620
- release -21 with BSIMSOI support for < 130nm designs

* Sat Jun 19 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 20-4.cvs20100619
- prerelease -21 with BSIMSOI support for < 130nm designs

* Tue Dec 8 2009  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 20-3
- Fixed build on CentOS-5

* Tue Dec 8 2009  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 20-2
- Improved interoperobability with xcircuit

* Mon Nov 16 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 20-1
- new upstream release

* Sun Aug 02 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 19-1
- new upstream release
- RHBZ #514484 A Long Warning Message (patched)
- RHBZ #511695 FTBFS ngspice-18-2.fc11

* Sat Feb 21 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 18-2
- x11 windows (help and plot) fixes #RHBZ 481525

* Sat Jan 10 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 18-1
- new upstream release

* Sun Jun 15 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-16
- Bugfix: #449409: FTBFS ngspice-17-14.fc9

* Fri Apr 18 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-15
- rebuild

* Fri Aug 24 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-13
- mass rebuild for fedora 8 - BuildID

* Mon Aug 06 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-12
- fixed ScriptletSnippets for Texinfo #246780
- moved documentations to -doc package

* Sat Mar 17 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-11
- droped patch: ngspice-bjt.patch, upstream will provide a better patch soon

* Sat Mar 17 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-10
- fixed bug #227519 in spec file - Ville Skyttä
- patch: ngspice-bjt.patch fixes the problem with bjt devices that have less than five nodes

* Tue Jan 09 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-9
- dropped --enable-cider since it requires non-opensource software
- dropped --enable-predictor from %%configure

* Tue Dec 19 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-8
- patch0 for xcircuit pipemode
- XCircuit can work as an ng-spice front-end
- fixed infodir to mean FE guidelines

* Sun Oct 15 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-7
- Fixed src/spinit.in for 64 bit

* Thu Oct 12 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-6
- Testing on 64 bit arch

* Mon Sep 04 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-5
- Added libXt-devel to include X headers

* Wed Aug 30 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 17-4
- Fix to pass compiler flags in xgraph.

* Tue Aug 29 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-3
- Fixed BR and script-without-shellbang for debug file

* Mon Aug 28 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-2
- Fixed BRs and excluded libbsim4.a
- Removed duplicates and useless ldconfig from %%post

* Sun Aug 27 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-1
- Initial Package for Fedora Extras
