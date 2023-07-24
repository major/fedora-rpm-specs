# -*-Mode: rpm-spec -*-

Name: wlogout
Version: 1.1.1
Release: 12%{?dist}
Summary: Wayland based logout menu
License: MIT
URL:     https://github.com/ArtsyMacaw/wlogout
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# appears to be from https://github.com/zserge/jsmn at git tag
# cdcfaafa49ffe5661978292a55cec7fd459571e4 and MIT license:
Provides: bundled(jsmn) = cdcfaafa49ffe5661978292a55cec7fd459571e4

BuildRequires: gcc
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: gnupg2

%description
A wayland based logout menu.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/zsh/
%{_datadir}/fish/
%{_datadir}/bash-completion/
%dir %{_sysconfdir}/%{name}

%license LICENSE

%doc README.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}.5.*

%config(noreplace) %{_sysconfdir}/%{name}/*

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-5
- fix issues from RHBZ#1821120

* Mon Apr 20 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-4
- fix issues from RHBZ#1821120

* Sun Apr 19 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-3
- fix issues from RHBZ#1821120

* Mon Apr 06 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-2
- fix issues from fedora-review

* Mon Mar 16 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.1-1
- version 1.1.1
