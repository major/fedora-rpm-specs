# -*-Mode: rpm-spec -*-

%global commit c7c3643760caea4bd26b1d56ed033a52f6e34124
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     bookworm
Version:  1.1.3
Release:  0.16.20200414git.%{shortcommit}%{?dist}
Summary:  Simple, focused eBook reader
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:  GPL-3.0-only
URL:      https://github.com/babluboy/bookworm
Source0:  %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:   bookworm-patch0-python3.patch
# https://github.com/babluboy/bookworm/pull/391
Patch1:   bookworm-patch1-webkitgtk41.patch

BuildRequires: gcc
BuildRequires: granite-devel
BuildRequires: gtk3-devel
BuildRequires: libgee-devel
BuildRequires: meson
BuildRequires: poppler-glib-devel
BuildRequires: vala
BuildRequires: webkit2gtk4.1-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires:      hicolor-icon-theme

%description

Read the books you love without having to worry about the different
format complexities like epub, pdf, mobi, cbr, etc. This version
supports EPUB, MOBI, FB2, PDF, FB2 and Comics (CBR and CBZ) formats
with support for more formats to follow soon.

Check the Bookworm website for details on features, shortcuts,
installation guides for supported distros :
https://babluboy.github.io/bookworm/

%prep
%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang com.github.babluboy.bookworm
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.github.babluboy.bookworm.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.github.babluboy.bookworm.appdata.xml

%files -f com.github.babluboy.bookworm.lang
%{_bindir}/com.github.babluboy.bookworm
%{_datadir}/com.github.babluboy.bookworm/
%{_datadir}/applications/com.github.babluboy.bookworm.desktop
%{_datadir}/glib-2.0/schemas/com.github.babluboy.bookworm.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.babluboy.bookworm.svg
%{_metainfodir}/com.github.babluboy.bookworm.appdata.xml

%doc README.md

%license COPYING

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.16.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1.3-0.15.20200414git.c7c3643
- Use webkit2gtk4.1

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.3-0.14.20200414git.c7c3643
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.13.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.12.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.11.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.10.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.9.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.8.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.7.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.6.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.3-0.5.20200414git.c7c3643
- Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.4.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.3.20200414git.c7c3643
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.2.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.3-0.1.20200414git.c7c3643
- pre-release of 0.1.3

* Wed Apr 08 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-4
- resolve RHBZ#1822231

* Tue Mar 31 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-3
- changes per RHBZ#1812411

* Wed Mar 11 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-2
- fix Source0

* Sat Feb 22 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-1
- Initial version of the package
