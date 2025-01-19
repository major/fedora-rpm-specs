Name:           nwg-launchers
Version:        0.7.1
Release:        8%{?dist}
Summary:        GTK-based launchers for sway and other window managers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/nwg-piotr/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  cmake(nlohmann_json)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.5.0
BuildRequires:  pkgconfig(gtkmm-3.0)

# Gdk-pixbuf loader for svg icons
Requires:       librsvg2%{?_isa}

%description
GTK-based launchers: application grid, button bar, menu, dmenu
for sway and other window managers.
The project priorities are:
 - it must work well on sway;
 - it should work as well as possible on Wayfire, i3, dwm and Openbox.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


# This set of application launchers is written for minimalistic keyboard-oriented
# environments and is not intended to be used with major DEs such as GNOME or KDE.
# Therefore, upstream does not provide .desktop files and we're not generating
# them downstream
%files
%license LICENSE
%doc %{_datadir}/%{name}/README.md
%doc examples
%{_bindir}/nwgbar
%{_bindir}/nwgdmenu
%{_bindir}/nwggrid
%{_bindir}/nwggrid-server
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/icon-missing.{png,svg}
%{_datadir}/%{name}/nwgbar/
%{_datadir}/%{name}/nwgdmenu/
%{_datadir}/%{name}/nwggrid/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.1-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1 (#2137099)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 25 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Fri Sep 17 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1
- Add runtime dependency on librsvg pixbuf loader

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Sat Jan 30 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.3-1
- Update to 0.4.3

* Fri Nov 06 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Thu Nov 05 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Tue Sep 22 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Thu Sep 17 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.3.4-1
- Initial import (#1878898)
