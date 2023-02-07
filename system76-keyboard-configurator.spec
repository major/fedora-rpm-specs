%bcond_without check

%global tag      v1.3.0
%global forgeurl https://github.com/pop-os/keyboard-configurator
Version:         1.3.0
%forgemeta

Name:          system76-keyboard-configurator
Release:       3%{?dist}
Summary:       System76 Keyboard Configurator

License:       GPLv3
URL:           %{forgeurl}
Source:        %{forgesource}

Patch0:        fix-target-dependencies.patch
# Submitted for inclusion upstream.
# https://github.com/pop-os/keyboard-configurator/pull/117
Patch1:        update-palette-0.6.patch

ExclusiveArch: %{rust_arches}

BuildRequires: rust-packaging
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/appstream-util


%description
Application for configuration of System76 keyboard firmware.


%prep
%forgeautosetup -p1
%cargo_prep
%generate_buildrequires
# Temporarily remove workspace dependencies from the cargo manifest files before
# generating build requirements with cargo-inspector
for f in Cargo.toml backend/Cargo.toml widgets/Cargo.toml; do
  cd $(dirname $f)
  sed -i.br -r -e '/=\s*\{[^}]+path\s*=/d' Cargo.toml
  %cargo_generate_buildrequires -f default
  mv -f Cargo.toml{.br,}
  cd - >/dev/null
done


%build
%cargo_build


%install
%cargo_install
%__install -D -m 0644 -vp linux/com.system76.keyboardconfigurator.desktop                %{buildroot}%{_datadir}/applications/com.system76.keyboardconfigurator.desktop
%__install -D -m 0644 -vp linux/com.system76.keyboardconfigurator.appdata.xml            %{buildroot}%{_datadir}/metainfo/com.system76.keyboardconfigurator.appdata.xml
%__install -D -m 0644 -vp data/icons/scalable/apps/com.system76.keyboardconfigurator.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.system76.keyboardconfigurator.svg    
%__install -D -m 0644 -vp debian/com.system76.pkexec.keyboardconfigurator.policy         %{buildroot}%{_datadir}/polkit-1/actions/com.system76.pkexec.keyboardconfigurator.policy 


%if %{with check}
%check
%cargo_test
desktop-file-validate                 linux/com.system76.keyboardconfigurator.desktop
appstream-util validate-relax --nonet linux/com.system76.keyboardconfigurator.appdata.xml
%endif


%files
%{_bindir}/%{name}
%{_datadir}/applications/com.system76.keyboardconfigurator.desktop
%{_datadir}/metainfo/com.system76.keyboardconfigurator.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/com.system76.keyboardconfigurator.svg
%{_datadir}/polkit-1/actions/com.system76.pkexec.keyboardconfigurator.policy


%changelog
* Sun Feb 05 2023 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-3
- Rebuild for fixed frame pointer compiler flags in Rust RPM macros.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Link Dupont <linkdupont@fedoraproject.org> - 1.3.0-1
- New upstream version (RHBZ#2143483)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Link Dupont <linkdupont@fedoraproject.org> - 1.2.0-1
- New upstream version (RHBZ#2101683)

* Sat Feb 12 2022 Link Dupont <linkdupont@fedoraproject.org> - 1.0.0-5
- New upstream snapshot

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Link Dupont <linkdupont@fedoraproject.org> - 1.0.0-3.20211119git38c1c7b
- Patch to fix FTBFS with palette-0.6

* Mon Nov 22 2021 Link Dupont <linkdupont@fedoraproject.org> - 1.0.0-2.20211119git38c1c7b
- Updated dependencies

* Fri Oct  1 2021 Link Dupont <linkdupont@fedoraproject.org> - 1.0.0-1
- Initial package
