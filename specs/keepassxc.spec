# KeePassXC 2.8 requires Qt 6, which is unavailable on EPEL 8.

Name:           keepassxc
Version:        2.8.0
Release:        3%{?dist}
Summary:        Cross-platform password manager
License:        GPL-2.0-or-later AND BSD-2-Clause AND MIT AND CC0-1.0 AND Apache-2.0 AND LGPL-2.0-only AND LGPL-2.1-only
URL:            https://keepassxc.org/
Source0:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz
Source1:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz.sig
Source2:        https://keepassxc.org/keepassxc_master_signing_key.asc

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# due zxcvbn-c not being available on 32bit x86
ExcludeArch:    %{ix86}

%if (%{defined fedora} && 0%{?fedora} >= 44) || (%{defined rhel} && 0%{?rhel} >= 10)
BuildRequires:  botan3-devel
%else
BuildRequires:  botan2-devel
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
# Required for LC_ALL=en_US.UTF-8 during tests
BuildRequires:  glibc-langpack-en
BuildRequires:  keyutils-libs-devel
BuildRequires:  libappstream-glib
BuildRequires:  libusb1-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
# Concerning minizip dependency drama, this is the list of available minizip packages
# for all active branches
# == el9 ==
# minizip
# minizip1.2
#
# == fedora >= 40 ==
# minizip-ng
# minizip-ng-compat
# Read https://fedoraproject.org/wiki/Changes/MinizipNGTransition 
%if 0%{?el9}
BuildRequires:  minizip1.2-devel
%else
BuildRequires:  minizip-ng-compat-devel
%endif
BuildRequires:  pcsc-lite-devel
BuildRequires:  qrencode-devel
BuildRequires:  readline-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  zlib-devel
BuildRequires:  rubygem-asciidoctor
# Required for GPG signature verification
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
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

# KeePassXC bundles the ykcore code due to lack of support from Yubico and
# stratification of version across various operating system distros. Additionally,
# KeePassXC has modified the API of ykcore to make it more functional when using
# non-YubiKey keys (ie, OnlyKey).
Provides:       bundled(ykcore)

# Use the system zxcvbn-c library on Fedora. EPEL does not currently provide
# zxcvbn-c, so KeePassXC falls back to its bundled copy there.
# EPEL request: https://bugzilla.redhat.com/show_bug.cgi?id=2541423
%if 0%{?fedora}
BuildRequires:  zxcvbn-c-devel
%else
Provides:       bundled(zxcvbn-c) = 2.6
%endif

# https://github.com/keepassxreboot/keepassxc/pull/13810
Recommends: (wl-clipboard if gnome-shell)

%description
KeePassXC is a community fork of KeePassX
KeePassXC is an application for people with extremely high demands on secure
personal data management.
KeePassXC saves many different information e.g. user names, passwords, urls,
attachments and comments in one single database. For a better management
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

%autosetup -n %{name}-%{version}

# Older version of appstream-util can't parse some url types
%if 0%{?rhel} == 9
sed -i '/type="vcs-browser"/d' ./share/linux/org.keepassxc.KeePassXC.appdata.xml
sed -i '/type="contribute"/d' ./share/linux/org.keepassxc.KeePassXC.appdata.xml
%endif

%build
%cmake \
    %{?flatpak:-DKEEPASSXC_DIST_TYPE=Flatpak} \
    -DKEEPASSXC_BUILD_TYPE=Release \
    -DKPXC_FEATURE_BROWSER=ON \
    -DKPXC_FEATURE_SSHAGENT=ON \
    -DKPXC_FEATURE_FDOSECRETS=ON \
    -DKPXC_FEATURE_NETWORK=ON \
    -DKPXC_FEATURE_UPDATES=OFF \
    -DKPXC_FEATURE_DOCS=ON \
    -DWITH_TESTS=ON
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
# C language fails https://github.com/keepassxreboot/keepassxc/issues/11813
export LC_ALL=en_US.UTF-8
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
%{_datadir}/keepassxc/docs
%{_datadir}/keepassxc/icons
%{_datadir}/keepassxc/wordlists
%{_datadir}/applications/org.%{name}.KeePassXC.desktop
%{_datadir}/metainfo/org.%{name}.KeePassXC.appdata.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/*/*keepassxc*
%{_datadir}/polkit-1/actions/org.keepassxc.KeePassXC.policy
%{_mandir}/man1/%{name}-cli.1*
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Oct 25 2026 Jan Grulich <jgrulich@redhat.com> - 2.8.0-3
- Rebuild (qt6)

* Thu Oct 22 2026 Germano Massullo <germano.massullo@thetra.eu> - 2.8.0-2
- Disable 32bit x86

* Thu Oct 22 2026 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.8.0-1
- Update to 2.8.0-beta1 rhbz#2538859
- Drop EPEL 8 support as Qt 6 is unavailable
- Drop XCB workaround
- Drop unused dependencies (qt6-qtbase-private-devel, libargon2-devel,
  libcurl-devel, libgcrypt-devel, libmicrohttpd-devel, libsodium-devel,
  and libyubikey-devel)
- Use system zxcvbn-c on Fedora
- Update license expression

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Wed Mar 11 2026 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.7.12-1
- Update to 2.7.12 rhbz#2445950

* Sat Jan 24 2026 Michael Kuhn <suraia@fedoraproject.org> - 2.7.11-3
- Add conditional recommends for wl-clipboard

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Nov 24 2025 Germano Massullo (Thetra) <germano.massullo@thetra.eu> - 2.7.11-1
- 2.7.11 release
- Add org.keepassxc.KeePassXC.appdata.xml.patch

* Sun Nov 16 2025 Germano Massullo (Thetra) <germano.massullo@thetra.eu> - 2.7.10-6
- Replace botan2 with botan3 on EPEL>=10

* Tue Nov 11 2025 Germano Massullo (Thetra) <germano.massullo@thetra.eu> - 2.7.10-5
- Replace botan2 with botan3 on Fedora>=44

* Tue Nov 04 2025 Jan Grulich <jgrulich@redhat.com> - 2.7.10-4
- Rebuild (qt5)

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 26 2025 Jan Grulich <jgrulich@redhat.com> - 2.7.10-2
- Rebuild (qt5)

* Tue Mar 04 2025 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.7.10-1
- Update to 2.7.10 rhbz#2349308
- Use gcc-toolset only for EL8 https://developers.redhat.com/articles/2024/10/15/rest-peace-gcc-toolset-and-gnu-debugger
- Workaround issue #11813 depending on glibc-langpack-en and setting LC_ALL
- Set KEEPASSXC_BUILD_TYPE to Release
- Drop unused WITH_XC_KEESHARE_SECURE
- Drop dependency on ykpers-devel as it's not required since 2.7.0 pr#6654
- Simplify minizip dependency logic

* Wed Jan 22 2025 Jan Grulich <jgrulich@redhat.com> - 2.7.9-9
- Rebuild (qt5)

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
