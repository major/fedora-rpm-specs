Summary:        Tools to manage network attached LXI compatible instruments
Name:           lxi-tools
Version:        2.8
Release:        2%{?dist}
# src/language-specs/lua-lxi-gui.lang is LGPL-2.1-or-later, rest is BSD-3-Clause
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://lxi-tools.github.io/
Source0:        https://github.com/lxi-tools/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxi-tools/lxi-tools/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  meson >= 0.53.2
BuildRequires:  readline-devel
BuildRequires:  liblxi-devel >= 1.13
BuildRequires:  lua-devel >= 5.1
BuildRequires:  pkgconfig(bash-completion)
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires:  glib2-devel >= 2.70
BuildRequires:  gtk4-devel >= 4.6.0
BuildRequires:  gtksourceview5-devel >= 5.4.0
BuildRequires:  json-glib-devel >= 1.4
BuildRequires:  libadwaita-devel >= 1.2
BuildRequires:  %{_bindir}/desktop-file-validate
BuildRequires:  %{_bindir}/appstream-util
%endif
Recommends:     bash-completion

%description
LXI tools are open source software tools for managing network attached
LXI (LAN eXtensions for Instrumentation) compatible test instruments
such as modern oscilloscopes, power supplies, spectrum analyzers etc.

Features include automatic discovery of test instruments, sending SCPI
commands, grabbing screenshots from supported instruments, benchmarking
SCPI message performance, and powerful scripting for test automation.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%meson \
%if 0%{?fedora} || 0%{?rhel} > 9
  -Dgui=true
%else
  -Dgui=false
%endif
%meson_build

%install
%meson_install

%if 0%{?fedora} || 0%{?rhel} > 9
%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/io.github.%{name}.lxi-gui.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/io.github.%{name}.lxi-gui.appdata.xml
%endif

%files
%license LICENSE
%doc AUTHORS NEWS README.md
%{_bindir}/lxi
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/lxi*
%{_mandir}/man1/lxi.1*
%if 0%{?fedora} || 0%{?rhel} > 9
%{_bindir}/lxi-gui
%{_datadir}/applications/io.github.%{name}.lxi-gui.desktop
%{_datadir}/glib-2.0/schemas/io.github.%{name}.lxi-gui.gschema.xml
%{_datadir}/icons/hicolor/*/apps/io.github.%{name}.lxi-gui*.svg
%{_metainfodir}/io.github.%{name}.lxi-gui.appdata.xml
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 01 2024 Robert Scheck <robert@fedoraproject.org> 2.8-1
- Upgrade to 2.8 (#2329636)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Robert Scheck <robert@fedoraproject.org> 2.7-1
- Upgrade to 2.7 (#2233001)

* Sat Jul 29 2023 Robert Scheck <robert@fedoraproject.org> 2.6-1
- Upgrade to 2.6 (#2227265)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Robert Scheck <robert@fedoraproject.org> 2.5-1
- Upgrade to 2.5 (#2172316)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Robert Scheck <robert@fedoraproject.org> 2.4-2
- Added upstream patch to build successfully using Lua 5.1

* Fri Dec 16 2022 Robert Scheck <robert@fedoraproject.org> 2.4-1
- Upgrade to 2.4 (#2153674)

* Sun Oct 30 2022 Robert Scheck <robert@fedoraproject.org> 2.3-1
- Upgrade to 2.3 (#2138618)

* Sat Oct 15 2022 Robert Scheck <robert@fedoraproject.org> 2.2-1
- Upgrade to 2.2 (#2135055)

* Sun Oct 02 2022 Robert Scheck <robert@fedoraproject.org> 2.1-3
- Build the lxi-gui application for Fedora 36 (and later)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 20 2022 Robert Scheck <robert@fedoraproject.org> 2.1-1
- Upgrade to 2.1 (#2049045)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Robert Scheck <robert@fedoraproject.org> 1.21-1
- Upgrade to 1.21

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.20-4
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Robert Scheck <robert@fedoraproject.org> 1.20-1
- Upgrade to 1.20

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Robert Scheck <robert@fedoraproject.org> 1.12-1
- Upgrade to 1.12

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.5-1
- Upgrade to 1.5

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.4-1
- Upgrade to 1.4

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.3-1
- Upgrade to 1.3

* Sun Oct 08 2017 Robert Scheck <robert@fedoraproject.org> 1.1-1
- Upgrade to 1.1
- Initial spec file for Fedora and Red Hat Enterprise Linux
