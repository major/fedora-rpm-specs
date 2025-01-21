Name:       xload
Version:    1.2.0
Release:    3%{?dist}
Summary:    Tool to display system load average

License:    X11
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.gz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
# BuildRequires:  pkgconfig(xt) # no longer needed
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
xload displays a periodically updating histogram of the system load average.

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
%{_bindir}/xload
%{_mandir}/man1/xload.1*
%{_datadir}/X11/app-defaults/XLoad

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Jos de Kloe <josdekloe@gmail.com> 1.2.0-1
- Update to 1.2.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Jos de Kloe <josdekloe@gmail.com> 1.1.4-3
- SPDX migration: change generic MIT to specific X11 license tag.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 05 2022 Jos de Kloe <josdekloe@gmail.com> 1.1.4-1
- Update to 1.1.4

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.3-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.1.3-1
- Split xload out from xorg-x11-apps into a separate package (#1933946)
