%global base_name partitionmanager

%global kf6min 5.240.0
%global qt6min 6.5.0
%global kpmcoremin 24.01


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           kde-partitionmanager
Version:        25.12.2
Release:        1%{?dist}
Summary:        KDE Partition Manager

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND CC-BY-4.0 AND CC0-1.0 AND GFDL-1.2-or-later
URL:            https://apps.kde.org/partitionmanager/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/partitionmanager-%{version}.tar.xz

BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core) >= %{qt6min}
BuildRequires:  cmake(Qt6Gui) >= %{qt6min}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6min}

BuildRequires:  cmake(KF6Config) >= %{kf6min}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6min}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6min}
BuildRequires:  cmake(KF6Crash) >= %{kf6min}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6min}
BuildRequires:  cmake(KF6I18n) >= %{kf6min}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6min}
BuildRequires:  cmake(KF6KIO) >= %{kf6min}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6min}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6min}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6min}
BuildRequires:  cmake(KF6DocTools) >= %{kf6min}

BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(KPMcore) >= %{kpmcoremin}

Requires:       kf6-filesystem

%description
KDE Partition Manager is a utility program to help you manage the disk devices,
partitions and file systems on your computer. It allows you to easily create, 
copy, move, delete, resize without losing data, backup and restore partitions.

KDE Partition Manager supports a large number of file systems, 
including ext2/3/4, reiserfs, NTFS, FAT16/32, jfs, xfs and more.

Starting from version 1.9.50 KDE Partition Manager has become the GUI part of 
KPMcore (KDE PartitionManager core) which contain the libraries used to 
manipulate filesystems.


%prep
%autosetup -p1 -n partitionmanager-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang partitionmanager --with-kde --with-html

%check
# Validate .desktop file
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*partitionmanager.desktop
# Validate appdata file
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml


%files -f partitionmanager.lang
%license LICENSES/*
%{_kf6_bindir}/partitionmanager
%{_kf6_datadir}/applications/*partitionmanager.desktop
%{_kf6_datadir}/solid/actions/open_in_partitionmanager.desktop
%{_kf6_datadir}/config.kcfg/partitionmanager.kcfg
%{_datadir}/icons/hicolor/*/*/*
%{_kf6_metainfodir}/*partitionmanager.appdata.xml


%changelog
* Wed Feb 04 2026 Steve Cossette <farchord@gmail.com> - 25.12.2-1
- 25.12.2

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 25.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jan 07 2026 farchord@gmail.com - 25.12.1-1
- 25.12.1

* Sat Dec 06 2025 Steve Cossette <farchord@gmail.com> - 25.12.0-1
- 25.12.0

* Fri Nov 28 2025 Steve Cossette <farchord@gmail.com> - 25.11.90-1
- 25.11.90

* Sat Nov 15 2025 Steve Cossette <farchord@gmail.com> - 25.11.80-1
- 25.11.80

* Tue Nov 04 2025 Steve Cossette <farchord@gmail.com> - 25.08.3-1
- 25.08.3

* Wed Oct 08 2025 Steve Cossette <farchord@gmail.com> - 25.08.2-1
- 25.08.2

* Sun Sep 21 2025 Steve Cossette <farchord@gmail.com> - 25.08.1-1
- 25.08.1

* Sun Aug 17 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 25.08.0-3
- Drop i686 support (leaf package)

* Sat Aug 16 2025 Neal Gompa <ngompa@fedoraproject.org> - 25.08.0-2
- Undo RPMAutoSpec conversion

* Sat Aug 09 2025 Steve Cossette <farchord@gmail.com> - 25.08.0-1
- 25.08.0

* Sat Jul 26 2025 Steve Cossette <farchord@gmail.com> - 25.07.90-1
- 25.07.90

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 14 2025 Steve Cossette <farchord@gmail.com> - 25.07.80-1
- 25.07.80

* Thu Jul 03 2025 Steve Cossette <farchord@gmail.com> - 25.04.3-1
- 25.04.3

* Thu Jun 05 2025 Steve Cossette <farchord@gmail.com> - 25.04.2-1
- 25.04.2

* Wed May 14 2025 Steve Cossette <farchord@gmail.com> - 25.04.1-1
- 25.04.1

* Sat Apr 12 2025 Steve Cossette <farchord@gmail.com> - 25.04.0-1
- 25.04.0

* Sun Mar 23 2025 Steve Cossette <farchord@gmail.com> - 25.03.80-1
- 25.03.80

* Wed Mar 05 2025 Steve Cossette <farchord@gmail.com> - 24.12.3-1
- 24.12.3

* Fri Feb 21 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-2
- Rebuild for ppc64le enablement

* Thu Feb 06 2025 Steve Cossette <farchord@gmail.com> - 24.12.2-1
- 24.12.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Wed Nov 20 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Wed Nov 06 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Thu Sep 26 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Fri Aug 23 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Sat Jun 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Sun May 19 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Sat Apr 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Fri Feb 23 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Thu Feb 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.85-1
- 24.01.85

* Wed Dec 06 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

* Sun Oct 15 2023 Mattia Verga <mattia.verga@proton.me> - 23.08.2-2
- Use qt6/kf6 for Fedora >= 40

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sun May 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Sat Apr 08 2023 Mattia Verga <mattia.verga@proton.me> - 23.03.90-6
- Remove inline fix for desktop file

* Sat Apr 08 2023 Mattia Verga <mattia.verga@proton.me> - 23.03.90-5
- Fix unstable declaration

* Sat Apr 08 2023 Mattia Verga <mattia.verga@proton.me> - 23.03.90-4
- Update minimum requirements in specfile

* Sat Apr 08 2023 Mattia Verga <mattia.verga@proton.me> - 23.03.90-3
- Convert license tag to SPDX

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 27 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- feat: 22.12.3

* Tue Jan 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.0-2
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.08.3-1
- 22.08.3

* Sat Oct 15 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.08.2-1
- fix: update spec file

* Sat Oct 15 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.08.1-2
- 22.08.2

* Thu Sep 08 2022 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Sun Aug 21 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Sun Jun 19 2022 Mattia Verga <mattia.verga@protonmail.com> - 22.04.2-1
- Update to 22.04.2 (fedora#2095249)

* Sat Mar 19 2022 Mattia Verga <mattia.verga@protonmail.com> - 22.03.80-2
- Add PolKit to BR

* Sat Mar 19 2022 Mattia Verga <mattia.verga@protonmail.com> - 22.03.80-1
- Unstable version 22.03.80

* Thu Mar 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Mon Feb 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Mattia Verga <mattia.verga@protonmail.com> - 21.12.0-1
- Release stable version 21.12.0

* Mon Nov 15 2021 Mattia Verga <mattia.verga@protonmail.com> - 21.11.80-1
- Release development version 21.11.80

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 25 2021 Mattia Verga <mattia.verga@protonmail.com> - 21.04.0-1
- Release stable version 21.04.0

* Sat Mar 06 2021 Mattia Verga <mattia.verga@protonmail.com> - 20.12.3-1
- Release stable version 20.12.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattia Verga <mattia.verga@protonmail.com> - 20.12.0-1
- Release stable version 20.12.0

* Sun Dec 06 2020 Mattia Verga <mattia.verga@protonmail.com> - 20.11.90-1
- Update to unstable release 20.11.90

* Sat Nov 14 2020 Mattia Verga <mattia.verga@protonmail.com> - 20.11.80-1
- Update to unstable release 20.11.80
- Move to KDE release-service versioning

* Sat Oct 17 2020 Mattia Verga <mattia.verga@protonmail.com> - 4.2.0-1
- Update to stable release 4.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Mattia Verga <mattia.verga@protonmail.com> - 4.1.0-1
- Update to stable release 4.1.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 2019 Mattia Verga <mattia.verga@protonmail.com> - 4.0.0-1
- Update to stable release 4.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Mattia Verga <mattia.verga@email.it> - 3.3.1-1
- Update to 3.3.1

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.0-2
- Remove obsolete scriptlets

* Tue Dec 26 2017 Mattia Verga <mattia.verga@email.it> - 3.3.0-1
- Update to 3.3.0

* Sun Dec 03 2017 Mattia Verga <mattia.verga@email.it> - 3.2.1-3
- Backport patch to fix mountpoint creation

* Fri Dec 01 2017 Mattia Verga <mattia.verga@email.it> - 3.2.1-2
- Backport patch from upstream to fix #1517718
- Use --with-html in find_lang
- Change appdata dir to metainfo

* Wed Nov 01 2017 Mattia Verga <mattia.verga@email.it> - 3.2.1-1
- Update to 3.2.1

* Sun Oct 01 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.2.0-1
- Update to 3.2.0

* Wed Sep 06 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.1.2-1
- Update to 3.1.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.1.0-1
- Update to 3.1.0
- Rename desktop and appdata files to lowercase

* Sun Jun 04 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.0.1-3
- Rebuild for kpmcore 3.1.0

* Thu Feb 09 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.0.1-2
- Rebuild for kpmcore 3.0.3

* Sun Jan 15 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.0.1-1
- Upgrade to stable 3.0.1
- Link to kpmcore 3.0.2

* Sun Jan 01 2017 Mattia Verga <mattia.verga@tiscali.it> - 3.0.0-2
- Link to kpmcore 3.0.1

* Wed Dec 21 2016 Mattia Verga <mattia.verga@tiscali.it> - 3.0.0-1
- Upgrade to stable 3.0.0

* Wed Nov 09 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.9.90-1
- Upgrade to unstable 2.9.90
- Extend LVM support

* Sun Jul 10 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.2.1-2
- Remove nonexistent doc files to fix build

* Sun Jul 10 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.2.1-1
- Update to stable 2.2.1

* Sat Jun 11 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.2.0-1
- Update to stable 2.2.0

* Sun Mar 13 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.1.0-1
- Update to stable 2.1.0

* Sun Feb 28 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.0.3-1
- Update to stable 2.0.3
- Use pkgconfig for libs
- Alphabetically ordered BR

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.0.0-2
- KPMcore has been renamed to kpmcore, BR changed
- Better formatting of BR
- Move .desktop and appdata validation under %%check

* Thu Jan 14 2016 Mattia Verga <mattia.verga@tiscali.it> - 2.0.0-1
- Update to stable 2.0.0
- Bind to same KPMcore version
- Library removed from sources

* Thu Dec 03 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.9.50-1
- Update to 1.9.50

* Sun Jun 21 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.2.1-7
- Validate appdata file

* Wed Jun 17 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.2.1-6
- Fix KF5 requires
- Remove hardened build option since it's now default

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Apr 05 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.2.1-3
- Fix documentation files

* Sun Apr 05 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.2.1-2
- Fix typos

* Sun Apr 05 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.2.1-1
- 1.2.1 release, port to kf5
- License changed to GPLv3

* Sun Feb 22 2015 Mattia Verga <mattia.verga@tiscali.it> - 1.1.1-1
- 1.1.1 release

* Sun Nov 16 2014 Mattia Verga <mattia.verga@tiscali.it> - 1.1.0-3
- Fix detection of devices without partition table

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-1
- 1.1.0 release, improve scriptlets/kde4 macro usage, include translations

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-14.20130815svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Mattia Verga <mattia.verga@tiscali.it> - 1.0.3-13.20130815svn
- Upgrade to svn 2013-05-15 - adds support for decrypting LUKS volumes
- Compress source with xz

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-12.20130624svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 Mattia Verga <mattia.verga@tiscali.it> - 1.0.3-11.20130624svn
- Fix to enable udisks2 backend compatibility

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-10.20121209svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 09 2012 Mattia Verga <mattia.verga@tiscali.it> - 1.0.3-9.20121209svn
- Upgrade to svn 2012-12-09
- Add BTRFS support
- Add exfat support

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8.20120205svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Mattia Verga <mattia.verga@tiscali.it> - 1.0.3-7.20120205svn
- Enable PIE following change in Pakaging Guidelines

* Wed Mar 14 2012 Mattia Verga <mattia.verga@tiscali.it> - 1.0.3-6.20120205svn
- Rebuilt for parted-3.1

* Mon Jan 30 2012 Mattia Verga <mattia.verga@tiscali.it> - 1.0.3-5.20120205svn
- Upgrade to svn 2012-02-05
- Fix bug #787194

* Mon Jan 30 2012 Mattia Verga <mattia.verga@tiscali.it> - 1.0.3-5.20120130svn
- bugfix release

* Tue Dec 27 2011 Mattia Verga <mattia.verga@tiscali.it> - 1.0.3-5.20111223svn
- Added kde-filesystem to Requires
- Added icon cache refresh at installation/uninstallation

* Fri Dec 23 2011 Mattia Verga <mattia.verga@tiscali.it> - 1.0.3-4.20111223svn
- Upgrade to svn 2011-12-22
- Fix bug #757661
- Removed language detection, no translations in svn

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 01 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0.3-1
- 1.0.3 bugfix release

* Tue May 18 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0.2-1
- bugfix release

* Wed Mar 31 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0.1-1%{?dist}.2
- rebuild for new parted

* Sun Feb 14 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0.1-1%{?dist}.1
- DSO fix for rawhide

* Mon Jan 25 2010 Thomas Janssen <thomasj@fedoraproject.org> 1.0.1-1
- New upstream source

* Wed Nov 18 2009 Thomas Janssen <thomasj@fedoraproject.org> 1.0.0-2
- Moved desktop-file-validate to %%install
- Removed superfluous BR qt4-devel

* Wed Nov 18 2009 Thomas Janssen <thomasj@fedoraproject.org> 1.0.0-1
- Initial Fedora release
