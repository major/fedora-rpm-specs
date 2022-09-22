Name:           fuzzel
Version:        1.7.0
Release:        2%{?dist}
Summary:        Application launcher for wlroots based Wayland compositors

License:        MIT
URL:            https://codeberg.org/dnkl/fuzzel
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.53
BuildRequires:  tllist-static

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fcft) >= 3.0.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpng)
# BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
Fuzzel is a Wayland-native application launcher, similar to rofi's drun mode.

Features:
  * Wayland native
  * Rofi drun-like mode of operation
  * dmenu mode where newline separated entries are read from stdin
  * Emacs key bindings
  * Icons!
  * Remembers frequently launched applications


%prep
%autosetup -n %{name} -p1


%build
%meson                  \
  -Dsvg-backend=nanosvg \
  %{nil}
%meson_build


%install
%meson_install
# Will be installed to correct location with rpm macros
rm %{buildroot}%{_docdir}/%{name}/LICENSE


%check
%meson_test


%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 (#2051006)

* Mon Jan 31 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.5-3
- build: Switch to nanosvg | Fix FTBFS 36

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.5-1
- chore(update): 1.6.5

* Sat Oct 09 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.4-1
- chore(update): 1.6.4

* Fri Sep 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.3-1
- build(update): 1.6.3

* Sun Aug 15 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.2-1
- build(update): 1.6.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.1-1
- build(update): 1.6.1

* Wed Jun 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.0-1
- build(update): 1.6.0

* Tue May 04 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.4-1
- build(update): 1.5.4

* Mon Apr 12 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.3-1
- build(update): 1.5.3

* Mon Apr 12 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.2-1
- build(update): 1.5.2

* Mon Mar 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.1-2
- style: Trivial changes for pushing into official repo

* Tue Feb 02 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5.1-0.1
- Update to 1.5.1

* Fri Jan 29 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5.0-0.1
- Update to 1.5.0

* Sat Jan 09 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.4.2-0.1
- Initial package
