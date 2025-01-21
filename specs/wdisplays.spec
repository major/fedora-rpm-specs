# -*-Mode: rpm-spec -*-

Name:     wdisplays
Version:  1.1.1
Release:  6%{?dist}
Summary:  GUI display configurator for wlroots compositors
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:  GPL-3.0-or-later
URL:      https://github.com/artizirk/wdisplays

Source:  %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: libepoxy-devel
BuildRequires: meson
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

Conflicts: wlroots < 0.7.0
Requires:  hicolor-icon-theme

%description

wdisplays is a graphical application for configuring displays in
Wayland compositors. It borrows some code from kanshi. It should work
in any compositor that implements the
wlr-output-management-unstable-v1 protocol, including sway. The goal
of this project is to allow precise adjustment of display settings in
kiosks, digital signage, and other elaborate multi-monitor setups.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot}

desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    --set-icon %{name} \
    --set-key=Terminal --set-value=false \
    --remove-key=Version \
    --add-category=Settings --add-category=HardwareSettings \
    %{buildroot}/%{_datadir}/applications/network.cycles.%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*

%doc README.md

%license LICENSES/*

%clean

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.1-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-1
- new version

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Bob Hepple <bob.hepple@gmail.com> - 1.1-5
- rebuilt to fix FTBFS #2047112

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Bob Hepple <bob.hepple@gmail.com> - 1.1-3
- fixed install of .desktop file

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 20 2021 Bob Hepple <bob.hepple@gmail.com> - 1.1-1
- new version, new repo, new license

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Aleksei Bavshin <alebastr89@gmail.com> - 1.0-2
- Add patch for sway 1.5 compatibility
- Remove unnecessary BR: wlroots-devel

* Fri May 15 2020 Bob Hepple <bob.hepple@gmail.com> - 1.0-1
- new release

* Tue May 05 2020 Bob Hepple <bob.hepple@gmail.com> - 0.9-0.4.20200504git0faafdc
- added hicolor-icon-theme

* Tue May 05 2020 Bob Hepple <bob.hepple@gmail.com> - 0.9-0.3.20200504git0faafdc
- rebuilt to use desktop-file-install to modify the desktop file instead of patching

* Mon May 04 2020 Bob Hepple <bob.hepple@gmail.com> - 0.9-0.2.20200504git.0faafdc
- rebuilt for RHBZ#1830870

* Mon May 04 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1-0.1.20200504git.0faafdc
- prepare for Fedora review

* Wed Feb 19 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1-0.1.20200219git.ba331ca
- Initial version of the package
