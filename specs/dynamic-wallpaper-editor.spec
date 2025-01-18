%global uuid    com.github.maoschanz.DynamicWallpaperEditor

Name:           dynamic-wallpaper-editor
Version:        2.7
Release:        10%{?dist}
Summary:        Utility for creation or edition GNOME desktop's XML wallpapers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/maoschanz/dynamic-wallpaper-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme

%description
The GNOME desktop allows the wallpaper to change with time.

These dynamic wallpapers are XML files, and you don't want to write these files
yourself: Dynamic Wallpaper Editor is a little utility for the creation or the
edition of these XML wallpapers.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jul 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.7-1
- build(update): 2.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6-1
- build(update): 2.6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5-1
- Update to 2.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4-1
- Update to 2.4

* Sun Sep 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3-1
- Update to 2.3

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.1-2
- Tiny fix

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Wed Jul 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0-2
- Update to 2.1.0

* Mon Jul 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-2
- Initial package
