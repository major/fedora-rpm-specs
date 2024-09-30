Summary:    X font list utility
Name:       xlsfonts
Version:    1.0.7
Release:    7%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

# https://gitlab.freedesktop.org/xorg/app/xlsfonts/-/commit/2b9d8f5bac5d
Patch0:		2b9d8f5bac5d.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(x11)
Obsoletes: xorg-x11-utils < 7.5-39

%description
xlsfonts lists the fonts available on an X server.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%{_bindir}/xlsfonts
%{_mandir}/man1/xlsfonts.1*

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 22 2024 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.0.7-6
- Fix RHBZ #2261808

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 4 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.0.7-1
- New upstream release 1.0.7

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.6-2
- Add Obsoletes for xorg-x11-utils
- Use the make_build rpm macro

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.0.6-1
- Initial split packaging (#1918037)

