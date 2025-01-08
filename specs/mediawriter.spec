Name:           mediawriter
Version:        5.2.3
Release:        1%{?dist}
Summary:        Fedora Media Writer

License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/FedoraQt/MediaWriter
Source0:        https://github.com/FedoraQt/MediaWriter/archive/MediaWriter-%{version}.tar.gz

Provides:       liveusb-creator = %{version}-%{release}
Obsoletes:      liveusb-creator <= 3.95.4-2

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  libappstream-glib
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  xz-devel

Requires:       qt6-qtdeclarative
Requires:       qt6-qtsvg

%if !0%{?flatpak}
Requires:       polkit
%endif
Requires:       xz-libs

%if !0%{?flatpak}
%if 0%{?fedora} && 0%{?fedora} != 25
Requires: storaged
%else
Requires: udisks
%endif
%endif

%description
A tool to write images of Fedora media to portable drives
like flash drives or memory cards.

%prep
%autosetup -p1 -n MediaWriter-%{version}


%build
%cmake

%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.fedoraproject.MediaWriter.appdata.xml

%files
%license LICENSE.GPL-2 LICENSE.LGPL-2
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/metainfo/org.fedoraproject.MediaWriter.appdata.xml
%{_datadir}/applications/org.fedoraproject.MediaWriter.desktop
%{_datadir}/icons/hicolor/16x16/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/22x22/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/24x24/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/32x32/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/48x48/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/64x64/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/128x128/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/256x256/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/512x512/apps/org.fedoraproject.MediaWriter.png

%changelog
* Mon Jan 06 2025 Jan Grulich <jgrulich@redhat.com> - 5.2.3-1
- 5.2.3

* Mon Nov 25 2024 Jan Grulich <grulja@gmail.com> - 5.2.1-1
- 5.2.1

* Fri Nov 22 2024 Jan Grulich <jgrulich@redhat.com> - 5.2.0-1
- 5.2.0

* Mon Nov 11 2024 Jan Grulich <jgrulich@redhat.com> - 5.1.90-2
- Fix overfloating heading for longer texts
  Resolves: bz#2324977

* Wed Oct 30 2024 Jan Grulich <jgrulich@redhat.com> - 5.1.90-1
- 5.1.90

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Jan Grulich <jgrulich@redhat.com> - 5.1.2-1
- 5.1.2

* Tue Mar 26 2024 Jan Grulich <jgrulich@redhat.com> - 5.1.0-1
- 5.1.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Jan Grulich <jgrulich@redhat.com> - 5.0.8-1
- 5.0.8

* Mon Sep 04 2023 Jan Grulich <jgrulich@redhat.com> - 5.0.7-1
- 5.0.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 02 2023 Jan Grulich <jgrulich@redhat.com> - 5.0.6-2
- Rebuild (qt6)
  Resolves: bz#2192551

* Wed Mar 22 2023 Jan Grulich <jgrulich@redhat.com> - 5.0.6-1
- 5.0.6

* Mon Mar 20 2023 Jan Grulich <jgrulich@redhat.com> - 5.0.5-1
- 5.0.5

* Tue Jan 31 2023 Jan Grulich <jgrulich@redhat.com> - 5.0.4-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 26 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.4-1
- 5.0.4

* Thu Aug 25 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.3-1
- 5.0.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.2-1
- 5.0.2

* Fri May 13 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.1-1
- 5.0.1

* Mon May 09 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.0-2
- Updated upstream tarball

* Mon May 09 2022 Jan Grulich <jgrulich@redhat.com> - 5.0.0-1
- 5.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Jan Grulich <jgrulich@redhat.com> - 4.2.2-2
- Use portal file dialog when possible

* Fri May 14 2021 Jan Grulich <jgrulich@redhat.com> - 4.2.2-1
- 4.2.2

* Thu Mar 25 2021 Jan Grulich <jgrulich@redhat.com> - 4.2.1-2
- Set correct path to helper binary

* Mon Mar 22 2021 Jan Grulich <jgrulich@redhat.com> - 4.2.1-1
- 4.2.1

* Wed Mar 03 2021 Jan Grulich <jgrulich@redhat.com> - 4.2.0-3
- Fix windows build script

* Tue Jan 26 2021 Kalev Lember <klember@redhat.com> - 4.2.0-2
- Install the theme into correct prefix when building for /app

* Mon Jan 25 2021 Jan Grulich <jgrulich@redhat.com> - 4.2.0-1
- 4.2.0

* Mon Jan 04 2021 Jan Grulich <jgrulich@redhat.com> - 4.1.7-2
- Fix UI issues in download dialog with Qt 5.15

* Thu Dec 17 2020 Jan Grulich <jgrulich@redhat.com> - 4.1.7-1
- 4.1.7

* Wed Sep 16 2020 Jan Grulich <jgrulich@redhat.com> - 4.1.6-1
- 4.1.6

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Martin Bříza <m@rtinbriza.cz> - 4.1.5-1
- Update to 4.1.5
- Resolves #1818672

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.1.4-2
- cleanup qt5 deps

* Thu May 02 2019 Tomáš Popela <tpopela@redhat.com> - 4.1.4-1
- Update to 4.1.4

* Sun Apr 21 2019 Martin Bříza <m@rtinbriza.cz> - 4.1.3-1
- Update to 4.1.3
- Resolves #1574717

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Martin Bříza <m@rtinbriza.cz> - 4.1.2-1
- Update to 4.1.2
- Update URLs
- Resolves #1590315

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.1-2
- Remove obsolete scriptlets

* Mon Nov 13 2017 Martin Bříza <mbriza@redhat.com> 4.1.1-1
- Update to 4.1.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Martin Bříza <mbriza@redhat.com> 4.1.0-1
- Update to 4.1.0
- Depend on UDisks2 instead of storage if Fedora != 25

* Tue Apr 11 2017 Martin Bříza <mbriza@redhat.com> 4.0.95-2
- Get rid of {?_isa} in the dependencies 

* Mon Mar 20 2017 Martin Bříza <mbriza@redhat.com> 4.0.95-1
- Update to 4.0.95

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Martin Bříza <mbriza@redhat.com> 4.0.8-0
- Update to 4.0.8

* Tue Nov 22 2016 Martin Bříza <mbriza@redhat.com> 4.0.7-0
- Update to 4.0.7

* Mon Nov 21 2016 Martin Bříza <mbriza@redhat.com> 4.0.5-0
- Update to 4.0.5

* Fri Nov 11 2016 Martin Bříza <mbriza@redhat.com> 4.0.4-0
- Update to 4.0.4

* Wed Nov 02 2016 Martin Bříza <mbriza@redhat.com> 4.0.3-0
- Update to 4.0.2

* Wed Nov 02 2016 Martin Bříza <mbriza@redhat.com> 4.0.1-0
- Update to 4.0.1

* Mon Oct 31 2016 Martin Bříza <mbriza@redhat.com> 4.0.0-2
- Don't forget to update the icon cache

* Mon Oct 31 2016 Martin Bříza <mbriza@redhat.com> 4.0.0-1
- Make mediawriter obsolete the liveusb-creator package

* Mon Oct 31 2016 Martin Bříza <mbriza@redhat.com> 4.0.0-0
- Update to 4.0.0

* Tue Oct 11 2016 Martin Bříza <mbriza@redhat.com> 3.97.2-0
- Update to 3.97.2

* Fri Sep 23 2016 Martin Bříza <mbriza@redhat.com> 3.97.1-0
- Update to 3.97.1

* Thu Sep 22 2016 Martin Bříza <mbriza@redhat.com> 3.97.0-0
- Update to 3.97.0

* Fri Sep 16 2016 Martin Bříza <mbriza@redhat.com> 3.96.0-0
- Update to 3.96.0

* Wed Aug 10 2016 Martin Bříza <mbriza@redhat.com> 0-1.1git728a879
- Fixed MOC errors when compiling on F25 and above

* Tue Aug 9 2016 Martin Bříza <mbriza@redhat.com> 0-0.2git0049ab3
- Fixed a package name

* Tue Aug 9 2016 Martin Bříza <mbriza@redhat.com> 0-0.1git0049ab3
- Initial release
