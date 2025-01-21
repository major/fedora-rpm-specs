## This macro activates/deactivates debug option
%global without_debug 1
# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-epg-daemon
Version:        1.3.24
Release:        9%{?dist}
Summary:        A daemon to download EPG data from internet and manage it in a mysql database
License:        GPL-1.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-BSD
URL:            https://github.com/horchi/vdr-epg-daemon
Source0:        https://github.com/horchi/vdr-epg-daemon/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# fix: Optimization flags are not honored.
Patch0:         %{name}-makefile.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  libuuid-devel
BuildRequires:  jansson-devel
BuildRequires:  perl-generators
BuildRequires:  zlib-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  imlib2-devel
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  libarchive-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       mariadb-server
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
Requires:       vdr

%description 
epgd is part of the double team epgd+epg2vdr to effectively retrieve,
store and import epg data to vdr. It is designed to handle large amount of
data and pictures in a distributed environment with one epg-server and
many possible vdr-clients - therefore it relays on mysql. 

Though it is possible to use epgd alone with mysql it only makes sense to
use it as back-end to the vdr-plugin epg2vdr. That being said you need to
install, setup and configure mysql, epgd and epg2vdr in order to get a
working environment.

%prep
%autosetup -p1 -n %{name}-%{version}

iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

## Optimization flags in 'Make.config' file
sed -i \
    -e 's|PREFIX      ?= /usr/local|PREFIX       =  %{_prefix}|' \
    -e 's|PLGDEST      = $(PREFIX)/lib/epgd/plugins|PLGDEST      = %{_libdir}/epgd|' \
    -e 's|_PLGDEST     = $(DESTDIR)$(PREFIX)/lib/epgd/plugins|_PLGDEST     = $(DESTDIR)%{_libdir}/epgd|' \
    -e 's|HTTPDEST     = $(DESTDIR)/var/epgd/www|HTTPDEST     = $(DESTDIR)%{vdr_resdir}/epgd|' \
    -e 's|SYSTEMDDEST  = $(DESTDIR)/etc/systemd/system|SYSTEMDDEST  = $(DESTDIR)%{_unitdir}|' \
    -e 's|INIT_SYSTEM  = none|INIT_SYSTEM  = systemd|' \
    -e 's|INIT_AFTER   = mysql.service|INIT_AFTER   = mariadb.service|' \
    -e 's|@@OPTFLAGS | %{optflags}|' \
    Make.config


%if 0%{?without_debug}
sed -i -e 's|DEBUG = 1||' Make.config
%else
##Nothing
%endif

## Optimization flags for ../epglv
sed -i \
    -e 's|@@LIBDIR| %{_libdir}|' \
    -e 's|@@OPTFLAGS | %{optflags}|' \
    -e 's|$(PLGDIR)/$(TARGET);|$(DESTDIR)/$(PLGDIR)/$(TARGET);|' \
    -e 's|$(TARGET) $(PLGDIR);|$(TARGET) $(DESTDIR)/$(PLGDIR);|' \
    epglv/Makefile

##epglv readme file
mv epglv/README epglv/README-epglv

# Add shebang
# Add bash to beginning of file
for file in scripts/epgd-{showmerge,showtimer,conflictsof,showtimerat,showdones}; do
   sed -i '1 i\#!/bin/bash' $file
done

for file in scripts/epgh-{request,login}; do
   sed -i '1 i\#!/bin/bash' $file
done

%build
%make_build

%install
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_libdir}/mariadb/plugin
%make_install

%post
%systemd_post epgd.service
%systemd_post epghttpd.service

%preun
%systemd_preun epgd.service
%systemd_preun epghttpd.service

%postun
%systemd_postun_with_restart epgd.service
%systemd_postun_with_restart epghttpd.service

%files
%doc HISTORY* README* epglv/README* contrib/README.fedora
%license COPYING http/www/font/LICENSE.txt
%{_bindir}/epg*
%dir %{_sysconfdir}/epgd
%config(noreplace) %{_sysconfdir}/epgd/*
%{_unitdir}/epg*.service
%dir %{_libdir}/epgd
%{_libdir}/epgd/libepgd-epgdata.so
%{_libdir}/mariadb/plugin/mysqlepglv.so
%{vdr_resdir}/epgd/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Richard W.M. Jones <rjones@redhat.com> - 1.3.24-8
- Rebuild for Jansson 2.14
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3PYINSQGKQ4BB25NQUI2A2UCGGLAG5ND/)

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.24-7
- Rebuilt for new VDR API version 2.7.2

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.24-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.24-4
- Rebuilt for new VDR API version 2.6.9

* Thu Jul 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.24-3
- Rebuilt for new VDR API version 2.6.8

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.24-2
- Rebuilt for Python 3.13

* Mon May 27 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.24-1
- Update to 1.3.24

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.23-2
- Rebuilt for new VDR API version

* Sat Mar 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.23-1
- Update to 1.3.23

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.21-7
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.21-6
- Rebuilt for new VDR API version

* Thu Sep 28 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.21-5
- Build against the 'mariadb-connector-c-devel' package

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.3.21-3
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 1.3.21-2
- Rebuild fo new imlib2

* Tue Feb 14 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.21-1
- Update to 1.3.21

* Sun Feb 12 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.19-1
- Update to 1.3.19

* Wed Feb 08 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.12-1
- Update to 1.3.12

* Tue Feb 07 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.11-1
- Update to 1.3.11

* Sun Jan 29 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.7-1
- Update to 1.3.7

* Sat Jan 28 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.5-1
- Update to 1.3.5

* Fri Jan 27 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3

* Wed Jan 25 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-2
- Rebuilt for new VDR API version

* Sat Dec 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-1
- Update URL address
- Update to 1.2.4
- Rebuilt for new VDR API version

* Wed Aug 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-4
- Add %%{name}-pthread.patch fix (BZ#2113752)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.3-2
- Rebuilt for Python 3.11

* Tue Apr 26 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Fri Feb 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-3
- Rebuilt for new VDR API version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-1
- Reworking of vdr-epg-daemon-makefile.patch
- Update to 1.2.2

* Tue Jan 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.1.165-7
- Rebuilt for new VDR API version

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.1.165-6
- Rebuilt with OpenSSL 3.0.0

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.165-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.165-4
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.165-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.165-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 01 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.165-1
- Update to 1.1.165

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.163-2
- Rebuilt for new VDR API version

* Tue Aug 18 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.163-1
- Update to 1.1.163

* Tue Jul 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.162-1
- Update to 1.1.162

* Tue Jul 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.161-1
- Update to 1.1.161

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.159-2
- Rebuilt for Python 3.9

* Sun Mar 01 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.159-1
- Update to 1.1.159

* Mon Feb 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.158-1
- Update to 1.1.158

* Tue Feb 18 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.157-1
- Update to 1.1.157

* Wed Feb 12 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.156-1
- Update to 1.1.156

* Tue Feb 11 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.155-1
- Update to 1.1.155

* Mon Feb 10 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.153-1
- Update to 1.1.153

* Sun Feb 09 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.151-1
- Update to 1.1.151

* Wed Jan 29 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.150-1
- Update to 1.1.150

* Sun Dec 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.149-1
- Update to 1.1.149

* Tue Dec 10 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.148-1
- Update to 1.1.148

* Thu Nov 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.147-1
- Update to 1.1.147

* Thu Aug 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.146-7
* - Add if condition for rawhide

* Sat Aug 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.146-6
- Add --embed flag for python 3.8 Support in Makefile

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.146-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.146-4
- Add if condition for f31 with BR python3-devel

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.146-3
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.146-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.146-1
- Update to 1.1.146

* Thu Oct 04 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.145-1
- Update to 1.1.145

* Thu Oct 04 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.144-1
- Update to 1.1.144

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.141-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.141-1
- Update to 1.1.141
- Dropped  %%{name}-mariadb-fix-build.patch

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.140-1
- Update to 1.1.140
- Rebuilt for vdr-2.4.0

* Sun Mar 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.138-1
- Update to 1.1.138

* Sat Mar 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.137-1
- Update to 1.1.137

* Fri Mar 09 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.135-1
- Update to 1.1.135
- remove mysql link
- spec file cleanup

* Thu Feb 15 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.134-1
- Update to 1.1.134

* Sat Feb 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.132-1
- Update to 1.1.132

* Sat Feb 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.131-1
- Update to 1.1.131
- use correct mariadb-API header file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.126-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.126-1
- Update to 1.1.126

* Wed Aug 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.122-2
- Add %%{name}-mariadb-connector-c.patch (BZ#1494106)

* Wed Aug 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.122-1
- Update to 1.1.122

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 1.1.121-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.121-1
- Update to 1.1.121

* Thu Jul 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.120-2
- Add %%{name}-mariadb-fix-build.patch fixes (BZ#1298401).

* Sat Jul 08 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.120-1
- Update to 1.1.120

* Tue Jun 27 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.119-1
- Update to 1.1.119

* Sat Jun 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.118-1
- Update to 1.1.118
- Set INIT_SYSTEM to systemd in Make.config as default

* Sat Jun 10 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.117-1
- Update to 1.1.117

* Fri Jun 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.116-1
- Update to 1.1.116

* Tue May 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.115-1
- Update to 1.1.115

* Fri Mar 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.114-1
- Update to 1.1.114
- Adjust %%{name}-makefile.patch

* Sat Mar 18 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.112-1
- Update to 1.1.112

* Fri Mar 17 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.110-1
- Update to 1.1.110

* Sun Mar 12 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.108-1
- Update to 1.1.108

* Fri Mar 10 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.107-1
- Update to 1.1.107

* Thu Mar 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.106-1
- Update to 1.1.106

* Sat Mar 04 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.103-1
- Update to 1.1.103

* Wed Mar 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.102-1
- Update to 1.1.102
- Dropped %%{name}-systemd.patch

* Mon Feb 27 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.101-1
- Update to 1.1.101
- Add %%{name}-systemd.patch

* Mon Feb 27 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.100-1
- Update to 1.1.100

* Fri Feb 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.99-1
- Update to 1.1.99

* Wed Feb 22 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.97-2
- Changed INIT_AFTER to mariadb.service in Make.config

* Wed Feb 22 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.97-1
- Update to 1.1.97

* Thu Feb 16 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.95-1
- Update to 1.1.95
- Add BR systemd-devel

* Wed Feb 15 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.94-1
- Update to 1.1.94

* Tue Feb 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.93-1
- Update to 1.1.93

* Thu Feb 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.91-1
- Update to 1.1.91

* Wed Feb 08 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.90-1
- Update to 1.1.90

* Tue Feb 07 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.89-1
- Update to 1.1.89

* Wed Jan 25 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.88-1
- Update to 1.1.88

* Wed Jan 25 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.87-1
- Update to 1.1.87

* Fri Jan 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.85-1
- Update to 1.1.85

* Thu Jan 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.84-1
- Update to 1.1.84

* Thu Jan 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.81-1
- Update to 1.1.81

* Wed Jan 18 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.79-1
- Update to 1.1.79

* Sat Jan 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.78-1
- Update to 1.1.78

* Thu Jan 12 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.75-1
- Update to 1.1.75

* Wed Jan 04 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.73-1
- Update to 1.1.73

* Mon Jan 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.72-1
- Update to 1.1.72

* Thu Dec 15 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.70-1
- Update to 1.1.70

* Mon Dec 05 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.66-1
- Update to 1.1.66

* Mon Dec 05 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.65-1
- Update to 1.1.65

* Sun Dec 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.64-1
- Update to 1.1.64

* Sat Dec 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.63-1
- Update to 1.1.63

* Fri Dec 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.62-1
- Update to 1.1.62

* Fri Dec 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.61-1
- Update to 1.1.61

* Thu Dec 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.58-1
- Update to 1.1.58

* Thu Dec 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.57-1
- Update to 1.1.57

* Wed Nov 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.56-1
- Update to 1.1.56

* Wed Nov 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.55-1
- Update to 1.1.55

* Tue Nov 29 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.54-1
- Update to 1.1.54

* Fri Nov 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.53-1
- Update to 1.1.53

* Fri Nov 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.52-1
- Update to 1.1.52

* Thu Nov 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.51-1
- Update to 1.1.51

* Thu Nov 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.50-1
- Update to 1.1.50

* Thu Nov 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.48-1
- Update to 1.1.48

* Mon Nov 21 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.47-1
- Update to 1.1.47

* Sat Nov 19 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.46-1
- Update to 1.1.46

* Sat Nov 19 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.44-1
- Update to 1.1.44

* Mon Nov 14 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.42-1
- Update to 1.1.42

* Thu Nov 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.41-1
- Update to 1.1.41

* Thu Nov 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.40-1
- Update to 1.1.40

* Wed Nov 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.39-1
- Update to 1.1.39

* Wed Nov 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.38-1
- Update to 1.1.38

* Tue Nov 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.37-1
- Update to 1.1.37

* Tue Nov 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.36-1
- Update to 1.1.36

* Tue Nov 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.35-1
- Update to 1.1.35

* Mon Oct 31 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.34-1
- Update to 1.1.34

* Mon Oct 31 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.32-1
- Update to 1.1.32

* Sun Oct 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.31-1
- Update to 1.1.31

* Sat Oct 29 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.30-1
- Update to 1.1.30

* Thu Oct 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.29-1
- Update to 1.1.29

* Wed Oct 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.28-1
- Update to 1.1.28

* Wed Oct 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.27-1
- Update to 1.1.27

* Thu Oct 20 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.24-2
- Rebuild

* Thu Oct 20 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.24-1
- Update to 1.1.24
- Use rpm macros

* Thu Oct 20 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.21-1
- Update to 1.1.21

* Wed Oct 19 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.19-1
- Update to 1.1.19

* Wed Oct 19 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.18-1
- Update to 1.1.18

* Wed Oct 12 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.16-1
- Update to 1.1.16

* Fri Sep 09 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.15-1
- Update to 1.1.15

* Tue Aug 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.14-1
- Update to 1.1.14

* Mon Aug 29 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.13-1
- Update to 1.1.13

* Fri Aug 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.12-1
- Update to 1.1.12

* Tue Jul 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.11-1
- Update to 1.1.11

* Thu Jul 21 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.10-1
- Update to 1.1.10

* Wed Jul 20 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.8-1
- Update to 1.1.8

* Sun Jul 17 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7

* Fri Jul 15 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6

* Fri Jul 08 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2
- Changed makefile patch name  to %%{name}-makefile.patch

* Mon Jul 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Change service name to mariadb.service

* Fri Jun 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.101-1
- Update to 1.0.101

* Wed May 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.54-1
- Update to 1.0.54

* Tue May 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.52-1
- Update to 1.0.52

* Tue May 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.51-1
- Update to 1.0.51

* Mon May 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.49-1
- Update to 1.0.49

* Sat Apr 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.48-1
- Update to 1.0.48

* Fri Apr 29 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.47-1
- Update to 1.0.47

* Thu Apr 28 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.46-1
- Update to 1.0.46

* Wed Apr 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.45-2
- Added missing epghttpd.service file

* Wed Apr 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.45-1
- Update to 1.0.45

* Tue Apr 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.43-1
- Update to 1.0.43

* Sun Apr 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.41-1
- Update to 1.0.41

* Sun Apr 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.40-1
- Update to 1.0.40

* Sun Apr 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.39-1
- Update to 1.0.39

* Sat Apr 23 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.38-1
- Update to 1.0.38

* Fri Apr 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.37-1
- Update to 1.0.37

* Fri Apr 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.36-1
- Update to 1.0.36

* Thu Apr 21 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.34-1
- Update to 1.0.34

* Wed Apr 20 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.31-1
- Update to 1.0.31

* Tue Apr 19 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.27-1
- Update to 1.0.27

* Mon Apr 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.23-1
- Update to 1.0.23

* Wed Mar 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Tue Mar 29 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Sun Mar 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Sun Mar 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sat Mar 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat Mar 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.12-1
- Update to 0.7.12

* Fri Mar 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.11-1
- Update to 0.7.11

* Fri Mar 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.10-1
- Update to 0.7.10

* Fri Mar 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.9-1
- Update to 0.7.9

* Thu Mar 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.8-1
- Update to 0.7.8

* Wed Mar 23 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Fri Mar 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.6.52-1
- Update to 0.6.52

* Sat Mar 12 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.6.36-1
- Update to 0.6.36

* Fri Feb 12 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.6.20-1
- Update to 0.6.20
- Added shebang
- Corrected spelling-error

* Wed Feb 10 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.6.15-1
- Update to 0.6.15

* Fri Jan 29 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.5.32-1
- Update to 0.5.32
- Modified vdr-epg-daemon-makefile.patch
- Added BR python-devel
- Added BR libmicrohttpd-devel
- Added BR vdr-devel

* Wed Oct 28 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-7.20151027git4b79017
- rebuild for new git release
- dropped epgd-tool-fedora.diff

* Mon Oct 26 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-6.20151026gitf50def4
- rebuild for new git release

* Sun Aug 16 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-5.20150810git8887f01
- Mark license files as %%license where available
- added epgd-tool-fedora.diff so mariadb is taken

* Sat Aug 15 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-4.20150810git8887f01
- rebuild for new git release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3.20150202git7927905
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.2-2.20150202git7927905
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-1.20150202git7927905
- Update to 0.2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-8.20140526git006a005
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-7.20140526git006a005
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.2.1-6.20140526git006a005
- rebuild for new git release

* Wed May 21 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.2.1-5.20140520git356b6ac
- rebuild for new git release

* Thu May 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.2.1-4.20140515git44e364a
- rebuild for new git release

* Wed May 14 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.2.1-3.20140514gitbef6c18
- rebuild for new git release

* Tue May 13 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.2.1-2.20140512git997069a
- rebuild for new git release

* Sat May 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.2.1-1.20140510gite1d19b8
- rebuild for new git release
- Add BR libjpeg-turbo-devel
- Add BR imlib2-devel
- Add BR libxslt-devel
- Add BR libxml2-devel

* Wed May 07 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.2.0-1.20140507gitd5f1b4d
- rebuild for new git release

* Mon May 05 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-8.20140505gitd7fb6ca
- removed unnecessary BR: mariadb-server
- added mariadb-server to Requires 
- used %%install for installing and fix perm of files from buildroot
- shortened summary text

* Mon May 05 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-7.20140505gitd7fb6ca
- added macro for activate/deactivate debug option
- optflags settings
- added epglv README
- used 'cp -p' rather than 'mv' for copying files from buildroot

* Mon May 05 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-6.20140505gitd7fb6ca
- rebuild for new git release
- replaced hardlinks by macro in %%prep section
- Fixed the License tag
- added %%dir %%{_libdir}/epgd because it's owned by the package
- added BR mariadb-server
- added BR systemd-units
- added comment about upstream patch
- added fedora optflags to Make.config

* Sat May 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-5.20140428giteb7f12a
- fixed description

* Thu May 01 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-4.20140428giteb7f12a
- added patch for epgd-tool.diff

* Mon Apr 28 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-3.20140428giteb7f12a
- rebuild for new git release

* Fri Apr 25 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-2.20140424gita9d880b
- added missing epgd binary
- removed vdr-devel dependencies
- placed libepg in %%{_libdir}

* Thu Apr 24 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-1.20140424gita9d880b
- rebuild for initial release
