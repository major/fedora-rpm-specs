%bcond_without check

%global tag      v1.3.7
%global forgeurl https://github.com/pop-os/keyboard-configurator
Version:         1.3.7
%forgemeta

Name:          system76-keyboard-configurator
Release:       %autorelease
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
%autochangelog
