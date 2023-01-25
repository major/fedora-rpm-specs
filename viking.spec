Name:           viking
Version:        1.8
Release:        12%{?dist}
Summary:        GPS data editor and analyzer

License:        GPLv2+
URL:            http://viking.sourceforge.net/
Source0:        http://downloads.sourceforge.net/viking/viking-%{version}.tar.bz2
#Patch0:         path-to-manpages-docbook-xsl.patch
ExcludeArch:    s390 s390x

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  expat-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gpsd-devel
BuildRequires:  gtk2-devel
BuildRequires:  libcurl-devel
BuildRequires:  gtk-doc
BuildRequires:  gnome-doc-utils
BuildRequires:  libexif-devel
BuildRequires:  bzip2-devel
BuildRequires:  file-devel
BuildRequires:  libgexiv2-devel
BuildRequires:  sqlite-devel
BuildRequires:  docbook-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  mapnik-devel
BuildRequires:  rarian-compat
BuildRequires:  geoclue2-devel
BuildRequires:  liboauth-devel
BuildRequires:  nettle-devel
BuildRequires:  libzip-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

Requires:       hicolor-icon-theme
Requires:       gpsbabel
Requires:       expect

%description
Viking is a free/open source program to manage GPS data. You can import
and plot tracks and waypoints, show OpenStreetMap and/or Terraserver maps
under it, download geocaches for an area on the map, make new tracks and
waypoints, see real-time GPS position, etc.

%prep
%autosetup
# Convert to utf-8
for file in ChangeLog NEWS TODO; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

%build
%configure
%make_build CFLAGS="${RPM_OPT_FLAGS} -fcommon"

%install
%make_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
desktop-file-install                                        \
    --add-category="GTK;Network;"                           \
    --delete-original                                       \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-gnome

%check
make test

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog* NEWS README TODO
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jan 24 2023 Adam Williamson <awilliam@redhat.com> - 1.8-12
- rebuild for new libgps

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 06 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.8-9
- Rebuild for new gpsd

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Björn Esser <besser82@fedoraproject.org> - 1.8-7
- Rebuild (gpsd)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.8-4
- Rebuild (gpsd)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Björn Esser <besser82@fedoraproject.org> - 1.8-2
- Rebuild (gpsd)

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.8-1
- Fix FTBFS (rhbz#1800235)
- Update to new upstream version 1.8

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-5
- Rebuild for gpsd

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 1.7-3
- Rebuild (gpsd)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-1
- Update to new upstream version 1.7

* Fri Sep 28 2018 Federico Bruni <fede@inventati.org> - 1.6.2-8
- Add man page and fix help files location (rhbz#1633836)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.2-1
- Update to new upstream version 1.6.2

* Wed Nov 25 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-1
- Fix for lock (rhbz#1258559, rhbz#1258095, rhbz#1229082)
- Update to new upstream version 1.6.1

* Sat Aug 15 2015 Till Maas <opensource@till.name> - 1.6-4
- Fix FTBFS (#1240039)
- Use %%license
- Remove unused mapnik-devel BR

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.6-2
- Add patch to fix issue with new gpsd (rhbz#1206642)

* Wed May 06 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.6-1
- Update to new upstream version 1.6

* Sat Mar 07 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.1-4
- Rebuild (libgps)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.1-1
- Update to new upstream version 1.5.1

* Thu Nov 28 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-2
- Rebuild for libgps

* Fri Oct 18 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-1
- Update to new upstream version 1.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update to new upstream version 1.4.1

* Tue Feb 19 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-1
- Update to new upstream version 1.4

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 24 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2.1-1
- Update to new upstream version 1.3.2.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-1
- Update to new upstream version 1.3.1

* Mon Apr 30 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-2
- Update requirements

* Mon Apr 30 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-1
- Update to new upstream version 1.3

* Sat Feb 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-3
- Orphan BR

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 08 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Curl patch removed (is now upstream)
- Update to new upstream version 1.2.2

* Tue Aug 23 2011 Tom Callaway <spot@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1
- Enable gpsd 2.96+ support
- Fix compile with curl 7.21.7 (curl/types.h is gone)

* Fri Jun 03 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-1
- Update to new upstream version 1.2

* Sun Mar 06 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.1-1
- Update to new upstream version 1.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Update description to fix #673009
- Update to new upstream version 1.0.1

* Sat Nov 20 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-2
- Remove patch, is now upstream

* Sat Nov 20 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-1
- Add test suite
- Update to new upstream version 1.0

* Wed Nov 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.96-1
- Update to new upstream version 0.9.96

* Wed Sep 29 2010 jkeating - 0.9.95-3
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.95-2
- Disable scrollkeeper

* Tue Sep 07 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.95-1
- Remove old patch0
- Add new BR
- Update to new upstream version 0.9.95

* Wed Jul 14 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.94-1
- Update file section
- Update DSOLinking patch
- Update to new upstream version 0.9.94

* Thu May 27 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.93-1
- Update to new upstream version 0.9.93

* Sun May 09 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.91-4
- Rebuilt for new gpsd release

* Tue Apr 27 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.91-3
- New patch to fix DSOLinking (#565080)

* Mon Mar 22 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.91-2
- Added patch to fix DSOLinking (#565080)

* Sat Feb 27 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.91-1
- Update to new upstream version 0.9.91

* Sun Sep 13 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.9-1
- Update to new upstream version 0.9.9

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.8-2
- use new gpsd header (gpsdclient.h)

* Sat Mar 28 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.8-1
- Update to new upstream version, 0.9.8

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.7-2
- Add missing hicolor-icon-theme

* Sat Jan 24 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.7-1
- Initial package for Fedora
