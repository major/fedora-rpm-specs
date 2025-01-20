Summary: Take care of your own pigeon as they fight
Name: pigeonascent
Version: 1.5.2
Release: 12%{?dist}
License: MIT
Url: https://escada-games.itch.io/pigeon-ascent
Source0: http://www.identicalsoftware.com/pigeonascent/%{name}-%{version}.tgz
Source1: pigeonascent.desktop
Source2: pigeonascent.png
Source3: pigeonascent.metainfo.xml
BuildRequires: godot3-headless
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires: hicolor-icon-theme
Requires: godot3-runner
BuildArch:      noarch
ExcludeArch:    ppc64le
ExcludeArch:    s390x

%description
Take care of your own pigeon as they fight increasingly stronger foes, and
then facing the legendary Pigeon God at the end… can you keep death far from
your bird?

%prep
%setup -q -n pigeonAscent

%build
godot3-headless --export-pack Linux64 pigeonascent.pck

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
install -p -m 644 pigeonascent.pck %{buildroot}%{_datadir}/%{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml

%files
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%license LICENSE
%{_datadir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 03 2023 Dennis Payne <dulsi@identicalsoftware.com> - 1.5.2-7
- Use godot3 not godot4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Dennis Payne <dulsi@identicalsoftware.com> - 1.5.2-5
- Exclude architectures without godot support

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 20 2021 Dennis Payne <dulsi@identicalsoftware.com> - 1.5.2-2
- Use only buildroot not RPM_BUILD_ROOT

* Tue Sep 28 2021 Dennis Payne <dulsi@identicalsoftware.com> - 1.5.2-1
- Initial package creation.
