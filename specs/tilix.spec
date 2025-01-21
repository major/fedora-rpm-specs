%global gtkd_version 3.8.5

# Package notes writer does not support the gold linker, used for D packages.
# See rhbz: 2043178, 2064996
%undefine _package_note_file

# ldc doesn't support -specs=... in LDFLAGS
%undefine _annotated_build
%undefine _hardened_build

Name:           tilix
Version:        1.9.6
Release:        8%{?dist}
Summary:        Tiling terminal emulator

# The tilix source code is MPL-2.0,
# source/gx/gtk/x11.d is GPL-2.0-or-later,
# source/secret is LGPL-3.0-or-later,
# source/x11 is LGPL-3.0-only
# data/gsettings/com.gexperts.Tilix.gschema.xml is GPL-3.0-or-later
# data/scripts/tilix_int.sh is GPL-3.0-or-later
# data/icons are LGPL-3.0-or-later OR CC-BY-SA-3.0.
# This makes the combined license:
License:        MPL-2.0 AND GPL-2.0-or-later AND LGPL-3.0-or-later AND LGPL-3.0-only AND GPL-3.0-or-later AND (LGPL-3.0-or-later OR CC-BY-SA-3.0)
URL:            https://github.com/gnunn1/tilix
Source0:        https://github.com/gnunn1/tilix/archive/%{version}/%{name}-%{version}.tar.gz
# Fix test failure
# metainfo: Add a developer-id
Patch:          https://github.com/gnunn1/tilix/commit/69fe457b58b58eb6f679bc50ef040d08b40fb65d.patch

ExclusiveArch:  %{ldc_arches}

BuildRequires:  gettext-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  glib2-devel
BuildRequires:  ldc
BuildRequires:  meson
BuildRequires:  pkgconfig(gtkd-3) >= %{gtkd_version}
BuildRequires:  pkgconfig(vted-3) >= %{gtkd_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  /usr/bin/appstreamcli
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/po4a-translate

# For directory ownership
Requires:       dbus
Requires:       hicolor-icon-theme

Requires:       gtkd%{?_isa} >= %{gtkd_version}

%description
Tilix is a tiling terminal emulator with the following features:

 - Layout terminals in any fashion by splitting them horizontally or vertically
 - Terminals can be re-arranged using drag and drop both within and between
   windows
 - Terminals can be detached into a new window via drag and drop
 - Input can be synchronized between terminals so commands typed in one
   terminal are replicated to the others
 - The grouping of terminals can be saved and loaded from disk
 - Terminals support custom titles
 - Color schemes are stored in files and custom color schemes can be created by
   simply creating a new file
 - Transparent background
 - Supports notifications when processes are completed out of view

The application was written using GTK 3 and an effort was made to conform to
GNOME Human Interface Guidelines (HIG).


%package        nautilus
Summary:        Tilix extension for Nautilus
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nautilus-python%{?_isa}

%description    nautilus
This package provides a Nautilus extension that adds the 'Open in Tilix'
option to the right-click context menu in Nautilus.


%prep
%autosetup -p1

%if 0%{?flatpak}
sed -i -e "/^Exec=/ s|/usr/bin|%{_bindir}|" data/dbus/com.gexperts.Tilix.service
%endif


%build
export DFLAGS="%{_d_optflags} --allinst"
%meson
%meson_build

%if 0%{?flatpak}
gcc %optflags %__global_ldflags -o tilix-flatpak-toolbox experimental/flatpak/tilix-flatpak-toolbox.c
%endif

# Rename license files so that we can include them in %%license
cp -a data/icons/LICENSE LICENSE-data-icons
cp -a source/x11/LICENSE LICENSE-source-x11


%install
%meson_install

%if 0%{?flatpak}
install -m 755 tilix-flatpak-toolbox $RPM_BUILD_ROOT%{_bindir}
%endif

%find_lang tilix --with-man


%check
%meson_test

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/com.gexperts.Tilix.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/com.gexperts.Tilix.desktop


%files -f tilix.lang
%license LICENSE*
%doc README.md
%{_bindir}/tilix
%if 0%{?flatpak}
%{_bindir}/tilix-flatpak-toolbox
%endif
%{_datadir}/applications/com.gexperts.Tilix.desktop
%{_datadir}/dbus-1/services/com.gexperts.Tilix.service
%{_datadir}/glib-2.0/schemas/com.gexperts.Tilix.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.gexperts.Tilix.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.gexperts.Tilix-symbolic.svg
%{_datadir}/metainfo/com.gexperts.Tilix.appdata.xml
%{_datadir}/tilix/
%{_mandir}/man1/tilix.1*

%files nautilus
%{_datadir}/nautilus-python/extensions/open-tilix.py*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Kalev Lember <klember@redhat.com> - 1.9.6-7
- Rebuilt for ldc 1.40

* Sat Oct 26 2024 Otto Liljalaakso <otto.liljalaakso@iki.fi> - 1.9.6-6
- Add --allinst compiler flag to fix FTBFS

* Tue Aug 06 2024 Kalev Lember <klember@redhat.com> - 1.9.6-5
- Rebuilt for ldc 1.39

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 13 2024 Otto Liljalaakso <otto.liljalaakso@iki.fi> - 1.9.6-3
- Apply upstream patch to fix failing test case

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 08 2023 Kalev Lember <klember@redhat.com> - 1.9.6-1
- Update to 1.9.6
- Drop old terminix obsoletes

* Tue Oct 17 2023 Kalev Lember <klember@redhat.com> - 1.9.5-12
- Rebuilt for ldc 1.35

* Mon Jul 24 2023 Kalev Lember <klember@redhat.com> - 1.9.5-11
- Rebuilt for ldc 1.33

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Kalev Lember <klember@redhat.com> - 1.9.5-9
- Switch to undeaD xml library

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Kalev Lember <klember@redhat.com> - 1.9.5-7
- Run self tests as part of the package build

* Wed Nov 23 2022 Kalev Lember <klember@redhat.com> - 1.9.5-6
- Backport upstream patch to fix compatibility with nautilus 43

* Sat Nov 19 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.9.5-5
- Rebuild for gtkd-3.10.0

* Tue Aug 09 2022 Otto Liljalaakso <otto.liljalaakso@iki.fi> - 1.9.5-4
- License review
- Switch to SPDX license ids

* Wed Jul 27 2022 Kalev Lember <klember@redhat.com> - 1.9.5-3
- Rebuilt for ldc 1.30

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 17 2022 Otto Urpelainen <oturpe@iki.fi> - 1.9.5-1
- Update to 1.9.5
- Resolves rhbz#2057650

* Thu Mar 17 2022 Otto Urpelainen <oturpe@iki.fi> - 1.9.4-4
- Disable package-notes
- Resolves rhbz#2064996

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 09 2021 Kalev Lember <klember@redhat.com> - 1.9.4-1
- Update to 1.9.4
- Switch to meson build system

* Mon Feb 22 2021 Kalev Lember <klember@redhat.com> - 1.9.3-8
- Rebuilt for ldc 1.25

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Kalev Lember <klember@redhat.com> - 1.9.3-6
- Rebuilt for ldc 1.23

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Kalev Lember <klember@redhat.com> - 1.9.3-4
- Rebuilt for ldc 1.20

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 1.9.3-1
- Update to 1.9.3

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 1.9.0-2
- Rebuilt for ldc 1.15

* Mon Mar 18 2019 Kalev Lember <klember@redhat.com> - 1.9.0-1
- Update to 1.9.0

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 1.8.9-3
- Rebuilt for ldc 1.14

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 1.8.9-1
- Update to 1.8.9

* Fri Jan 04 2019 Kalev Lember <klember@redhat.com> - 1.8.7-1
- Update to 1.8.7

* Wed Nov 07 2018 Kalev Lember <klember@redhat.com> - 1.8.5-1
- Update to 1.8.5

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 1.8.3-3
- Rebuilt for ldc 1.12

* Mon Sep 03 2018 Kalev Lember <klember@redhat.com> - 1.8.3-2
- Add missing python2-gobject dependency to tilix-nautilus (#1539039)

* Tue Aug 21 2018 Kalev Lember <klember@redhat.com> - 1.8.3-1
- Update to 1.8.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 1.8.1-2
- Rebuilt for ldc 1.11

* Sun May 27 2018 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Wed May 16 2018 James Ye <jye836@gmail.com> - 1.7.9-1
- Update to 1.7.9

* Mon Mar 19 2018 Kalev Lember <klember@redhat.com> - 1.7.7-1
- Update to 1.7.7
- Remove no longer needed icon cache scriptlets

* Mon Feb 19 2018 Kalev Lember <klember@redhat.com> - 1.7.5-3
- Rebuilt for ldc 1.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Kalev Lember <klember@redhat.com> - 1.7.5-1
- Update to 1.7.5

* Sun Dec 17 2017 Kalev Lember <klember@redhat.com> - 1.7.3-1
- Update to 1.7.3
- Set minimum required gtkd version

* Sat Nov 11 2017 Vadim Rutkovsky <vrutkovs@redhat.com> - 1.7.1-1
- Update to 1.7.1

* Thu Oct 12 2017 Kalev Lember <klember@redhat.com> - 1.6.4-5
- Rebuilt for gtkd 3.6.6

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 1.6.4-4
- Rebuilt for ldc 1.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 1.6.4-1
- Update to 1.6.4

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Mon Apr 10 2017 Kalev Lember <klember@redhat.com> - 1.5.6-1
- Update to 1.5.6
- Obsolete terminix-nautilus for upgrade path from terminix copr

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 1.5.4-4
- Include data/icons/LICENSE and source/x11/LICENSE as %%license (#1434003)

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 1.5.4-3
- Update licensing breakdown (#1434003)
- Add explicit dbus and hicolor-icon-theme deps for directory ownership

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 1.5.4-2
- Use _d_optflags and disable debug print to stderr

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 1.5.4-1
- Initial Fedora packaging
