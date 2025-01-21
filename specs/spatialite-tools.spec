Name:           spatialite-tools
Version:        5.1.0a
Release:        4%{?dist}
Summary:        A set of useful CLI tools for SpatiaLite

License:        GPL-3.0-or-later
Source0:        https://www.gaia-gis.it/gaia-sins/spatialite-tools-sources/%{name}-%{version}.tar.gz
URL:            https://www.gaia-gis.it/fossil/spatialite-tools

BuildRequires: make
BuildRequires:  expat-devel
BuildRequires:  freexl-devel
BuildRequires:  gcc
BuildRequires:  geos-devel
BuildRequires:  libspatialite-devel
BuildRequires:  librttopo-devel
BuildRequires:  libxml2-devel
BuildRequires:  minizip-devel
BuildRequires:  proj-devel
BuildRequires:  readline-devel
BuildRequires:  readosm-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel

%description
Spatialite-Tools is a set of useful CLI tools for SpatiaLite.


%prep
%autosetup -p1

# Remove unused Makefiles
rm -f Makefile-static*


%build
export LDFLAGS="%{__global_ldflags} -lxml2 -lm"
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc AUTHORS
%{_bindir}/exif_loader
%{_bindir}/shp_doctor
%{_bindir}/shp_sanitize
%{_bindir}/spatialite
%{_bindir}/spatialite_convert
%{_bindir}/spatialite_dem
%{_bindir}/spatialite_dxf
%{_bindir}/spatialite_gml
%{_bindir}/spatialite_network
%{_bindir}/spatialite_osm*
%{_bindir}/spatialite_tool
%{_bindir}/spatialite_xml_*
%{_bindir}/spatialite_xml2utf8

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Sandro Mani <manisandro@gmail.com> - 5.1.0a-1
- Update to 5.1.0a

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Sandro Mani <manisandro@gmail.com> - 5.0.1-1
- Update to 5.0.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> - 5.0.0-1
- Update to 5.0.0

* Thu Aug 20 08:46:50 GMT 2020 Sandro Mani <manisandro@gmail.com> - 4.3.0-46
- Rebuild (sqlite)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Ondrej Dubaj <odubaj@redhat.com> - 4.3.0-44
- Rebuild for sqlite 3.32.3

* Fri Jun 05 2020 Ondrej Dubaj <odubaj@redhat.com> - 4.3.0-43
- Rebuild for sqlite 3.32.2

* Tue May 26 2020 Ondrej Dubaj <odubaj@redhat.com> - 4.3.0-42
- Rebuild for sqlite 3.32.1

* Wed Feb 05 2020 Ondrej Dubaj <odubaj@redhat.com> - 4.3.0-41
- Rebuild for sqlite 3.31.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Petr Kubat <pkubat@redhat.com> - 4.3.0-39
- Rebuild for sqlite 3.30.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Petr Kubat <pkubat@redhat.com> - 4.3.0-37
- Rebuild for sqlite 3.29.0

* Mon May 13 2019 Petr Kubat <pkubat@redhat.com> - 4.3.0-36
- Rebuild for sqlite 3.28.0

* Thu Feb 28 2019 Petr Kubat <pkubat@redhat.com> - 4.3.0-35
- Rebuild for sqlite 3.27.2

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.3.0-34
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Petr Kubat <pkubat@redhat.com> - 4.3.0-32
- Rebuild for sqlite 3.26.0

* Thu Oct 11 2018 Petr Kubat <pkubat@redhat.com> - 4.3.0-31
- Rebuild for sqlite 3.25.2

* Mon Jul 23 2018 Volker Froehlich <volker27@gmx.at> - 4.3.0-30
- Rebuild for sqlite 3.24.0
- Add BR for gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Tom Hughes <tom@compton.nu> - 4.3.0-28
- Rebuilt for sqlite 3.22.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 04 2017 Petr Kubat <pkubat@redhat.com> - 4.3.0-26
- Rebuild for sqlite 3.20.1

* Wed Aug 02 2017 Petr Kubat <pkubat@redhat.com> - 4.3.0-25
- Rebuild for sqlite 3.20.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Petr Kubat <pkubat@redhat.com> - 4.3.0-23
- Rebuild for sqlite 3.19.3

* Thu May 25 2017 Petr Kubat <pkubat@redhat.com> - 4.3.0-22
- Rebuild for sqlite 3.19.1

* Mon Apr 03 2017 Petr Kubat <pkubat@redhat.com> - 4.3.0-21
- Rebuild for sqlite 3.18.0

* Wed Feb 22 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 4.3.0-20
- Rebuild for sqlite 3.17.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Volker Froehlich <volker27@gmx.at> - 4.3.0-18
- Rebuild for libproj

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.3.0-17
- Rebuild for readline 7.x

* Sat Jan  7 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 4.3.0-16
- Rebuild for sqlite 3.16.2

* Fri Jan  6 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 4.3.0-15
- Rebuild for sqlite 3.16.1

* Wed Sep 21 2016 Jakub Dorňák <jdornak@redhat.com> - 4.3.0-14
- Rebuild for sqlite 3.14.2

* Tue Aug 16 2016 Jakub Dorňák <jdornak@redhat.com> - 4.3.0-13
- Rebuild for sqlite 3.14.1

* Thu Jul 28 2016 Jakub Dorňák <jdornak@redhat.com> - 4.3.0-12
- Rebuild for sqlite 3.13.0

* Mon May  2 2016 Jakub Dorňák <jdornak@redhat.com> - 4.3.0-10
- Rebuild for sqlite 3.12.2

* Wed Feb 17 2016 Jan Stanek <jstanek@redhat.com> - 4.3.0-9
- Rebuild for sqlite 3.11.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Jan Stanek <jstanek@redhat.com> - 4.3.0-7
- Rebuild for sqlite 3.10.2

* Wed Jan 13 2016 Jan Stanek <jstanek@redhat.com> - 4.3.0-6
- Rebuild for sqlite 3.10.0

* Mon Dec 28 2015 Volker Froehlich <volker27@gmx.at> - 4.3.0-5
- Rebuild for sqlite 3.9.2

* Thu Oct 15 2015 Jan Stanek <jstanek@redhat.com> - 4.3.0-4
- Rebuild for sqlite 3.9.0

* Wed Sep 23 2015 Jan Stanek <jstanek@redhat.com> - 4.3.0-3
- Rebuild for sqlite 3.8.11.1

* Wed Jul 29 2015 Jan Stanek <jstanek@redhat.com> - 4.3.0-2
- Rebuild for sqlite 3.8.11

* Sat Jul  4 2015 Volker Froehlich <volker27@gmx.at> - 4.3.0-1
- New upstream release
- Add libxml2-devel as BR

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Jan Stanek <jstanek@redhat.com> - 4.2.0-12
- Rebuild for sqlite 3.8.10.2

* Mon May 18 2015 Jan Stanek <jstanek@redhat.com> - 4.2.0-11
- Rebuild for sqlite 3.8.10.1

* Tue Apr 14 2015 Jan Stanek <jstanek@redhat.com> - 4.2.0-10
- Rebuild for sqlite 3.8.9

* Sat Mar 14 2015 Volker Froehlich <volker27@gmx.at> - 4.2.0-9
- Rebuild for proj 4.9.1

* Thu Feb 26 2015 Jan Stanek <jstanek@redhat.com> - 4.2.0-8
- Rebuild for sqlite 3.8.8.3

* Tue Jan 20 2015 Jan Stanek <jstanek@redhat.com> - 4.2.0-7
- Rebuild for sqlite 3.8.8
- Add check for the correct sqlite-devel version

* Fri Dec 12 2014 Jan Stanek <jstanek@redhat.com> - 4.2.0-6
- Rebuild for sqlite 3.8.7.4

* Tue Nov 25 2014 Jan Stanek <jstane@redhat.com> - 4.2.0-5
- Rebuild for sqlite 3.8.7.2

* Tue Oct 21 2014 Jan Stanek <jstanek@redhat.com> - 4.2.0-4
- Rebuild for sqlite 3.8.7

* Wed Aug 20 2014 Volker Fröhlich <volker27@gmx.at> - 4.2.0-3
- Rebuild for sqlite 3.8.6

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 4.2.0-1
- Upate to 4.2.0

* Sat Jun 14 2014 Volker Fröhlich <volker27@gmx.at> - 4.1.1-5
- Rebuild for sqlite 3.8.5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun  5 2014 Volker Fröhlich <volker27@gmx.at> - 4.1.1-3
- Solve BZ 1048587 (spatialite command complains about sqlite version)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul  1 2013 Volker Fröhlich <volker27@gmx.at> - 4.1.1-1
- New upstream release

* Tue Jun  4 2013 Volker Fröhlich <volker27@gmx.at> - 4.1.0-2
- Add dxf utility to files section

* Tue Jun  4 2013 Volker Fröhlich <volker27@gmx.at> - 4.1.0-1
- New upstream release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec  2 2012 Volker Fröhlich <volker27@gmx.at> - 4.0.0-1
- New upstream release
- Remove PPC restrictions

* Sat Aug 18 2012 Volker Fröhlich <volker27@gmx.at> - 3.1.0b-1
- Update for new release
- Update URL and source URL
- Drop LDFLAG -lm
- Exclude ppc as well

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-0.6.RC4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-0.5.RC4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 17 2011 Volker Fröhlich <volker27@gmx.at> - 2.4.0-0.4.RC4
- Support readline
- Drop EPEL5 specific statements and definitions
- Drop unnecessary defattr
- Slightly improved description
- More explicit files section

* Fri Feb 25 2011 Volker Fröhlich <volker27@gmx.at> - 2.4.0-0.3.RC4
- Exclude ppc64

* Fri Jan 14 2011 Volker Fröhlich <volker27@gmx.at> - 2.4.0-0.2.RC4
- Dropped prefix from configure macro
- Corrected license
- Use macros in source URL

* Mon Dec 20 2010 Volker Fröhlich <volker27@gmx.at> - 2.4.0-0.1.RC4
- Inital packaging
