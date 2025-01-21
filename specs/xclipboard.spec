Name:       xclipboard
Version:    1.1.5
Release:    2%{?dist}
Summary:    Utility to collect and display text selections

License:    MIT-open-group
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
xclipboard is used to collect and display text selections that are
sent to the CLIPBOARD by other clients.  It is typically used to save
CLIPBOARD selections for later use.  It stores each CLIPBOARD
selection as a separate string, each of which can be selected.

%prep
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xclipboard
%{_bindir}/xcutsel
%{_mandir}/man1/xclipboard.1*
%{_mandir}/man1/xcutsel.1*
%{_datadir}/X11/app-defaults/XClipboard

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.1.5-1
- 1.1.5

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.1.4-4
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4 (RHBZ #2105829)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.3-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.1.3-1
- Split xclipboard out from xorg-x11-apps into a separate package
  (#1933939)
