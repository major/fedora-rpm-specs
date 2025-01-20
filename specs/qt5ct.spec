Name:           qt5ct
Version:        1.1
Release:        29%{?dist}
Summary:        Qt5 Configuration Tool

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://sourceforge.net/projects/%{name}/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libXrender-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
# qt5ct-qtplugin uses gui-private
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

## FIXME?: ftbfs without this, not sure why yet -- rex
BuildRequires: pkgconfig(libudev)

%description
qt5ct allows users to configure Qt5 settings (theme, font, icons, etc.) under
DE/WM without Qt integration.

%prep
%setup -q


%build
%qmake_qt5

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Copy translations into right place
install -d %{buildroot}%{_datadir}/%{name}/translations
install -D -pm 644 src/%{name}/translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
%find_lang %{name} --with-qt

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%dir %{_datadir}/%{name}/translations/
%{_qt5_plugindir}/platformthemes/libqt5ct.so
%{_qt5_plugindir}/styles/libqt5ct-style.so

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Jan Grulich <jgrulich@redhat.com> - 1.1-28
- Rebuild (qt5)

* Thu Sep 05 2024 Jan Grulich <jgrulich@redhat.com> - 1.1-27
- Rebuild (qt5)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-26
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 30 2024 Jan Grulich <jgrulich@redhat.com> - 1.1-24
- Rebuild (qt5)

* Fri Mar 15 2024 Jan Grulich <jgrulich@redhat.com> - 1.1-23
- Rebuild (qt5)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Jan Grulich <jgrulich@redhat.com> - 1.1-20
- Rebuild (qt5)

* Mon Oct 09 2023 Jan Grulich <jgrulich@redhat.com> - 1.1-19
- Rebuild (qt5)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Jan Grulich <jgrulich@redhat.com> - 1.1-17
- Rebuild (qt5)

* Wed Apr 12 2023 Jan Grulich <jgrulich@redhat.com> - 1.1-16
- Rebuild (qt5)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Jan Grulich <jgrulich@redhat.com> - 1.1-14
- Rebuild (qt5)

* Mon Oct 31 2022 Jan Grulich <jgrulich@redhat.com> - 1.1-13
- Rebuild (qt5)

* Wed Sep 21 2022 Jan Grulich <jgrulich@redhat.com> - 1.1-12
- Rebuild (qt5)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.1-10
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.1-9
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.1-8
- Rebuild (qt5)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.1-4
- .spec cosmetics, use %%make_build

* Mon Nov 23 07:55:05 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1.1-3
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.1-2
- rebuild (qt5)

* Tue Aug 25 2020 Christian Dersch <lupinix@mailbox.org> - 1.1-1
- new version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Christian Dersch <lupinix@fedoraproject.org> - 1.0-1
- new version

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.38-9
- rebuild (qt5)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.38-7
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.38-6
- rebuild (qt5)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.38-4
- rebuild (qt5)

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.38-3
- rebuild (qt5)

* Wed Apr 10 2019 Pete Walter <pwalter@fedoraproject.org> - 0.38-2
- rebuild (qt5)

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.38-1
- new version

* Fri Mar 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.35-8
- rebuild (qt5)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.35-6
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 0.35-5
- rebuild (qt5)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.35-3
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.35-2
- rebuild (qt5)

* Wed Apr 18 2018 Christian Dersch - 0.35-1
- new version

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 0.34-5
- rebuild (qt5)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 0.34-3
- rebuild (qt5)

* Mon Nov 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.34-1
- qt5ct-0.34 is available (#1509757)

* Mon Oct 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.33-2
- rebuild (qt5)

* Mon Aug 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.33-1
- qt5ct-0.33 (#1450654)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.31-3
- rebuild (qt5)

* Sun May 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.31-2
- Rebuilt for Qt 5.9 beta

* Mon Apr 10 2017 Christian Dersch <lupinix@mailbox.org> - 0.31-1
- new version

* Thu Mar 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.30-2
- rebuild (qt5)

* Thu Feb 09 2017 Christian Dersch <lupinix@mailbox.org> - 0.30-1
- new version

* Wed Jan 25 2017 Christian Dersch <lupinix@mailbox.org> - 0.29-1
- new version

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.27-2
- bump release

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.27-1.2
- branch rebuild (qt5)

* Tue Oct 04 2016 Christian Dersch <lupinix@mailbox.org> - 0.27-1
- new version

* Tue Sep 06 2016 Christian Dersch <lupinix@mailbox.org> - 0.26-1
- new version

* Thu Aug 11 2016 Christian Dersch <lupinix@mailbox.org> - 0.25-1
- new version

* Sun Jul 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.24-3
- rebuild (qt5-qtbase)

* Wed Jun 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.24-2
- add versioned dependency on qtbase version used to build

* Thu Jun 02 2016 Christian Dersch <lupinix@mailbox.org> - 0.24-1
- new version

* Mon May 02 2016 Christian Dersch <lupinix@mailbox.org> - 0.23-1
- new version (0.23)

* Tue Mar 29 2016 Christian Dersch <lupinix@mailbox.org> - 0.22-1
- initial spec
