%global uuid    com.github.Latesil.%{name}

Name:           theme-switcher
Version:        2.0.4
Release:        20%{?dist}
Summary:        Switch dark/light GTK theme automatically during day/night

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/Latesil/theme-switcher
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Default systemd user unit preset for < F32
# * https://fedoraproject.org/wiki/Changes/Systemd_presets_for_user_units
Source1:        99-default.preset

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
BuildRequires:  meson >= 0.50.0
BuildRequires:  glib2-devel
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)

Requires:       gnome-terminal
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-gobject

%{?systemd_requires}

%description
A global automated switcher for dark/light GTK theme during day/night and more.

Theme-switcher automatically can switch your:

  - GTK theme
  - GNOME Terminal profiles
  - Wallpapers
  - More will come...

To read docs run:

  xdg-open %{_docdir}/%{name}/README.md


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}

%if 0%{?fedora} < 32
install -Dpm0644 %{SOURCE1} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
%endif


%check
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_user_post %{name}-auto.service

%preun
%systemd_user_preun %{name}-auto.service


%files -f %{uuid}.lang
%license LICENSE
%doc README.md CREDITS
%{_bindir}/%{name}-auto.py
%{_bindir}/%{name}-gui
%{_bindir}/%{name}-manual.py
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{_userunitdir}/%{name}-auto.*
%{python3_sitelib}/Themeswitcher/

%if 0%{?fedora} < 32
%{_prefix}/lib/systemd/user-preset/99-default.preset
%endif


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.4-19
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.4-17
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.0.4-14
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.4-11
- Rebuilt for Python 3.11

* Sun May 01 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.4-10
- build: Add dep gnome-terminal | GH#13

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.4-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.4-4
- Add systemd user unit preset which required for < F32

* Fri May 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.4-3
- Update to 2.0.4

* Fri May 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Thu May 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Fri Nov 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-1.20191109git9f0fdab
- Update to 1.0.0

* Mon Nov 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-1.20191104git7ec63be
- Update to latest git snapshot

* Sat Nov 02 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-1.20191102git0e9c4e0
- Update to latest git snapshot

* Wed Jul 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-1.20190801git570f378
- Update to latest git snapshot

* Sun Jul 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9-8.20190728gitb1a6284
- Update to latest git snapshot

* Sun Jul 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9-1.20190714git284cadb
- Update to latest git snapshot

* Wed Jun 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20190612gitceb42e5
- Initial package
