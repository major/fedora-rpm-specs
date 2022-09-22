# -*-Mode: rpm-spec -*-

%global commit 54de46d120396ead4dcbce0b52cf506c200380f5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     wev
Version:  1.0.1
Release:  0.20211132git%{shortcommit}%{?dist}
Summary:  A tool for debugging events on a sway Wayland window
License:  MIT
URL:      https://git.sr.ht/~sircmpwn/wev
Source0:  %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

# GNOME (ie mutter) still uses wl_seat-5.
# REMOVE THIS PATCH when META_WL_SEAT_VERSION becomes '6'
# in mutter/wayland/meta-wayland-versions.h
Patch0:   mutter-wl_seat-5.patch

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
