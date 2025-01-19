Name: neo
Summary: Digital rain in your terminal

# README.md says "GNU GPL v3", but license headers in source files
# and the --version option say "version 3 or later". 
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later

Version: 0.6.1
Release: 10%{?dist}

URL: https://github.com/st3w/neo
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

# When the program is invoked with the --version option,
# the printed text contains the date of the build,
# which makes builds non-reproducible.
# This patch removes the build-date information.
Patch0: %{name}--reproducible-build.patch

BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(ncurses)


%description
%{name} recreates the digital rain effect known from the film "The Matrix".
Streams of random characters will endlessly scroll down your terminal screen.

%{name} handles Unicode, 16/256 and 32-bit color. It has automatic detection
for terminal color, and supports resizing gracefully.


%prep
%autosetup -p1


%build
./autogen.sh
%configure
%make_build


%install
%make_install


%files
%doc doc/NEWS
%license doc/COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.1-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.1-2
- Fix license tag ("GPLv3" -> "GPLv3+")
- Add a patch to remove build-date information

* Mon Jun 13 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.1-1
- Update to v0.6.1

* Fri Dec 17 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6-1
- Initial packaging
