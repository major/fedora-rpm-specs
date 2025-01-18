Name:           gcolor3
Version:        2.4.0
Release:        14%{?dist}
Summary:        A simple color chooser written in GTK3 (like gcolor2)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.hjdskes.nl/projects/gcolor3/

Source0:        https://gitlab.gnome.org/World/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# Extracted from upstream merge request:
#   https://gitlab.gnome.org/World/gcolor3/-/merge_requests/151
Patch0:         gcolor3-2.4.0-libportal-0.5.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gnome-common
BuildRequires:  gtk3-devel >= 3.12.0
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(libportal-gtk3)
Requires:       hicolor-icon-theme

%description
Gcolor3 is a color selection dialog written in GTK+ 3. It is much alike Gcolor2,
but uses the newer GTK+ version to better integrate into your modern desktop.
It has the same feature set as Gcolor2, except that recent versions of Gcolor3
use an .ini style file to save colors (older versions use the same file as
Gcolor2).

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang gcolor3
desktop-file-validate %{buildroot}%{_datadir}/applications/nl.hjdskes.gcolor3.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/nl.hjdskes.gcolor3.appdata.xml

%files -f gcolor3.lang
%doc README.md
%license LICENSE
%{_bindir}/gcolor3
%{_datadir}/applications/nl.hjdskes.gcolor3.desktop
%{_datadir}/icons/hicolor/scalable/apps/nl.hjdskes.gcolor3.svg
%{_datadir}/icons/hicolor/symbolic/apps/nl.hjdskes.gcolor3-symbolic.svg
%{_metainfodir}/nl.hjdskes.gcolor3.appdata.xml
%{_mandir}/man1/gcolor3.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 David King <amigadave@amigadave.com> - 2.4.0-5
- Backports upstream libportal 0.5 support

* Sun Jan 09 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.0-4
- rebuild against new libportal

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Timothée Floure <timothee.floure@posteo.net> - 2.4.0-1
- New upstream release (2.4.0 adds Wayland support)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Timothée Floure <fnux@fedoraproject.org> - 2.3.1-5
- Disable -Werror compilation flag due to deprecation warnings in F30+

* Thu Sep 19 2019 Kalev Lember <klember@redhat.com> - 2.3.1-4
- Fix typo in hicolor-icon-theme requires

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Timothée Floure <fnux@fedoraproject.org> - 2.3.1-2
  - Add missing dependency on hicoler-icon-theme

* Mon Sep 03 2018 Timothée Floure <fnux@fedoraproject.org> - 2.3.1-1
  - New upstream release (2.3.1)
  - Use meson to build the application
  - Update project homepage
  - Update project URL

* Tue Jun 26 2018 Timothée Floure <fnux@fedoraproject.org> - 2.2-5
  - Fix compilation for F28+ (patch1)

* Sun Sep 03 2017 Timothée Floure <timothee.floure@fnux.ch> - 2.2-4
  - Update license field from GPLv2 to GPLv2+
  - Use the --nonet flag in gcolor3.appdata.xml's validation
  - Add an empty line between each changelog entry

* Wed Aug 09 2017 Timothée Floure <timothee.floure@fnux.ch> - 2.2-3
  - Patch and validate gcolor3.appdata.xml
  - Use the license macro instead of the doc macro for the LICENSE file
  - Remove the deprecated RPM Group
  - use the make_build macro instead of make %{?_smp_mflags}
  - Add minimal version for gtk3-devel (in BuildRequires)
  - Use a more explicit name for the source file

* Sun Apr 23 2017 Timothée Floure <timothee.floure@fnux.ch> - 2.2-2
  - Improve specfile in order to comply with the "Fedora Packaging Guidelines"

