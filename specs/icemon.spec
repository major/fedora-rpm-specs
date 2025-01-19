Name:           icemon
Version:        3.3
Release:        16%{?dist}
Summary:        Icecream GUI monitor

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://kfunk.org/tag/icemon/
Source0:        https://github.com/icecc/icemon/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        icemon.metainfo.xml
# Backport of docbook -> asciidoc from upstream
# https://github.com/icecc/icemon/commit/479490ffbe0d13ed3059b67241671cb78521a10a
Patch1:         icemon-asciidoc.patch

BuildRequires:    gcc-c++
BuildRequires:    pkgconfig(icecc) >= 1.3
BuildRequires:    cmake
BuildRequires:    desktop-file-utils
BuildRequires:    extra-cmake-modules
BuildRequires:    qt5-qtbase-devel
BuildRequires:    asciidoc
BuildRequires:    libappstream-glib

Requires:    hicolor-icon-theme

%description
A GUI monitor for Icecream, a distributed compiler system.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{SOURCE1}
# FIXME: This command would install it to /usr/share/appdata .
# DESTDIR=%{buildroot} appstream-util install %{SOURCE1}
install -m644 -D %{SOURCE1} %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml

%check
%ctest

%files
%{_bindir}/%{name}
%{_datadir}/applications/icemon.desktop
%{_datadir}/icons/hicolor/*/apps/icemon.png
%{_mandir}/man1/icemon.1.*
%{_metainfodir}/icemon.metainfo.xml
%license COPYING
%doc CHANGELOG.md README.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun  3 2021 Jan Kratochvil <jan.kratochvil@redhat.com> - 3.3-6
- Backport docbook -> asciidoc from upstream.
- Reduce BuildRequires.
- Use build, install and test rpmbuild macros.
- Many changes provided by reviewer Robert-André Mauchin.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Jeff Law <law@redhat.com> - 3.3-3
- Drop build requirement for qt5-devel

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Michal Schmidt <mschmidt@redhat.com> - 3.3-1
- Updated to 3.3

* Fri Aug 02 2019 Michael Cullen <michael@cullen-online.com> - 3.2.0-1
- Updated to 3.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 David Tardon <dtardon@redhat.com> - 3.1.0-9
- rebuild for icecream 1.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jul 30 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-5
- Removed useless BuildRequires on gzip
- Changed BuildRequires hicolor-icon-theme to be Requires since it is a runtime dependency
* Fri Jul 28 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-4
- Added BuildRequires on gcc-c++
* Fri Jul 28 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-3
- Decompressed SVG file to fix rpmlint warning
- Added BuildRequires on docbook-dtds to fix build error without network
- Changed license to GPLv2+ according to file headers
- Added calls to gtk-update-icon-cache
* Thu Jul 27 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-2
- Found a better description for spec file
* Thu Jul 27 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-1
- Initial Packaging

