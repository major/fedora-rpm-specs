%global commit a836933742cc6e6f97d53de6f52cd58a2e1113b0
%global forgeurl https://github.com/Yubico/yubioath-desktop/

Name:       yubioath-desktop
Version:    5.1.0
Summary:    Yubikey tool for generating OATH event-based HOTP and time-based TOTP codes
License:    BSD
Release:    11%{?dist}
URL:        %{forgeurl}

%forgemeta

Source0:    %{forgesource}
Source1:    %{name}.rpmlintrc
Patch0:     rhbz-2053900-p0.patch

BuildRequires: make
BuildRequires: qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtsvg-devel gcc-c++
BuildRequires: python3 desktop-file-utils qt5-qtquickcontrols2-devel
BuildRequires: qt5-qtbase-private-devel qt5-qtmultimedia-devel
Requires:      pyotherside qt5-qtdeclarative qt5-qtquickcontrols pcsc-lite-ccid
Requires:      yubikey-manager < 5.0.0

%description
The Yubico Authenticator is a graphical desktop tool and CLI for generating
Open AuTHentication (OATH) event-based HOTP and time-based TOTP one-time
password codes, with the help of a YubiKey that protects the shared secrets.

%prep
%forgesetup
%autosetup -p1 -n %{archivename}
sed -i -e "s/python /python3 /" %{name}.pro
sed -i -e "1s|^#.*$|#!%{__python3}|g" build_qrc.py py/yubikey.py

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications resources/com.yubico.yubioath.desktop

# icons
install -Dpm0644 -t %{buildroot}%{_datadir}/icons/hicolor/128x128/apps resources/icons/*.png

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/applications/*

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Gerald Cox <gbcox@fedoraproject.org> - 5.1.0-10
- Requires yubikey-manager < 5.0.0 rhbz#2136583

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 5.1.0-8
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 5.1.0-7
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 5.1.0-6
- Rebuild (qt5)

* Sun Feb 13 2022 Gerald Cox <gbcox@member.fsf.org> - 5.1.0-5
- Rebuild to circumvent fedpkg update bug rhbz#2053900

* Sun Feb 13 2022 Gerald Cox <gbcox@member.fsf.org> - 5.1.0-4
- Resync build

* Sun Feb 13 2022 Gerald Cox <gbcox@member.fsf.org> - 5.1.0-3
- Titlebar icon incorrect for wayland rhbz#2053900

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 08 2021 Gerald Cox <gbcox@member.fsf.org> - 5.1.0-1
- Upstream release rhbz#2010689

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 20 2021 Gerald Cox <gbcox@member.fsf.org> - 5.0.5-2
- Correct runtime dependency - rhbz#1951421

* Thu Apr 15 2021 Gerald Cox <gbcox@member.fsf.org> - 5.0.5-1
- Upstream release - rhbz#1950109

* Tue Feb 09 2021 Gerald Cox <gbcox@fedoraproject.org> - 5.0.4-7.20210209git9ea38f7
- Patch for yubikey-manager 4.0 rhbz#1925637

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-6.git2e13158
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.4-5.git2e13158
- drop hard-coded Qt5 runtime dep (rely solely on symbol versioning)

* Mon Nov 23 07:55:54 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.0.4-4.git2e13158
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.0.4-3.git2e13158
- rebuild (qt5)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2.git2e13158
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Gerald Cox <gbcox@fedoraproject.org> - 5.0.4-1.git2e13158
- Upstream release rhbz#1835890

* Tue Apr 14 2020 Gerald Cox <gbcox@fedoraproject.org> - 5.0.3-1.git5e94bd8
- Upstream release rhbz#1823928

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-2.git4df579e
- rebuild (qt5)

* Fri Jan 31 2020 Gerald Cox <gbcox@fedoraproject.org> - 5.0.2-1.git4df579e
- Upstream release rhbz#1796501

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4.gitc58db92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.1-3.gitc58db92
- rebuild (qt5)

* Mon Oct 21 2019 Gerald Cox <gbcox@fedoraproject.org> - 5.0.1-2.gitc58db92
- Add rpmlintrc - rhbz#1762309

* Wed Oct 16 2019 Gerald Cox <gbcox@fedoraproject.org> - 5.0.1-1.gitc58db92
- Upstream release - rhbz#1762309

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.0-2.git121efe3
- rebuild (qt5)

* Mon Sep 23 2019 Gerald Cox <gbcox@fedoraproject.org> - 5.0.0-1.git121efe3b
- Upstream release - rhbz#1754707

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-8.gitd1187b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 4.3.5-7.gitd1187b6
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 4.3.5-6.gitd1187b6
- rebuild (qt5)

* Mon Apr 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.3.5-5.gitd1187b6
- track Qt private api usage (#1697330)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-4.gitd1187b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Gerald Cox <gbcox@fedoraproject.org> - 4.3.5-3.gitd1187b6
- Upstream release - rhbz#1655888

* Thu Jan 03 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.3.5-2.git0a8c363
- Trivial fixes

* Mon Dec 31 2018 Gerald Cox <gbcox@fedoraproject.org> - 4.3.5-1.git0a8c363
- Upstream release rhbz#1655888

* Tue Aug 14 2018 Seth Jennings <sethdjennings@gmail.com> - 4.3.3-4
- add python-unversioned-command to BuildRequires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.3.3-2
- Rebuilt for Python 3.7

* Wed May 2 2018 Seth Jennings <sethdjennings@gmail.com> - 4.3.3-1
- Upstream release

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.2.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.2.0-2
- Remove obsolete scriptlets

* Fri Dec 15 2017 Seth Jennings <sethdjennings@gmail.com> - 4.2.0-1
- Upstream release.

* Mon Aug 21 2017 Seth Jennings <sethdjennings@gmail.com> - 4.1.3-1
- Upstream release.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Seth Jennings <spartacus06@gmail.com> - 3.0.1-2
- Fix desktop application executable name

* Mon Jul 25 2016 Seth Jennings <spartacus06@gmail.com> - 3.0.1-1
- Upstream release.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Seth Jennings <spartacus06@gmail.com> - 2.3.0-2
- Add pyusb as a required package to avoid python ImportError (#1302895).

* Fri Nov 20 2015 Seth Jennings <spartacus06@gmail.com> - 2.3.0-1
- Upstream release.

* Thu Aug 27 2015 Seth Jennings <spartacus06@gmail.com> - 2.2.1-1
- Upstream release.

* Thu Aug 06 2015 Seth Jennings <spartacus06@gmail.com> - 2.1.1-3
- Use __python2 macro.

* Thu Aug 06 2015 Seth Jennings <spartacus06@gmail.com> - 2.1.1-2
- Add pcsc-lite-ccid requirement

* Thu Aug 06 2015 Seth Jennings <spartacus06@gmail.com> - 2.1.1-1
- Initial package release.
