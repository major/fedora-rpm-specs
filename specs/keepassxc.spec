%undefine __cmake_in_source_build
# EPEL7 not possible because libgcrypt version is 1.5

Name:           keepassxc
Version:        2.7.9
Release:        8%{?dist}
Summary:        Cross-platform password manager
# Automatically converted from old format: Boost and BSD and CC0 and GPLv3 and LGPLv2 and LGPLv2+ and LGPLv3+ and Public Domain - review is highly recommended.
License:        BSL-1.0 AND LicenseRef-Callaway-BSD AND CC0-1.0 AND GPL-3.0-only AND LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-LGPLv2+ AND LGPL-3.0-or-later AND LicenseRef-Callaway-Public-Domain
URL:            https://keepassxc.org/
Source0:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz
Source1:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz.sig
Source2:        https://keepassxc.org/keepassxc_master_signing_key.asc
# Patch0: fixes GNOME quirks on Wayland sessions. Read
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/3BVLBS4B3XHJEXFVGD7RK2ZMXZG6JQZT/
# read also https://github.com/keepassxreboot/keepassxc/pull/3520/files
#
# Patch0 improved by pewpeww https://src.fedoraproject.org/rpms/keepassxc/pull-request/1
#
# 23 March 2022 Germano Massullo's update: Jan Grulich said that Qt patch https://code.qt.io/cgit/qt/qtbase.git/commit/?id=dda7dab8274991e4a61a97c352d4367f8f815bb9
# is included in qt5-qtbase in all Fedora versions since 32, even before it landed upstream, but it is not in RHEL qt5-qtbase package.
# So I think it is no longer needed in Fedora
# 
# Concerning upstream Qt6 version, the patch was reverted and kept for Qt 6.3, but concerning keepassxc it is not important since it uses Qt 5
#
# 29 April 2022 Germano Massullo's update: users in upstream bugreports
# https://github.com/keepassxreboot/keepassxc/issues/7959
# https://github.com/keepassxreboot/keepassxc/issues/5608
# are reporting regression. I am resuming xcb.patch to all branches
#
# 27 July 2022 Germano Massullo's update: new Qt release
# https://bodhi.fedoraproject.org/updates/FEDORA-2022-d1ac004bb1
# reintroduced xcb patch for GNOME Wayland mentioning in the description the
# problems keepassxc users experienced
#
# 15 April 2023 Germano Massullo's update: xcb.patch causes users no longer being
# able to move KeepassXC database entries between groups on Fedora 38 GNOME
# https://bugzilla.redhat.com/show_bug.cgi?id=2186217
# disabling the patch fixes the problem, therefore it has been disabled on
# Fedora >= 38
Patch0:         xcb.patch

BuildRequires:  botan2-devel
BuildRequires:  cmake >= 3.1
BuildRequires:  desktop-file-utils
%if %{defined rhel}
BuildRequires:  gcc-toolset-12-gcc-c++
BuildRequires:  gcc-toolset-12-annobin-plugin-gcc
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libappstream-glib
BuildRequires:  libargon2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel >= 1.7
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libsodium-devel
BuildRequires:  libusb1-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  libyubikey-devel
# Concerning minizip dependency drama, this is the list of available minizip packages
# for all active branches
# == el8, el9 ==
# minizip
# minizip1.2
#
# == f38, f39 ==
# minizip-ng
# minizip-compat
#
# == fedora >= 40 ==
# minizip-ng
# minizip-ng-compat
# Read https://fedoraproject.org/wiki/Changes/MinizipNGTransition 
%if 0%{?el8} || 0%{?el9}
BuildRequires:  minizip1.2-devel
%endif
%if %{defined fedora} && 0%{?fedora} >= 38 && 0%{?fedora} < 40
BuildRequires:  minizip-compat-devel
%endif
%if %{defined fedora} && 0%{?fedora} >= 40
BuildRequires:  minizip-ng-compat-devel
%endif
BuildRequires:  pcsc-lite-devel
BuildRequires:  qrencode-devel
BuildRequires:  readline-devel
BuildRequires:  qt5-qtbase-devel >= 5.2
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel >= 5.2
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  ykpers-devel
BuildRequires:  zlib-devel
BuildRequires:  rubygem-asciidoctor
# for gpg verification
BuildRequires:  gnupg2

# enforces on the user system, Qt version to be the same one used to build KeepassXC
# This avoids "not a bug" bugreports like this one
# https://bugzilla.redhat.com/show_bug.cgi?id=2068981
# Moreover it is very important in case of mass rebuild of Qt+applications that
# are dependent from Qt, because it happened (see following bugreport) that users experienced
# that their system was not able to install a new Qt update due packaging bugs, but the system
# was able to update keepassxc (which was built upon new Qt release), resulting in a
# Qt - KeepassXC mismatch
# https://bugzilla.redhat.com/show_bug.cgi?id=2111413
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

# KeePassXC bundles the ykcore code due to lack of support from Yubico and
# stratification of version across various operating system distros. Additionally,
# KeePassXC has modified the API of ykcore to make it more functional when using
# non-YubiKey keys (ie, OnlyKey).
Provides: bundled(ykcore)

# Unsupported CPU architectures on EPEL8
# filled https://bugzilla.redhat.com/show_bug.cgi?id=2144863
# to be compliant to "Architecture Build Failures" paragraph of Fedora Packaging Guidelines 
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_architecture_build_failures
%if %{defined rhel} && 0%{?rhel} == 8
ExcludeArch: s390x
%endif

%description
KeePassXC is a community fork of KeePassX
KeePassXC is an application for people with extremely high demands on secure
personal data management.
KeePassXC saves many different information e.g. user names, passwords, urls,
attachemts and comments in one single database. For a better management
user-defined titles and icons can be specified for each single entry.
Furthermore the entries are sorted in groups, which are customizable as well.
The integrated search function allows to search in a single group or the
complete database.
KeePassXC offers a little utility for secure password generation. The password
generator is very customizable, fast and easy to use. Especially someone who
generates passwords frequently will appreciate this feature.
The complete database is always encrypted either with AES (alias Rijndael) or
Twofish encryption algorithm using a 256 bit key. Therefore the saved
information can be considered as quite safe.



%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%setup -q

# Apply xcb.patch only for EPEL and Fedora <38
%if (%{defined rhel} || (%{defined fedora} && 0%{?fedora} < 38))
%autopatch -p1
%endif

# Older version of appstream-util can't parse some url types
%if (%{defined rhel} && 0%{?rhel} <= 9)
sed -i '/type="vcs-browser"/d' ./share/linux/org.keepassxc.KeePassXC.appdata.xml
sed -i '/type="contribute"/d' ./share/linux/org.keepassxc.KeePassXC.appdata.xml
%endif

# Older version of desktop-file-utils before 0.26 don't know about some fields
# Remove when desktop-file-utils 0.26 is available in EPEL8
%if (%{defined rhel} && 0%{?rhel} <= 9)
sed -i 's/Version=1.5/Version=1.0/' ./share/linux/org.keepassxc.KeePassXC.desktop.in
sed -i '/^SingleMainWindow=true/d' ./share/linux/org.keepassxc.KeePassXC.desktop.in
%endif

%build
%if %{defined rhel} && 0%{?rhel} == 8
%enable_devtoolset12
# disable -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1, as gcc-toolset-{10,11,12}-annobin
# do not provide gcc-annobin.so anymore, despite that they provide annobin.so. but
# redhat-rpm-config still passes -fplugin=gcc-annobin to the compiler.
%undefine _annotated_build
%endif
%cmake \
    %{?flatpak:-DKEEPASSXC_DIST_TYPE=Flatpak} \
    -DWITH_XC_ALL=ON \
    -DWITH_XC_KEESHARE_SECURE=ON \
    -DWITH_XC_UPDATECHECK=OFF \
    -DWITH_XC_DOCS=ON \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
 
%install
%cmake_install
%if %{defined flatpak}
install -m0755 utils/keepassxc-flatpak-wrapper.sh %{buildroot}%{_bindir}/keepassxc-wrapper
%endif
 
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original \
    --add-mime-type application/x-keepassxc \
    %{buildroot}%{_datadir}/applications/org.%{name}.KeePassXC.desktop
 
%find_lang %{name} --with-qt

%check
# 'testcli' fails with "Subprocess aborted" in Koji and local mock
%ctest --exclude-regex testcli
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.KeePassXC.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.%{name}.KeePassXC.appdata.xml

%files -f %{name}.lang
%doc README.md
%license COPYING LICENSE*
%{_bindir}/keepassxc
%{_bindir}/keepassxc-cli
%{_bindir}/keepassxc-proxy
%if %{defined flatpak}
%{_bindir}/keepassxc-wrapper
%endif
%{_datadir}/keepassxc
%{_datadir}/keepassxc/wordlists
%{_datadir}/applications/org.%{name}.KeePassXC.desktop
%{_datadir}/metainfo/org.%{name}.KeePassXC.appdata.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/*/*keepassxc*
%{_libdir}/%{name}
%{_mandir}/man1/%{name}-cli.1*
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Jan Grulich <jgrulich@redhat.com> - 2.7.9-7
- Rebuild (qt5)

* Sun Dec 29 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 2.7.9-6
- Install wrapper script in flatpak builds

* Thu Sep 05 2024 Jan Grulich <jgrulich@redhat.com> - 2.7.9-5
- Rebuild (qt5)

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.9-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 2.7.9-2
- Fix flatpak build

* Fri Jun 21 2024 Germano Massullo <germano.massullo@gmail.com> - 2.7.9-1
- 2.7.9 release

* Thu May 30 2024 Jan Grulich <jgrulich@redhat.com> - 2.7.8-2
- Rebuild (qt5)

* Fri May 10 2024 Germano Massullo <germano.massullo@gmail.com> - 2.7.8-1
- 2.7.8 release
- Removed Obsoletes/Provides keepassx

* Tue May 07 2024 Germano Massullo <germano.massullo@gmail.com> - 2.7.7-4
- Added Obsoletes/Provides keepassx

* Fri Mar 15 2024 Jan Grulich <jgrulich@redhat.com> - 2.7.7-3
- Rebuild (qt5)

* Wed Mar 13 2024 Germano Massullo <germano.massullo@gmail.com> - 2.7.7-2
- replaced minizip depencendy for all active branches

* Wed Mar 13 2024 Germano Massullo <germano.massullo@gmail.com> - 2.7.7-1
- 2.7.7 release

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Jan Grulich <jgrulich@redhat.com> - 2.7.6-6
- Rebuild (qt5)

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 2.7.6-5
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Sat Nov 18 2023 Germano Massullo <germano.massullo@gmail.com> - 2.7.6-4
- rebuild (qt5) el9-next

* Mon Oct 09 2023 Jan Grulich <jgrulich@redhat.com> - 2.7.6-3
- Rebuild (qt5)

* Wed Sep 27 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 2.7.6-2
- Build with minizip-ng for F38+

* Wed Aug 16 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.7.6-1
- Update to 2.7.6

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Jan Grulich <jgrulich@redhat.com> - 2.7.5-2
- Rebuild (qt5)

* Mon May 15 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.7.5-1
- Update to 2.7.5
- Use enable_devtoolset12 macro for EPEL8
- Undefined _annotated_build for EPEL8
- Remove unneeded comment about DOCS
- Remove custom mimetype desktop file as this method is deprecated

* Sat Apr 29 2023 Michael J Gruber <mjg@fedoraproject.org> - 2.7.4-10
- adjust URL to current working one

* Sun Apr 16 2023 Germano Massullo <germano.massullo@gmail.com> - 2.7.4-9
- Rebuild (qt5)

* Sat Apr 15 2023 Germano Massullo <germano.massullo@gmail.com> - 2.7.4-8
- disables xcb patch for Fedora >= 38

* Wed Apr 12 2023 Jan Grulich <jgrulich@redhat.com> - 2.7.4-7
- Rebuild (qt5)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Jan Grulich <jgrulich@redhat.com> - 2.7.4-5
- Rebuild (qt5)

* Tue Nov 22 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.4-4
- Updates gcc-toolset version from 11 to 12
- Removes s390x from EPEL 8

* Mon Nov 21 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.7.4-3
- Fix builds for EPEL and F35

* Thu Nov 17 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.4-2
- rebuilt for RHEL 9.1

* Tue Nov 01 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.4-1
- 2.7.4 release
- Adds appdata.patch

* Tue Nov 01 2022 Jan Grulich <jgrulich@redhat.com> - 2.7.1-16
- Rebuild (qt5)

* Mon Oct 31 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.7.1-15
- Verify gpg signature (rhbz#1514247)
- Use minizip-compat-devel for >=F38

* Mon Oct 31 2022 Jan Grulich <jgrulich@redhat.com> - 2.7.1-14
- Rebuild (qt5)

* Thu Sep 22 2022 Otto Liljalaakso <otto.liljalaakso@iki.fi> - 2.7.1-13
- Re-enable LTO (rhbz#2127754)
- Enable most tests (rhbz#2127757)

* Wed Sep 21 2022 Jan Grulich <jgrulich@redhat.com> - 2.7.1-12
- Rebuild (qt5)

* Mon Jul 25 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.1-11
- reverting Jan Grulich's removal of %%{?_qt5:Requires: %%{_qt5}%{?_isa} = %%{_qt5_version}}

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 2.7.1-9
- Rebuild (qt5)

* Wed Jul 13 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.1-8
- enabled DWITH_XC_DOCS=ON on epel8

* Mon Jul 11 2022 Carl George <carl@george.computer> - 2.7.1-7
- Fix conditional logic to build on EPEL9
- Enable man pages on EPEL8

* Wed Jun 01 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.1-6
- rebuilt due EPEL8 Qt new version

* Wed May 25 2022 Mukundan Ragavan <nonamedotc@gmail.com> - 2.7.1-5
- rebuilt

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 2.7.1-4
- Rebuild (qt5)

* Fri Apr 29 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.1-3
- enabled Patch0:xcb.patch for all branches
- adds gcc-toolset-11-toolchain for el8
- replaces minizip-devel with minizip1.2-devel for el8

* Mon Apr 11 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.1-2
- replaces BuildRequires: minizip-compat-devel with BuildRequires: minizip-devel

* Wed Apr 06 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.1-1
- 2.7.1 release

* Tue Mar 22 2022 Germano Massullo <germano.massullo@gmail.com> - 2.7.0-1
- 2.7.0 release
- adds BuildRequires: botan2-devel
- adds BuildRequires: pcsc-lite-devel
- adds Provides: bundled(ykcore)
- enforcing on the user system, Qt version to be the same one used to build KeepassXC
- replaces BuildRequires: quazip-qt5-devel with BuildRequires: minizip-compat-devel

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 2.6.6-6
- Rebuild (qt5)

* Mon Feb 21 2022 Germano Massullo <germano.massullo@gmail.com> - 2.6.6-5
- User pewpeww improved xcb.patch - https://src.fedoraproject.org/rpms/keepassxc/pull-request/1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Björn Esser <besser82@fedoraproject.org> - 2.6.6-3
- Rebuild (quazip)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.6-1
- Update to 2.6.6

* Sat May 01 2021 Germano Massullo <germano.massullo@gmail.com> - 2.6.4-2
- added xcb.patch that fixes GNOME quirks on Wayland sessions. Read https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/3BVLBS4B3XHJEXFVGD7RK2ZMXZG6JQZT/

* Sun Jan 31 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.4-1
- Update to 2.6.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Germano Massullo <germano.massullo@gmail.com> - 2.6.3-2
- EL8: disabled documentation, removed rubygem-asciidoctor and quazip depencendies. For bugzilla tickets about missing dependencies, read this spec file near Fedora/EL8 macros

* Wed Jan 13 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.3-1
- Update to 2.6.3

* Mon Oct 26 2020 Germano Massullo <germano.massullo@gmail.com> - 2.6.2-2
- replaced -WITH_XC_UPDATECHECK=OFF with -DWITH_XC_UPDATECHECK=OFF Read https://bugzilla.redhat.com/show_bug.cgi?id=1887609

* Fri Oct 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Thu Aug 20 2020 Germano Massullo <germano.massullo@gmail.com> - 2.6.1-1
- 2.6.1 release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Wed Jul 01 2020 Jeff Law <law@redhat.com> - 2.5.4-2
- Diable LTO

* Thu Apr 09 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.4-1
- Update to 2.5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3

* Sun Jan 05 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2

* Tue Nov 12 2019 Germano Massullo <germano.massullo@gmail.com> - 2.5.1-1
- 2.5.1 release

* Mon Oct 28 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.5.0-1
- 2.5.0

* Thu Sep 19 2019 Germano Massullo <germano.massullo@gmail.com> - 2.4.3-6
- Replaced BuildRequires: quazip-devel with BuildRequires: quazip-qt5-devel

* Mon Sep 16 2019 Germano Massullo <germano.massullo@gmail.com> - 2.4.3-5
- Added BuildRequires: quazip-devel

* Thu Sep 05 2019 Germano Massullo <germano.massullo@gmail.com> - 2.4.3-4
- Added -DWITH_XC_KEESHARE_SECURE=ON

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 2.4.3-2
- Rebuilt (libqrencode.so.4)

* Tue Jun 11 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3

* Fri May 31 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2

* Tue Apr 16 2019 Germano Massullo <germano.massullo@gmail.com> - 2.4.1-1
- 2.4.1 release
- Added WITH_XC_UPDATECHECK=OFF

* Wed Mar 20 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0
- Drop unneeded sed lines in spec file
- Added BR for qrencode-devel and qt5-qtsvg-devel

* Mon Mar 18 2019 Remi Collet <remi@fedoraproject.org> - 2.3.4-3
- rebuild for libargon2 new soname

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4

* Thu Jul 19 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.3-3
- Fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Tue May 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Wed Mar 07 2018 Germano Massullo <germano.massullo@gmail.com> - 2.3.1-1
- 2.3.1 release
- used -DWITH_XC_ALL=ON to enable all features. Read https://github.com/keepassxreboot/keepassxc/issues/1558#issuecomment-369291706

* Wed Feb 28 2018 Germano Massullo <germano.massullo@gmail.com> - 2.2.4-7
- added BuildRequires: libargon2-devel
- added BuildRequires: libcurl-devel
- added BuildRequires: libgcrypt-devel >= 1.7
- added BuildRequires: libsodium-devel
- added BuildRequires: gcc-c++ >= 4.7
- added %%{_mandir}/man1/%%{name}-cli.1*

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.4-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.4-4
- Remove obsolete scriptlets

* Wed Dec 27 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.4-3
- Fix specfile error

* Sat Dec 16 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.4-2
- Adjust for changes in appdata and desktop filename change

* Thu Dec 14 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.4-1
- 2.2.4 release
- removed patch to fix typo in a XML tag

* Tue Dec 12 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.3-1
- 2.2.3 release
- added patch to fix typo in a XML tag

* Sun Oct 22 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2
- Fix desktop file names
- Added BR on libappstream-glib
- Install appdata file

* Mon Oct 02 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.1-1
- 2.2.1 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Germano Massullo <germano.massullo@gmail.com> - 2.2.0-1
- 2.2.0 release
- added %%{_bindir}/keepassxc-cli
- changed -DWITH_XC_YUBIKEY=OFF to -DWITH_XC_YUBIKEY=ON
- added BuildRequires: ykpers-devel and BuildRequires: libyubikey-devel

* Fri May 19 2017 Germano Massullo <germano.massullo@gmail.com> - 2.1.4-2
- Disabled Yubikey support. It will be re-enabled on 2.2.0 release

* Sun May 14 2017 Germano Massullo <germano.massullo@gmail.com> - 2.1.4-1
- First release on Fedora repository
