Name:          foxtrotgps
Version:       1.2.2
Release:       21%{?dist}
Summary:       GTK+ mapping and GPS application
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           http://www.foxtrotgps.org
Source0:       http://www.foxtrotgps.org/releases/%{name}-%{version}.tar.xz
Patch0:        dialog10-fix.patch
Patch1:        gpsd-API-v9-fix.patch
Patch2:        gpsd-API-v10-fix.patch

BuildRequires: gcc
BuildRequires: bluez-libs-devel
BuildRequires: dbus-devel
BuildRequires: gtk2-devel
BuildRequires: libglade2-devel
BuildRequires: libcurl-devel
BuildRequires: libexif-devel
BuildRequires: libxml2-devel
BuildRequires: sqlite-devel
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: gpsd-devel
BuildRequires: make

Requires: gpsd

# The following two package are only needed, if someone wants
# to geotag photos, which is an optional functionality. We 
# decided to include them, because then all functionality is
# available without manual package installation.
Requires: gpscorrelate
Requires: jhead

%description
FoxtrotGPS is an easy-to-use graphical tool that can be used
to track the position of a GPS receiver on a map in relation to
user-defined points of interest (POIs), a destination and waypoints,
and tracks loaded from files or internet routing-services.

FoxtrotGPS also allows internet-connected users to share their position
with other users and send messages.

By default it uses map data from the OpenStreetMap.org project; 
additionally a variety of other repositories can easily be added.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p0

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

sed -i 's/Lieu/Lieu;/' %{buildroot}/usr/share/applications/foxtrotgps.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
rm -rf %{buildroot}/usr/share/doc/%{name}/
rm -rf %{buildroot}/usr/share/info/dir

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS HACKING NEWS
%doc contrib/README.osb2foxtrot

%{_bindir}/foxtrotgps
%{_bindir}/convert2gpx
%{_bindir}/convert2osm
%{_bindir}/gpx2osm
%{_bindir}/poi2osm
%{_bindir}/osb2foxtrot
%{_bindir}/georss2foxtrotgps-poi
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/foxtrotgps.png
%{_datadir}/pixmaps/foxtrotgps-*.png
%{_datadir}/GConf/gsettings/org.foxtrotgps.convert
%{_datadir}/glib-2.0/schemas/org.foxtrotgps.gschema.xml
%{_mandir}/man?/*
%{_infodir}/foxtrotgps.info.*
%{_datadir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.2-20
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Adam Williamson <awilliam@redhat.com> - 1.2.2-15
- rebuild for new libgps

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 06 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.2-12
- Rebuild for new gpsd

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Björn Esser <besser82@fedoraproject.org> - 1.2.2-10
- Rebuild (gpsd)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Dr. Tilmann Bubeck <bubeck@fedoraproject.org> - 1.2.2-7
- Update for gpsd API version 10 and gpsd 3.22

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Björn Esser <besser82@fedoraproject.org> - 1.2.2-5
- Rebuild (gpsd)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Dr. Tilmann Bubeck <bubeck@fedoraproject.org> - 1.2.2-3
- Fixed compile bug for GCC 10, introduced with fedora 32
- Update for gpsd API version 9 and gpsd 3.20

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Tilmann Bubeck <bubeck@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.1-7
- Rebuild (gpsd)


* Sun Apr 28 2019 Tilmann Bubeck <bubeck@fedoraproject.org> - 1.2.1-6
- Updated patch to a better version from upstream.

* Sun Apr 28 2019 Tilmann Bubeck <bubeck@fedoraproject.org> - 1.2.1-5
- Patched for gpsd-3.18.

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.1-4
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.1-1
- Update to 1.2.1

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-9
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 27 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-2
- Rebuild (gpsd)

* Mon Mar  2 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-1
- Update to 1.2.0 (rhbz 1157448)
- Use %%licenese

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 27 2013 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.1.1-7
- Rebuilt, because libgps was updated. Fixed dates in specfile.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.1.1-4
- Obsoletes: tangogps

* Sat Aug 04 2012 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.1.1-3
- fixed typo in description

* Wed Aug 01 2012 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.1.1-2
- removed Requires: dbus, cleaned up spec file, 
  removed EPEL 5 support, consistent use of %%{buildroot} and %%{name}

* Tue Jul 31 2012 Dr. Tilmann Bubeck <t.bubeck@reinform.de> - 1.1.1-1
- initial package based upon Fedora's tangogps.spec

