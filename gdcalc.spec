Summary: Financial, statistics, scientific and programmers calculator for GTK+
Name: gdcalc
Version: 3.3
Release: 3%{?dist}
License: GPLv2
URL: https://gitlab.com/wef/%{name}
Source: %{url}/-/archive/%version/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: bison
BuildRequires: ncurses-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: autoconf, automake, libtool
BuildRequires: desktop-file-utils

Requires: units
Requires: hicolor-icon-theme

%description
gdcalc is a financial, statistics, scientific and programmers
calculator for gtk+-based under Unix and Linux.

It has both Algebraic notation (ie. conventional, TI or Casio-like)
and Reverse Polish Notation (HP-style).

To customise for fonts & colours:

mkdir ~/.config/%{name}
cp /etc/%{name}/%{name}.css ~/.config/%{name}/

This package includes the original dcalc for curses (Unix console)

If you want to know more about RPN calculators (and why they are more
intuitive than algebraic calculators with their = sign) take a look at
http://www.hpcalc.org

%prep
%autosetup
./autogen.sh

%build
%configure
%make_build

%install
%make_install
install -Dpm0644 %{name}.glade %{buildroot}%{_datadir}/%{name}/%{name}.glade
install -Dpm0644 %{name}.css %{buildroot}%{_sysconfdir}/%{name}/%{name}.css
install -Dpm0644 pixmaps/HP-16C-48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mkdir -p %{buildroot}/%{_mandir}/man1
gzip -c doc/%{name}.1 > %{buildroot}%{_mandir}/man1/%{name}.1.gz
gzip -c doc/dcalc.1 > %{buildroot}%{_mandir}/man1/dcalc.1.gz
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{name}.desktop

%files
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/48x48/apps/*
%config(noreplace) %{_sysconfdir}/%{name}/

%doc README.md doc/manual_en.html
%{_mandir}/man1/*.1*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 18 2022 Bob Hepple <bob.hepple@gmail.com> - 3.3-1
- include man pages
- new version

* Wed Mar 09 2022 Bob Hepple <bob.hepple@gmail.com> - 3.2-3
- rebuilt

* Tue Mar 08 2022 Bob Hepple <bob.hepple@gmail.com> - 3.2-2
- rebuilt

* Sat Oct 23 2021 Bob Hepple <bob.hepple@gmail.com> - 3.2-1
- new version

* Wed Oct 20 2021 Bob Hepple <bob.hepple@gmail.com> - 3.1-1
- new host, new version

* Fri Oct 01 2021 Bob Hepple <bob.hepple@gmail.com> - 3.0-2
- rebuilt for RHBZ#2009666

* Thu Sep 30 2021 Bob Hepple <bob.hepple@gmail.com> - 3.0-1
- ported from GTK-2 to GTK-3
