Name:           qmasterpassword
Version:        2.0
Release:        5%{?dist}
Summary:        Stateless graphical Master Password Manager

%global project_name qMasterPassword
%global git_tag v%{version}

License:        GPL-3.0-only
URL:            https://github.com/bkueng/qMasterPassword
Source0:        https://github.com/bkueng/%{project_name}/archive/%{git_tag}/%{project_name}-%{git_tag}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel >= 6.5.0
BuildRequires:  qt6-qttools-devel >= 6.5.0
BuildRequires:  openssl-devel
BuildRequires:  libscrypt-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
qMasterPassword is a password manager based on Qt. Access all your passwords
using only a single master password. But in contrast to other managers it does
not store any passwords: Unique passwords are generated from the master password
and a site name. This means you automatically get different passwords for each
account and there is no password file that can be lost or get stolen. There is
also no need to trust any online password service.

https://spectre.app also contains other compatible software for various
platforms, like Android or iOS.


%prep
%setup -qn %{project_name}-%{version}


%build
%{cmake} \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DDISABLE_FILL_FORM_SHORTCUTS=1
%{cmake_build}


%install
%{cmake_install}
%find_lang translation --with-qt

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        data/%{project_name}.desktop

install -m 0644 -p -D data/icons/app_icon.png \
        %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -m 0644 -p -D data/%{project_name}.appdata.xml \
        %{buildroot}%{_metainfodir}/%{project_name}.appdata.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{project_name}.appdata.xml
%{cmake} \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Debug
%{cmake_build} --target test


%files -f translation.lang
%license LICENSE
%doc README.md HISTORY
%{_bindir}/%{project_name}
%{_datadir}/applications/%{project_name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{project_name}.appdata.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Stefan Becker <chemobejk@gmail.com> 2.0-1
- update to version 2.0
- drop downstream patches
- switch from qmake + make to cmake + ninja
- disable fill form shortcuts as they don't work under Wayland anyway
- add translations (de, pl)

* Fri Oct 06 2023 Stefan Becker <chemobejk@gmail.com> 1.2.4-1
- update to version 1.2.4
- change from Qt5 to Qt6
- changes from package review (bz #2241780)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2.2-15
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.2.2-13
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Beat Küng <beat-kueng@gmx.net> 1.2.2-1
- update to version 1.2.2

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.2.1-2
- use %%qmake_qt5 to ensure proper build flags

* Thu Jul 16 2015 Beat Küng <beat-kueng@gmx.net> 1.2.1-1
- update to version 1.2.1
- add BuildRequires: libX11-devel, libXtst-devel

* Thu Jul 16 2015 Beat Küng <beat-kueng@gmx.net> 1.1-3
- readd build version requirement for qt >= 5.2
- use escaping for %%check in changelog

* Wed Jul 15 2015 Beat Küng <beat-kueng@gmx.net> 1.1-2
- remove requirement for qt >= 5.2 (users are expected to already use a newer
  version)
- run unit tests in %%check

* Sat Feb 14 2015 Beat Küng <beat-kueng@gmx.net> 1.1-1
- first version
