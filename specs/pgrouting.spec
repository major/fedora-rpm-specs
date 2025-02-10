Name:          pgrouting
Version:       3.7.2
Release:       1%{?dist}
Summary:       Provides routing functionality to PostGIS / PostgreSQL
License:       GPL-2.0-or-later AND BSL-1.0 AND MIT
URL:           https://pgrouting.org
Source:        https://github.com/pgRouting/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: perl-interpreter
BuildRequires: perl-File-Find
BuildRequires: perl-version
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: postgresql-server-devel
BuildRequires: boost-graph
BuildRequires: cmake

Requires:      postgresql-server
Requires:      postgis


%description
pgRouting extends the PostGIS / PostgreSQL geospatial database to provide
geospatial routing functionality.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%cmake -DPOSTGRESQL_PG_CONFIG=%{_bindir}/pg_server_config
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%license BOOST_LICENSE_1_0.txt
%license tools/licences/MIT_license.txt
%license tools/licences/GNU_license.txt
%license tools/licences/CCM_license.txt
%doc CODE_OF_CONDUCT.md NEWS README.md CONTRIBUTING.md
%{_libdir}/pgsql/libpgrouting-%{sub %version 1 3}.so
%{_datadir}/pgsql/extension/pgrouting--*--%{version}.sql
%{_datadir}/pgsql/extension/pgrouting--%{version}.sql
%{_datadir}/pgsql/extension/pgrouting.control

%changelog
* Fri Feb 07 2025 Carlos Rodriguez-Fernandez <carlosrodrifernandez@gmail.com> - 3.7.2-1
- Update to version 3.7.2

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 02 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-1
- Update to version 3.7.0

* Sun Nov 10 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-1
- Update to version 3.6.3

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 06 2024 blinxen <h-k-81@hotmail.com> - 3.6.2-1
- Update to version 3.6.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 blinxen <h-k-81@hotmailcom> - 3.6.1-1
- Renamed to pgrouting

* Thu Jan 11 2024 blinxen <h-k-81@hotmailcom> - 3.6.1-1
- Unretire pgRouting

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 3.1.2-3
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Volker Froehlich <volker27@gmx.at> - 3.1.2-1
- New upstream release
- Add perl-version as BR

* Tue Aug 04 2020 Volker Froehlich <volker27@gmx.at> - 3.1.0-1
- New upstream release

* Sat Aug 01 2020 Volker Froehlich <volker27@gmx.at> - 3.0.2-4
- Use new cmake macros
- Add build dependencies (Perl no longer in buildroot)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Volker Froehlich <volker27@gmx.at> - 3.0.2-1
- New upstream release

* Sun Mar 08 2020 Patrik Novotný <panovotn@redhat.com> - 3.0.0-0.rc1.2
- Require clang and llvm (JIT enabled in PostgreSQL)

* Sun Feb 02 2020 Volker Froehlich <volker27@gmx.at> - 3.0.0-0.rc1.1
- New upstream release
- Add gcc-c++ as a BR
- Remove BR for cgal and gmp, which 3.0 does no longer depend on

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 5 2019 Devrim Gündüz <devrim@gunduz.org> - 2.6.2-3
- Rebuilt for Proj 5.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Volker Froehlich <volker27@gmx.at> - 2.6.2-1
- New upstream release

* Thu Oct 18 2018 Petr Kubat <pkubat@redhat.com> - 2.6.1-2
- rebuild for PostgreSQL 11

* Wed Oct 10 2018 Volker Froehlich <volker27@gmx.at> - 2.6.1-1
- New upstream release

* Mon Sep 24 2018 Volker Froehlich <volker27@gmx.at> - 2.5.4-1
- New upstream release

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 2.5.2-6
- rebuild against postgresql-server-devel (rhbz#1618698)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.5.2-4
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Volker Froehlich <volker27@gmx.at> - 2.5.2-2
- Rebuild for boost

* Sun Nov 12 2017 Volker Froehlich <volker27@gmx.at> - 2.5.2-1
- New upstream release

* Fri Oct 13 2017 Volker Froehlich <volker27@gmx.at> - 2.5.1-1
- New upstream release

* Sat Oct 07 2017 Pavel Raiskup <praiskup@redhat.com> - 2.5.0-2
- rebuild for PostgreSQL 10

* Thu Sep 14 2017 Volker Froehlich <volker27@gmx.at> - 2.5.0-1
- New upstream release
- Update documentation files included

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 2.4.1-4
- Rebuilt for Boost 1.64

* Sun Jun 04 2017 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-3
- Rebuilt for new CGAL

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Mar 24 2017 Volker Froehlich <volker27@gmx.at> - 2.4.1-1
- New upstream release

* Tue Mar 21 2017 Volker Froehlich <volker27@gmx.at> - 2.4.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 2.3.2-2
- Rebuilt for Boost 1.63

* Sat Jan 07 2017 Volker Froehlich <volker27@gmx.at> - 2.3.2-1
- New upstream release

* Sun Dec 18 2016 Volker Froehlich <volker27@gmx.at> - 2.3.1-1
- New upstream release

* Mon Oct 10 2016 Pavel Raiskup <praiskup@redhat.com> - 2.2.3-6
- bump: build in rawhide done too early

* Mon Oct 10 2016 Petr Kubat <pkubat@redhat.com> - 2.2.3-5
- Rebuild for PostgreSQL 9.6.0

* Mon Sep 26 2016 volker27@gmx.at - 2.2.3-4
- Rebuild for cgal

* Sat Jul 30 2016 Volker Froehlich <volker27@gmx.at> - 2.2.3-3
- Solve __throw_bad_alloc on creating the extension
  Thank you, Jonathan Wakely
- Remove obsolete build option

* Thu Jul 28 2016 Volker Froehlich <volker27@gmx.at> - 2.2.3-2
- Fix the build: https://github.com/pgRouting/pgrouting/issues/576

* Mon May 16 2016 Volker Froehlich <volker27@gmx.at> - 2.2.3-1
- New release

* Thu Apr 28 2016 Volker Froehlich <volker27@gmx.at> - 2.2.2-1
- New release

* Tue Apr 19 2016 Volker Froehlich <volker27@gmx.at> - 2.2.1-1
- New release

* Sun Apr 10 2016 Volker Froehlich <volker27@gmx.at> - 2.2.0-1
- New release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 2.1.0-3
- Rebuilt for Boost 1.60

* Fri Jan 08 2016 Pavel Kajaba <pkajaba@redhat.com> - 2.1.0-2
- Rebuild for PostgreSQL 9.5 (rhbz#1296584)

* Fri Sep 18 2015 Volker Froehlich <volker27@gmx.at> - 2.1.0-1
- New release
- Update source URL and add BR for Perl data dumper module

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.0.0-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.0.0-10
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 01 2015 Volker Froehlich <volker27@gmx.at> - 2.0.0-7
- Rebuild for cgal 4.6

* Sat Feb 14 2015 Volker Fröhlich <volker27@gmx.at> - 2.0.0-6
- Require a specific major version for postgresql-server (BZ#1181158)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.0.0-5
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 2.0.0-2
- rebuild for boost 1.55.0

* Sat Sep 28 2013 Volker Fröhlich <volker27@gmx.at> - 2.0.0-1
- New upstream release; drop all patches
- New license is GPLv2+
- New source URL
- Filter private provides
- Add dependency on postgresql-server

* Fri Sep 13 2013 Volker Fröhlich <volker27@gmx.at> - 1.05-7
- Rebuild for PostgreSQL 9.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.05-5
- Rebuild for boost 1.54.0

* Sun Mar 31 2013 Volker Fröhlich <volker27@gmx.at> - 1.05-4
- Link to gmp
- Move most stuff from prep section to patches
- Solve FTBFS (BZ #914327), due to upstream issue 77
- Solve upstream bug 35, issue with NULL geometries

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Volker Fröhlich <volker27@gmx.at> - 1.05-2
- Rebuild for new soname version in CGAL 4.1

* Wed Aug 15 2012 Volker Fröhlich <volker27@gmx.at> - 1.05-1
- Update to 1.05
- Update URL
- Update description
- Correct FSF address
- Retire patch0
- Introduce macros with_gaul and tarname; create conditionals based on the first
- Update flags patch and manually add custom flag
- Replace make macros with the command
- Remove unnecessary BR geos-devel
- Remove unnecessary R postgresql; Postgis takes care of that
- Drop rm for buildroot before install
- Drop ldconfig, because libs are in sub-directory
- Drop version requirements in BRs and Requires.
  All shipped versions are new enough in Fedora
- Enable DD option and added BR CGAL-devel
- Simplify attr and drop defattr in files section

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 14 2010 Viji Nair <viji [AT] fedoraproject DOT org> - 1.03-3
- Fixed patch naming conventions.
- Added backup option for files being patched with suffix.
- Changed the package name from postgresql-pgrouting to pgRouting

* Sun Nov 14 2010 Viji Nair <viji [AT] fedoraproject DOT org> - 1.03-2
- Changed the license to GPLv2+ and Boost.
- Removed the override of CMAKE_INSTALL_PREFIX.
- Removed test for %%{?_lib}.
- Added VERBOSE=1 and %%{?_smp_mflags} for make.
- Patch for removing the preset CFLAGS.
- Removed gcc-c++ from BuildRequires.

* Thu Nov 11 2010 Viji Nair <viji [AT] fedoraproject DOT org> - 1.03-1
- Initial import.
