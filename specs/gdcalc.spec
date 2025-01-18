Summary: Financial, statistics, scientific and programmers calculator for GTK+
Name: gdcalc
Version: 3.4
Release: 6%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
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
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{name}.desktop

%files
%license COPYING
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%config(noreplace) %{_sysconfdir}/%{name}/

%doc README.md doc/manual_en.html
%{_mandir}/man1/*.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 11 2023 Bob Hepple - 3.4-1
- new version

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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
