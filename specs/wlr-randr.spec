%global forgeurl https://git.sr.ht/~emersion/wlr-randr

Name:           wlr-randr
Version:        0.4.1
Release:        3%{?dist}
Summary:        An xrandr clone for wlroots compositors

# Overall project license: MIT
#
# protocol/wlr-output-management-unstable-v1.xml:
# The file is licensed under HPND-sell-variant; it is processed to C-compilable
# files by the `wayland-scanner` binary during build and doesn't alter the main
# license of the binary.
License:        MIT
URL:            https://sr.ht/~emersion/wlr-randr/
Source0:        %{forgeurl}/refs/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{forgeurl}/refs/download/v%{version}/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)

%description
wlr-randr is an xrandr clone for wlroots compositors

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wlr-randr

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 06 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1 (#2268231)

* Sun Jan 28 2024 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0 (#2258908)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 13 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1 (#2243195)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 (#2164209)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0
- Convert License tag to SPDX
- Update upstream URL
- Verify source signature

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20200408git5ff601a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 28 2020 Morian Sonnet <MorianSonnet@googlemail.com> - 0-4.20200408git5ff601a
- Remove unnecessary BuildRequires

* Mon Apr 27 2020 Morian Sonnet <MorianSonnet@googlemail.com> - 0-3.20200408git5ff601a
- Remove unnecessary explicit requires

* Sat Apr 25 2020 Morian Sonnet <MorianSonnet@googlemail.com> - 0-2.20200408git5ff601a
- Use recommended source URL

* Mon Dec 02 2019 Morian Sonnet <MorianSonnet@googlemail.com> - 0-1.20190321gitc4066aa
- Initial build

