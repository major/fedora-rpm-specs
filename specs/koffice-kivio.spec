
%global translations kivio-translations-20100511

Name:           koffice-kivio
Epoch:          3
Version:        1.6.3
Release:        70%{?dist}
Summary:        A flowcharting application

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.koffice.org/
Source0:        http://download.kde.org/stable/koffice-%{version}/src/koffice-%{version}.tar.bz2
# collected from svn://anonsvn.kde.org/home/kde/branches/stable/l10n/
# ./create_tarball_kivio.rb -n -a kivio
Source1:        %{translations}.tar.xz
# script used to fetch translations (patched extragear-tarball script)
Source100:      create_tarball_kivio.rb
# config file for the above script
Source101:      config.ini

# disable some nested subdirectories which are not needed for Kivio
Patch0:         koffice-1.6.3-only-kivio.patch
# rename koffice.po and kofficefilters.po because they conflict with KOffice 2
Patch1:         koffice-1.6.3-rename-po.patch
# fix kivio.desktop to validate
Patch2:         koffice-1.6.3-kivio-desktop.patch

# build the translations standalone, using the KDE 4 CMake framework
Patch50:        kivio-translations-20100511-standalone.patch

# fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
# fix aarch64 FTBFS due to libtool not liking the file output on *.so files
Patch303: kde3-libtool-aarch64.patch
# Fix configure bits compromised by LTO optimizations
Patch304: kdelibs-3.5.10-configure.patch
# autoconf 2.7x
Patch305: kde3-autoconf-version.patch
Patch306: koffice-kivio-configure-c99.patch

BuildRequires:  gcc-c++
# for kde-config --kde-version
BuildRequires:  kdelibs3-devel >= 3.5.10-50
# See http://bugzilla.redhat.com/244091
%global kdelibs3_ver %(kde-config --kde-version 2>/dev/null || echo 3.5.10)
BuildRequires:  automake libtool
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel
BuildRequires:  GraphicsMagick-devel
BuildRequires:  libart_lgpl-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  gettext-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl-interpreter

# for translations:
BuildRequires:  cmake kdelibs4-devel gettext kde-filesystem
BuildRequires: make

# directory ownership
Requires:       hicolor-icon-theme

Provides:       kivio = %{version}-%{release}
Obsoletes:      kivio < %{version}-%{release}

Requires:       %{name}-libs = %{version}-%{release}

Conflicts:      koffice-core < 3:1.7

# koffice-langpack-2:2.1.91-1 included translated Kivio documentation, so force
# upgrading to 2:2.1.91-2 which fixes that to prevent file conflicts
Conflicts:      koffice-langpack < 2:2.1.91-2

%description
%{summary}.

%package libs
Epoch:          0
Summary:        Runtime libraries for %{name}
Conflicts:      koffice-libs < 3:1.7
Requires:       kdelibs3 >= %{kdelibs3_ver}
License:        LGPLv2+
%description libs
%{summary}.


%prep
%setup -q -n koffice-%{version} -a 1
%patch -P0 -p1 -b .only-kivio
%patch -P1 -p1 -b .rename-po
%patch -P2 -p1 -b .kivio-desktop

pushd %{translations}
%patch -P50 -p1 -b .standalone
# rename koffice.po and kofficefilters.po because they conflict with KOffice 2
for i in po/* ; do
  if [ -f "$i/koffice.po" ] ; then
    mv -f "$i/koffice.po" "$i/koffice1.po"
  fi
  if [ -f "$i/kofficefilters.po" ] ; then
    mv -f "$i/kofficefilters.po" "$i/koffice1filters.po"
  fi
done
popd

# rename the KOffice README which conflicts with the Kivio one
mv README README.koffice

# build only the subdirectories needed for Kivio
echo "pics servicetypes lib kivio filters doc" >inst-apps

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .libtool-aarch64
%patch -P304 -p1 -b .configure
%patch -P305 -p1 -b .autoconf2.7x
%patch -P306 -p1 -b .c99
make -f admin/Makefile.common cvs


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh

%configure \
  --disable-rpath --disable-dependency-tracking \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --with-pic --enable-shared --disable-static \
  --with-extra-libs=%{_libdir} \
  --disable-final

# kill rpath harder, inspired by https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Removing_Rpath
# other more standard variants didnt work or caused other problems
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' libtool

%make_build

pushd %{translations}
%cmake_kde4 .
%make_build
popd


%install
%make_install

pushd %{translations}
make install/fast DESTDIR=%{buildroot}
popd

# Replace absolute symlinks with relative ones
pushd %{buildroot}%{_docdir}/HTML
for lang in *; do
  if [ -d $lang ]; then
    pushd $lang
    for i in */*; do
      [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../../common $i/common
    done
    popd
  fi
done
popd

desktop-file-validate %{buildroot}%{_datadir}/applications/kde/kivio.desktop

## unpackaged files
# libtool archives
rm -f %{buildroot}%{_libdir}/lib*.la
# devel headers
rm -rf %{buildroot}%{_includedir}
# devel symlinks
rm -f %{buildroot}%{_libdir}/libkiviocommon.so
rm -f %{buildroot}%{_libdir}/libko*.so
rm -f %{buildroot}%{_libdir}/libkstore.so
rm -f %{buildroot}%{_libdir}/libkwmf.so
# hyphenation dictionaries (Kivio doesn't support hyphenation)
rm -rf %{buildroot}%{_datadir}/apps/koffice/hyphdicts
# irrelevant general KOffice documentation files
rm -rf %{buildroot}%{_docdir}/HTML/en/koffice
rm -rf %{buildroot}%{_docdir}/HTML/en/koffice-apidocs

%find_lang kivio --with-kde
%find_lang koffice1
cat koffice1.lang >>kivio.lang
rm -f koffice1.lang
%find_lang koffice1filters
cat koffice1filters.lang >>kivio.lang
rm -f koffice1filters.lang

# dedupe translations, as find_lang queries both kde-config and kde4-config for
# the same documentation directory and takes files from both
sort -u kivio.lang >kivio-unique.lang
mv -f kivio-unique.lang kivio.lang


%files -f kivio.lang
%doc kivio/AUTHORS kivio/README README.koffice
%doc kivio/CHANGELOG kivio/CHANGES
%license kivio/LICENSE
%{_bindir}/kivio
%{_libdir}/libkdeinit_kivio.so
%{_libdir}/kde3/*
%{_datadir}/apps/kivio/
%{_datadir}/apps/koffice/
%{_datadir}/apps/kofficewidgets/
%{_datadir}/config.kcfg/kivio.kcfg
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/*.desktop
%{_datadir}/applications/kde/kivio.desktop
%{_datadir}/icons/hicolor/*/apps/kivio.png

%ldconfig_scriptlets libs

%files libs
%doc COPYING.LIB
%{_libdir}/lib*.so.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0:1.6.3-69
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  8 2022 Florian Weimer <fweimer@redhat.com> - 3:1.6.3-63
- Port configure script to C99 (#2151969)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3:1.6.3-61
- Sync KDE 3 autotools fixes from kdelibs3.spec (FTBFS #1987625, #1999505)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 3:1.6.3-53
- .spec cleanup, use %%make_build %%make_install %%license %%ldconfig_scriptlets
- BR: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3:1.6.3-50
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3:1.6.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3:1.6.3-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3:1.6.3-44
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3:1.6.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3:1.6.3-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3:1.6.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  2 2013 Ville Skyttä <ville.skytta@iki.fi> - 3:1.6.3-40
- Add URL to koffice source tarball.
- Compress translations tarball with xz.

* Mon Apr 01 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3:1.6.3-39
- use automake --force-missing to get aarch64 support (#925029/#925627)
- also use automake --copy (the default is symlinking)

* Sat Mar 09 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3:1.6.3-38
- revert to stock 1.6.3 (no useful changes in the Trinity snapshot)
- unify KDE 3 autotools fixes between packages, fixes FTBFS (#914117)
- clean up specfile

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3:1.6.3-37.trinity.20100511svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3:1.6.3-36.trinity.20100511svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3:1.6.3-35.trinity.20100511svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3:1.6.3-34.trinity.20100511svn
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3:1.6.3-33.trinity.20100511svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 18 2010 Kevin Kofler <Kevin@tigcc.ticalc.org>
- 3:1.6.3-32.trinity.20100511
- document tarball origin as requested in the review
- Conflicts: koffice-langpack < 2:2.1.91-2, documentation files conflict

* Sat May 15 2010 Kevin Kofler <Kevin@tigcc.ticalc.org>
- 3:1.6.3-31.trinity.20100511
- ship /usr/share/apps/koffice/koffice_shell.rc, Kivio needs it

* Thu May 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org>
- 3:1.6.3-30.trinity.20100511
- split out kivio from the koffice 1.6 packaging
