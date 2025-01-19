%undefine __cmake_in_source_build

Name:           kshutdown
Version:        5.2
Release:        14%{?dist}
Summary:        Graphical shutdown utility for Plasma 5
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://kshutdown.sourceforge.net/
Source0:        http://sourceforge.net/projects/%{name}/files/KShutdown/%{version}/%{name}-source-%{version}.zip

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kcrash-devel

%description
KShutdown is a graphical shutdown utility which allows you to turn off
or suspend computer at the specified time. It features various time and delay
options, command line support, and notifications.

%prep
%autosetup

%build
%{cmake_kf5} -DKS_KF5=true
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kshutdown.desktop

%files -f %{name}.lang
%doc ChangeLog LICENSE TODO
%{_bindir}/kshutdown
%{_datadir}/knotifications5/kshutdown.notifyrc
%{_datadir}/applications/kshutdown.desktop
%{_datadir}/icons/hicolor/*/apps/kshutdown.png

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 5.2-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Jan Grulich <jgrulich@redhat.com> - 5.2-1
- 5.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Jan Grulich <jgrulich@redhat.com> - 5.0-1
- Update to 5.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Jan Grulich <jgrulich@redhat.com> - 4.2-1
- Update to 4.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.1-0.2.beta
- Remove obsolete scriptlets

* Tue Aug 29 2017 Jan Grulich <jgrulich@redhat.com> - 4.1.1-0.1.beta
- Update to 4.1.1 beta

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Jan Grulich <jgrulich@redhat.com> - 4.1-0.1.beta
- Update to 4.1 beta

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 12 2016 Jan Grulich <jgrulich@redhat.com> - 4.0-1
- Update to 4.0

* Mon May 02 2016 Jan Grulich <jgrulich@redhat.com> - 3.99.1-0.1.beta
- Update to 3.99.1 beta

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.99-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Jan Grulich <jgrulich@redhat.com> - 3.99-0.1.beta
- Update to 3.99 based on KF5

* Thu May 14 2015 Jan Grulich <jgrulich@redhat.com> - 3.3-0.1.beta
- Update to 3.3beta

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Jan Grulich <jgrulich@redhat.com> - 3.2-1
- update to 3.2

* Sat Aug 03 2013 Jan Grulich <jgrulich@redhat.com> - 3.0-1
- update to 3.0

* Wed Jun 19 2013 Jan Grulich <jgrulich@redhat.com> - 3.0-0.3.beta8
- update to 3.0beta8

* Sun May 26 2013 Jan Grulich <jgrulich@redhat.com> - 3.0-0.2.beta7
- update to 3.0beta7

* Sat Feb 16 2013 Jan Grulich <jgrulich@redhat.com> - 3.0-0.1.beta6
- update to 3.0beta6

* Thu Aug 23 2007 Chitlesh Goorah  <chitlesh [AT] fedoraproject DOT org> - 1.0.1-1
- mass rebuild for fedora 8 - BuildID

* Fri Apr 27 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> 1.0-3
- bug fixing #241019 for gnome

* Fri Apr 27 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> 1.0-2
- patched the default values to allow user permissions on actions
- added 64x64 and 128x128 png icons so that kshutdown looks beautiful on katapult

* Fri Apr 20 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> 1.0-1
- New upstream release

* Sat Feb 03 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> 0.9.1beta-2
- bug fix #224430

* Wed Jan 10 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> 0.9.1beta-1
- New upstream development release 0.9.1beta
- Dropped fedora vendor
- Minor fixes in the spec files
- Fixed absolute paths

* Sun Sep 10 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> 0.8.2-5
- Added %%{?dist}

* Wed Aug 23 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> 0.8.2-4
- Fixed symlinks and rpmlint warnings

* Wed Mar 29 2006 Kushal Das <kushal@fedoraproject.org> 0.8.2-3
- Changed release tag

* Wed Mar 29 2006 Kushal Das <kushal@fedoraproject.org> 0.8.2-2
- Changed post/postun , lang part & buildrequires

* Sun Mar 26 2006 Kushal Das <kushal@fedoraproject.org> 0.8.2-1
- initial release
