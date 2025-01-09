%undefine __cmake_in_source_build

%define openchange_version 2.0
%define intltool_version 0.35.5

%define strict_build_settings 0

### Abstract ###

Name: evolution-mapi
Version: 3.55.1
Release: 1%{?dist}
Summary: Evolution extension for MS Exchange 2007 servers
License: LGPL-2.1-or-later
URL: https://gitlab.gnome.org/GNOME/evolution/-/wikis/home
Source: http://download.gnome.org/sources/%{name}/3.55/%{name}-%{version}.tar.xz

Obsoletes: evolution-mapi-devel <= 3.23.1

%global eds_evo_version %{version}

### Dependencies ###

Requires: evolution >= %{eds_evo_version}
Requires: evolution-data-server >= %{eds_evo_version}
Requires: %{name}-langpacks = %{version}-%{release}

### Build Dependencies ###

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: intltool >= %{intltool_version}
BuildRequires: make

BuildRequires: pkgconfig(camel-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(evolution-data-server-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(evolution-mail-3.0) >= %{eds_evo_version}
BuildRequires: pkgconfig(evolution-shell-3.0) >= %{eds_evo_version}
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libebackend-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(libebook-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(libecal-2.0) >= %{eds_evo_version}
BuildRequires: pkgconfig(libedata-book-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(libedata-cal-2.0) >= %{eds_evo_version}
BuildRequires: pkgconfig(libemail-engine) >= %{eds_evo_version}
BuildRequires: pkgconfig(libmapi) >= %{openchange_version}

%description
This package allows Evolution to interact with MS Exchange 2007 servers.

%package langpacks
Summary: Translations for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description langpacks
This package contains translations for %{name}.

%prep
%autosetup -p1 -S gendiff

%build
CFLAGS="$RPM_OPT_FLAGS"

# Add stricter build settings here as the source code gets cleaned up.
# We want to make sure things like compiler warnings and avoiding deprecated
# functions in the GNOME/GTK+ libraries stay fixed.
#
# Please file a bug report at bugzilla.gnome.org if these settings break
# compilation, and encourage the upstream developers to use them.

%if %{strict_build_settings}
CFLAGS="$CFLAGS \
	-DG_DISABLE_DEPRECATED=1 \
	-DPANGO_DISABLE_DEPRECATED=1 \
	-DGDK_PIXBUF_DISABLE_DEPRECATED=1 \
	-DGDK_DISABLE_DEPRECATED=1 \
	-DGTK_DISABLE_DEPRECATED=1 \
	-DEDS_DISABLE_DEPRECATED=1 \
	-Wdeclaration-after-statement \
	-Werror-implicit-function-declaration"
%endif

export CFLAGS="$CFLAGS -Wno-deprecated-declarations"

%cmake -G "Unix Makefiles"
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS ChangeLog INSTALL README
%{_libdir}/evolution/modules/module-mapi-configuration.so
%{_libdir}/evolution-data-server/camel-providers/libcamelmapi.so
%{_libdir}/evolution-data-server/camel-providers/libcamelmapi.urls
%{_libdir}/evolution-data-server/addressbook-backends/libebookbackendmapi.so
%{_libdir}/evolution-data-server/calendar-backends/libecalbackendmapi.so
%{_libdir}/evolution-data-server/registry-modules/module-mapi-backend.so
%{_libdir}/evolution-mapi/libcamelmapi-priv.so
%{_libdir}/evolution-mapi/libevolution-mapi.so
%{_datadir}/metainfo/org.gnome.Evolution-mapi.metainfo.xml
%{_datadir}/evolution-data-server/mapi

%files langpacks -f %{name}.lang

%changelog
* Tue Jan 07 2025 Milan Crha <mcrha@redhat.com> - 3.55.1-1
- Update to 3.55.1

* Fri Sep 13 2024 Milan Crha <mcrha@redhat.com> - 3.54.0-1
- Update to 3.54.0

* Thu Aug 22 2024 Milan Crha <mcrha@redhat.com> - 3.52.1-3
- Rebuilt against new Samba 4.21

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.52.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 24 2024 Milan Crha <mcrha@redhat.com> - 3.52.1-1
- Update to 3.52.1

* Fri Mar 15 2024 Milan Crha <mcrha@redhat.com> - 3.52.0-1
- Update to 3.52.0

* Tue Jan 30 2024 Milan Crha <mcrha@redhat.com> - 3.51.1-4
- Rebuilt against new Samba 4.20rc1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.51.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.51.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Milan Crha <mcrha@redhat.com> - 3.51.1-1
- Update to 3.51.1

* Fri Sep 15 2023 Milan Crha <mcrha@redhat.com> - 3.50.0-1
- Update to 3.50.0

* Fri Aug 04 2023 Milan Crha <mcrha@redhat.com> - 3.49.2-1
- Update to 3.49.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Milan Crha <mcrha@redhat.com> - 3.49.1-1
- Update to 3.49.1

* Fri May 26 2023 Milan Crha <mcrha@redhat.com> - 3.48.1-1
- Update to 3.48.1

* Fri Mar 17 2023 Milan Crha <mcrha@redhat.com> - 3.48.0-1
- Update to 3.48.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.47.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Milan Crha <mcrha@redhat.com> - 3.47.1-1
- Update to 3.47.1

* Fri Dec 02 2022 Milan Crha <mcrha@redhat.com> - 3.46.1-1
- Update to 3.46.1

* Fri Sep 16 2022 Milan Crha <mcrha@redhat.com> - 3.46.0-1
- Update to 3.46.0

* Tue Aug 09 2022 Adam Williamson <awilliam@redhat.com> - 3.45.1-3
- Rebuild against new libndr

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Milan Crha <mcrha@redhat.com> - 3.45.1-1
- Update to 3.45.1

* Fri May 27 2022 Milan Crha <mcrha@redhat.com> - 3.44.2-1
- Update to 3.44.2

* Fri Apr 22 2022 Milan Crha <mcrha@redhat.com> - 3.44.1-1
- Update to 3.44.1

* Fri Mar 18 2022 Milan Crha <mcrha@redhat.com> - 3.44.0-1
- Update to 3.44.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Milan Crha <mcrha@redhat.com> - 3.43.1-1
- Update to 3.43.1

* Fri Oct 29 2021 Milan Crha <mcrha@redhat.com> - 3.42.1-1
- Update to 3.42.1

* Fri Sep 17 2021 Milan Crha <mcrha@redhat.com> - 3.42.0-1
- Update to 3.42.0

* Fri Aug 13 2021 Milan Crha <mcrha@redhat.com> - 3.41.1-4
- Rebuild for new evolution-data-server

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.41.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Milan Crha <mcrha@redhat.com> - 3.41.1-2
- Rebuild for new samba

* Fri Jul 09 2021 Milan Crha <mcrha@redhat.com> - 3.41.1-1
- Update to 3.41.1

* Fri Apr 30 2021 Milan Crha <mcrha@redhat.com> - 3.40.1-1
- Update to 3.40.1

* Fri Mar 19 2021 Milan Crha <mcrha@redhat.com> - 3.40.0-1
- Update to 3.40.0

* Fri Mar 12 2021 Milan Crha <mcrha@redhat.com> - 3.39.3-1
- Update to 3.39.3

* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 3.39.2-1
- Update to 3.39.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.39.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Milan Crha <mcrha@redhat.com> - 3.39.1-1
- Update to 3.39.1

* Fri Sep 11 2020 Milan Crha <mcrha@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Fri Sep 04 2020 Milan Crha <mcrha@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Fri Aug 07 2020 Milan Crha <mcrha@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 3.37.3-1
- Update to 3.37.3

* Fri May 29 2020 Milan Crha <mcrha@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Fri Apr 24 2020 Milan Crha <mcrha@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Fri Mar 06 2020 Milan Crha <mcrha@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Fri Jan 31 2020 Milan Crha <mcrha@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Milan Crha <mcrha@redhat.com> - 3.35.3-2
- Rebuild for new samba

* Fri Jan 03 2020 Milan Crha <mcrha@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Fri Nov 22 2019 Milan Crha <mcrha@redhat.com> - 3.35.2-1
- Update to 3.35.2

* Fri Oct 11 2019 Milan Crha <mcrha@redhat.com> - 3.35.1-1
- Update to 3.35.1

* Mon Oct 07 2019 Milan Crha <mcrha@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Sep 09 2019 Milan Crha <mcrha@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 19 2019 Milan Crha <mcrha@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Mon Aug 05 2019 Milan Crha <mcrha@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Milan Crha <mcrha@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Mon Jun 17 2019 Milan Crha <mcrha@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Mon May 20 2019 Milan Crha <mcrha@redhat.com> - 3.33.2-1
- Update to 3.33.2

* Mon Apr 22 2019 Milan Crha <mcrha@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Mon Apr 08 2019 Milan Crha <mcrha@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Milan Crha <mcrha@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Feb 18 2019 Milan Crha <mcrha@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Mon Feb 04 2019 Milan Crha <mcrha@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Milan Crha <mcrha@redhat.com> - 3.31.4-1
- Update to 3.31.4

* Mon Dec 10 2018 Milan Crha <mcrha@redhat.com> - 3.31.3-1
- Update to 3.31.3

* Mon Nov 12 2018 Milan Crha <mcrha@redhat.com> - 3.31.2-1
- Update to 3.31.2

* Mon Oct 08 2018 Milan Crha <mcrha@redhat.com> - 3.31.1-1
- Update to 3.31.1
- Add missing Obsoletes for evolution-mapi-devel subpackage

* Mon Sep 24 2018 Milan Crha <mcrha@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Mon Sep 03 2018 Milan Crha <mcrha@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 27 2018 Milan Crha <mcrha@redhat.com> - 3.29.92-1
- Update to 3.29.92

* Mon Aug 13 2018 Milan Crha <mcrha@redhat.com> - 3.29.91-1
- Update to 3.29.91

* Mon Jul 30 2018 Milan Crha <mcrha@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Mon Jul 16 2018 Milan Crha <mcrha@redhat.com> - 3.29.4-1
- Update to 3.29.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Milan Crha <mcrha@redhat.com> - 3.29.3-1
- Update to 3.29.3

* Mon May 21 2018 Milan Crha <mcrha@redhat.com> - 3.29.2-1
- Update to 3.29.2

* Mon Apr 16 2018 Milan Crha <mcrha@redhat.com> - 3.29.1-1
- Update to 3.29.1

* Mon Apr 09 2018 Milan Crha <mcrha@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Milan Crha <mcrha@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Milan Crha <mcrha@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Mon Feb 19 2018 Milan Crha <mcrha@redhat.com> - 3.27.91-1
- Update to 3.27.91

* Tue Feb 06 2018 Milan Crha <mcrha@redhat.com> - 3.27.90-1
- Update to 3.27.90

* Mon Jan 08 2018 Milan Crha <mcrha@redhat.com> - 3.27.4-1
- Update to 3.27.4

* Mon Dec 11 2017 Milan Crha <mcrha@redhat.com> - 3.27.3-1
- Update to 3.27.3

* Mon Nov 13 2017 Milan Crha <mcrha@redhat.com> - 3.27.2-1
- Update to 3.27.2

* Wed Nov 08 2017 Milan Crha <mcrha@redhat.com> - 3.27.1-2
- Rebuild for newer libical

* Mon Oct 16 2017 Milan Crha <mcrha@redhat.com> - 3.27.1-1
- Update to 3.27.1

* Mon Oct 02 2017 Milan Crha <mcrha@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Mon Sep 11 2017 Milan Crha <mcrha@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Mon Sep 04 2017 Milan Crha <mcrha@redhat.com> - 3.25.92.2-1
- Update to 3.25.92.2

* Mon Sep 04 2017 Milan Crha <mcrha@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Tue Aug 22 2017 Ville Skyttä <ville.skytta@iki.fi> - 3.25.91-2
- Install COPYING as %%license

* Mon Aug 21 2017 Milan Crha <mcrha@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Mon Aug 07 2017 Milan Crha <mcrha@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 3.25.4-3
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Milan Crha <mcrha@redhat.com> - 3.25.4-1
- Update to 3.25.4

* Mon Jun 19 2017 Milan Crha <mcrha@redhat.com> - 3.25.3-1
- Update to 3.25.3

* Mon May 22 2017 Milan Crha <mcrha@redhat.com> - 3.25.2-1
- Update to 3.25.2

* Thu Apr 27 2017 Milan Crha <mcrha@redhat.com> - 3.25.1-2
- Split translations into separate package

* Mon Apr 24 2017 Milan Crha <mcrha@redhat.com> - 3.25.1-1
- Update to 3.25.1

* Mon Apr 10 2017 Milan Crha <mcrha@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Mon Mar 20 2017 Milan Crha <mcrha@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Mon Mar 13 2017 Milan Crha <mcrha@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Mon Feb 27 2017 Milan Crha <mcrha@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Mon Feb 13 2017 Milan Crha <mcrha@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Milan Crha <mcrha@redhat.com> - 3.23.4-1
- Update to 3.23.4

* Mon Dec 12 2016 Milan Crha <mcrha@redhat.com> - 3.23.3-1
- Update to 3.23.3

* Mon Nov 21 2016 Milan Crha <mcrha@redhat.com> - 3.23.2-1
- Update to 3.23.2

* Mon Oct 24 2016 Milan Crha <mcrha@redhat.com> - 3.23.1-1
- Update to 3.23.1

* Mon Sep 19 2016 Milan Crha <mcrha@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Mon Sep 12 2016 Milan Crha <mcrha@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Mon Aug 29 2016 Milan Crha <mcrha@redhat.com> - 3.21.91-1
- Update to 3.21.91

* Mon Aug 15 2016 Milan Crha <mcrha@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Mon Jun 20 2016 Milan Crha <mcrha@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Mon May 23 2016 Milan Crha <mcrha@redhat.com> - 3.21.2-1
- Update to 3.21.2

* Mon Apr 25 2016 Milan Crha <mcrha@redhat.com> - 3.21.1-1
- Update to 3.21.1

* Mon Apr 11 2016 Milan Crha <mcrha@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Mon Mar 21 2016 Milan Crha <mcrha@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 14 2016 Milan Crha <mcrha@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Mon Feb 15 2016 Milan Crha <mcrha@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David Tardon <dtardon@redhat.com> - 3.19.4-2
- rebuild for libical 2.0.0

* Mon Jan 18 2016 Milan Crha <mcrha@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Mon Dec 14 2015 Milan Crha <mcrha@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Mon Oct 26 2015 Milan Crha <mcrha@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Mon Sep 21 2015 Milan Crha <mcrha@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Milan Crha <mcrha@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Mon Aug 31 2015 Milan Crha <mcrha@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Mon Aug 17 2015 Milan Crha <mcrha@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Mon Jul 20 2015 Milan Crha <mcrha@redhat.com> - 3.17.4-1
- Update to 3.17.4

* Mon Jun 22 2015 Milan Crha <mcrha@redhat.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Milan Crha <mcrha@redhat.com> - 3.17.2-1
- Update to 3.17.2

* Mon Apr 27 2015 Milan Crha <mcrha@redhat.com> - 3.17.1-1
- Update to 3.17.1

* Mon Apr 13 2015 Milan Crha <mcrha@redhat.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Milan Crha <mcrha@redhat.com> - 3.16.0-1
- Update to 3.16.0

* Mon Mar 16 2015 Milan Crha <mcrha@redhat.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar 02 2015 Milan Crha <mcrha@redhat.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 Milan Crha <mcrha@redhat.com> - 3.13.90-1
- Update to 3.13.90

* Mon Jan 26 2015 Milan Crha <mcrha@redhat.com> - 3.13.10-1
- Update to 3.13.10

* Mon Dec 22 2014 Milan Crha <mcrha@redhat.com> - 3.13.9-1
- Update to 3.13.9

* Mon Nov 24 2014 Milan Crha <mcrha@redhat.com> - 3.13.8-1
- Update to 3.13.8

* Mon Oct 27 2014 Milan Crha <mcrha@redhat.com> - 3.13.7-1
- Update to 3.13.7

* Mon Sep 22 2014 Milan Crha <mcrha@redhat.com> - 3.13.6-1
- Update to 3.13.6

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Milan Crha <mcrha@redhat.com> - 3.13.4-1
- Update to 3.13.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Milan Crha <mcrha@redhat.com> - 3.12.2-1
- Update to 3.12.2
- Remove upstream patch to adapt to OpenChange 2.1 release changes

* Mon Apr 28 2014 Milan Crha <mcrha@redhat.com> - 3.12.1-2
- Add upstream patch to adapt to OpenChange 2.1 release changes

* Mon Apr 14 2014 Milan Crha <mcrha@redhat.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Milan Crha <mcrha@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Mon Mar 17 2014 Milan Crha <mcrha@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Mon Mar 03 2014 Milan Crha <mcrha@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Mon Feb 17 2014 Milan Crha <mcrha@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Mon Feb 03 2014 Milan Crha <mcrha@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Mon Jan 13 2014 Milan Crha <mcrha@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Sun Dec 01 2013 Matthew Barnes <mbarnes@redhat.com> - 3.11.2-3
- Add $RPM_OPT_FLAGS to $CFLAGS (RH bug #1035931)

* Thu Nov 21 2013 Milan Crha <mcrha@redhat.com> - 3.11.2-2
- Rebuild for new libical (RH bug #1023020)

* Mon Nov 18 2013 Milan Crha <mcrha@redhat.com> - 3.11.2-1
- Update to 3.11.2
- Disable compiler warnings about deprecated symbols

* Fri Nov 08 2013 Milan Crha <mcrha@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Mon Oct 14 2013 Milan Crha <mcrha@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Mon Sep 23 2013 Milan Crha <mcrha@redhat.com> - 3.10.0-1
- Update to 3.10.0
- Fix URL tag in the .spec file to point to evolution project

* Mon Sep 16 2013 Milan Crha <mcrha@redhat.com> - 3.9.92-1
- Update to 3.9.92

* Mon Aug 19 2013 Milan Crha <mcrha@redhat.com> - 3.9.90-1
- Update to 3.9.90

* Mon Jul 29 2013 Milan Crha <mcrha@redhat.com> - 3.9.5-1
- Update to 3.9.5

* Wed Jul 10 2013 Milan Crha <mcrha@redhat.com> - 3.9.3-2
- Rebuild against newer evolution-data-server

* Mon Jun 17 2013 Milan Crha <mcrha@redhat.com> - 3.9.3-1
- Update to 3.9.3

* Mon May 27 2013 Milan Crha <mcrha@redhat.com> - 3.9.2-1
- Update to 3.9.2

* Sat May 25 2013 Rex Dieter <rdieter@fedoraproject.org> 3.9.1-2
- rebuild (libical)

* Mon Apr 29 2013 Milan Crha <mcrha@redhat.com> - 3.9.1-1
- Update to 3.9.1

* Mon Mar 25 2013 Milan Crha <mcrha@redhat.com> - 3.8.0-1
- Update to 3.8.0

* Mon Mar 18 2013 Milan Crha <mcrha@redhat.com> - 3.7.92-1
- Update to 3.7.92
- Remove patch to drop GTK_DOC_CHECK from configure.ac (fixed upstream)

* Mon Mar 04 2013 Milan Crha <mcrha@redhat.com> - 3.7.91-1
- Update to 3.7.91
- Add patch to drop GTK_DOC_CHECK from configure.ac

* Mon Feb 18 2013 Milan Crha <mcrha@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Mon Feb 04 2013 Milan Crha <mcrha@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Mon Jan 14 2013 Milan Crha <mcrha@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Wed Dec 19 2012 Matthew Barnes <mbarnes@redhat.com> - 3.7.3-1
- Update to 3.7.3

* Mon Nov 19 2012 Milan Crha <mcrha@redhat.com> - 3.7.2-1
- Update to 3.7.2

* Mon Oct 22 2012 Milan Crha <mcrha@redhat.com> - 3.7.1-1
- Update to 3.7.1

* Mon Sep 17 2012 Milan Crha <mcrha@redhat.com> - 3.5.92-1
- Update to 3.5.92

* Mon Sep 03 2012 Milan Crha <mcrha@redhat.com> - 3.5.91-1
- Update to 3.5.91

* Mon Aug 20 2012 Milan Crha <mcrha@redhat.com> - 3.5.90-1
- Update to 3.5.90

* Mon Aug 06 2012 Milan Crha <mcrha@redhat.com> - 3.5.5-1
- Update to 3.5.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Milan Crha <mcrha@redhat.com> - 3.5.4-1
- Update to 3.5.4

* Tue Jun 26 2012 Matthew Barnes <mbarnes@redhat.com> - 3.5.3-1
- Update to 3.5.3

* Mon Jun 04 2012 Milan Crha <mcrha@redhat.com> - 3.5.2-1
- Update to 3.5.2

* Sun Apr 29 2012 Matthew Barnes <mbarnes@redhat.com> - 3.5.1-1
- Update to 3.5.1

* Tue Apr 24 2012 Milan Crha <mcrha@redhat.com> - 3.4.0-3
- Rebuild against newer OpenChange

* Thu Apr 19 2012 Milan Crha <mcrha@redhat.com> - 3.4.0-2
- Rebuild against newer OpenChange

* Tue Apr 03 2012 Milan Crha <mcrha@redhat.com> - 3.4.0-1
- Update to 3.4.0
- Bump OpenChange dependency to 1.0

* Tue Mar 06 2012 Milan Crha <mcrha@redhat.com> - 3.3.91-1
- Update to 3.3.91
- Remove add-rpath patch (obsolete)

* Thu Feb 23 2012 Milan Crha <mcrha@redhat.com> - 3.3.90-2
- Do not change rpath on .so files (fixes Red Hat bug #790056)

* Mon Feb 20 2012 Milan Crha <mcrha@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Mon Feb 06 2012 Milan Crha <mcrha@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Mon Jan 16 2012 Milan Crha <mcrha@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Milan Crha <mcrha@redhat.com> - 3.3.3-1
- Update to 3.3.3
- Remove patch to remove usage of deprecated flags (fixed upstream)

* Mon Nov 21 2011 Milan Crha <mcrha@redhat.com> - 3.3.2-1
- Update to 3.3.2
- Add patch to remove usage of deprecated flags

* Mon Oct 24 2011 Milan Crha <mcrha@redhat.com> - 3.3.1-1
- Update to 3.3.1

* Mon Sep 26 2011 Milan Crha <mcrha@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Mon Sep 19 2011 Milan Crha <mcrha@redhat.com> - 3.1.92-1
- Update to 3.1.92

* Mon Sep 05 2011 Milan Crha <mcrha@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> - 3.1.90-1
- Update to 3.1.90

* Mon Aug 15 2011 Milan Crha <mcrha@redhat.com> - 3.1.5-1
- Update to 3.1.5

* Thu Aug 11 2011 Milan Crha <mcrha@redhat.com> - 3.1.4-1
- Update to 3.1.4
- Remove patch to enable GLib deprecated stuff (fixed upstream)

* Tue Jul 05 2011 Matthew Barnes <mbarnes@redhat.com> - 3.1.3-1
- Update to 3.1.3

* Tue Jun 14 2011 Milan Crha <mcrha@redhat.com> - 3.1.2-1
- Update to 3.1.2
- Add patch to enable GLib deprecated stuff (due to G_CONST_RETURN deprecation)

* Mon May 09 2011 Milan Crha <mcrha@redhat.com> - 3.1.1-1
- Update to 3.1.1

* Wed Apr 06 2011 Matthew Barnes <mbarnes@redhat.com> - 3.0.0-2
- Rebuild against newer Samba4 and OpenChange libraries.

* Mon Apr 04 2011 Milan Crha <mcrha@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Mon Mar 21 2011 Milan Crha <mcrha@redhat.com> - 2.91.92-1
- Update to 2.91.92

* Mon Mar 07 2011 Milan Crha <mcrha@redhat.com> - 2.91.91-1
- Update to 2.91.91

* Mon Feb 21 2011 Milan Crha <mcrha@redhat.com> - 2.91.90-1
- Update to 2.91.90

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-4
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.6-2
- Rebuild

* Mon Jan 31 2011 Milan Crha <mcrha@redhat.com> - 2.91.6-1
- Update to 2.91.6

* Mon Jan 10 2011 Milan Crha <mcrha@redhat.com> - 2.91.5-1
- Update to 2.91.5

* Mon Dec 20 2010 Milan Crha <mcrha@redhat.com> - 2.91.4-1
- Update to 2.91.4

* Mon Nov 29 2010 Milan Crha <mcrha@redhat.com> - 2.91.3-1
- Update to 2.91.3

* Mon Nov 08 2010 Milan Crha <mcrha@redhat.com> - 2.91.2-1
- Update to 2.91.2

* Mon Oct 18 2010 Milan Crha <mcrha@redhat.com> - 2.91.1-1
- Update to 2.91.1

* Mon Oct 11 2010 Milan Crha <mcrha@redhat.com> - 2.91.0-1
- Update to 2.91.0

* Wed Sep 29 2010 jkeating - 0.31.92-3
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Milan Crha <mcrha@redhat.com> - 0.31.92-2
- Bump openchange requirement to 0.9-8

* Mon Sep 13 2010 Milan Crha <mcrha@redhat.com> - 0.31.92-1
- Update to 0.31.92
- Remove patch for Gnome bug #627999 (fixed upstream)

* Mon Aug 30 2010 Milan Crha <mcrha@redhat.com> - 0.31.91-1
- Update to 0.31.91
- Add patch for Gnome bug #627999 (Cannot autocomplete)

* Mon Aug 16 2010 Matthew Barnes <mbarnes@redhat.com> - 0.31.90-1
- Update to 0.31.90

* Mon Aug 02 2010 Matthew Barnes <mbarnes@redhat.com> - 0.31.6-1
- Update to 0.31.6
- Roll back evo_base_version to 2.32.

* Tue Jul 13 2010 Milan Crha <mcrha@redhat.com> - 0.31.5-1
- Update to 0.31.5

* Mon Jun 07 2010 Milan Crha <mcrha@redhat.com> - 0.31.3-1
- Update to 0.31.3

* Mon May 24 2010 Milan Crha <mcrha@redhat.com> - 0.31.2-1
- Update to 0.31.2

* Mon May 03 2010 Milan Crha <mcrha@redhat.com> - 0.31.1-1
- Update to 0.31.1

* Mon Feb 08 2010 Milan Crha <mcrha@redhat.com> - 0.29.90-1
- Update to 0.29.90

* Mon Jan 25 2010 Milan Crha <mcrha@redhat.com> - 0.29.6-1
- Update to 0.29.6

* Tue Jan 12 2010 Milan Crha <mcrha@redhat.com> - 0.29.5-1
- Update to 0.29.5

* Sat Jan 09 2010 Matthew Barnes <mbarnes@redhat.com> - 0.29.4-2
- Rebuild against OpenChange 0.9.

* Mon Dec 21 2009 Milan Crha <mcrha@redhat.com> - 0.29.4-1
- Update to 0.29.4

* Mon Nov 30 2009 Milan Crha <mcrha@redhat.com> - 0.29.3-1
- Update to 0.29.3
- Remove patch for Gnome bug #588453 (fixed upstream).
- Remove patch for Gnome bug #595260 (fixed upstream).
- Remove patch for Gnome bug #595355 (fixed upstream).
- Remove patch for Gnome bug #595480 (fixed upstream).

* Tue Sep 22 2009 Milan Crha <mcrha@redhat.com> - 0.28.0-1
- Update to 0.28.0
- Add patch for Gnome bug #588453 (slow retrieval of message IDs).
- Add patch for Gnome bug #595260 (crash in mapi_sync_deleted).
- Add patch for Gnome bug #595355 (crash and incorrect header parsing).
- Add patch for Gnome bug #595480 (crash on fetching GAL).

* Mon Sep 07 2009 Milan Crha <mcrha@redhat.com> - 0.27.92-1
- Update to 0.27.92

* Mon Aug 24 2009 Milan Crha <mcrha@redhat.com> - 0.27.91-1
- Update to 0.27.91

* Mon Aug 10 2009 Milan Crha <mcrha@redhat.com> - 0.27.90-1
- Update to 0.27.90

* Tue Jul 28 2009 Milan Crha <mcrha@redhat.com> - 0.27.5-2
- Add new libebookbackendmapigal.so to a list of installed files.
- Bump requirement of evolution and evolution-data-server to 2.27.5.

* Mon Jul 27 2009 Milan Crha <mcrha@redhat.com> - 0.27.5-1
- Update to 0.27.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Matthew Barnes <mbarnes@redhat.com> - 0.27.4-1
- Update to 0.27.4

* Thu Jul 02 2009 Matthew Barnes <mbarnes@redhat.com> - 0.27.3-4
- Remove redundant library flag from pkg-config file.

* Mon Jun 29 2009 Matthew Barnes <mbarnes@redhat.com> - 0.27.3-3
- Rebuild against mutated openchange (see RH bug #503783).

* Fri Jun 26 2009 Matthew Barnes <mbarnes@redhat.com> - 0.27.3-2
- Remove ldconfig calls since all the libraries we install are
  dlopen'ed modules (RH bug #586991).

* Mon Jun 15 2009 Matthew Barnes <mbarnes@redhat.com> - 0.27.3-1
- Update to 0.27.3

* Fri May 29 2009 Matthew Barnes <mbarnes@redhat.com> - 0.27.2-1
- Update to 0.27.2

* Mon May 04 2009 Matthew Barnes <mbarnes@redhat.com> - 0.27.1-1
- Update to 0.27.1
- Bump eds_major to 2.28.
- Bump evo and eds req's to 2.27.1.

* Mon Apr 13 2009 Matthew Barnes <mbarnes@redhat.com> - 0.26.1-1
- Update to 0.26.1

* Thu Mar 19 2009 Matthew Barnes <mbarnes@redhat.com> - 0.26.0.1-1
- Update to 0.26.0.1

* Mon Mar 16 2009 Matthew Barnes <mbarnes@redhat.com> - 0.26.0-1
- Update to 0.26.0

* Mon Mar 02 2009 Matthew Barnes <mbarnes@redhat.com> - 0.25.92-1
- Update to 0.25.92

* Thu Feb 26 2009 Matthew Barnes <mbarnes@redhat.com> - 0.25.91-3
- Formal package review cleanups.

* Thu Feb 19 2009 Matthew Barnes <mbarnes@redhat.com> - 0.25.91-2
- Add some missing build requirements.

* Mon Feb 16 2009 Matthew Barnes <mbarnes@redhat.com> - 0.25.91-1
- Update to 0.25.91

* Thu Feb 05 2009 Matthew Barnes <mbarnes@redhat.com> - 0.25.90-1
- Update to 0.25.90

* Mon Jan 19 2009 Matthew Barnes <mbarnes@redhat.com> - 0.25.5-1
- Update to 0.25.5

* Tue Jan 06 2009 Matthew Barnes <mbarnes@redhat.com> - 0.25.4-1
- Update to 0.25.4
- Handle translations.

* Mon Dec 15 2008 Matthew Barnes <mbarnes@redhat.com> - 0.25.3-1
- Update to 0.25.3

* Fri Dec 12 2008 Matthew Barnes <mbarnes@redhat.com> - 0.1-1
- Initial packaging of evolution-mapi.
