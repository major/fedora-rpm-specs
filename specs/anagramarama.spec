Name:           anagramarama
Version:        0.7
Release:        9%{?dist}
Summary:        Anagram puzzle game
# Almost all is GPLv2+ with some graphics being CC-BY-SA
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://identicalsoftware.com/anagramarama/

Source0:        %{url}/%{name}-%{version}.tgz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libgamerzilla-devel
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: SDL2-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_image-devel
Requires:      hicolor-icon-theme


%description
Anagramarama is a simple wordgame in which one tries to guess all the different
permutations of a scrambled word which form another word within the
time limit.  Guess the original word and you move on to the next
level.


%prep
%setup -q


%build
%cmake
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%files
%doc readme
%license gpl.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/man/man6/%{name}.6*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Dennis Payne <dulsi@identicalsoftware.com> - 0.7-1
- Newest release

* Thu Dec 16 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.6-1
- Newest release

* Mon Sep 13 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.5-3
- Use name macro everywhere and updated license

* Fri Aug 06 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.5-2
- Changed man page to use asterisk and moved commands to check section

* Fri Aug 06 2021 Dennis Payne <dulsi@identicalsoftware.com> - 0.5-1
- Initial build
