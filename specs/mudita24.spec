%global commit0 e38b1a39a8ca4f82b74d7b70bf9a3489e37b3588
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate 20160218

Name:           mudita24
Version:        1.1.0
Release:        15.%{commitdate}git%{shortcommit0}%{?dist}
Summary:        ALSA GUI control tool for Envy24 (ice1712) soundcards

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/NielsMayer/mudita24
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.xpm

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)
Requires:       alsa-utils

%description
Mudita24 is a modification of the Linux alsa-tools' envy24control: an
application controlling the digital mixer, channel gains and other hardware
settings for sound cards based on the VIA Ice1712 chipset aka Envy24. Unlike
most ALSA mixer controls, this application displays a level meter for each
input and output channel and maintains peak level indicators. This is based
on Envy24's hardware peak metering feature.

Mudita24 provides alternate name to avoid confusion with "envy24control
0.6.0" until changes in this version propagate upstream. As balance to the
"Envy", this project needed some Mudita "In Buddhism the third of the four
divine abidings is mudita, taking joy in the good fortune of another. This
virtue is considered the antidote to envy and the opposite of
schadenfreude."

This utility is preferable to alsamixer for those with ice1712-based
cards: M-Audio Delta 1010, Delta 1010LT, Delta DiO 2496, Delta 66, Delta 44,
Delta 410 and Audiophile 2496. Terratec EWS 88MT, EWS 88D, EWX 24/96, DMX
6Fire, Phase 88. Hoontech Soundtrack DSP 24, Soundtrack DSP 24 Value,
Soundtrack DSP 24 Media 7.1. Event Electronics EZ8. Digigram VX442.
Lionstracs, Mediastaton. Terrasoniq TS 88. Roland/Edirol DA-2496.


%prep
%autosetup -n %{name}-%{commit0}

%build
pushd %{name}
%cmake .
%cmake_build
popd

%install
pushd %{name}
%cmake_install
popd
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}
mkdir %{buildroot}%{_datadir}/pixmaps
install -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
    %{SOURCE1}

%files
%license %{name}/COPYING
%doc README %{name}/README.profiles
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-14.20160218gite38b1a3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4.20160218gite38b1a3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3.20160218gite38b1a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.1.0-2.20160218gite38b1a3
- Add icon and .desktop file

* Sat May 16 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.1.0-1.20160218gite38b1a3
- Initial release for Fedora
