%global snapdate 20160506
%global commit d8c05cd022a15586e946da6e5d19d861a489ff5e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           alliance
Version:        5.1.1
Release:        35.%{snapdate}git%{shortcommit}%{?dist}
Summary:        VLSI EDA System
License:        GPL-2.0-only
URL:            https://soc-extras.lip6.fr/en/alliance-abstract-en/
Source:         http://www-asim.lip6.fr/pub/alliance/distribution/latest/alliance-%{version}.tar.bz2
Source1:        alliance.fedora

Source2:       alliance-tutorials-go-all.sh
Source3:       alliance-tutorials-go-all-clean.sh
Source4:       alliance-examples-go-all.sh
Source5:       alliance-examples-go-all-clean.sh

# Update alliance-5.1.1 to commit %%{shortcommit} from
# https://www-soc.lip6.fr/git/alliance.git
Patch00: 0000-alliance-5.1.1-git%{shortcommit}.patch

Patch01: 0001-Remove-stray-files.patch
Patch02: 0002-Update-autostuff.patch
Patch03: 0003-Consolidate-installation-dirs.patch
Patch04: 0004-Misc-installation-dirs-fixes.patch
Patch05: 0005-Use-inttypes-macros-to-print-int32_t.patch
Patch06: 0006-Use-ring_yy-instead-of-yy.patch
Patch07: 0007-Eliminate-CFLAGS.patch
Patch08: 0008-Rework-Makefile.ams.patch
Patch09: 0009-Misc.-doc-fixes.patch
Patch10: 0010-Fedora-profiles.patch
# Bashisms in /etc/profile.d/alc_env.csh
Patch11: 0011-Use-setenv-instead-of-set-RHBZ-1337691.patch
# Flex compatibility issues
Patch12: 0012-Remove-yylineno.patch
# GCC-10 incompatibilities
Patch13: 0013-GCC-10-fixes.patch


BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  libstdc++-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  m4
BuildRequires:  tex(epsf.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(picinpar.sty)
BuildRequires:  tex(subfigure.sty)
BuildRequires:  tex(wrapfig.sty)
BuildRequires:  transfig
BuildRequires:  /usr/bin/convert
BuildRequires:  /usr/bin/dvipdf
BuildRequires:  autoconf automake libtool

%if 0%{?rhel}
BuildRequires:  openmotif-devel
BuildRequires:  pkgconfig
%else
BuildRequires:  motif-devel
%endif
Requires:       xorg-x11-fonts-misc
# RHBZ 442379
Requires(post): %{name}-libs%{?_isa} = %{version}-%{release}

%description
Alliance is a complete set of free cad tools and portable libraries for VLSI
design. It includes a vhdl compiler and simulator, logic synthesis tools,
and automatic place and route tools. A complete set of portable cmos libraries
is provided. Alliance is the result of a twelve year effort spent at SoC
department of LIP6 laboratory of the Pierre & Marie Curie University (Paris
VI, France). Alliance has been used for research projects such as the 875 000
transistors StaCS superscalar microprocessor and 400 000 transistors ieee
Gigabit HSL Router.

Alliance provides CAD tools covering most of all the digital design flow:

 * VHDL Compilation and Simulation
 * Model checking and formal proof
 * RTL and Logic synthesis
 * Data-Path compilation
 * Macro-cells generation
 * Place and route
 * Layout edition
 * Netlist extraction and verification
 * Design rules checking

Alliance is listed among Fedora Electronic Lab (FEL) packages.

%package        libs
Summary:        Alliance VLSI CAD System - Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       electronics-menu

%description    libs
Architecture dependent files for the Alliance VLSI CAD Sytem.

%package        devel
Summary:        Alliance VLSI CAD System - Development libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
%{summary}

%package        doc
Summary:        Alliance VLSI CAD System - Documentations
BuildArch:      noarch
Requires:       gnuplot
BuildRequires:  tetex-latex
BuildRequires:  make

%description    doc
Documentation and tutorials for the Alliance VLSI CAD Sytem.

%prep
%setup -qn %{name}
%patch -P00 -p2

%patch -P01 -p2
%patch -P02 -p2
%patch -P03 -p2
%patch -P04 -p2
%patch -P05 -p2
%patch -P06 -p2
%patch -P07 -p2
%patch -P08 -p2
%patch -P09 -p2
%patch -P10 -p2
%patch -P11 -p2
%patch -P12 -p2
%patch -P13 -p2

pushd src > /dev/null

# Don't build attila
rm -r attila

# Setup auto*stuff
./autostuff

# The configure.ins confuse rpm
# rename them into configure.in~
sed -i -e 's/configure.in/configure.in~/g' autostuff
for x in $(find */* -name configure.in); do
mv $x $x~
done

chmod +x configure

cp -p %{SOURCE1} .
sed -i "s|ALLIANCE_TOP/bin|%{_libdir}/alliance/bin|" distrib/*.desktop

# ------------------------------------------------------------------------------

## Convert to UTF-8
for nonUTF8 in \
  FAQ \
  alcban/man1/alcbanner.1 \
  distrib/doc/alc_origin.1 \
  loon/doc/loon.1 \
  boog/doc/boog.1 \
  m2e/doc/man1/m2e.1 \
  documentation/overview/overview.tex \
  documentation/alliance-examples/tuner/build_tuner \
  documentation/alliance-examples/tuner/README \
  documentation/alliance-examples/tuner/tuner.vbe \
  documentation/alliance-examples/mipsR3000/sce/mips_dpt.c \
  documentation/alliance-examples/mipsR3000/asm/mips_defs.h \
; do \
  %{_bindir}/iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
  mv -f $nonUTF8.conv $nonUTF8
done

pushd documentation/alliance-examples/
#wrong-file-end-of-line-encoding
sed -i 's/\r//' mipsR3000/asm/*
popd

find documentation/tutorials/ \
   \( -name *.vbe  -o \
    -name *.pat  -o \
    -name *.vhdl -o \
    -name *.vst  -o \
    -name *.c \) \
    -exec chmod 0644 {} ';'
popd > /dev/null

%build
# The C parts use implicit ints, implicit function declarations,
# and old-style function declarations heavily.
%global build_type_safety_c 0
export CFLAGS="%build_cflags -std=gnu89"
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
pushd src > /dev/null
%configure --enable-alc-shared             \
           --disable-static                \
           --prefix=%{_libdir}/%{name}     \
           --bindir=%{_libdir}/%{name}/bin \
           --libdir=%{_libdir}/%{name}/lib \
           --includedir=%{_libdir}/%{name}/include \
           --docdir=%{_pkgdocdir} \
           --mandir=%{_mandir}

# Is not parallel-build-safe
make
popd

%install
pushd src > /dev/null
%make_install

# Add automated scripts to examples
#install -pm 755 %{SOURCE4} alliance-examples/go-all.sh
#install -pm 755 %{SOURCE5} alliance-examples/go-all-clean.sh

#pushd alliance-examples/
#    # FEL self test for alliance
#    #./go-all.sh 2>&1 | tee self-test-examples.log
#    # clean temporary files
#    ./go-all-clean.sh
#popd

find %{buildroot} -name '*.la' -delete -print

# Adding icons for the menus
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
cp -p distrib/*.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

# desktop files with enhanced menu from electronics-menu now on Fedora
# thanks Peter Brett
for d in distrib/*.desktop; do
desktop-file-install --dir %{buildroot}%{_datadir}/applications/ $d
done

# protecting hardcoded links
#ln -sf ../../..%{_datadir}/%{name}/cells %{buildroot}%{_prefix}/cells
#ln -sf ../../..%{_datadir}/%{name}/etc   %{buildroot}%{_prefix}/etc
#ln -sf ../../..%{_datadir}/%{name}/man   %{buildroot}%{_prefix}/man

# rename manpages to avoid conflicts
# RHBZ 252941
pushd $RPM_BUILD_ROOT%{_mandir} > /dev/null
/usr/bin/rename .1 .1alc man1/*
/usr/bin/rename .3 .3alc man3/*
/usr/bin/rename .5 .5alc man5/*
# Reflect man page renamer to man page includes
sed -i -e 's,^\(.so man[13]/alc_.*.[13]\)$,\1alc,' man*/*
popd > /dev/null

# Rename alliance subdir into html
mv %{buildroot}%{_pkgdocdir}/alliance %{buildroot}%{_pkgdocdir}/html
# Directly install files to go into 5%{_pkgdocdir}
install -m 644 README CHANGES FAQ alliance.fedora %{buildroot}%{_pkgdocdir}


%{__mkdir} -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
cat > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf << EOF
# Alliance VLSI design system
%{_libdir}/%{name}/lib
EOF

%{_fixperms} %{buildroot}/*
popd > /dev/null

%post
source %{_sysconfdir}/profile.d/alc_env.sh

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_pkgdocdir}/README
%{_pkgdocdir}/CHANGES
%{_pkgdocdir}/FAQ
%{_pkgdocdir}/alliance.fedora
%license src/LICENCE src/COPYING*

%{_datadir}/alliance
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/applications/*.desktop
%dir %{_libdir}/alliance
%{_libdir}/alliance/bin
%{_mandir}/man1/*.1*
%config(noreplace) %{_sysconfdir}/alliance
%config(noreplace) %{_sysconfdir}/profile.d/alc_env.*

%files devel
%dir %{_libdir}/alliance
%{_libdir}/alliance/include
%dir %{_libdir}/alliance/lib
%{_libdir}/alliance/lib/*.so
%{_mandir}/man3/*.3*

%files libs
%dir %{_libdir}/alliance
%dir %{_libdir}/alliance/lib
%{_libdir}/alliance/lib/lib*.so.*
%{_mandir}/man5/*.5*
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/*

%files doc
%{_pkgdocdir}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-35.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-34.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-33.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-32.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 5.1.1-31.20160506gitd8c05cd
- Set build_type_safety_c to 0 (#2187002)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-30.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 15 2023 Florian Weimer <fweimer@redhat.com> - 5.1.1-29.20160506gitd8c05cd
- Build in C89 mode (#2187002)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-28.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.1.1-27.20160506gitd8c05cd
- Convert license to SPDX.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-26.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-25.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-24.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-23.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Adam Jackson <ajax@redhat.com> - 5.1.1-22.20160506gitd8c05cd
- Remove unused BuildRequires: libXp-devel

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-21.20160506gitd8c05cd
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 5.1.1-20.20160506gitd8c05cd
- Force C++14 as the code is not ready for C++17

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-19.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.1.1-18.20160506gitd8c05cd
- Drop lesstif.
- Spec file cleanup.
- Add 0013-GCC-10-fixes.patch (F32FTBFS, RHBZ#1799147).

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-17.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-16.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-15.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-14.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.1.1-13.20160506gitd8c05cd
- BR: /usr/bin/dvipdf instead of ghostscript (F28FTBFS).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-12.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.1.1-11.20160506gitd8c05cd
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-10.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-9.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-8.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-7.20160506gitd8c05cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 20 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.1.1-6.20160506gitd8c05cd
- Upstream update.
- Rebase patches.
- Remove reference to FLEX_BETA.

* Fri May 20 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.1.1-5.20160220git10a7b7e
- Remove bashisms in /etc/profile/alc_env.csh (RHBZ#1337691).
- Work around flex-2.6.0 compatibility issues triggering a FTBFS.

* Tue Mar 01 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.1.1-4.20160220git10a7b7e
- Rework spec.
- Add upstream changes.
- Rework package configuration.
- Introduce *-devel.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 27 2015 Björn Esser <fedora@besser82.io> - 5.1.1-2
- Rebuilt for libXm so-name bump
- Use %%license
- Cleanup trailing whitespace

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 19 2014 Christopher Meng <rpm@cicku.me> - 5.1.1-0
- Update to 5.1.1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-40.20090901snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 5.0-39.20090901snap
- Add missing tex BRs (#913874, #991959, #1105945)
- Fix FTBFS with -Werror=format-security
- Fix FTBFS with latest bison
- Remove unneeded macros

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-38.20090901snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-37.20090901snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-36.20090901snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-35.20090901snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-34.20090901snap
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-33.20090901snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-32.20090901snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 02 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-31.20090901snap
- updated to upstream's 20090901 snapshot
- Removed all patches which are accepted by upstream

* Thu Aug 27 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-30.20090827snap
- updated to upstream's 20090828 snapshot
- merged patches with upstream's snapshot: 64 bits stability patches and upstream enhancements
- fixed EPEL-5 build

* Sat Aug 8 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-29.20070718snap
- improved rawhide build with respect to the broken patches

* Thu Jul 9 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-28.20070718snap
- improved stability on 64 bit architecture
- Patches (14 to 100) added along with new features from upstream

* Sat Jul 4 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-27.20070718snap
- improved autogeneration of documentation and fixed the examples

* Tue Feb 24 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-26.20070718snap
- fixed build due to new releases of flex and bison

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-25.20070718snap
 - Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 01 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-24.20070718snap
- Improved VHDL generic implementation

* Mon Nov 10 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-23.20070718snap
- Added Requires xorg-x11-fonts-misc to fix launch crash

* Mon Nov 3 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-22.20070718snap
- rebuild for F10

* Mon Sep 15 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-21.20070718snap
- Bugfix : Alliance incorrectly mungs your path and adds the cwd to the path #459336
- Bugfix : Latest alc_env fixes broken system man path #452645

* Mon Aug 04 2008 Aanjhan Ranganathan <aanjhan [AT] tuxmaniac DOT com> - 5.0-20.20070718snap
- Bumped release version to match changelog

* Fri Aug 01 2008 Aanjhan Ranganathan <aanjhan [AT] tuxmaniac DOT com> - 5.0-16.20070718snap
- Rebuild using latest lesstif-devel. For #368441
- Temporarily set fuzz parameter of patch system to be 2

* Fri May 30 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-16.20070718snap
- Bugfix /etc/profile.d/alc_env.csh problem #449062 #448480

* Mon May 26 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-15.20070718snap
- Bugfix: error in postinstall scriptlet: /etc/profile.d/alc_env.sh not found #442379
- Bugfix: /etc/profile.d/alc_env.csh assumes MANPATH is preset #440083

* Tue May 20 2008 Thibault North < tnorth [AT] fedoraproject DOT org> - 5.0-14.20070718snap
- Add to Electronics Menu

* Fri Mar 21 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-13.20070718snap
- Requiring new FEL menu structure
- Fixing previous desktop files
- closing unconfirmed bug #427691
- fixing multilibs issues #340621

* Tue Mar 18 2008 Thibault North < tnorth [AT] fedoraproject DOT org> - 5.0-13.20070718snap
- dropped patch4: alliance-tutorials.patch
- fixed TexLive related issues for documentation
-   commenting previous make in directory tutorials
-   attached tutorials made in F8 Werewolf
- dropped BR :tetex-latex
- added patch4: including more useful includes to C files
- fixed bug #434020 : alliance failed massrebuild attempt for GCC4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.0-12.20070718snap
- Autorebuild for GCC 4.3

* Sun Feb 10 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-11.20070718snap
- mass rebuild for gcc43 on rawhide
- ensuring multilibs (#340621)

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-10.20070718snap
- complying to freedesktop policies - categories

* Sat Aug 18 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-9.20070718snap
- fixing desktop files
- fixing MANPATH and PATH for proper priority

* Thu Aug 16 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-8.20070718snap
- fixing conflicts with QuantLib-doc package (#252941)
- update license macro to comply with new guidelines)

* Sun Aug 12 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-7.20070718snap
- moved Architecture independent files to %%{_datadir}/%%{name}
- Uses verbs in the comments line for desktop files

* Thu Aug 02 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-6.20070718snap
- chose libdir/alliance as prefix
- added new icons to the menus
- removed useless attila
- fixed MANPATH override

* Sat Jul 28 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-5.20070718snap
- fixed unused-direct-shlib-dependency and undefined-non-weak-symbol warnings

* Tue Jul 24 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-4.20070718snap
- removed X-Desktop-File-Install-Version=0.10 from desktop files
- moved the alc_env to /etc/profile.d
- updated to meet reviewer's statements - #248649

* Thu Jul 19 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-3.20070718snap
- New upstream release which includes bug fixes

* Wed Jul 18 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-2.20060509snap
- minor fixes to the tutorials + added transfig ghostscript tetex-latex as BR
- corrected some hardcoded links in the scripts
- removed %%preun and updated alliance.fedora
- spec file updated to satisfy the review

* Tue Jul 17 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-1
- prepared spec file for review and spec clean ups
- removed rm and ln from %%post and %%preun
- removed log.3.gz from mandir since it's a duplicate and conflicts with man-pages

* Sat Jul 14 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-0.7
- since it is not parallel-build-safe, smp mflags are removed : (by wwoods)
- added missing BR : flex : (by wwoods)
- added missing BR : bison: (by rdieter)

* Fri Jul 13 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-0.6
- removing useless copyrighted lines from .ioc files
- added alliance.fedora among the %%doc

* Thu Jul 12 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-0.5
- removing copyrighted materials
- patching the remaining examples so that they will still be valid under another folder

* Wed Jul 04 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-0.4
- removing unwanted debug duplicates

* Wed May 02 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-0.3
- added desktop files

* Wed Feb 14 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-0.2
- fixing documentations

* Wed Dec 13 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 5.0-0.1
- Initial package

* Thu Feb 17 2005 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Synch with current version: bug & compliance with gcc 3.4.x.

* Fri Jul 16 2004 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Added Tutorial sub-package (now managed by autoconf/automake).
- Removed release tag, must be given at compile time using the
  --define command line argument of rpmbuild (see mkdistrib).

* Sat Nov 15 2003 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- assert is now in assert.h, patch mut.h to include it if
  GCC_VERSION >= 3003 (gcc >= 3.3.x).

* Sat Oct 18 2003 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Synched with 2003/10/18 version.
- Missing depcomp : added "--add-missing --copy" to the individual
  packages in autostuff, so the first who needs depcomp will add
  it at top level.

* Sun Oct 13 2002 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- autoconf m4 macros moved back in the Alliance source tree to avoid
  re-declaration on our development computers (on which the macros
  are in teh source tree).
- Adopt the versioning scheme from czo.
- Try to switch to dynamic libraries.

* Wed Jul 17 2002  Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Moved autoconf m4 macros to /usr/share/aclocal.
- Synched with the current CVS version of Alliance.

* Fri May 31 2002  Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- GenPat added.
- GenLib docs added.
- seplace/seroute/sea bug fixes.

* Thu May 16 2002  Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Corrected buggy substitution of ALLIANCE_TOP in alc_env.csh.
- Remove the alc_env.* scripts in "/etc/profile.d" only if this
  is the last package to be removed.

* Mon May  6 2002  Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Initial packaging for release 5.0 (alpha stage).
