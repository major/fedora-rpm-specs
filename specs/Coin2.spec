#
# Copyright (c) 2004-2018, 2022 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%define coin_includedir %{_includedir}/Coin2
%define coin_htmldir %{_datadir}/Coin2

%define libopenal_SONAME libopenal.so.1
%define libsimage_SONAME libsimage.so.20

Summary: High-level 3D visualization library
Name: Coin2
Version: 2.5.0
Release: 51%{?dist}

# LICENSE.GPL says ".. or later" but source files tell "GPLv2"
License: GPL-2.0-only
URL: http://www.coin3d.org

Source0: ftp://ftp.coin3d.org/pub/coin/src/all/Coin-%{version}.tar.gz

Patch0: Coin-2.4.6-simage-soname.diff
Patch1: Coin-2.4.6-openal-soname.diff
Patch2: Coin-2.4.6-man3.diff
Patch3: Coin-2.5.0-doxygen.diff
Patch4: Coin-2.5.0-gcc-4.7.0.diff
Patch5: Coin-2.5.0-inttypes.patch
Patch6: Coin-2.5.0-config.patch
Patch7: Coin-2.5.0-Use-NULL-instead-of-0.patch
Patch8: Coin2-configure-c99.patch

BuildRequires: gcc-c++
BuildRequires: libGLU-devel
BuildRequires: libXext-devel

BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: doxygen
BuildRequires: /usr/bin/rename
BuildRequires: /usr/bin/perl
BuildRequires: make

%description
Coin is a 3D graphics library with an Application Programming Interface
based on the Open Inventor 2.1 API.

%package devel
Summary: Development files for Coin
Requires: %{name} = %{version}-%{release}
Requires: zlib-devel bzip2-devel
Requires: fontconfig-devel
Requires: freetype-devel
Requires: libGLU-devel
Requires: pkgconfig
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Provides: pkgconfig(Coin)

%description devel
Development package for Coin2

%prep
%setup -q -n Coin-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1

# Update doxygen configuration
doxygen -u docs/coin.doxygen.in

find -name 'Makefile.*' -exec sed -i -e 's,\$(datadir)/Coin,$(datadir)/Coin2,' {} \;

# bogus permissions
find . \( -name '*.h' -o -name '*.cpp' -o -name '*.c' \) -a -executable -exec chmod -x {} \;

# convert sources to utf-8
for a in $(find . -type f -exec file -i {} \; | grep -i iso | sed -e 's,:.*,,'); do \
  /usr/bin/iconv -f ISO-8859-1 -t utf-8 $a > $a~; \
  mv $a~ $a; \
done

sed -i -e 's,@LIBSIMAGE_SONAME@,"%{libsimage_SONAME}",' \
  src/glue/simage_wrapper.c
sed -i -e 's,@LIBOPENAL_SONAME@,"%{libopenal_SONAME}",' \
  src/glue/openal_wrapper.c

%build
%configure \
	--includedir=%{coin_includedir} \
	--disable-dependency-tracking \
	--enable-shared \
	--disable-dl-libbzip2 \
	--disable-dl-glu \
	--disable-dl-zlib \
	--disable-dl-freetype \
	--disable-dl-fontconfig \
	--disable-spidermonkey \
	--enable-man \
	--enable-html \
	--enable-3ds-import \
	htmldir=%{coin_htmldir}/Coin \
	CPPFLAGS="$(pkg-config --cflags freetype2)"
%{make_build}

# Strip the default libdir
sed -i -e "s,\-L%{_libdir} ,," coin-default.cfg

# coin-config is arch dependent
sed -i -e "s,/share/Coin/conf/,/%{_lib}/Coin2/conf/,g" bin/coin-config

%install
%{make_install}

pushd $RPM_BUILD_ROOT%{_mandir} > /dev/null
/usr/bin/rename .1 .1coin2 man1/*
/usr/bin/rename .3 .3coin2 man3/*
popd > /dev/null
rm -f ${RPM_BUILD_ROOT}%{_libdir}/lib*.la

install -d -m 755 ${RPM_BUILD_ROOT}%{_libdir}/Coin2
mv ${RPM_BUILD_ROOT}%{_datadir}/Coin2/conf ${RPM_BUILD_ROOT}%{_libdir}/Coin2

mv ${RPM_BUILD_ROOT}%{_bindir}/coin-config ${RPM_BUILD_ROOT}%{_libdir}/Coin2/coin-config
ln -s %{_libdir}/Coin2/coin-config ${RPM_BUILD_ROOT}%{_bindir}/coin-config
mv ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/Coin.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/Coin2.pc
ln -s %{_libdir}/pkgconfig/Coin2.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/Coin.pc
mv ${RPM_BUILD_ROOT}%{_datadir}/aclocal/coin.m4 ${RPM_BUILD_ROOT}%{_datadir}/aclocal/coin2.m4
ln -s %{_datadir}/aclocal/coin2.m4 ${RPM_BUILD_ROOT}%{_datadir}/aclocal/coin.m4

%ldconfig_scriptlets

%post devel
link=$(readlink -e "%{_bindir}/coin-config")
if [ "$link" = "%{_bindir}/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi
if [ "$link" = "%{_libdir}/Coin2/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi

/usr/sbin/alternatives --install "%{_bindir}/coin-config" coin-config \
  "%{_libdir}/Coin2/coin-config" 40 \
  --slave %{_libdir}/pkgconfig/Coin.pc Coin.pc %{_libdir}/pkgconfig/Coin2.pc \
  --slave %{_datadir}/aclocal/coin.m4 coin.m4 %{_datadir}/aclocal/coin2.m4 \
  --slave %{_libdir}/libCoin.so libCoin.so %{_libdir}/libCoin.so.40

%preun devel
if [ $1 = 0 ]; then
  /usr/sbin/alternatives --remove coin-config "%{_libdir}/Coin2/coin-config"
fi

%files
%doc AUTHORS ChangeLog* README THANKS FAQ*
%license COPYING LICENSE*
%{_libdir}/libCoin.so.*

%files devel
%ghost %{_bindir}/coin-config
%{coin_includedir}
%ghost %{_libdir}/libCoin.so
%{_datadir}/aclocal/coin2.m4
%ghost %{_datadir}/aclocal/coin.m4
%dir %{_datadir}/Coin2
%{_datadir}/Coin2/draggerDefaults
%{_datadir}/Coin2/shaders
%{_libdir}/Coin2
%{_mandir}/man?/*
%doc %{coin_htmldir}/Coin
%{_libdir}/pkgconfig/Coin2.pc
%ghost %{_libdir}/pkgconfig/Coin.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Florian Weimer <fweimer@redhat.com> - 2.5.0-45
- Port configure script to C99

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-43
- Convert license to SPDX.
- Modernize spec.
- Update sources to sha512.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-35
- BR: gcc-c++ instead of gcc (RHBZ#1603265).

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-30
- Add Coin-2.5.0-Use-NULL-instead-of-0.patch (Fix F26FTBFS, RHBZ#1423093).
- Spec file cosmetics.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-28
- BR: /usr/bin/perl (Fix F25FTBFS).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-26
- Remove %%defattr.
- Add %%license.
- Fix bogus %%changelog entry.
- Drop Coin-2.5.0-freetype-fix.patch.
- Work-around Fedora's freetype header chaos.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.5.0-24
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Ralf Corsepius <corsepiu@fedoraproject.org> - 2.5.0-23
- Rebuilt for GCC-5.0.
- Fix bogus %%changelog entries.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Brent Baude <baude@us.ibm.com> - 2.5.0-20
- Added quotes around pkg config off freetype to fix configure issue
- Added patch to fix freetype headers after headers moved in recent
- freetype packages.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-18
- Update config.{guess,sub} to allow building for aarch64*
  (Add Coin2-2.5.0-config.patch).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 11 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-14
- Set licence tag to GPLv2.

* Wed Jan 11 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-13
- Add Coin-2.5.0-inttypes.patch (Make *-devel multilib compliant;
  Fix autoconf clashes).

* Thu Jan 05 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-12
- Fix gcc-4.7.0 FTBS (Add Coin-2.5.0-gcc-4.7.0.diff).

* Mon Nov 07 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-11
- Modernize spec.
- Don't use bash's "==" in alternatives' scriptlets.
- Don't ship README.*.
- Don't add build-time to doxygen generated docs.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-9
- Reflect upstream having changed URL.
- Introduce alternative coin-config to allow parallel installation of
  other Coin*-devel packages.
- Further minor *.spec cleanups.

* Sun Nov 22 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-8
- Eliminate /usr/share/Coin.
- Rename mans into *coin2.
- Fix broken calls to rename.

* Mon Sep 28 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.5.0-7
- Reflect openal/openal-soft changes.
- Work-around "file" reporting bogus results (BZ 526054).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Ralf Corsépius <rc040203@freenet.de> - 2.5.0-4
- Rebuild for gcc43.
- Update copyright.

* Thu Nov 29 2007 Ralf Corsépius <rc040203@freenet.de> - 2.5.0-3
- Rebuild with doxygen-1.5.3-1 (BZ 343601).

* Wed Oct 03 2007 Ralf Corsépius <rc040203@freenet.de> - 2.5.0-2
- Fix permissions on source files.
- Convert sources to utf-8.

* Tue Oct 02 2007 Ralf Corsépius <rc040203@freenet.de> - 2.5.0-1
- Upstream update.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 2.4.6-2
- Update license tag.

* Sun Apr 15 2007 Ralf Corsépius <rc040203@freenet.de> - 2.4.6-1
- Upstream update.
- Re-base the patches to 2.4.6.
- Spec file massage.

* Tue Feb 20 2007 Ralf Corsépius <rc040203@freenet.de> - 2.4.5-5
- Install coin-default.cfg into %%{_prefix}/%%{_lib}

* Mon Feb 19 2007 Ralf Corsépius <rc040203@freenet.de> - 2.4.5-4
- Filter errant -L%%_libdir from coin-config.cfg.
- Remove *.la.

* Fri Sep 15 2006 Ralf Corsépius <rc040203@freenet.de> - 2.4.5-3
- Add doxygen hack.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.4.5-2
- Mass rebuild.

* Tue May 30 2006 Ralf Corsépius <rc040203@freenet.de> - 2.4.5-1
- Upstream update.
- Drop gcc-4.1 patch.
- Spec file cleanup.

* Wed Feb 22 2006 Ralf Corsépius <rc040203@freenet.de> - 2.4.4-10
- Rename man3 manpages to .3sim (PR 182212).

* Sun Feb 19 2006 Ralf Corsepius <rc040203@freenet.de> - 2.4.4-9
- Rebuild.

* Mon Jan 16 2006 Ralf Corsepius <rc040203@freenet.de> - 2.4.4-8
- Add R: fontconfig-devel to devel package.

* Mon Jan 16 2006 Ralf Corsepius <rc040203@freenet.de> - 2.4.4-7
- Add R: freetype-devel to devel package.

* Thu Dec 22 2005 Ralf Corsepius <rc040203@freenet.de> - 2.4.4-6
- Remove hacks to mesa/X11 packaging bugs now reported to be fixed.

* Thu Dec 15 2005 Ralf Corsepius <rc040203@freenet.de> - 2.4.4-5
- More hacks for modular X11.
- Add Coin-2.4.4-gcc-4.1.diff.

* Mon Nov 21 2005 Ralf Corsepius <rc040203@freenet.de> - 2.4.4-4
- Try to work around modular X having broken package deps.

* Thu Sep 22 2005 Ralf Corsepius <ralf@links2linux.de> - 2.4.4-3
- Remove simacros patch.
- Remove libtool patch.
- Link against freetype2.

* Tue Sep 20 2005 Ralf Corsepius <ralf@links2linux.de> - 2.4.4-1
- Upstream update.

* Thu Jul 07 2005 Ralf Corsepius <ralf@links2linux.de> - 0:2.4.3-1
- Upstream update.

* Tue May 17 2005 Ralf Corsepius <ralf@links2linux.de> - 0:2.4.1-1
- Upstream update.
