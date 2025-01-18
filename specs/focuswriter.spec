Name:           focuswriter
Version:        1.8.9
Release:        2%{?dist}
Summary:        A full screen, distraction-free writing program
License:        GPL-3.0-or-later
URL:            http://gottcode.org/%{name}/
Source0:        http://gottcode.org/%{name}/%{name}-%{version}.tar.bz2

Patch0:         0001-Remove-icon-from-AppData.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  zlib-devel
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  hunspell-devel

%description
A full screen, distraction-free writing program. You can customize your
environment by changing the font, colors, and background image to add ambiance
as you type. FocusWriter features an on-the-fly updating word count, optional
auto-save, optional daily goals, and an interface that hides away to allow you
to focus more clearly; additionally, when you open the program your current
work-in-progress will automatically load and position you at the end of your
document, so that you can immediately jump back in.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 15 2024 Vojtech Trefny <vtrefny@redhat.com> - 1.8.9-1
- Update to 1.8.9

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 22 2024 Jan Grulich <jgrulich@redhat.com> - 1.8.8-2
- Rebuild (qt6)

* Wed May 22 2024 Vojtech Trefny <vtrefny@redhat.com> - 1.8.8-1
- Update to 1.8.8

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 1.8.7-2
- Rebuild (qt6)

* Mon May 06 2024 Vojtech Trefny <vtrefny@redhat.com> - 1.8.7-1
- Update to 1.8.7

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 1.8.6-4
- Rebuild (qt6)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Vojtech Trefny <vtrefny@redhat.com> - 1.8.6-1
- Update to 1.8.6

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 3 2023 Vojtech Trefny <vtrefny@redhat.com> - 1.8.5-1
- Update to 1.8.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Vojtech Trefny <vtrefny@redhat.com> - 1.8.4-1
- Update to 1.8.4

* Fri Nov 11 2022 Vojtech Trefny <vtrefny@redhat.com> - 1.8.3-2
- Change license string to the SPDX format required by Fedora

* Thu Sep 29 2022 Vojtech Trefny <vtrefny@redhat.com> - 1.8.3-1
- Update to 1.8.3

* Wed Sep 7 2022 Vojtech Trefny <vtrefny@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.8.1-3
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Vojtech Trefny <vtrefny@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Mon Jun 20 2022 Vojtech Trefny <vtrefny@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Vojtech Trefny <vtrefny@redhat.com> - 1.7.6-1
- Update to 1.7.6

* Mon Feb 24 2020 Vojtech Trefny <vtrefny@redhat.com> - 1.7.5-1
- Update to 1.7.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Vojtech Trefny <vtrefny@redhat.com> - 1.7.4-1
- Update to 1.7.4

* Sat Sep 28 2019 Vojtech Trefny <vtrefny@redhat.com> - 1.7.3-1
- Update to 1.7.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.5-7
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.5.5-2
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Dec 24 2015 Jean-Francois Saucier <jsaucier@gmail.com> - 1.5.5-1
- Update to the new upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 1.4.6-5
- rebuild for new libzip

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Richard Hughes <richard@hughsie.com> - 1.4.6-1
- Update to the new upstream version

* Thu Jan  9 2014 Jean-Francois Saucier <jsaucier@gmail.com> - 1.4.4-1
- Update to the new upstream version

* Wed Aug 21 2013 Remi Collet <rcollet@redhat.com> - 1.3.5.1-6
- rebuild for new libzip

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 04 2012 Remi Collet <remi@fedoraproject.org> - 1.3.5.1-2
- rebuild for new libzip

* Wed Jan 11 2012 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.5.1-1
- Update to the new upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.2.1-1
- Update to the new upstream version

* Thu Dec 23 2010 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.1-3
- Remove the qt-devel version number
- Reorder the files section at the end of the spec

* Wed Nov 24 2010 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.1-2
- Fix as per suggestion in bug #652257

* Wed Nov 10 2010 Jean-Francois Saucier <jsaucier@gmail.com> - 1.3.1-1
- Initial build for Fedora
