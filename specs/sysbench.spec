Summary:       System performance benchmark
Name:          sysbench
Version:       1.0.20
Release:       17%{?dist}
License:       GPL-2.0-or-later
URL:           https://github.com/akopytov/sysbench/
Source0:       https://github.com/akopytov/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/akopytov/sysbench/pull/379
Patch0:        sysbench-1.0.20-python3.patch
# egrep is deprecated, use grep -E instead in order to fix build on F38+
Patch1:        sysbench-1.0.20-fix_deprecated_egrep_call.patch

BuildRequires: make
BuildRequires: automake
BuildRequires: ck-devel
BuildRequires: docbook-style-xsl
BuildRequires: libaio-devel
BuildRequires: libtool
BuildRequires: libxslt
BuildRequires: luajit-devel
BuildRequires: mariadb-connector-c-devel
BuildRequires: libpq-devel
# Tests
BuildRequires: /usr/bin/cram
BuildRequires: python3

# luajit is needed and is not available for ppc64le and s390x
# Use the same arches as luajit.
# On F35+ and EL9+, luajit doesn't support s390x and ppc64le anymore
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9
ExclusiveArch:  %{arm} %{ix86} x86_64 %{mips} aarch64
%else
ExclusiveArch:  %{arm} %{ix86} x86_64 %{mips} aarch64 ppc64le s390x
%endif


%description
SysBench is a modular, cross-platform and multi-threaded benchmark
tool for evaluating OS parameters that are important for a system
running a database under intensive load.

The idea of this benchmark suite is to quickly get an impression about
system performance without setting up complex database benchmarks or
even without installing a database at all. Current features allow to
test the following system parameters:
- file I/O performance
- scheduler performance
- memory allocation and transfer speed
- POSIX threads implementation performance
- database server performance (OLTP benchmark)

Primarily written for MySQL server benchmarking, SysBench will be
further extended to support multiple database backends, distributed
benchmarks and third-party plug-in modules.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
rm -r third_party/luajit/luajit/
rm -r third_party/concurrency_kit/ck/
rm -r third_party/cram/


%build
export CFLAGS="%{optflags}"
autoreconf -vif
%configure --with-mysql \
           --with-pgsql \
           --with-system-ck \
           --with-system-luajit \
           --without-gcc-arch

%make_build

%install
%make_install
mv %{buildroot}%{_docdir}/sysbench/manual.html .

%check
cd tests
./test_run.sh

%files
%license COPYING
%doc ChangeLog README.md manual.html
%{_bindir}/*
%{_datadir}/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.20-16
- Drop EOL releases, fix luajit arches

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.20-15
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Xavier Bachelot <xavier@bachelot.org> 1.0.20-11
- Fix build on EL9
- egrep is deprecated, use grep -E instead in order to fix build on F38+
- Drop conditionals for EL6

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Andreas Schneider <asn@redhat.com> - 1.0.26-7
- Do not build on ppc64le and s390x (no luajit available)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.20-5
- Enable on ppc64le and s390x
- Add upstream patch for python3 in testsuite

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.0.20-4
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 29 2020 Xavier Bachelot <xavier@bachelot.org> 1.0.20-1
- Update to 1.0.20 (RHBZ#1827878)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Xavier Bachelot <xavier@bachelot.org> 1.0.17-2
- Fix EPEL build.
- Clean up conditionals around BuildRequires.

* Fri Mar 15 2019 Xavier Bachelot <xavier@bachelot.org> 1.0.17-1
- Update to 1.0.17 (RHBZ#1689249).

* Tue Feb 12 2019 Xavier Bachelot <xavier@bachelot.org> 1.0.16-1
- Update to 1.0.16.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Xavier Bachelot <xavier@bachelot.org> 1.0.15-3
- Remove opt_report_interval test for armv7hl (RHBZ#1606468).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Xavier Bachelot <xavier@bachelot.org> 1.0.15-1
- Update to 1.0.15 (RHBZ#1597935).

* Mon Apr 09 2018 Xavier Bachelot <xavier@bachelot.org> 1.0.14-1
- Update to 1.0.14 (RHBZ#1547329).

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Xavier Bachelot <xavier@bachelot.org> 1.0.12-1
- Update to 1.0.12 (RHBZ#1535455).

* Tue Dec 12 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.11-1
- Update to 1.0.11 (RHBZ#1524754).

* Thu Nov 02 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.10-1
- Update to 1.0.10 (RHBZ#1508249).
- Build against mariadb-connector-c for Fedora 27+ (RHBZ#1493697).

* Mon Sep 18 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.9-2
- Add patch to fix build against mariadb 10.2.8.

* Wed Sep 06 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.9-1
- Update to 1.0.9 (RHBZ#1488694).
- Drop upstreamed patch.
- Drop Group: tag.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.8-2
- Add patch from Honza Horak to fix build against mariadb 10.2 (RHBZ#1470540).

* Wed Jul 05 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.8-1
- Update to 1.0.8.
- Fix creation and installation of manual.html file.
- Sort BuildRequires.

* Tue May 16 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.7-1
- Update to 1.0.7.

* Sun Apr 16 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.6-1
- Update to 1.0.6.
- Use bundled cram for EL6.
- Tweak conditionals.
- Remove --with-gcc-arch=native hack on arm.

* Fri Apr 07 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.5-1
- Update to 1.0.5.
- Fix conditional around ExclusiveArch.
- Restore EL6 support, luajit (RHBZ#1432377) and python-cram (RHBZ#1432378) are
  currently missing though.

* Mon Mar 13 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.4-2
- Don't build aarch64 on el7.

* Mon Mar 13 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.4-1
- Fix build for i686.
- Drop bundled cram.

* Wed Mar 08 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.3-1
- Update to 1.0.3 (RHBZ#1424670).
- Restrict arches to the same ones as luajit.
- Add --with-gcc-arch=native to configure for %%{arm} and aarch64.
- Ignore test suite results for aarch64, it segfaults in koji.

* Sat Feb 25 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.2-2
- Run test suite.

* Sat Feb 25 2017 Xavier Bachelot <xavier@bachelot.org> 1.0.2-1
- Update to 1.0.2 (RHBZ#1424670).

* Sun Feb 12 2017 Honza Horak <hhorak@redhat.com> - 1.0.0-1
- Update to the first proper release 1.0.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 04 2014 Xavier Bachelot <xavier@bachelot.org> 0.4.12-12
- Modernize specfile.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 06 2011 Xavier Bachelot <xavier@bachelot.org> 0.4.12-5
- Add BR: libaio-devel (rhbz#735882).

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 0.4.12-4
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 24 2010 Xavier Bachelot <xavier@bachelot.org> 0.4.12-2
- Rebuild against new mysql.

* Wed Jul 07 2010 Xavier Bachelot <xavier@bachelot.org> 0.4.12-1
- Update to 0.4.12.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.4.10-5
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Xavier Bachelot <xavier@bachelot.org> 0.4.10-3
- License is GPLv2+, not GPLv2.

* Sat Mar 14 2009 Xavier Bachelot <xavier@bachelot.org> 0.4.10-2
- Make postgres support optional, the version in rhel4 is too old.
- Drop TODO and manual.html from %%doc, they are empty.

* Thu Mar 05 2009 Xavier Bachelot <xavier@bachelot.org> 0.4.10-1
- Adapt original spec file taken from PLD.
