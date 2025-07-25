Name:           inertiablast
Version:        0.93
Release:        11%{?dist}
Summary:        Steal energy pods to defeat the empire
# Almost all is GPLv2+ with some graphics using the other licenses
# Automatically converted from old format: GPLv2+ and CC0 and CC-BY and (CC-BY or GPLv3) - review is highly recommended.
License:        GPL-2.0-or-later AND CC0-1.0 AND LicenseRef-Callaway-CC-BY AND (LicenseRef-Callaway-CC-BY OR GPL-3.0-only)
URL:            http://identicalsoftware.com/inertiablast/

Source0:        %{url}/%{name}-%{version}.tgz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: libgamerzilla-devel
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: SDL2-devel
BuildRequires: SDL2_mixer-devel
Requires:      hicolor-icon-theme


%description
The rebellion captured several warships but lack the energy pod to
power the ships. You are part of a risky expedition to steal the energy
pods. Defense systems will attempt to stop you. The energy pods are
often stored in tunnels making them hard to retrieve. The massive weight
of the pod increases the difficultly in getting out.

Inertia Blast is a remake of an C64 game called Thrust.


%prep
%setup -q


%build
%cmake
%cmake_build


%install
%cmake_install
\

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/man/man6/%{name}.6*


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.93-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 14 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.93-1
- Upgrade to new release

* Mon Sep 13 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.92-2
- Fix buildrequires to use SDL2 not SDL.

* Mon Sep 06 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.92-1
- Upgrade to new release.

* Mon Sep 06 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.91-2
- Add man page, use name macro everywhere and update license.

* Sun Sep 05 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.91-1
- Initial build
