Name:           osm2pgsql
Version:        1.9.1
Release:        1%{?dist}
Summary:        Import map data from OpenStreetMap to a PostgreSQL database

License:        GPLv2+
URL:            https://github.com/openstreetmap/osm2pgsql
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  catch2-devel catch2-static
BuildRequires:  expat-devel
BuildRequires:  fmt-devel
BuildRequires:  json-devel
BuildRequires:  libosmium-devel
BuildRequires:  libpq-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  proj-devel
BuildRequires:  protozero-devel protozero-static
BuildRequires:  zlib-devel
BuildRequires:  postgresql
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  postgis
BuildRequires:  python3
BuildRequires:  python3-behave
BuildRequires:  python3-osmium
BuildRequires:  python3-psycopg2

%description
Provides a tool for loading OpenStreetMap data into a PostgreSQL / PostGIS
database suitable for applications like rendering into a map, geocoding with
Nominatim, or general analysis.

%prep
%autosetup -p1
rm -rf contrib
mkdir -p contrib/catch2
ln -sf /usr/include/catch2 contrib/catch2/include

%build
%cmake \
  -DEXTERNAL_FMT=ON \
  -DEXTERNAL_LIBOSMIUM=ON \
  -DEXTERNAL_PROTOZERO=ON \
  -DBUILD_TESTS=ON \
%cmake_build

%install
%cmake_install

%check
PGTESTS_LOCALE="C.UTF-8" %postgresql_tests_run
mkdir tablespacetest
psql -c "CREATE TABLESPACE tablespacetest LOCATION '$PWD/tablespacetest'" postgres
LANG="C.UTF-8" %ctest -j1

%files
%doc AUTHORS CONTRIBUTING.md README.md
%license COPYING
%{_mandir}/man1//%{name}*.1*
%{_bindir}/%{name}*
%{_datadir}/%{name}/

%changelog
* Wed Aug 23 2023 Tom Hughes <tom@compton.nu> - 1.9.1-1
- Update to 1.9.1 upstream release

* Wed Aug 16 2023 Tom Hughes <tom@compton.nu> - 1.9.0-1
- Update to 1.9.0 upstream release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Tom Hughes <tom@compton.nu> - 1.8.1-2
- Unbundle libraries
- Enable tests

* Tue Jun 27 2023 Tom Hughes <tom@compton.nu> - 1.8.1-1
- Update to 1.8.1 upstream release

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.6.0-6
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.6.0-3
- Rebuilt for Boost 1.78

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 1.6.0-2
- Rebuild for proj-9.0.0

* Wed Jan 26 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Update to latest upstream release 1.6.0 (#2039668)

* Sat Jan 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.2-1
- Update to latest upstream release 1.5.2 (#2039668)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.1-1
- Update to latest upstream release 1.5.1 (rhbz#1950346)

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.4.1-6
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 1.4.1-4
- Rebuilt for removed libstdc++ symbols (#1937698)

* Sun Mar 07 2021 Sandro Mani <manisandro@gmail.com> - 1.4.1-3
- Rebuild (proj)

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.4.1-2
- rebuild for libpq ABI fix rhbz#1908268

* Wed Feb 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update to latest upstream version 1.4.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.4.0-2
- Rebuilt for Boost 1.75

* Wed Dec 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to latest upstream version 1.4.0 (#1905287)

* Thu Nov  5 20:16:50 CET 2020 Sandro Mani <manisandro@gmail.com> - 1.3.0-2
- Rebuild (proj)

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream version 1.3.0 (rhbz#1861496)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to latest upstream version 1.2.2 (rhbz#1851781)

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.2.1-3
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Update BRs
- Update to latest upstream version 1.2.1 (rhbz#1763938)

* Tue Oct 22 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Update to latest upstream version 1.2.0 (rhbz#1763938)

* Fri Aug 30 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Update to latest upstream version 1.0.0 (rhbz#1742995)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 5 2019 Devrim Gündüz <devrim@gunduz.org> - 0.96.0-4
- Rebuilt for Proj 5.2.0

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 0.96.0-3
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.96.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.96.0-1
- Update to latest upstream version 0.96.0 (rhbz#1442296)

* Fri Mar 23 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.94.0-1
- Update to latest upstream version 0.94.0 (rhbz#1479517)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.92.1-8
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 17 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.92.1-6
- Rebuilt

* Tue Aug 22 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.92.1-5
- Add patch to fix build failure (rhbz#1470894)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 0.92.1-2
- Rebuilt for Boost 1.64

* Sat Jun 24 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.92.1-1
- Update to latest upstream version 0.92.1 (rhbz#1442296)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.92.0-2
- Rebuilt for libgeos

* Sun Dec 18 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.92.0-1
- Update to latest upstream version 0.92.0 (rhbz#1403406)

* Wed Aug 03 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.90.1-1
- Update to latest upstream version 0.90.1 (rhbz#1357715)

* Sun Apr 03 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.90.0-1
- Fix link (rhbz#1266784)
- Update to latest upstream version 0.90.0 (rhbz#1312619)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.88.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.88.1-4
- Rebuilt for Boost 1.60

* Sat Oct 17 2015 Kalev Lember <klember@redhat.com> - 0.88.1-3
- Rebuilt for libgeos soname bump

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.88.1-2
- Rebuilt for Boost 1.59

* Wed Aug 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.88.1-1
- Update to 0.88.1 (RHBZ#1217478).
- Add %%license.
- Add BR: lua-devel.

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.88.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 29 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.88.0-1
- Update to latest upstream version 0.88.0 (rhbz#1217478)

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.87.3-3
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.87.3-1
- Update to latest upstream version 0.87.3 (rhbz#1217478)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.87.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 16 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.87.2-4
- REbuild for libproj

* Wed Mar 04 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.87.2-1
- Update to latest upstream version 0.87.2 (rhbz#1178374)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.87.0-3
- Rebuild for boost 1.57.0

* Tue Jan 06 2015 Dan Horák <dan[at]danny.cz> - 0.87.0-2
- workaround Boost detection for ppc64le until buildsys is refreshed from latest autoconf-archive

* Wed Dec 10 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.87.0-1
- Update to latest upstream version 0.87.0 (rhbz#1172614)

* Wed Oct 29 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.86.0-1
- Update to latest upstream version 0.86.0 (rhbz#1157481)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.84.0-3
- Rebuild for protobuf (rhbz#1126749)
 
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 05 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.84.0-1
- Update to latest upstream version 0.84.0

* Tue Nov 05 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.82.0-3
- Rebuilt for geos

* Sat Oct 05 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.82.0-2
- Rebuilt for geos

* Thu Sep 12 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.82.0-1
- Update to latest upstream version 0.82.0
- Spec file updated

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70.5-0.14.20121021svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 0.70.5-0.13.20121021svn
- Rebuild with new geos.

* Sat Jan 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.70.5-0.12.20121021svn
- Rebuilt for geos

* Mon Nov 19 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 0.70.5-0.11.20121021svn
- Rebuild with newer geos.

* Thu Nov 15 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.70.5-0.10.20121021svn
- Rebuilt for geos

* Sun Oct 21 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.70.5-0.9.20121021svn
- Update to new svn checkout from 2012-10-21
- gazetteer was removed
- nodecachefilereader included
- Minor changes

* Fri Apr 13 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.70.5-0.8.20120413svn
- Patch to remove gazetteer stuff reworked 
- Update to new upstream version 20120413 (Rev. 28284)

* Mon Mar 19 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.70.5-0.7.20120319svn
- Update to new upstream version 20120319 (Rev. 28116)

* Sat Sep 10 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.70.5-0.6.20110910svn
- Update to new upstream version 20110910 (Rev. 26638)

* Sat Jul 02 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.70.5-0.5.20110702svn
- Added new BRs
- Update existing patch acc. the details in #510073

* Sat Jun 25 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.70.5-0.4.20110327svn
- Fix autotool issue (osm2pgsql-configure.patch updated)

* Sun Mar 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.70.5-0.3.20110327svn
- Build with svn checkout detail as version information
- Remove gazetteer stuff, Patch for configure.ac and Makefile.am 
- Updated to new checkout

* Tue Nov 23 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.2.20101124svn
- Typo fixed in summary
- Prefix removed 
- Doc updated
- Replaced define

* Wed Aug 18 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20100821svn
- Initial package for Fedora
