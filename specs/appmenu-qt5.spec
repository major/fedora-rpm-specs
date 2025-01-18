Name:       appmenu-qt5
Version:    0.3.0+16.10.20160628.1
Release:    38%{?dist}
Summary:    Support for global DBus-exported application menu in Qt5

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:    LGPL-3.0-only
URL:        https://launchpad.net/%{name}
Source0:    http://archive.ubuntu.com/ubuntu/pool/main/a/%{name}/%{name}_%{version}.orig.tar.gz

Patch1:     appmenu-qt5-0.3.0-fix-qt-compatibility.patch

BuildRequires:  dbusmenu-qt5-devel
BuildRequires:  gtk2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  systemd-devel
BuildRequires: make

%description
This is a different, Qt5-compatible approach of the existing appmenu-qt
(https://launchpad.net/appmenu-qt).

%{name} is a Qt5 QPA theme plugin that adds support for application
menus to Qt5 applications.  This only works for Qt5 versions >= 5.2
currently.  To enable the support, set QT_QPA_PLATFORMTHEME=%{name}
in your environment or install the %{name}-profile.d package to
enable system-wide, see README.fedora *BEFORE* for further information.


%package profile.d
Summary:    Profile.d-config for %{name}

BuildArch:  noarch

Requires:   %{name}		== %{version}-%{release}
Requires:   setup

%description profile.d
This package contains profile.d-config-files for %{name}.


%prep
%autosetup -c -p1
%{__mkdir} -p %{_target_platform}

# Set permissions on integration-file.
%{__chmod} 0644 data/%{name}.sh

# Create %%{name}.csh for profile.d.
%{__cat} << EOF > data/%{name}.csh
setenv QT_QPA_PLATFORMTHEME %{name}
EOF
%{_bindir}/touch -r data/%{name}.sh data/%{name}.csh

# Create README.fedora
%{__cat} << EOF > README.fedora
This package contains a script named %{name}.sh, which activates
the global menu for Qt5 applications.

To activate it globally for all users, install %{name}-profile.d.
This is not recommended, because it works currently only with plasma-
widget-menubar in KDE SC4, all other desktops are not affected. It
would cause that the menubar of Qt5 applications is not visible there.
Unfortunately %{name} is its own Qt5-"platform", which means
enabling it breaks all other platform integration in Qt 5.  There is
not much you can do about that, but not enabling it.

To activate it for a certain user, integrate the contenst of the same
file located in %%doc into the appropriate autostart.
EOF


%build
pushd %{_target_platform}
%{qmake_qt5} CONFIG+=enable-by-default ../appmenu.pro
%make_build
popd


%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%{__install} -pm 0644 data/%{name}.csh %{buildroot}%{_sysconfdir}/profile.d
# for some reason a cmake config gets pulled into the install
rm -fr %{buildroot}%{_libdir}/cmake

%files
%license COPYING
%doc data/%{name}.csh data/%{name}.sh README README.fedora
%{_libdir}/qt5/plugins/platformthemes/lib%{name}.so

%files profile.d
%{_sysconfdir}/profile.d/%{name}.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0+16.10.20160628.1-37
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-30
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-29
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-28
- Rebuild (qt5)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 07:47:26 CET 2020 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-24
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-23
- rebuild (qt5)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0+16.10.20160628.1-21
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-19
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-18
- rebuild (qt5)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-16
- rebuild (qt5)

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0+16.10.20160628.1-15
- rebuild 9qt5)

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0+16.10.20160628.1-14
- rebuild (qt5)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0+16.10.20160628.1-12
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-10
- rebuild (qt5)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0+16.10.20160628.1-9
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0+16.10.20160628.1-8
- rebuild (qt5)

* Thu Mar 29 2018 Jan Grulich <jgrulich@redhat.com> - 0.3.0+16.10.20160628.1-7
- Fix build against latest Qt5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0+16.10.20160628.1-5
- BR: qt5-qtbase-private-devel

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0+16.10.20160628.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 07 2016 Björn Esser <fedora@besser82.io> - 0.3.0+16.10.20160628.1-1
- Update to new release v0.3.0+16.10.20160628.1
- Un-retirement (rhbz 1382811)
- Update to recent packaging-guidelines

* Fri Oct 07 2016 Björn Esser <fedora@besser82.io> - 0.3.0+16.10.20160628.1-0.1
- Re-review after retirement (rhbz 1382811)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.r26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.r26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.r26-4
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.r26-3
- %%changelog cleanup
- Move the .cmake file to a -devel subpackage

* Sun Jan 25 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.r26-2
- Dropped non-existent version number
- Use the script as example, move it to %%doc
- Add README.fedora

* Wed Dec 17 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 0.r26-1
- Initial package
