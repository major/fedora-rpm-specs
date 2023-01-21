Name:       editres
Version:    1.0.7
Release:    6%{?dist}
Summary:    X11 utility to view and edit application resources

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

Patch01:    editres-1.0.6-format-security.patch

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-resutils < 7.7-9

%description
editres is a tool that allows users and application developers to view
the full widget hierarchy of any Xt Toolkit application that speaks the
Editres protocol  In addition, editres will help the user construct
resource specifications, allow the user to apply the resource to
the application and view the results dynamically.

%prep
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules --disable-xprint
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/X11/app-defaults/Editres
%{_datadir}/X11/app-defaults/Editres-color

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.7-2
- Fix Obsoletes line to actually obsolete the -8 resutils

* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.7-1
- Split editres out from xorg-x11-resutils into a separate package (#1934345)
