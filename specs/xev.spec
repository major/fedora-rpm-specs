Summary:    X Event utility
Name:       xev
Version:    1.2.6
Release:    10%{?dist}
License:    MIT
URL:        https://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr) >= 1.2

Obsoletes: xorg-x11-utils < 7.5-39

%description
xev displays the X11 protocol events sent to a given window.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%{_bindir}/xev
%{_mandir}/man1/xev.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 04 2024 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.6-1
- xev 1.2.6

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.4-2
- Bump Obsoletes line for xorg-x11-utils
- Use the make_build rpm macro

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.2.4-1
- Initial split packaging

