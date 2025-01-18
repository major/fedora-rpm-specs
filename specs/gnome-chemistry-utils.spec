Name:           gnome-chemistry-utils
Version:        0.14.17
Release:        49%{?dist}
Summary:        A set of chemical utilities

#openbabel/* is GPLv2+
License:        GPL-3.0-or-later AND GPL-2.0-or-later
URL:            http://www.nongnu.org/gchemutils/
Source0:        http://download.savannah.nongnu.org/releases/gchemutils/0.14/%{name}-%{version}.tar.xz
Patch0:         %{name}-%{version}-gnm11242.patch
Patch1:         %{name}-%{version}-10041.patch
Patch2:         remove-gnome-common.patch
Patch3:         %{name}-%{version}-porting_openbabel3.patch
Patch4:         gdk-use-x11-backend.patch
Patch5:         0001-Use-yelp-instead-of-gnome-doc-utils.patch
Patch6:         %{name}-fix_pointer_types.patch

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  libGLU-devel
BuildRequires:  make
BuildRequires:  man-pages-reader
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(bodr) >= 5
BuildRequires:  pkgconfig(chemical-mime-data) >= 0.1.94
BuildRequires:  pkgconfig(lasem-0.6) >= 0.6.0
BuildRequires:  pkgconfig(libgoffice-0.10) >= 0.10.12
BuildRequires:  pkgconfig(libspreadsheet-1.12) >= 1.11.6
BuildRequires:  pkgconfig(openbabel-3)
BuildRequires:  yelp-tools

# https://gitlab.gnome.org/GNOME/goffice/-/issues/70
ExcludeArch:    %{ix86}

Requires:       gchem3d%{?_isa} = %{version}-%{release}
Requires:       gchemcalc%{?_isa} = %{version}-%{release}
Requires:       gchempaint%{?_isa} = %{version}-%{release}
Requires:       gchemtable%{?_isa} = %{version}-%{release}
Requires:       gcrystal%{?_isa} = %{version}-%{release}
Requires:       gspectrum%{?_isa} = %{version}-%{release}

%description
This is a meta-package for applications in the GNOME Chemistry Utils suite:

* A 3D molecular structure viewer (GChem3D).
* A Chemical calculator (GChemCalc).
* A 2D structure editor (GChemPaint).
* A periodic table of the elements application (GChemTable).
* A crystalline structure editor (GCrystal).
* A spectra viewer (GSpectrum).


%package        libs
Summary:        GNOME Chemistry Utils libraries
Requires:       bodr
Requires:       chemical-mime-data

%description    libs
This package contains common libraries for the GNOME Chemistry Utils suite.


%package        gnumeric
Summary:        Gnome Chemistry Utils plugin for Gnumeric
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    gnumeric
This package is a set of chemical utils. Several programs are available:
* A 3D molecular structure viewer (GChem3D).
* A Chemical calculator (GChemCalc).
* A 2D structure editor (GChemPaint).
* A periodic table of the elements application (GChemTable).
* A crystalline structure editor (GCrystal).
* A spectra viewer (GSpectrum).
This package contains a plugin adding a few chemistry-related functions to
gnumeric.


%package -n     gchem3d
Summary:        3D molecular structure viewer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n gchem3d
This package contains GChem3D, a 3D molecular structure viewer that is part of
the GNOME Chemistry Utils.


%package -n     gchemcalc
Summary:        Chemical calculator
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n gchemcalc
This package contains GChemCalc, a chemical calculator that is part of
the GNOME Chemistry Utils.


%package -n     gchempaint
Summary:        2D chemical structure editor
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       gnome-icon-theme

%description -n gchempaint
This package contains GChemPaint, a 2D chemical structure editor that is part of
the GNOME Chemistry Utils.


%package -n     gchemtable
Summary:        Periodic table of the chemical elements
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n gchemtable
This package contains GChemTable, an application for displaying the periodic
table of the chemical elements. It's part of the GNOME Chemistry Utils.


%package -n     gcrystal
Summary:        Crystalline structure editor
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       gnome-icon-theme

%description -n gcrystal
This package contains GCrystal, a crystalline structure editor that is part of
the GNOME Chemistry Utils.


%package -n     gspectrum
Summary:        Spectrum viewer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n gspectrum
This package contains GSpectrum, a spectrum viewer that is part of
the GNOME Chemistry Utils.


%prep
%autosetup -p1
autoreconf -ivf

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --disable-update-databases \
           --disable-scrollkeeper \
           --disable-silent-rules \
           --disable-schemas-compile \
           openbabel_CFLAGS="`pkg-config --cflags openbabel-3`" \
           openbabel_LIBS="`pkg-config --libs openbabel-3`"
%make_build

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install

desktop-file-validate \
       %{buildroot}%{_datadir}/applications/{gchem3d,gchemcalc,gchempaint,gchemtable,gcrystal,gspectrum}-0.14.desktop

# rename so that the desktop ID does not change for each API bump
for app_id in gchem3d gchemcalc gchempaint gchemtable gcrystal gspectrum; do
    echo $app_id
    mv %{buildroot}%{_datadir}/applications/$app_id-0.14.desktop \
       %{buildroot}%{_datadir}/applications/$app_id.desktop
    desktop-file-edit --set-key=Exec --set-value="env LD_LIBRARY_PATH=%{_libdir}/gchemutils $app_id-0.14" \
       %{buildroot}%{_datadir}/applications/$app_id.desktop
done

%find_lang gchemutils-0.14
%find_lang gchem3d-0.14 --with-gnome
%find_lang gchemcalc-0.14 --with-gnome
%find_lang gchempaint-0.14 --with-gnome
%find_lang gchemtable-0.14 --with-gnome
%find_lang gcrystal-0.14 --with-gnome
%find_lang gspectrum-0.14 --with-gnome

# kill libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# kill intrusive docs
rm -rf %{buildroot}%{_docdir}/gchemutils

# Move private libraries into private directory
mv %{buildroot}%{_libdir}/lib*-0.14.so* %{buildroot}%{_libdir}/gchemutils/

# kill KDE MIME .desktop files
rm -rf %{buildroot}%{_datadir}/mimelnk

# validate the .appdata.xml
mkdir -p %{buildroot}%{_metainfodir}
cp -p %{buildroot}%{_datadir}/appdata/*.appdata.xml %{buildroot}%{_metainfodir}/
rm -rf %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING

%files -n gchem3d -f gchem3d-0.14.lang
%{_bindir}/gchem3d-0.14
%{_bindir}/gchem3d
%{_metainfodir}/gchem3d.appdata.xml
%{_datadir}/applications/gchem3d.desktop
%{_datadir}/icons/hicolor/scalable/apps/gchem3d.svg
%{_mandir}/man1/gchem3d.1*

%files -n gchemcalc -f gchemcalc-0.14.lang
%{_bindir}/gchemcalc-0.14
%{_bindir}/gchemcalc
%{_metainfodir}/gchemcalc.appdata.xml
%{_datadir}/applications/gchemcalc.desktop
%{_datadir}/icons/hicolor/scalable/apps/gchemcalc.svg
%{_mandir}/man1/gchemcalc.1*

%files -n gchempaint -f gchempaint-0.14.lang
%{_bindir}/gchempaint-0.14
%{_bindir}/gchempaint
%{_metainfodir}/gchempaint.appdata.xml
%{_datadir}/applications/gchempaint.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.paint.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.paint.plugins.arrows.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/gchempaint.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-gchempaint.svg
%{_mandir}/man1/gchempaint.1*

%files -n gchemtable -f gchemtable-0.14.lang
%{_bindir}/gchemtable-0.14
%{_bindir}/gchemtable
%{_metainfodir}/gchemtable.appdata.xml
%{_datadir}/applications/gchemtable.desktop
%{_datadir}/icons/hicolor/scalable/apps/gchemtable.svg
%{_mandir}/man1/gchemtable.1*

%files -n gcrystal -f gcrystal-0.14.lang
%{_bindir}/gcrystal-0.14
%{_bindir}/gcrystal
%{_metainfodir}/gcrystal.appdata.xml
%{_datadir}/applications/gcrystal.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.crystal.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/gcrystal.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-gcrystal.svg
%{_mandir}/man1/gcrystal.1*

%files -n gspectrum -f gspectrum-0.14.lang
%{_bindir}/gspectrum-0.14
%{_bindir}/gspectrum
%{_metainfodir}/gspectrum.appdata.xml
%{_datadir}/applications/gspectrum.desktop
%{_datadir}/icons/hicolor/scalable/apps/gspectrum.svg
%{_mandir}/man1/gspectrum.1*

%files libs -f gchemutils-0.14.lang
%license COPYING
%{_libdir}/gchemutils/
%{_libdir}/goffice/*/plugins/gchemutils
%{_libexecdir}/babelserver
%{_datadir}/gchemutils/
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.gschema.xml
%{_datadir}/mime/packages/gchemutils.xml

%files gnumeric
%{_libdir}/gnumeric/*/plugins/gchemutils/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 01 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.14.17-48
- Rebuilt for lasem 0.6.0
- Add patch to fix pointer types in text.cc

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 29 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.14.17-44
- Switch to SPDX license identifier

* Mon Nov 06 2023 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-43
- Rebuild

* Sat Nov 04 2023 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-42
- Rebuild for gnumeric-1.12.56
- Drop i686 architecture

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 04 2023 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-40
- Rebuild for gnumeric-1.12.55

* Sat Jan 21 2023 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-39
- Rebuild for gnumeric-1.12.54

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 18 2022 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-37
- Rebuild for gnumeric-1.12.53

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 15 2022 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-35
- Add patch from Debian: switch to yelp
- Add patch from Debian: use x11 GDK backend for gchem3d and gcrystal
- Fix gchempaint crashing on startup
- Add gnome-icon-theme to gcrystal and gchempaint requires to avoid missing UI icons

* Wed Apr 20 2022 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-34
- Rebuild for gnumeric-1.12.52

* Sun Jan 23 2022 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-33
- Rebuild for gnumeric-1.12.51

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.14.17-31
- Fix GDK_BACKEND for using Wayland/X11
- Fix desktop files

* Wed Sep 22 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.14.17-30
- Porting to openbabel3
- Move private libraries into private directory

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 13 2021 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-28
- Rebuild for gnumeric-1.12.50

* Sun Mar 21 2021 Julian.Sikorski <belegdol+github@gmail.com> - 0.14.17-27
- Rebuild for gnumeric-1.12.49
- Fix merge molecules button (patch #10041)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-25
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 0.14.17-24
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-22
- Rebuild for gnumeric-1.12.47

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-20
- Rebuild for gnumeric-1.12.46

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-18
- Rebuild for gnumeric-1.12.45

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-16
- Rebuild for gnumeric-1.12.44

* Sat Aug 11 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-15
- Rebuilt for and patched to compile with gnumeric-1.12.42

* Fri Jul 20 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-14
- Fixed FTBFS: BR gcc-c++, gcc is not enough

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-12
- Rebuilt for gnumeric-1.12.41
- Dropped mozplugin sections entirely as Fedora 26 is the oldest supported release

* Sun May 06 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-11
- Rebuilt for gnumeric-1.12.40

* Sat Mar 17 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-10
- Rebuilt for gnumeric-1.12.39
- Removed ldconfig scriptlets as per https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.17-8
- Remove obsolete scriptlets

* Sun Dec 31 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-7
- Rebuilt for gnumeric-1.12.38

* Tue Nov 21 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-6
- Rebuilt for gnumeric-1.12.36

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-3
- Rebuilt for gnumeric-1.12.35
- Disabled mozilla plugin on Fedora 26 and above
- Fixed Source0 URL

* Mon Mar 27 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-2
- Rebuilt for gnumeric-1.12.34

* Mon Feb 13 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.17-1
- Updated to 0.14.17
- Dropped upstreamed .desktop file fix

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.16-3
- Rebuilt for gnumeric-1.12.33

* Tue Dec 06 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.16-2
- Fixed corrupted icon in gchemtable .desktop file (rhbz #1402039)
- Dropped scriptlets no longer necessary on F24 and above
- Switched to desktop-file-validate
- Added .appdata.xml validation
- Cleaned up BuildRequires

* Thu Nov 24 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.16-1
- Updated to 0.14.16

* Tue Nov 01 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.15-1
- Updated to 0.14.15

* Sat Oct 29 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.14-4
- Added lasem support

* Fri Oct 14 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.14.14-3
- rebuild for openbabel-2.4.1

* Sat Aug 27 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.14-2
- Rebuilt for gnumeric-1.12.32

* Mon Jul 04 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.14-1
- Updated to 0.14.14

* Tue Jun 21 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.12-3
- Rebuilt for gnumeric-1.12.30
- Spec file cleanups

* Sat May 07 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.12-2
- Rebuilt for gnumeric-1.12.29

* Thu Mar 31 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.12-1
- Updated to 0.14.12

* Wed Mar 23 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.11-2
- Rebuilt for gnumeric-1.12.28

* Mon Mar 07 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.11-1
- Updated to 0.14.11
- Dropped included patches

* Sat Feb 20 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.14.10-18
- Rebuild for openbabel

* Mon Feb 15 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-17
- Fixed FTBFS

* Sun Feb 07 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-16
- Rebuilt for gnumeric-1.12.27

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-14
- Fixed crash when trying to draw on existing chart (RH #1302135)

* Thu Dec 31 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-13
- Rebuilt for gnumeric-1.12.26

* Mon Dec 28 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-12
- Rebuilt for gnumeric-1.12.25

* Thu Nov 26 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-11
- Fixed crash when importing an invalid string (RH #1285154)

* Thu Nov 19 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-10
- Rebuilt for gnumeric 1.12.24

* Thu Jul 30 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-9
- Rebuilt for gnumeric 1.12.23

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-7
- Rebuilt for gnumeric-1.12.22

* Tue Apr 07 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-6
- Rebuilt for gnumeric-1.12.21

* Wed Feb 25 2015 Dominik Mierzejewski <rpm@greysector.net> - 0.14.10-5
- rebuilt for openbabel-2.3.90

* Fri Feb 06 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-4
- Rebuilt for gnumeric-1.12.20

* Thu Jan 29 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.10-3
- Rebuilt for gnumeric-1.12.19

* Fri Jan 16 2015 Richard Hughes <richard@hughsie.com> - 0.14.10-2
- Make the AppData files actually validate.

* Mon Jan 12 2015 Richard Hughes <richard@hughsie.com> - 0.14.10-1
- Updated to 0.14.10

* Thu Nov 06 2014 Richard Hughes <richard@hughsie.com> - 0.14.9-3
- Remove the API suffix to the desktop files; doing so breaks both the
  AppData support (as the AppStream ID has to match the desktop file name)
  and also GNOME Shell when the applications are added to the side-bar.

* Sat Sep 27 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.9-2
- Rebuilt for gnumeric-1.12.18

* Mon Sep 01 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.9-1
- Updated to 0.14.9
- Added appdata files

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Kalev Lember <kalevlember@gmail.com> - 0.14.8-6
- Fix scriptlet issues from the previous change

* Wed Jul 09 2014 Kalev Lember <kalevlember@gmail.com> - 0.14.8-5
- Split each application to a separate subpackage (#1117905)

* Thu Jun 12 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.8-4
- Rebuilt for gnumeric-1.12.17

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.8-2
- Rebuilt for gnumeric-1.12.16

* Tue May 13 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.8-1
- Updated to 0.14.8

* Sun May 04 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.7-6
- Rebuilt for gnumeric-1.12.15

* Mon Apr 21 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.7-5
- Rebuilt for gnumeric-1.12.14

* Fri Mar 21 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.7-4
- Rebuilt for gnumeric-1.12.13

* Tue Mar 04 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.7-3
- Rebuilt for gnumeric-1.12.12

* Wed Feb 19 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.7-2
- Rebuilt for gnumeric-1.12.11

* Sun Feb 16 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.7-1
- Updated to 0.14.7

* Fri Jan 31 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.6-1
- Updated to 0.14.6

* Wed Jan 01 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.5-1
- Updated to 0.14.5

* Tue Oct 15 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.3-2
- Rebuilt for gnumeric-1.12.8

* Sat Sep 14 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.3-1
- Updated to 0.14.3

* Sat Sep 14 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.2-8
- Rebuilt for gnumeric-1.12.7

* Sun Aug 25 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.2-7
- Rebuilt for gnumeric-1.12.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.2-5
- Rebuilt for gnumeric-1.12.4

* Sun Jun 30 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.2-4
- Rebuilt for gnumeric-1.12.3

* Mon Apr 29 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.2-3
- Rebuilt for gnumeric-1.12.2

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.14.2-2
- Drop desktop vendor tag.

* Sun Mar 17 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.2-1
- Updated to 0.14.2

* Sun Mar 10 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.1-1
- Updated to 0.14.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.14.0-1
- Updated to 0.14.0

* Sun Dec 02 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.99-1
- Updated to 0.13.99 (0.14.0beta2)
- ctfiles plugin was removed

* Sun Nov 18 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.98-2
- Rebuilt for gnumeric-1.11.90

* Mon Oct 01 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.98-1
- Updated to 0.13.98 (0.14.0beta1)

* Sun Aug 12 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.92-1
- Updated to 0.13.92

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.91-2
- Rebuilt for gnumeric-1.11.5

* Sun Jul 15 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.91-1
- Updated to 0.13.91
- -unstable suffixes are no more

* Tue Jun 26 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.7-2
- Rebuilt for gnumeric-1.11.4

* Mon Apr 23 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.7-1
- Updated to 0.13.7
- Updated the License tag

* Sun Apr 22 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.6-3
- Rebuilt for gnumeric 1.11.3

* Wed Mar 14 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.6-2
- Rebuilt for gnumeric-1.11.2

* Sat Feb 25 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.6-1
- Updated to 0.13.6
- Dropped upstreamed patches

* Sat Jan 07 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.13.5-1
- Updated to 0.13.5
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- GConf2 is no more

* Fri Nov 11 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.10-1
- Updated to 0.12.10

* Mon Aug 15 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.9-1
- Updated to 0.12.9
- Switched to .xz sources
- Added GSettings schemas

* Tue Aug 02 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.8-4
- Rebuilt for goffice-0.8.17 and gnumeric-1.10.17

* Sat Jun 18 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.8-3
- Rebuilt for goffice-0.8.16 and gnumeric-1.10.16

* Sun May 22 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.8-2
- Rebuilt for goffice-0.8.15 and gnumeric-1.10.15

* Tue May 10 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.8-1
- Updated to 0.12.8
- Dropped upstreamed patch
- Added GSettings scriptlets

* Sat Mar 26 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.7-2
- Rebuilt for goffice-0.8.14 and gnumeric-1.10.14

* Sun Feb 20 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.7-1
- Updated to 0.12.7
- Updated the gcc-4.6 fix

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 05 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.6-2
- Rebuilt for goffice-0.8.13 and gnumeric-1.10.13
- Added -fpermissive to CXXFLAGS to fix building with gcc-4.6

* Fri Jan 14 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.6-1
- Updated to 0.12.6

* Thu Dec 02 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.5-3
- Rebuilt for goffice-0.8.12 and gnumeric-1.10.12

* Thu Nov 25 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.5-2
- Rebuilt for openbabel-2.3.0

* Wed Nov 24 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.5-1
- Updated to 0.12.5
- Dropped the patch, it is included in the release

* Sun Oct 17 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.4-4
- Fixed crash when opening a 2D cml file in the 3D viewer (RH #643719)

* Sat Oct 02 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.4-3
- Rebuilt for goffice-0.8.11 and gnumeric-1.10.11

* Wed Sep 29 2010 jkeating - 0.12.4-2
- Rebuilt for gcc bug 634757

* Sun Sep 26 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.4-1
- Updated to 0.12.4

* Mon Sep 06 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.3-4
- Rebuilt for new goffice and gnumeric

* Tue Aug 17 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.3-3
- Rebuilt for new goffice and gnumeric

* Sat Aug 07 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.3-2
- Rebuilt for gnumeric 1.10.8

* Wed Aug 04 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.3-1
- Updated to 0.12.3

* Sat Jul 31 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.2-5
- Rebuilt for goffice 0.8.8

* Mon Jul 26 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.2-4
- Fixed the fonts issue properly (Savannah #30495)
- Fixed formal charges not being exported to OpenBabel (Savannah #30547)
- Fixed %%changelog typo

* Sun Jul 25 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.2-3
- Rebuilt for new goffice

* Sun Jul 25 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.2-2
- Patched the crash upon changing the text font (RH #614417, Savannah #30495)

* Sat Jul 24 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.2-1
- Updated to 0.12.2
- BR man-pages-reader instead of man
- Updated GConf scriptlets to macro version
- Dropped ancient gchempaint Provides and Obsoletes
- Dropped scrollkeeper BR

* Mon Jul 05 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.1-2
- Rebuilt for new gnumeric

* Thu Jun 17 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.1-1
- Updated to 0.12.1

* Thu May 13 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.12.0-1
- Updated to 0.12.0

* Fri May 07 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.11.98-1
- Updated to 0.11.98

* Sun May 02 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.11.91-2
- Added gnumeric-devel to BR, dropped libgnomeprintui22-devel
- Added -gnumeric subpackage
- Fixed -mozplugin subpackage Summary and Group entries

* Sun Apr 25 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.11.91-1
- Updated to 0.11.91

* Thu Apr 15 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.11.90-1
- Updated to 0.11.90
- Added --disable-silent-rules to %%configure

* Sat Apr 10 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.12-2
- Rebuilt for new goffice

* Sun Feb 28 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.12-1
- Updated to 0.10.12
- Dropped scrollkeeper scriptlets since they are not needed anymore
- Updated the icon cache scriptlets to the latest spec

* Mon Feb 22 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.10.11-2
- Rebuilt for new goffice

* Wed Feb 03 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.11-1
- Updated to 0.10.11
- Dropped included patch

* Sun Jan 10 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.10-2
- Added upstream patch fixing crash on come .cdx files (RH #553093, Savannah
  #28515)

* Fri Jan 01 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.10-1
- Updated to 0.10.10
- Switched to wildcard for goffice plugin installation path
- Dropped the goffice patch

* Wed Dec 30 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.9-3
- Rebuilt for goffice 0.7.17

* Tue Dec 01 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.9-2
- Rebuilt for new goffice
- Added patch from SVN to allow such build

* Sat Nov 14 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.9-1
- Updated to 0.10.9

* Mon Nov 09 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.8-2
- Require mozilla-filesystem instead of %%{_libdir}/mozilla/plugins

* Thu Sep 10 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.8-1
- Updated to 0.10.8

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.5-1
- Updated to 0.10.5
- Killed the .so symlinks, they were unnecessary

* Wed Mar 18 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.4-1
- Updated to 0.10.4
- Dropped upstreamed patches
- Dropped the KDE MIME .desktop files
- Remove the newly-appeared rpaths as well

* Tue Feb 24 2009 Martin Stransky <stransky@redhat.com> - 0.10.3-3
- Patched for NPAPI 1.9.1

* Mon Feb 23 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.3-2
- Patched gcc-4.4 build issues
- Fixed the Source URL
- Made the Provides/Obsoletes versioned
- Cleaned up the old gchempaint-devel Obsoletes
- Updated for goffice-0.6.6

* Tue Jan  6 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.3-1
- Updated to 0.10.3

* Sat Nov 29 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.2-1
- Updated to 0.10.2

* Sat Nov 15 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.1-1
- Updated to 0.10.1

* Fri Oct 31 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.10.0-1
- Updated to 0.10.0

* Wed Oct 22 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.98-1
- Updated to 0.9.98 (AKA 0.10.0 RC1)

* Sat Oct 18 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.93-1
- Updated to 0.9.93

* Mon Sep 29 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.92-1
- Updated to 0.9.92
- Added hicolor-icon-theme to Requires

* Mon Sep 15 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.91-2
- Added bodr to Requires
- Added chrpath to BuildRequires
- Switched to chrpath as a method to eliminate rpaths

* Sun Sep 14 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.91-1
- Updated to 0.9.91
- Dropped the ppc build patch (merged upstream)

* Sun Sep  7 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.90-2
- Patched the ppc build failure, thanks to Tom Callaway and Jean Bréfort

* Sun Sep  7 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.90-1
- Updated to 0.9.90
- Replaced the firefox/xulrunner conditional with gecko-devel
- Provide and obsolete gchempaint
- Dropped the rpath killer for the time being
- Dropped the -devel subpackage since it is not needed any more

* Mon Jul  7 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.7-2
- Rebuilt for new openbabel

* Wed Mar 19 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.7-1
- Updated to 0.8.7

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.6-2
- Autorebuild for GCC 4.3

* Sat Jan 26 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.6-1
- Updated to 0.8.6

* Fri Dec 21 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.5-1
- Updated to 0.8.5
- Conditionalised xulrunner usage

* Thu Dec  6 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.4-2
- Rebuilt against xulrunner
- Cleaned up the spec

* Tue Oct 30 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.4-1
- Updated to 0.8.4

* Mon Sep 17 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.3-1
- Updated to 0.8.3

* Sun Aug 26 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.2-4
- Adjusted License tag as per latest guidelines

* Mon Aug  6 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.2-3
- Added goffice04-devel to -devel subpackage Requires

* Sat Aug  4 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.2-2
- Added gnome-doc-utils to BuildRequires

* Sun Jul 29 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.2-1
- Updated to 0.8.2
- Added scrollkeeper stuff
- Added missing GConf Requires

* Fri Jun 29 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.1-1
- Updated to 0.8.1

* Sun May 20 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.0-1
- Updated to 0.8.0
- Added %%{_libdir}/mozilla/plugins to -mozplugin subpackage Requires

* Thu May 10 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.7.96-1
- Updated to 0.7.96

* Wed May  9 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.7.95-1
- Updated to 0.7.95

* Sat Apr 21 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.7.91-1
- Updated to 0.7.91

* Mon Apr  9 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.5-1
- Updated to 0.6.5
- Switched to bzip2 sources
- Added rpath killer

* Sun Jan 14 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.4-1
- Updated to 0.6.4

* Tue Dec 19 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.3-5
- Rebuild for new openbabel

* Sun Dec 03 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.3-4
- Removed obsolete stuff
- Fixed support for chemical-mime-data
- Removed --add-category X-Fedora from desktop-file-install command

* Sun Dec 03 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.3-3
- Added doxygen to BuildRequires
- Added support for chemical-mime-data

* Sun Dec 03 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.3-2
- Fixed Requires for -devel and -mozplugin packages
- Moved files in docs/reference/html to the devel package
- Install .desktop files using desktop-file-install
- Removed redundant stuff
- Preserve timestamps

* Sat Dec 02 2006 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.6.3-1
- Initial RPM release
