%undefine __cmake_in_source_build

%global json_glib_version 1.0.4
%global libmspack_version 0.4
%global libsoup_version 3.1.1

Name: evolution-ews
Version: 3.55.2
Release: 1%{?dist}
Summary: Evolution extension for Exchange Web Services
License: LGPL-2.1-or-later
URL: https://gitlab.gnome.org/GNOME/evolution/-/wikis/home
Source: http://download.gnome.org/sources/%{name}/3.55/%{name}-%{version}.tar.xz

%global eds_evo_version %{version}

Requires: evolution >= %{eds_evo_version}
Requires: evolution-data-server >= %{eds_evo_version}
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-langpacks = %{version}-%{release}

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: intltool
BuildRequires: make
BuildRequires: pkgconfig(camel-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(evolution-data-server-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(evolution-mail-3.0) >= %{eds_evo_version}
BuildRequires: pkgconfig(evolution-shell-3.0) >= %{eds_evo_version}
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires: pkgconfig(libebackend-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(libebook-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(libecal-2.0) >= %{eds_evo_version}
BuildRequires: pkgconfig(libedata-book-1.2) >= %{eds_evo_version}
BuildRequires: pkgconfig(libedata-cal-2.0) >= %{eds_evo_version}
BuildRequires: pkgconfig(libemail-engine) >= %{eds_evo_version}
BuildRequires: pkgconfig(libical)
BuildRequires: pkgconfig(libmspack) >= %{libmspack_version}
BuildRequires: pkgconfig(libsoup-3.0) >= %{libsoup_version}

%description
This package allows Evolution to interact with Microsoft Exchange servers,
versions 2007 and later, through its Exchange Web Services (EWS) interface.

%package core
Summary: Core files for %{name}
Requires: %{name}-langpacks = %{version}-%{release}
Requires: evolution-data-server >= %{eds_evo_version}
Requires: libmspack >= %{libmspack_version}

%description core
This package contains core files for %{name}, which do not depend on the evolution package.
These files add the functionality for the address books, calendars, task lists and memo lists
without bringing in the evolution package.

%package langpacks
Summary: Translations for %{name}
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}

%description langpacks
This package contains translations for %{name}.

%prep
%autosetup -p1 -S gendiff

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations"
%cmake -G "Unix Makefiles"
%cmake_build

%install
%cmake_install

%find_lang %{name}

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README
%{_libdir}/evolution/modules/module-ews-configuration.so
%{_libdir}/evolution/modules/module-microsoft365-configuration.so
%{_datadir}/evolution/errors/module-ews-configuration.error
%{_datadir}/metainfo/org.gnome.Evolution-ews.metainfo.xml

%files core
%{_libdir}/evolution-data-server/camel-providers/libcamelews.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.urls
%{_libdir}/evolution-data-server/camel-providers/libcamelmicrosoft365.so
%{_libdir}/evolution-data-server/camel-providers/libcamelmicrosoft365.urls
%{_libdir}/evolution-data-server/addressbook-backends/libebookbackendews.so
%{_libdir}/evolution-data-server/addressbook-backends/libebookbackendmicrosoft365.so
%{_libdir}/evolution-data-server/calendar-backends/libecalbackendews.so
%{_libdir}/evolution-data-server/calendar-backends/libecalbackendmicrosoft365.so
%{_libdir}/evolution-data-server/registry-modules/module-ews-backend.so
%{_libdir}/evolution-data-server/registry-modules/module-microsoft365-backend.so
%{_libdir}/evolution-ews/libcamelews-priv.so
%{_libdir}/evolution-ews/libevolution-ews.so
%{_libdir}/evolution-ews/libevolution-ews-common.so
%{_libdir}/evolution-ews/libevolution-microsoft365.so
%{_datadir}/evolution-data-server/ews/windowsZones.xml

%files langpacks -f %{name}.lang

%changelog
* Fri Jan 31 2025 Milan Crha <mcrha@redhat.com> - 3.55.2-1
- Update to 3.55.2

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.55.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Milan Crha <mcrha@redhat.com> - 3.55.1-2
- Split files which do not need the 'evolution' package into a 'core' subpackage,
  which can be installed separately

* Tue Jan 07 2025 Milan Crha <mcrha@redhat.com> - 3.55.1-1
- Update to 3.55.1

* Fri Nov 22 2024 Milan Crha <mcrha@redhat.com> - 3.54.2-1
- Update to 3.54.2

* Fri Oct 18 2024 Milan Crha <mcrha@redhat.com> - 3.54.1-1
- Update to 3.54.1

* Fri Sep 13 2024 Milan Crha <mcrha@redhat.com> - 3.54.0-1
- Update to 3.54.0

* Fri Aug 30 2024 Milan Crha <mcrha@redhat.com> - 3.53.3-1
- Update to 3.53.3

* Fri Aug 02 2024 Milan Crha <mcrha@redhat.com> - 3.53.2-1
- Update to 3.53.2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.53.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Milan Crha <mcrha@redhat.com> - 3.53.1-1
- Update to 3.53.1

* Fri May 24 2024 Milan Crha <mcrha@redhat.com> - 3.52.2-1
- Update to 3.52.2

* Fri Apr 19 2024 Milan Crha <mcrha@redhat.com> - 3.52.1-1
- Update to 3.52.1

* Fri Mar 15 2024 Milan Crha <mcrha@redhat.com> - 3.52.0-1
- Update to 3.52.0

* Fri Mar 01 2024 Milan Crha <mcrha@redhat.com> - 3.51.3-1
- Update to 3.51.3

* Fri Feb 09 2024 Milan Crha <mcrha@redhat.com> - 3.51.2-1
- Update to 3.51.2

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.51.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.51.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Milan Crha <mcrha@redhat.com> - 3.51.1-1
- Update to 3.51.1

* Fri Dec 01 2023 Milan Crha <mcrha@redhat.com> - 3.50.2-1
- Update to 3.50.2

* Fri Oct 20 2023 Milan Crha <mcrha@redhat.com> - 3.50.1-1
- Update to 3.50.1

* Fri Sep 15 2023 Milan Crha <mcrha@redhat.com> - 3.50.0-1
- Update to 3.50.0

* Fri Sep 01 2023 Milan Crha <mcrha@redhat.com> - 3.49.3-1
- Update to 3.49.3

* Fri Aug 04 2023 Milan Crha <mcrha@redhat.com> - 3.49.2-1
- Update to 3.49.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.49.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Milan Crha <mcrha@redhat.com> - 3.49.1-1
- Update to 3.49.1

* Fri May 26 2023 Milan Crha <mcrha@redhat.com> - 3.48.2-1
- Update to 3.48.2

* Fri Apr 21 2023 Milan Crha <mcrha@redhat.com> - 3.48.1-1
- Update to 3.48.1

* Fri Mar 17 2023 Milan Crha <mcrha@redhat.com> - 3.48.0-1
- Update to 3.48.0

* Fri Mar 03 2023 Milan Crha <mcrha@redhat.com> - 3.47.3-1
- Update to 3.47.3

* Fri Feb 10 2023 Milan Crha <mcrha@redhat.com> - 3.47.2-1
- Update to 3.47.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.47.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Milan Crha <mcrha@redhat.com> - 3.47.1-1
- Update to 3.47.1

* Fri Dec 02 2022 Milan Crha <mcrha@redhat.com> - 3.46.2-1
- Update to 3.46.2

* Fri Oct 21 2022 Milan Crha <mcrha@redhat.com> - 3.46.1-1
- Update to 3.46.1

* Fri Sep 16 2022 Milan Crha <mcrha@redhat.com> - 3.46.0-1
- Update to 3.46.0

* Fri Sep 02 2022 Milan Crha <mcrha@redhat.com> - 3.45.3-1
- Update to 3.45.3

* Fri Aug 05 2022 Milan Crha <mcrha@redhat.com> - 3.45.2-1
- Update to 3.45.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Milan Crha <mcrha@redhat.com> - 3.45.1-1
- Update to 3.45.1

* Fri Jul 01 2022 Milan Crha <mcrha@redhat.com> - 3.44.3-1
- Update to 3.44.3

* Fri May 27 2022 Milan Crha <mcrha@redhat.com> - 3.44.2-1
- Update to 3.44.2

* Wed May 11 2022 Milan Crha <mcrha@redhat.com> - 3.44.1-2
- Resolves: #2083947 (Limit linking of gtk+ in shared libraries)

* Fri Apr 22 2022 Milan Crha <mcrha@redhat.com> - 3.44.1-1
- Update to 3.44.1

* Fri Mar 18 2022 Milan Crha <mcrha@redhat.com> - 3.44.0-1
- Update to 3.44.0

* Fri Mar 04 2022 Milan Crha <mcrha@redhat.com> - 3.43.3-1
- Update to 3.43.3

* Fri Feb 11 2022 Milan Crha <mcrha@redhat.com> - 3.43.2-1
- Update to 3.43.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Milan Crha <mcrha@redhat.com> - 3.43.1-1
- Update to 3.43.1

* Fri Oct 29 2021 Milan Crha <mcrha@redhat.com> - 3.42.1-1
- Update to 3.42.1

* Fri Sep 17 2021 Milan Crha <mcrha@redhat.com> - 3.42.0-1
- Update to 3.42.0

* Fri Sep 03 2021 Milan Crha <mcrha@redhat.com> - 3.41.3-1
- Update to 3.41.3

* Fri Aug 13 2021 Milan Crha <mcrha@redhat.com> - 3.41.2-1
- Update to 3.41.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.41.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Milan Crha <mcrha@redhat.com> - 3.41.1-1
- Update to 3.41.1

* Fri Jun 04 2021 Milan Crha <mcrha@redhat.com> - 3.40.2-1
- Update to 3.40.2

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

* Fri Nov 20 2020 Milan Crha <mcrha@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Fri Oct 02 2020 Milan Crha <mcrha@redhat.com> - 3.38.1-1
- Update to 3.38.1

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

* Fri Mar 27 2020 Milan Crha <mcrha@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Fri Mar 06 2020 Milan Crha <mcrha@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Fri Feb 28 2020 Milan Crha <mcrha@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Fri Feb 14 2020 Milan Crha <mcrha@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Fri Jan 31 2020 Milan Crha <mcrha@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

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

* Mon Sep 02 2019 Milan Crha <mcrha@redhat.com> - 3.33.92-1
- Update to 3.33.92

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

* Mon Oct 10 2016 Milan Crha <mcrha@redhat.com> - 3.22.1-1
- Update to 3.22.1

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

* Mon Feb 29 2016 Milan Crha <mcrha@redhat.com> - 3.19.91-1
- Update to 3.19.91

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

* Mon Nov 23 2015 Milan Crha <mcrha@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Mon Oct 26 2015 Milan Crha <mcrha@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Mon Oct 12 2015 Milan Crha <mcrha@redhat.com> - 3.18.1-1
- Update to 3.18.1

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

* Mon Aug 25 2014 Milan Crha <mcrha@redhat.com> - 3.13.5-1
- Update to 3.13.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Milan Crha <mcrha@redhat.com> - 3.13.4-1
- Update to 3.13.4

* Mon Jul 14 2014 Milan Crha <mcrha@redhat.com> - 3.12.4-1
- Update to 3.12.4

* Mon Jun 09 2014 Milan Crha <mcrha@redhat.com> - 3.12.3-1
- Update to 3.12.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Milan Crha <mcrha@redhat.com> - 3.12.2-1
- Update to 3.12.2

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
- Add $RPM_OPT_FLAGS to $CFLAGS (RH bug #1035930)

* Thu Nov 21 2013 Milan Crha <mcrha@redhat.com> - 3.11.2-2
- Rebuild for new libical (RH bug #1023020)

* Mon Nov 18 2013 Milan Crha <mcrha@redhat.com> - 3.11.2-1
- Update to 3.11.2
- Disable compiler warnings about deprecated symbols

* Tue Oct 22 2013 Matthew Barnes <mbarnes@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Mon Oct 14 2013 Milan Crha <mcrha@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Mon Sep 23 2013 Milan Crha <mcrha@redhat.com> - 3.10.0-1
- Update to 3.10.0

* Mon Sep 16 2013 Milan Crha <mcrha@redhat.com> - 3.9.92-1
- Update to 3.9.92

* Mon Sep 02 2013 Milan Crha <mcrha@redhat.com> - 3.9.91-1
- Update to 3.9.91

* Mon Aug 19 2013 Milan Crha <mcrha@redhat.com> - 3.9.90-1
- Update to 3.9.90

* Mon Jul 29 2013 Milan Crha <mcrha@redhat.com> - 3.9.5-1
- Update to 3.9.5

* Mon Jul 08 2013 Milan Crha <mcrha@redhat.com> - 3.9.4-1
- Update to 3.9.4

* Mon Jun 17 2013 Milan Crha <mcrha@redhat.com> - 3.9.3-1
- Update to 3.9.3
- Add dependency on libmspack 0.4+

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

* Mon Mar 04 2013 Milan Crha <mcrha@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Mon Feb 18 2013 Milan Crha <mcrha@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Mon Feb 04 2013 Milan Crha <mcrha@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Mon Jan 14 2013 Milan Crha <mcrha@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Thu Dec 20 2012 Matthew Barnes <mbarnes@redhat.com> - 3.7.3.1-1
- Update to 3.7.3.1

* Mon Nov 19 2012 Milan Crha <mcrha@redhat.com> - 3.7.2-1
- Update to 3.7.2

* Mon Oct 22 2012 Milan Crha <mcrha@redhat.com> - 3.7.1-1
- Update to 3.7.1

* Mon Sep 17 2012 Milan Crha <mcrha@redhat.com> - 3.5.92-1
- Update to 3.5.92

* Mon Sep 03 2012 Milan Crha <mcrha@redhat.com> - 3.5.91-1
- Update to 3.5.91
- Remove patch for new xmlOutputBuffer API (fixed upstream)

* Mon Aug 20 2012 Milan Crha <mcrha@redhat.com> - 3.5.90-1
- Update to 3.5.90
- Add patch for new xmlOutputBuffer API

* Mon Aug 06 2012 Milan Crha <mcrha@redhat.com> - 3.5.5-1
- Update to 3.5.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Milan Crha <mcrha@redhat.com> - 3.5.4-1
- Update to 3.5.4

* Mon Jun 25 2012 Matthew Barnes <mbarnes@redhat.com> - 3.5.3-1
- Update to 3.5.3

* Mon Jun 04 2012 Milan Crha <mcrha@redhat.com> - 3.5.2-1
- Update to 3.5.2

* Sun Apr 29 2012 Matthew Barnes <mbarnes@redhat.com> - 3.5.1-1
- Update to 3.5.1

* Mon Mar 26 2012 Milan Crha <mcrha@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Mon Mar 19 2012 Milan Crha <mcrha@redhat.com> - 3.3.92-1
- Update to 3.3.92

* Tue Mar 06 2012 Milan Crha <mcrha@redhat.com> - 3.3.91-1
- Update to 3.3.91

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
- Removed the last patch (fixed upstream)

* Mon Nov 21 2011 Milan Crha <mcrha@redhat.com> - 3.3.2-1
- Update to 3.3.2
- Removed obsolete patches (fixed upstream)

* Mon Nov 07 2011 Matthew Barnes <mbarnes@redhat.com> - 3.3.1-1
- Initial packaging for Fedora 17.
