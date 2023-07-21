%undefine __cmake_in_source_build
%global app_name DNSCryptClient

Name:          dnscrypt-proxy-gui
Version:       1.24.18
Release:       5%{?dist}
Summary:       GUI wrapper for dnscrypt-proxy
License:       GPLv2+
Source0:       https://github.com/F1ash/%{name}/archive/%{version}.tar.gz
URL:           https://github.com/F1ash/%{name}

Requires:      systemd
Requires:      polkit
Requires:      dnscrypt-proxy
Requires:      hicolor-icon-theme
Requires:      kf5-kauth
Requires:      kf5-knotifications

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: glibc-headers
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel

BuildRequires: kf5-kauth-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: extra-cmake-modules
%{?systemd_requires}
BuildRequires: systemd

%description
The Qt/KF5 GUI wrapper over dnscrypt-proxy (version 1, 2)
for encrypting all DNS traffic between the user and DNS resolvers,
preventing any spying, spoofing or man-in-the-middle attacks.

%prep
%setup -q

%build
%cmake
%cmake_build


%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_name}.desktop

%post
%systemd_post %{app_name}@.service
%systemd_post %{app_name}_test@.service
%systemd_post %{app_name}_test_v2.service

%preun
%systemd_preun %{app_name}@.service
%systemd_preun %{app_name}_test@.service
%systemd_post %{app_name}_test_v2.service

%postun
%systemd_postun %{app_name}@.service
%systemd_postun %{app_name}_test@.service
%systemd_post %{app_name}_test_v2.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{app_name}
%{_datadir}/applications/%{app_name}.desktop
%{_libexecdir}/kf5/kauth/dnscrypt_client_helper
%{_datadir}/dbus-1/system-services/pro.russianfedora.dnscryptclient.service
%{_datadir}/polkit-1/actions/pro.russianfedora.dnscryptclient.policy
%{_datadir}/dbus-1/system.d/pro.russianfedora.dnscryptclient.conf
%{_libexecdir}/kf5/kauth/dnscrypt_client_test_helper
%{_datadir}/dbus-1/system-services/pro.russianfedora.dnscryptclienttest.service
%{_datadir}/polkit-1/actions/pro.russianfedora.dnscryptclienttest.policy
%{_datadir}/dbus-1/system.d/pro.russianfedora.dnscryptclienttest.conf
%{_libexecdir}/kf5/kauth/dnscrypt_client_reload_helper
%{_datadir}/dbus-1/system-services/pro.russianfedora.dnscryptclientreload.service
%{_datadir}/polkit-1/actions/pro.russianfedora.dnscryptclientreload.policy
%{_datadir}/dbus-1/system.d/pro.russianfedora.dnscryptclientreload.conf
%{_datadir}/knotifications5/%{app_name}.notifyrc
%{_unitdir}/%{app_name}@.service
%{_unitdir}/%{app_name}_test@.service
%{_unitdir}/%{app_name}_test_v2.service
%{_datadir}/icons/hicolor/64x64/apps/%{app_name}.png

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.24.18-2
- Rebuild (qt5)

* Sun Jun 12 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.24.18-1
- Update to 1.24.18

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.24.17-6
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.24.17-5
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Fl@sh <kaperang07@gmail.com> - 1.24.17-1
- enhanced R;
- version updated;

* Mon Nov 23 07:51:46 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1.21.16-14
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.21.16-13
- rebuild (qt5)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.21.16-11
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1.21.16-9
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.21.16-8
- rebuild (qt5)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.21.16-6
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 1.21.16-5
- rebuild (qt5)

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.21.16-4
- rebuild (qt5)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.21.16-2
- rebuild (Qt5)

* Wed Dec 26 2018 Fl@sh <kaperang07@gmail.com> - 1.21.16-1
- enhanced R, BR, %%postun, delete %%posttrans;
- version updated;

* Mon Dec 24 2018 Fl@sh <kaperang07@gmail.com> - 1.20.15-1
- enhanced %%description;
- added new unit file to %%files, %%post, %%preun, %%postun;
- version updated;

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.11.15-6
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 1.11.15-5
- rebuild (qt5)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.11.15-3
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.11.15-2
- rebuild (qt5)

* Mon Mar  5 2018 Fl@sh <kaperang07@gmail.com> - 1.11.15-1
- version updated;

* Wed Feb 21 2018 Fl@sh <kaperang07@gmail.com> - 1.11.14-1
- version updated;

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 1.11.11-4
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.11.11-2
- rebuild (qt)

* Mon Jan 15 2018 Fl@sh <kaperang07@gmail.com> - 1.11.11-1
- version updated;

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.11.10-7
- Remove obsolete scriptlets

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.11.10-6
- rebuild (qt5)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.11.10-5
- rebuild (qt5)

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.11.10-4
- BR: qt5-qtbase-private-devel
- drop explicit qt5/kf5 deps (rpm handles that automatically)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Fl@sh <kaperang07@gmail.com> - 1.11.10-1
- version updated;

* Tue Jun 27 2017 Fl@sh <kaperang07@gmail.com> - 1.10.10-1
- version updated;

* Thu Jun 22 2017 Fl@sh <kaperang07@gmail.com> - 1.10.9-1
- version updated;

* Sat Jun  3 2017 Fl@sh <kaperang07@gmail.com> - 1.10.8-1
- changed %%files for reload_helper;
- version updated;

* Mon May 22 2017 Fl@sh <kaperang07@gmail.com> - 1.9.8-1
- changed %%files for test_helper;
- version updated;

* Mon Mar 27 2017 Fl@sh <kaperang07@gmail.com> - 1.6.8-2
- release updated;

* Mon Mar 27 2017 Fl@sh <kaperang07@gmail.com> - 1.6.8-1
- version updated;
- changed %%post, %%preun, %%postun, %%files for new systemd unit;

* Sun Jan 29 2017 Fl@sh <kaperang07@gmail.com> - 1.5.7-1
- version updated;

* Tue Jan 10 2017 Fl@sh <kaperang07@gmail.com> - 1.3.7-1
- version updated;

* Fri Dec 16 2016 Fl@sh <kaperang07@gmail.com> - 1.2.3-4
- removed dbus-1 R;
- release updated;

* Wed Dec  7 2016 Fl@sh <kaperang07@gmail.com> - 1.2.3-3
- returned gcc-c++ BR;
- release updated;

* Wed Dec  7 2016 Fl@sh <kaperang07@gmail.com> - 1.2.3-2
- removed gcc-c++ BR, fixed dbus-1 R;
- added scriptlets for update Icon_Cache;
- added %%license in %%files;
- release updated;

* Wed Dec  7 2016 Fl@sh <kaperang07@gmail.com> - 1.2.3-1
- enhanced Summary and %%description;
- removed useless socket unit from scriplets and %%files;
- version updated;

* Mon Nov 28 2016 Fl@sh <kaperang07@gmail.com> - 1.2.2-4
- added cmake, gcc-c++ BR;
- added systemd scriptlets;
- release updated;

* Sun Nov 27 2016 Fl@sh <kaperang07@gmail.com> - 1.2.2-3
- changed package name to comply with the NamingGuidelines;
- release updated;

* Fri Nov 25 2016 Fl@sh <kaperang07@gmail.com> - 1.2.2-2
- changed package name to comply with the NamingGuidelines;
- release updated;

* Fri Nov 25 2016 Fl@sh <kaperang07@gmail.com> - 1.2.2-1
- version updated;

* Tue Nov 22 2016 Fl@sh <kaperang07@gmail.com> - 1.0.0-2
- enhanced Summary and %%description;
- release updated;

* Mon Nov 21 2016 Fl@sh <kaperang07@gmail.com> - 1.0.0-1
- Initial build
