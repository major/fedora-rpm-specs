%global upstream_tag    8.6.1
%global rpm_version     8.6.1
%global soname 3

# enable the following for intermediate builds
#global gitcommit 7b074becd59cf8c574190e49ce097640a2cfefd7

%if 0%{?gitcommit:1}
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global build_timestamp %(date +"%Y%m%d")
%global gittag .%{build_timestamp}git%{shortcommit}
%endif

Name:		IP2Location
Summary:	Tools for mapping IP address to geolocation information
Version:	%{rpm_version}
Release:	8%{?gittag}%{?dist}
License:	MIT
URL:		https://www.ip2location.com/
%if 0%{?gitcommit:1}
Source0:	https://github.com/chrislim2888/IP2Location-C-Library/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz
%else
Source0:	https://github.com/chrislim2888/IP2Location-C-Library/archive/%{upstream_tag}/%{name}-%{upstream_tag}.tar.gz
%endif

BuildRequires:	libtool
BuildRequires:  perl-generators
BuildRequires:	perl(Math::BigInt)
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires: make

Obsoletes:	libip2location < %{version}
Provides:	libip2location = %{version}
Requires:	%{name}-libs%{_isa} = %{version}-%{release}


%description
ip2location command enables the user to get the country, region, city,
coordinates, ZIP code, time zone, ISP, domain name, connection type,
area code, weather info, mobile carrier, elevation and usage type from any IP
address or hostname. This library has been optimized for speed and memory
utilization. The library contains API to query all IP2Location LITE and
commercial binary databases.

Users can download the latest LITE database from IP2Location web site using e.g.
the included downloader.


%package 	libs
Summary:	C library for mapping IP address to geolocation information
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Recommends:	%{name}%{_isa} = %{version}-%{release}
%endif

%description libs
IP2Location C library enables the user to get the country, region, city,
coordinates, ZIP code, time zone, ISP, domain name, connection type,
area code, weather info, mobile carrier, elevation and usage type from any IP
address or hostname. This library has been optimized for speed and memory
utilization. The library contains API to query all IP2Location LITE and
commercial binary databases.


%package 	devel
Summary:	Development files for the IP2Location library
Requires:	%{name}%{_isa} = %{version}-%{release}

Obsoletes:	libip2location-devel < %{version}
Provides:	libip2location-devel = %{version}


%description 	devel
IP2Location C library enables the user to get the country, region, city,
coordinates, ZIP code, time zone, ISP, domain name, connection type,
area code, weather info, mobile carrier, elevation and usage type from any IP
address or hostname. This library has been optimized for speed and memory
utilization. The library contains API to query all IP2Location LITE and
commercial binary databases.

This package contains the development files for the IP2Location library.


%package 	data-sample
Summary:	Sample data files for the IP2Location library
Requires:	%{name} = %{version}-%{release}

Obsoletes:	ip2location-country < %{version}
Provides:	ip2location-country = %{version}


%description 	data-sample
IP2Location C library enables the user to get the country, region, city,
coordinates, ZIP code, time zone, ISP, domain name, connection type,
area code, weather info, mobile carrier, elevation, usage type, address
type and category from any IP address or hostname.
This library has been optimized for speed and memory utilization. The library
contains API to query all IP2Location LITE and commercial binary databases.

This package contains the sample data files for testing the library.

Latest lite databases can be downloaded from
	https://lite.ip2location.com

Further sample databases can be downloaded from
	https://www.ip2location.com/development-libraries/ip2location/c


%prep
%if 0%{?gitcommit:1}
%setup -q -n IP2Location-C-Library-%{gitcommit}
%else
%setup -q -n IP2Location-C-Library-%{upstream_tag}
%endif

# remove a warning option which break configure on older gcc versions
# (at least gcc version 4.1.2 20080704)
perl -pi -e 's/-Wno-unused-result//' configure.ac


%build
autoreconf -fiv

%configure --disable-static
%make_build COPTS="$RPM_OPT_FLAGS"

# convert CSV to BIN
make -C data convert


%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH make check


%install
%make_install

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

# tools
install -d %{buildroot}%{_datadir}/%{name}/tools
install -pm 0755 tools/download.pl %{buildroot}%{_datadir}/%{name}/tools

# database directory
install -d %{buildroot}%{_datadir}/%{name}/
# note: according to https://www.ip2location.com/development-libraries/ip2location/c
# IPv6 sample file has *.SAMPLE* while IPv4 has *-SAMPLE* in ZIP file
install -p data/IP-COUNTRY.BIN %{buildroot}%{_datadir}/%{name}/IP-COUNTRY-SAMPLE.BIN
install -p data/IPV6-COUNTRY.BIN %{buildroot}%{_datadir}/%{name}/IPV6-COUNTRY.SAMPLE.BIN


%files
%doc AUTHORS ChangeLog README.md NEWS
%{_datadir}/%{name}/tools/
%{_bindir}/ip2location
%{_mandir}/man1/ip2location.1*


%files libs
%license COPYING LICENSE.TXT
%{_libdir}/libIP2Location.so.%{soname}
%{_libdir}/libIP2Location.so.%{soname}.0.0
%dir %{_datadir}/%{name}/


%files devel
%{_includedir}/IP2Loc*.h
%{_libdir}/libIP2Location.so

%doc Developers_Guide.txt


%files data-sample
%attr(644,-,-) %{_datadir}/%{name}/*.BIN


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Remi Collet <remi@remirepo.net> - 8.6.1-1
- update to 8.6.1
- drop patch merged upstream

* Sun Jun 04 2023 Peter Bieringer <pb@bieringer.de> - 8.6.0-7
- reenable "make check" for arch s390x and wait for upstream fix
- add IP2Location-8.6.0-bigendian.patch

* Sun Jun 04 2023 Peter Bieringer <pb@bieringer.de> - 8.6.0-6
- update to 8.6.0
- minor spec file alignment with upstream
- exclude "make check" for arch s390x as it segfaults for unknown reason

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Peter Bieringer <pb@bieringer.de> - 8.4.1-1
- update to 8.4.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Remi Collet <remi@remirepo.net> - 8.4.0-2
- add upstream patch fixing
  https://github.com/chrislim2888/IP2Location-C-Library/issues/47

* Tue May 25 2021 Remi Collet <remi@remirepo.net> - 8.4.0-1
- update to 8.4.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.1+1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Remi Collet <remi@remirepo.net> - 8.3.1+1-1
- update to 8.3.1-1 to fix library version in headers
- fix missing perl dependencies

* Mon Nov  9 2020 Remi Collet <remi@remirepo.net> - 8.3.1-4
- move library in libs subpackage

* Mon Nov 09 2020 Peter Bieringer <pb@bieringer.de> - 8.3.1-3
- update to 8.3.1

* Sat Nov 07 2020 Peter Bieringer <pb@bieringer.de> - 8.3.0-2
- update to commit 7b074becd59cf8c574190e49ce097640a2cfefd7
- add new 'ip2location' binary

* Fri Oct 30 2020 Remi Collet <remi@remirepo.net> - 8.3.0-1
- update to 8.3.0

* Wed Oct 07 2020 Peter Bieringer <pb@bieringer.de> - 8.2.0-12
- update version to 8.2.0 (soname: 3)

* Fri Sep 25 2020 Peter Bieringer <pb@bieringer.de> - 8.1.3-11
- update version to 8.1.3

* Fri Sep 25 2020 Peter Bieringer <pb@bieringer.de> - 8.1.2-11
- update version to 8.1.2 (soname: 2)

* Thu Sep 24 2020 Peter Bieringer <pb@bieringer.de> - 8.0.9-10
- add additional Obsoletes/Provides/BuildRequires

* Tue Sep 15 2020 Peter Bieringer <pb@bieringer.de> - 8.0.9-8
- subpackage data-sample: add suffix "SAMPLE" to included BIN files, fix file permissions
- use latest sources, git commit 6e49424dfc998856fa790df498bf77520e72ca28

* Fri Sep 11 2020 Peter Bieringer <pb@bieringer.de> - 8.0.9-7
- use latest sources, git commit 9a987645663b2e13191072df9d8866bf65bc85f5
- add subpackage data-sample including the generated BIN files

* Tue Sep 08 2020 Peter Bieringer <pb@bieringer.de> - 8.0.9-6
- add patch to sync with upstream
- add patch to make rpmlint happy

* Fri Aug 28 2020 Peter Bieringer <pb@bieringer.de>
- fix spec file according to BZ#1873302

* Sat Oct  5 2019 Peter Bieringer <pb@bieringer.de> - 8.0.9-5
- update version to 8.0.9

* Sun Feb 26 2017 Peter Bieringer <pb@bieringer.de> - 8.0.4-5
- update to 8.0.4
- add some fixes related to move to github
- integrate download.pl into github tree

* Sun May 03 2015 Peter Bieringer <pb@bieringer.de> - 7.0.1-4
- add Developers_Guide.txt to doc/devel
- change group of base package to System Environment/Libraries
- add check/post/postuninstall section
- migrate some settings from http://www.ip2location.com/rpm/ip2location-c.spec

* Fri Apr 17 2015 Peter Bieringer <pb@bieringer.de> - 7.0.1-3
- update to 7.0.1
- add ip2location-downloader/download.pl

* Thu Apr 16 2015 Peter Bieringer <pb@bieringer.de>
- update to 7.0.0

* Sat Jan 24 2015 Peter Bieringer <pb@bieringer.de>
- run "make clean" before "make" cleanup i368 objects containend in source code

* Sun Jul 20 2014 Peter Bieringer <pb@bieringer.de>
- adjustments for 6.0.2

* Thu Aug 22 2013 Peter Bieringer <pb@bieringer.de>
- adjustments for 6.0.1, update license version
- some RPM fixes

* Sun May 15 2011 Oden Eriksson <oeriksson@mandriva.com> 4.0.2-1mdv2011.0
+ Revision: 674881
- import ip2location

* Sun May 15 2011 Oden Eriksson <oeriksson@mandriva.com> 4.0.2-1mdv2010.2
- initial Mandriva package
