%global ename  dash-to-panel
%global extdir %{_datadir}/gnome-shell/extensions/dash-to-panel@jderose9.github.com

Name:           gnome-shell-extension-%{ename}
Version:        64
Release:        2%{?dist}
Summary:        Integrated icon taskbar and status panel for Gnome Shell
License:        GPL-2.0-or-later
URL:            https://github.com/home-sweet-gnome/dash-to-panel
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/home-sweet-gnome/dash-to-panel/pull/1948
Patch0:         %{name}-system-install-paths.patch
BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  %{_bindir}/glib-compile-schemas
Requires:       gnome-shell >= 45~rc

%description
Dash to Panel is an icon taskbar for Gnome Shell. This extension moves the dash
into the gnome main panel so that the application launchers and system tray are
combined into a single panel, similar to that found in KDE Plasma and Windows
7+. A separate dock is no longer needed for easy access to running and favorited
applications.

%prep
%autosetup -n %{ename}-%{version} -p1

%build
%make_build VERSION=%{version}

%install
%make_install VERSION=%{version}
rm -v %{buildroot}%{extdir}/{COPYING,README.md}

%find_lang %{ename}

%files -f %{ename}.lang
%license COPYING
%doc README.md
%{extdir}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{ename}.gschema.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 26 2024 Dominik Mierzejewski <dominik@greysector.net> - 64-1
- update to 64 (resolves rhbz#2319313)

* Wed Oct 02 2024 Dominik Mierzejewski <dominik@greysector.net> - 63-1
- update to 63 (resolves rhbz#2313910)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Dominik Mierzejewski <dominik@greysector.net> - 62-2
- rebuild without unused clutter dependency

* Fri Apr 05 2024 Dominik Mierzejewski <dominik@greysector.net> - 62-1
- update to 62 (#2272810)

* Sun Mar 24 2024 Dominik Mierzejewski <dominik@greysector.net> - 61-1
- update to 61 (#2271317)

* Thu Mar 07 2024 Dominik Mierzejewski <dominik@greysector.net> - 60-2
- apply upstream PR for GNOME Shell 46 support (#2267061)

* Sun Feb 04 2024 Dominik Mierzejewski <dominik@greysector.net> - 60-1
- update to 60 (#2257860)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 25 2023 Dominik Mierzejewski <dominik@greysector.net> - 59-1
- update to 59 (resolves rhbz#2240510)
- drop obsolete patches

* Thu Sep 07 2023 Dominik Mierzejewski <dominik@greysector.net> - 56-1
- update to 56
- apply upstream patch and PR for GNOME Shell 45 support

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Dominik Mierzejewski <dominik@greysector.net> - 55-2
- correct run-time dependencies
- add explicit slash to extdir
- add missing comment

* Wed Mar 15 2023 Dominik Mierzejewski <dominik@greysector.net> - 55-1
- intial package
