#
# Copyright (c) 2010-2017 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%global coin_includedir %{_includedir}/Coin3
%global coin_htmldir %{_datadir}/Coin3

%global libopenal_SONAME libopenal.so.1
%global libsimage_SONAME libsimage.so.20

Summary: High-level 3D visualization library
Name: Coin3
Version: 3.1.3
Release: 39%{?dist}

# https://bitbucket.org/Coin3D/coin/wiki/Home tells BSD,
# but the tarball is GPLv2
License: GPL-2.0-only

# Note: Upstream moved
# Original upstream site was URL: http://www.coin3d.org
# Now 404...
# URL: https://bitbucket.org/Coin3D/coin/wiki/Home
URL: https://www.coin3d.org/

# Original coin3d.org tarball:
# Source0: ftp://ftp.coin3d.org/pub/coin/src/all/Coin-3.1.3.tar.gz
# Meanwhile, the coin3d.org-tarball moved to
Source0: https://bitbucket.org/Coin3D/coin/downloads/Coin-%{version}.tar.gz

Patch1: 0001-simage-soname.patch
Patch2: 0002-openal-soname.patch
Patch3: 0003-man3.patch
Patch4: 0004-doxygen.patch
Patch5: 0005-gcc-4.7.patch
Patch6: 0006-inttypes.patch
Patch7: 0007-Convert-to-utf-8.patch
Patch8: 0008-Convert-to-utf-8.patch
Patch9: 0009-Convert-to-utf-8.patch
Patch10: 0010-GCC-4.8.0-fixes.patch
Patch11: 0011-Fix-SoCamera-manpage.patch
Patch12: 0012-memhandler-initialization.patch
Patch13: 0013-Use-NULL-instead-of-0.patch

BuildRequires: libGLU-devel
BuildRequires: libXext-devel

BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: doxygen
BuildRequires: /usr/bin/rename
BuildRequires: boost-devel
BuildRequires: /usr/bin/perl
BuildRequires: make

%description
Coin is a 3D graphics library with an Application Programming Interface
based on the Open Inventor 2.1 API.

%package devel
Summary: Development files for Coin
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: zlib-devel bzip2-devel
Requires: fontconfig-devel
Requires: freetype-devel
Requires: libGLU-devel
Requires: pkgconfig
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives
Provides: pkgconfig(Coin)

%description devel
Development package for Coin3

%prep
%setup -q -n Coin-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1

# Update doxygen configuration
doxygen -u docs/coin.doxygen.in

find -name 'Makefile.*' -exec sed -i -e 's,\$(datadir)/Coin,$(datadir)/Coin3,' {} \;

# bogus permissions
find . \( -name '*.h' -o -name '*.cpp' -o -name '*.c' \) -a -executable -exec chmod -x {} \;

# convert sources to utf-8
for a in $(find . -type f -exec file -i {} \; | grep -i iso | sed -e 's,:.*,,'); do \
  /usr/bin/iconv -f ISO-8859-1 -t utf-8 $a > $a~; \
  mv $a~ $a; \
done

sed -i -e 's,@LIBSIMAGE_SONAME@,"%{libsimage_SONAME}",' \
  src/glue/simage_wrapper.cpp
sed -i -e 's,@LIBOPENAL_SONAME@,"%{libopenal_SONAME}",' \
  src/glue/openal_wrapper.cpp

# HACK: Remove rid of %%optflags and friends
sed -i -e "s| @COIN_EXTRA_LDFLAGS@||" -e "s| @COIN_EXTRA_CFLAGS@||" Coin.pc.in coin.cfg.in

# get rid of bundled boost headers
rm -rf include/boost

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
make %{?_smp_mflags}

# Strip the default libdir
sed -i -e "s,\-L%{_libdir} ,," coin-default.cfg

# coin-config is arch dependent
sed -i -e "s,/share/Coin/conf/,/%{_lib}/Coin3/conf/,g" bin/coin-config

%install
make DESTDIR=$RPM_BUILD_ROOT install

pushd $RPM_BUILD_ROOT%{_mandir} > /dev/null
/usr/bin/rename .1 .1coin3 man1/*
/usr/bin/rename .3 .3coin3 man3/*
popd > /dev/null
rm -f ${RPM_BUILD_ROOT}%{_libdir}/lib*.la

install -d -m 755 ${RPM_BUILD_ROOT}%{_libdir}/Coin3
mv ${RPM_BUILD_ROOT}%{_datadir}/Coin3/conf ${RPM_BUILD_ROOT}%{_libdir}/Coin3

mv ${RPM_BUILD_ROOT}%{_bindir}/coin-config ${RPM_BUILD_ROOT}%{_libdir}/Coin3/coin-config
ln -s %{_libdir}/Coin3/coin-config ${RPM_BUILD_ROOT}%{_bindir}/coin-config
mv ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/Coin.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/Coin3.pc
ln -s %{_libdir}/pkgconfig/Coin3.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig/Coin.pc
mv ${RPM_BUILD_ROOT}%{_datadir}/aclocal/coin.m4 ${RPM_BUILD_ROOT}%{_datadir}/aclocal/coin3.m4
ln -s %{_datadir}/aclocal/coin3.m4 ${RPM_BUILD_ROOT}%{_datadir}/aclocal/coin.m4


%ldconfig_scriptlets

%post devel
link=$(readlink -e "%{_bindir}/coin-config")
if [ "$link" = "%{_bindir}/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi
if [ "$link" = "%{_libdir}/Coin3/coin-config" ]; then
  rm -f %{_bindir}/coin-config
fi

/usr/sbin/alternatives --install "%{_bindir}/coin-config" coin-config \
  "%{_libdir}/Coin3/coin-config" 60 \
  --slave %{_libdir}/pkgconfig/Coin.pc Coin.pc %{_libdir}/pkgconfig/Coin3.pc \
  --slave %{_datadir}/aclocal/coin.m4 coin.m4 %{_datadir}/aclocal/coin3.m4 \
  --slave %{_libdir}/libCoin.so libCoin.so %{_libdir}/libCoin.so.60

%preun devel
if [ $1 = 0 ]; then
  /usr/sbin/alternatives --remove coin-config "%{_libdir}/Coin3/coin-config"
fi

%files
%doc AUTHORS README THANKS FAQ*
%license LICENSE.GPL COPYING
%dir %{_datadir}/Coin3
%{_datadir}/Coin3/scxml
%{_libdir}/libCoin.so.*

%files devel
%ghost %{_bindir}/coin-config
%{coin_includedir}
%ghost %{_libdir}/libCoin.so
%{_datadir}/aclocal/coin3.m4
%ghost %{_datadir}/aclocal/coin.m4
%dir %{_datadir}/Coin3
%{_datadir}/Coin3/draggerDefaults
%{_datadir}/Coin3/shaders
%{_libdir}/Coin3
%{_mandir}/man?/*
%doc %{coin_htmldir}/Coin
%{_libdir}/pkgconfig/Coin3.pc
%ghost %{_libdir}/pkgconfig/Coin.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb  8 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.3-31
- Drop ldflags from Libs line in pkgconf file (avoids issues with
  https://fedoraproject.org/wiki/Changes/Package_information_on_ELF_objects)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-19
- Add 0013-Use-NULL-instead-of-0.patch (Fix F26FTBFS, GCC-7.0).
- Drop fedora < 24.

* Mon Sep 05 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-18
- BR: /usr/bin/perl (Fix F25FTBFS).

* Fri Apr 22 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-17
- Initialize memhandler member properly (bug 1323159)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-15
- Move COPYING to %%license.

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-14
- Work-around Fedora's freetype header chaos.

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 3.1.3-13
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.1.3-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.1.3-10
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.3-8
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 25 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-7
- Remove %%optflags and %%__global_ld_flags from *.pc and *.cfg.

* Sun Feb 22 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-6
- Don't use bundled boost-headers.
- Add %%license.

* Fri Feb 20 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-5
- Fix SoCamera manpage (Add 0011-Fix-SoCamera-manpage.patch).
- Reflect Fedora > 20 freetype2 header location having changed.
- More minor spec changes.

* Tue Aug 20 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-4
- Minor spec update.

* Fri Apr 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-3.20130419.0
- Rebase patches.
- Move utf-8 changes into patches.
- Fix GCC-4.8.0 FTBFS.

* Mon Jan 09 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-3
- Add Coin-3.1.3-gcc-4.7.patch (Address gcc-4.7.0 FTBS).
- Update spec file copyright/licence.
- Reflect package being licensed GPLv2.
- Add Coin-3.1.3-inttypes.patch (Make *-devel multilib compliant;
  Fix autoconf clashes).

* Mon Nov 07 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-2
- Modernize spec.
- Don't use bash's "==" in alternatives' scriptlets.
- Don't ship README.*.
- Don't add build-time to doxygen generated docs.
- Eliminate warnings from doxygen-generated manpages.

* Sun Dec 26 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.3-1
- Fedora submission.
