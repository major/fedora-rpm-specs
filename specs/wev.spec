# -*-Mode: rpm-spec -*-

%global commit 0fc054957275580a31d09679b95d9de9cf69d04a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     wev
Version:  1.0.1
Release:  0.20230429git%{shortcommit}%{?dist}
Summary:  A tool for debugging events on a sway Wayland window
License:  MIT
URL:      https://git.sr.ht/~sircmpwn/wev
Source0:  %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
A tool for debugging events on a sway Wayland window,
analogous to the X11 tool xev.

%prep
%autosetup -n %{name}-%{commit}

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.20230429git0fc0549
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.20230428git0fc0549
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.20230427git0fc0549
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.20230426git0fc0549
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 25 2023 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-0.20230425git0fc0549
- incorporate latest fixes
- SPDX license specifier

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.20211133git54de46d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.20211132git54de46d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.20211131git54de46d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-0.20211130git54de46d
- rebuilt

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.20210108git54de46d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.20210107git54de46d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-0.20210106git54de46d
- rebuilt to latest in master

* Wed Jul 29 2020 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-0.20200730git0be512f
- changes per RHBZ#1860772

* Tue Jul 28 2020 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-0.20200729git0be512f
- changes per RHBZ#1860772

* Mon Jul 27 2020 Bob Hepple <bob.hepple@gmail.com> - 1.0.1-0.20200727git0be512f
- Initial version of the package
