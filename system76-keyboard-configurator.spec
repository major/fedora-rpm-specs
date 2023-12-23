%bcond_without check

%global tag      v1.3.10
%global forgeurl https://github.com/pop-os/keyboard-configurator
Version:         1.3.10
%forgemeta

Name:          system76-keyboard-configurator
Release:       %autorelease
Summary:       System76 Keyboard Configurator

# * system76-keyboard-configurator: GPL-3.0-or-later
# * Rust crate dependencies:
#   (MIT OR Apache-2.0) AND Unicode-DFS-2016
#   Apache-2.0
#   Apache-2.0 OR BSL-1.0
#   Apache-2.0 OR MIT
#   Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
#   MIT
#   MIT OR Apache-2.0
#   Unicode-DFS-2016
#   Unlicense OR MIT
# LICENSE.dependencies contains a full license breakdown
License:       GPL-3.0-or-later AND Apache-2.0 AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:           %{forgeurl}
Source:        %{forgesource}

Patch0:        fix-target-dependencies.patch
# Submitted for inclusion upstream.
# https://github.com/pop-os/keyboard-configurator/pull/117
Patch1:        update-palette-0.6.patch

BuildRequires: cargo-rpm-macros >= 24
BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/appstream-util


%description
Application for configuration of System76 keyboard firmware.


%prep
%forgeautosetup -p1
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


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
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.system76.keyboardconfigurator.desktop
%{_datadir}/metainfo/com.system76.keyboardconfigurator.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/com.system76.keyboardconfigurator.svg
%{_datadir}/polkit-1/actions/com.system76.pkexec.keyboardconfigurator.policy


%changelog
%autochangelog
