Name:           qtpass
Version:        1.3.2
Release:        10%{?dist}
Summary:        Cross-platform GUI for pass

License:        GPLv3
URL:            https://qtpass.org/
Source0:        https://github.com/IJHack/qtpass/archive/v%{version}.tar.gz
# Wrapper script for GNOME on Wayland
Source1:        qtpass.sh.in


# required tools
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  sed
# required libraries (QT)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(Qt5Svg)
# install/check desktop files
BuildRequires:  desktop-file-utils
# for ownership of hicolor directories
Requires:       hicolor-icon-theme
# for icons to appear without freedesktop
Requires:       qt5-qtsvg
Requires:       pass

Recommends:     git
Recommends:     gpg2
Recommends:     pwgen

%description
QtPass is a cross-platform GUI for pass, the standard Unix password manager.

%prep
%autosetup -S git -n QtPass-%{version}


%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}
desktop-file-install %{name}.desktop
install -Dpm 644 artwork/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/qtpass-icon.svg
install -Dpm 644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Move the qtpass binary and replace it with the wrapper script
install -Dpm 755 %{buildroot}%{_bindir}/qtpass %{buildroot}%{_libexecdir}/qtpass
sed -e 's,/__PREFIX__,%{_libexecdir},g' %{SOURCE1} > %{buildroot}%{_bindir}/qtpass
chmod 755 %{buildroot}%{_bindir}/qtpass


%files
%doc README.md
%license LICENSE
%{_bindir}/qtpass
%{_libexecdir}/qtpass
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}-icon.svg
%{_mandir}/man1/%{name}.1*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 20 2022 Arthur Bols <arthur@bols.dev> - 1.3.2-9
- Added wrapper script that fixes GNOME on Wayland issues.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Arthur Bols <arthur@bols.dev> - 1.3.2-7
- Rebuilt for Fedora 35

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Fri Sep 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Dave Olsthoorn - 1.2.3-1
- new version, changelog: https://github.com/IJHack/qtpass/releases/tag/v1.2.3

* Thu May 10 2018 Dave Olsthoorn <dave@bewaar.me> - 1.2.2-1
- new version upstream

* Sun Feb 18 2018 Dave Olsthoorn <dave@bewaar.me> - 1.2.1-3
- add gcc-c++ to buildrequires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Dave Olsthoorn <dave@bewaar.me. - 1.2.1-1
- new version fixing a critical bug in password generation
  https://github.com/IJHack/QtPass/issues/338

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-2
- Remove obsolete scriptlets

* Thu Nov 09 2017 Dave Olsthoorn <dave@bewaar.me> - 1.2.0-1
- new version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Dave Olsthoorn <dave@bewaar.me> - 1.1.6-1
- new version, changelog: https://github.com/IJHack/qtpass/releases/tag/v1.1.6

* Wed Sep 28 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 1.1.4-1
- new version, changelog: https://github.com/IJHack/qtpass/releases/tag/v1.1.4

* Thu Jun 16 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 1.1.3-2
- install upstream manpage

* Wed Jun 15 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 1.1.3-1
- version bump
- add qt5-qtsvg as runtime dependency

* Sun May 22 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 1.1.1-3
- add appstream data file

* Sat Apr 23 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 1.1.1-2
- require hicolor

* Thu Apr 14 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 1.1.1-1
- new version
- Change license field to GPLv3 instead of GPL-3.0
- Fix require for pass
- Add icon cache scriplets

* Fri Apr  1 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com>
- Initial spec file
