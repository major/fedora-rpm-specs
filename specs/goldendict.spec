Name: goldendict
Version: 1.5.0
Release: 7%{?dist}

License: GPL-3.0-or-later
Summary: A feature-rich dictionary lookup program
URL: http://goldendict.org
Source0: https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5WebKit)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XmlPatterns)

BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(lzo2)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(xtst)

BuildRequires: eb-devel
BuildRequires: phonon-qt5-devel
BuildRequires: qtsingleapplication-qt5-devel

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make

Requires: qt5-qtsvg%{?_isa}

Recommends: %{name}-docs = %{?epoch:%{epoch}:}%{version}-%{release}

%description
GoldenDict is a feature-rich dictionary lookup program, supporting multiple
dictionary formats (StarDict/Babylon/Lingvo/Dictd/AARD/MDict/SDict) and
online dictionaries, featuring perfect article rendering with the complete
markup, illustrations and other content retained, and allowing you to type
in words without any accents or correct case.

%package docs
Summary: Documentation for %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description docs
Contain doc files of %{name}.

%prep
%autosetup -p1
rm -rf {qtsingleapplication,maclibs,winlibs}
sed -e '/qtsingleapplication.pri/d' -i %{name}.pro

%build
%qmake_qt5 PREFIX=%{_prefix} CONFIG+=qtsingleapplication CONFIG+=no_ffmpeg_player %{name}.pro
echo "%{version}" > version.txt
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/app-install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/locale
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/*.metainfo.xml

%files docs
%{_datadir}/%{name}/help

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.0-2
- Disabled ffmpeg player to reduce the set of dependencies.

* Wed May 31 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.0-1
- Updated to version 1.5.0.
- Enabled ffmpeg player.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.36.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-0.35.RC2
- Rebased to 1064880 snapshot with different bugfixes.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.34.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.33.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.32.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.31.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 1.5-0.30.RC2
- Fix missing #include for gcc-11

* Tue Sep 29 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-0.29.RC2
- Rebased to dda311c snapshot with different bugfixes.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.28.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-0.27.RC2
- Rebased to 6ca112b snapshot with Wayland crash fixes.

* Sun Mar 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-0.26.RC2
- Rebased to a1c7c5b snapshot with a separate desktop action for Wayland.

* Sun Mar 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-0.25.RC2
- Added a separate desktop icon for Gnome users with workaround.
- Updated to 353ea17 snapshot with crash fixes under Qt 5.13+.

* Sat Mar 14 2020 Mosaab Alzoubi <moceap@hotmail.com> - 1.5-0.24.RC2
- Workaround #1766935

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.23.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-0.22.RC2
- Updated to c53fe1c snapshot with additional crash fixes.

* Mon Jul 29 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-0.21.RC2
- Updated to latest Git snapshot with lots of Qt 5.12 crash fixes.
- SPEC cleanup.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.20.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.19.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Mosaab Alzoubi <moceap@hotmail.com> - 1.5-0.18.RC2
- TRY TO FIX https://koji.fedoraproject.org/koji/taskinfo?taskID=32260066

* Mon Sep 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-0.17.RC2
- Switched to Qt5 to fix major issues with HiDPI displays.
- Moved to latest snapshot to resolve issues with latest GCC compiler versions.
- Major SPEC cleanup.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.16.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.15.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.14.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.13.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-0.12.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.11.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.10.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-0.9.RC2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5-0.8.RC2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.5-0.7.RC2
- Add an AppData file for the software center

* Sun Dec 14 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.5-0.6.RC1
- Use system qtsingleapplication instead of bundled one

* Sun Dec 14 2014 Mosaab Alzoubi <moceap@hotmail.com> - 1.5-0.5.RC2
- Update on 20141214
- Add libtiff-devel as BR
- Add eb-devel as BR
- Add -docs subpackage

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-0.4.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-0.3.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Mosaab Alzoubi <moceap@hotmail.com> - 1.5-0.2.RC1
- Use %%qmake_qt4 as suggestion by Christophe​r Meng‎ (‏cickumqt/gmail.com‏)
- Remove repeated BR.
- Remove locale install lines, included in makeinstall function.

* Tue Jan 14 2014 Mosaab Alzoubi <moceap@hotmail.com> - 1.5-0.1.RC1
- Update to 1.5RC.
- General clean of spec.
- Using source from GitHub.
- New URL.
- Remove 3 fixes and patches, fixed in upstream.
- Fix a date in changelog.
- Use new desktop-files Fedora method.
- DISABLE_INTERNAL_PLAYER=1 because ffmpeg not found in Fedora repos.
- Add bzip2-devel,lzo-devel to BRs.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 1.0.1-7
- Fix FTBFS for gcc-4.7

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Howard Ning <mrlhwliberty@gmail.com> - 1.0.1-3
- Fix the path of hunspell dictionaries

* Fri Dec 10 2010 Howard Ning <mrlhwliberty@gmail.com> - 1.0.1-2
- Change the categories to fix 592954

* Fri Dec 10 2010 Howard Ning <mrlhwliberty@gmail.com> - 1.0.1-1
- New upstream

* Tue Oct 12 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-15
- New upstream

* Wed Aug 04 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-14
- Fix the git repo

* Wed Aug 04 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-13
- New upstream version

* Thu Jun 10 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-12
- New upstream version
- Better BGL support
- Updated translations
- Play audio from website

* Tue May 11 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-11
- Drop the patch files in favor of sed.
- Change to a more standard directory by removing app directory.
- Remove libzip-devel and kde-filesystem requirement.

* Tue May 11 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-10
- Clean up the spec file.
- Update to the latest upstream.
- Enhance dictiionary groups editing.
- Fix the scan popup issues more.
- Update the Chinese translation.

* Wed Apr 14 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-9
- Add kde-filesystem requirement.

* Sun Apr 11 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-8
- Patch the desktop file to conform the guideline.
- Clean up the spec file more.

* Fri Apr 09 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-7
- Clean up the spec file.
- Add ownership of the missing directories.

* Mon Mar 15 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-6
- Add missing translations.

* Sun Mar 07 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-5
- New upstream git.
- Add phonon-devel as build requirement.

* Sat Feb 06 2010 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-4
- New upstream git. Fix some sound problem and scan popup problem.

* Sat Dec 26 2009 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-3
- New upstream git. Fix punctuation indexing problem and audio problems.

* Thu Dec 10 2009 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-2
- Add LICENSE.txt
- Change the group to Applications/System

* Wed Dec 9 2009 Howard Ning <mrlhwliberty@gmail.com> - 0.9.0-1
- Initial Release
