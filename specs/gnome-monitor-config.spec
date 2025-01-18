%global commit 04b854e6411cd9ca75582c108aea63ae3c202f0e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20230925
%global fgittag %{gitdate}.git%{shortcommit}

Summary: GNOME Monitor Configuration Tool
Name: gnome-monitor-config
Version: 0
Release: 0.16%{?fgittag:.%{fgittag}}%{?dist}
#Note that the license isn't included in source yet, see this pull request:
#https://github.com/jadahl/gnome-monitor-config/pull/1
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/jadahl/gnome-monitor-config
Source0:  https://github.com/jadahl/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gcc
BuildRequires: cairo-devel

# 32bit package serves very little purpose:
ExcludeArch: %{ix86}

%description
A CLI configuration tool used for changing monitor settings in GNOME.
This can be used in Wayland, with functionality similar to xrandr on X11.

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
install -m 755 */src/%{name} -D %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%{_bindir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20230925.git04b854e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.15.20230925.git04b854e
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20230925.git04b854e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20230925.git04b854e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20230925.git04b854e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 05 2023 Jeremy Newton <alexjnewt AT hotmail DOT com> * 0-0.11.20230925.git04b854e
- Update to latest git

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20190520.gitbc2f76c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri May 31 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> 0-0.1.20190520.gitbc2f76c
- Intial Package
