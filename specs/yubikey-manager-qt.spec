%global bname ykman-gui
Name: yubikey-manager-qt
Summary: Application for configuring any YubiKey over all USB interfaces
Version: 1.2.5
Release: 8%{?dist}
URL: https://developers.yubico.com/yubikey-manager-qt/
Source0: https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1: https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
Source2:  gpgkey-6690D8BC.gpg
Patch1: yubikey-manager-qt-1.2.5-remove-cloud-upload.patch

License: BSD-2-Clause

BuildRequires: gnupg2
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: python3
BuildRequires: libyubikey
BuildRequires: python3-yubikey-manager >= 4
BuildRequires: qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel
BuildRequires: qt5-qtquickcontrols qt5-qtgraphicaleffects pyotherside
BuildRequires: desktop-file-utils
Requires:      pyotherside 
Requires:      qt5-qtquickcontrols
Requires:      python3-yubikey-manager


%description
Cross-platform application for configuring any YubiKey over all USB interfaces.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n %{name}
%patch 1 -p1
sed -i 's|python |python3 |g' ykman-cli/ykman-cli.pro
sed -i 's|python |python3 |g' ykman-gui/ykman-gui.pro


%build
#qmake-qt5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}" QMAKE_STRIP="/bin/true";
%{qmake_qt5}
#make %{?_smp_mflags}
%{make_build}

%install
make install INSTALL_ROOT="%{buildroot}"
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 0644 resources/icons/ykman.png %{buildroot}%{_datadir}/pixmaps/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications resources/%{bname}.desktop

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{bname}
%{_datadir}/applications/%{bname}.desktop
%{_datadir}/pixmaps/ykman.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Jakub Jelen <jjelen@redhat.com> - 1.2.5-7
- Fix crash on startup once more

* Thu Aug 22 2024 Jakub Jelen <jjelen@redhat.com> - 1.2.5-6
- Fix yubikey detection (#2251082)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Jakub Jelen <jjelen@redhat.com> - 1.2.5-2
- Add missing dependency (#2214260)
- Use SPDX identifier for license field

* Tue Feb 07 2023 Jakub Jelen <jjelen@redhat.com> - 1.2.5-1
- New upstream release (#2167005)
- Remove dependency on old version of python-yubikey-manager (#2148957)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Jakub Jelen <jjelen@redhat.com> - 1.2.4-6
- Prevent update to yubikey-manager 5 which breaks API for now (#2143324)

* Wed Aug 03 2022 Jakub Jelen <jjelen@redhat.com> - 1.2.4-5
- Remove unneeded dependency (#2114566)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 23 2022 Jakub Jelen <jjelen@redhat.com> - 1.2.4-3
- Rebuild to solve the interminent issue with during rebuild (#2047140)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Jakub Jelen <jjelen@redhat.com> - 1.2.4-1
- New upstream release (#2017577)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Jakub Jelen <jjelen@redhat.com> - 1.2.3-1
- New upstream release (#1961590)

* Wed Apr 14 2021 Jakub Jelen <jjelen@redhat.com> - 1.2.2-1
- New upstream release (#1949527)

* Tue Apr 06 2021 Jakub Jelen <jjelen@redhat.com> - 1.2.1-2
- Add missing requires (#1945428)

* Wed Mar 31 2021 Jakub Jelen <jjelen@redhat.com> - 1.2.1-1
- New upstream release (#1944747)

* Wed Mar 17 2021 Jakub Jelen <jjelen@redhat.com> - 1.2.0-1
- New upstream release (#1939620)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Jakub Jelen <jjelen@redhat.com> - 1.1.5-3
- Add missing dependency (#1900902)

* Tue Sep 22 2020 Jakub Jelen <jjelen@redhat.com> - 1.1.5-2
- First release for Fedora 

