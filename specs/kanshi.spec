%global forgeurl https://git.sr.ht/~emersion/kanshi

Name:           kanshi
Version:        1.7.0
Release:        3%{?dist}
Summary:        Dynamic display configuration for Wayland

# Overall project license: MIT
#
# protocol/wlr-output-management-unstable-v1.xml:
# The file is licensed under HPND-sell-variant; it is processed to C-compilable
# files by the `wayland-scanner` binary during build and doesn't alter the main
# license of the binary.
License:        MIT
URL:            https://sr.ht/~emersion/kanshi
Source0:        %{forgeurl}/refs/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{forgeurl}/refs/download/v%{version}/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
Source3:        %{name}.service

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.59.0
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(libvarlink)
BuildRequires:  pkgconfig(scdoc) >= 1.9.2
BuildRequires:  pkgconfig(scfg)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)

Enhances:       sway

%description
kanshi allows you to define output profiles that are automatically enabled
and disabled on hotplug. For instance, this can be used to turn a laptop's
internal screen off when docked.

This is a Wayland equivalent for tools like autorandr. kanshi can be used
on Wayland compositors supporting the wlr-output-management protocol.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
# install systemd service
install -D -m 0644 -pv %{SOURCE3} %{buildroot}%{_userunitdir}/%{name}.service


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*.*
%{_mandir}/man5/%{name}.*
%{_userunitdir}/%{name}.service


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 (#2290950)

* Mon Mar 25 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#2268225)

* Thu Feb 01 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1 (#2262318)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 27 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#2255992)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#2218855)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1 (#2153462)
- Convert License tag to SPDX

* Wed Aug 24 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0 (#2121130)
- Update upstream URL
- Add systemd user service

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Add source verification

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Aleksei Bavshin <alebastr89@gmail.com> - 1.1.0-1
- Initial import (#1825361)
