Name: radeon-profile
Version: 20200824
Release: 14%{?dist}
Summary: Application to read current clocks of ATi Radeon cards

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/marazmista/radeon-profile
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Categories in radeon-profile.desktop
# https://github.com/marazmista/radeon-profile/pull/251
Patch0: https://github.com/marazmista/%{name}/pull/251.patch#/fix-categories-cincradeon-profile.desktop.patch

# add AppData manifest
# https://github.com/marazmista/radeon-profile/pull/253
Patch1: https://github.com/marazmista/%{name}/pull/253.patch#/add-appdata-manifest.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: qt5-linguist

BuildRequires: pkgconfig(libdrm) >= 2.4.79
BuildRequires: pkgconfig(Qt5) >= 5.6
BuildRequires: pkgconfig(Qt5Charts)
BuildRequires: pkgconfig(xrandr)

Requires: hicolor-icon-theme

Recommends: glx-utils
Recommends: mesa-demos
Recommends: radeon-profile-daemon%{?_isa}

Suggests: xrandr

%description
Simple application to read current clocks of ATi Radeon cards (xf86-video-ati,
xf86-video-amdgpu).

Functionality:

- Monitoring of basic GPU parameters (frequencies, voltages, usage,
  temperature, fan speed)
- DPM profiles and power levels
- Fan control (HD 7000+), definition of multiple custom curves or fixed speed
- Overclocking (amdgpu) (Wattman, Overdrive, PowerPlay etc)
- Per app profiles/Event definitions (i.e. change fan profile when temp above
  defined or set DPM to high when selected binary executed)
- Define binaries to run with set of environment variablees (i.e. GALLIUM_HUD,
  MESA, LIBGL etc)


%prep
%autosetup -p1


%build
pushd %{name}

# Build translations
lrelease-qt5 %{name}.pro

%qmake_qt5 %{name}.pro
%make_build
popd


%install
%make_install \
    INSTALL_ROOT=%{buildroot} \
    -C %{name}

pushd %{name}/translations
find . -maxdepth 1 -name '*.qm' -exec install -Dpm644 '{}' -t '%{buildroot}%{_datadir}/%{name}/' \;
popd

install -Dpm0644 %{name}/extra/com.github.marazmista.%{name}.appdata.xml \
  -t %{buildroot}%{_metainfodir}/


%check
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md 
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 20200824-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 20200824-4
- build: Replace xorg-x11-server-utils with xrandr | RH#1934358

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200824-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  9 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 20200824-2
- feat: Add AppData manifest

* Fri Jan  8 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 20200824-1
- Initial package
