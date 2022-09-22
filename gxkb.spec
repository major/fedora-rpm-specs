Name: gxkb
Version: 0.9.3
Release: 3%{?dist}
Summary: X11 keyboard indicator and switcher

License: GPLv2+
URL: https://github.com/zen-tools/gxkb
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: make

BuildRequires: pkgconfig(glib-2.0) >= 2.16.0
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(libxklavier) >= 5.0

%description
gxkb is a tiny indicator applet which allows to quickly switch between
different keyboard layouts in X. A flag corresponding to the country of the
active layout is shown in the indicator area. The applet is written in C and
uses GTK+ library and therefore does not depend on any GNOME components.


%prep
%autosetup -p1


%build
./autogen.sh
%configure \
    --enable-appindicator=no
%make_build


%install
%make_install

# Move license file in proper location
mkdir -p %{buildroot}%{_licensedir}/%{name}/
mv %{buildroot}%{_docdir}/%{name}/COPYING %{buildroot}%{_licensedir}/%{name}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.xpm
%{_docdir}/%{name}/
%{_licensedir}/%{name}/
%{_mandir}/man1/*.1*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.3-1
- chore(update): 0.9.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.2-1
- build(update): 0.9.2

* Sat Apr 24 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-1
- build(update): 0.9.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.0-1
- Initial package
