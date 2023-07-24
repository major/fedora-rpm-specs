%global uuid com.github.aggalex.%{name}

Name:           wineglass
Version:        1.2.1
Release:        5%{?dist}
Summary:        GUI for Wine

# The entire source code is GPLv3+ except:
#   * GPLv2+:   src/Actions.vala
#               src/css/Css.vala
#               src/widgets/Application.vala
#               src/widgets/AppsList.vala
#               src/widgets/Headerbar.vala
#               src/widgets/MainBox.vala
#               src/widgets/NamePopover.vala
#               src/widgets/SettingsButton.vala
License:        GPLv3+
URL:            https://github.com/aggalex/Wineglass
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme
Requires:       wine
Requires:       winetricks

Recommends:     libvkd3d
Recommends:     wine-dxvk

%description
Wineglass is a small application that allows the user to manage their
wineprefixes easily and install windows programs without the need of the
terminal. It can:

  * Easily create and remove wineprefixes.
  * Install supported windows apps on their corresponding wineprefix.
  * Make installed apps available normally through the applications menu.
  * Provide an easy way to add windows libraries to wineprefixes through
    "winetricks".
  * Configure wine.
  * run winprefix-specific system apps.

This app is useful for running windows apps and games easily without hassle.


%prep
%autosetup -n Wineglass-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}

# Remove HiDPI dupes
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE.md
%doc README.md
%{_bindir}/%{uuid}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.xml


%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.1-1
- Initial Package
