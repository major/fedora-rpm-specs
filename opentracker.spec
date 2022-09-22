%global snapver 20210823

Name:             opentracker
Version:          0
Release:          0.2.%{snapver}cvs%{?dist}
Summary:          BitTorrent Tracker

License:          Beerware
URL:              http://erdgeist.org/arts/software/opentracker/
# cvs -d:pserver:anoncvs@cvs.erdgeist.org:/home/cvsroot co -D "2016-07-28" -d opentracker-%%{snapver} opentracker
# tar cjf opentracker-%%{snapver}.tar.bz2 opentracker-%%{snapver}
Source0:         %{name}-%{snapver}.tar.bz2
Source1:          %{name}-ipv4.service
Source2:          %{name}-ipv6.service
Source3:          %{name}.sysconfig

#Patch0:           %{name}-0-Makefile.patch
Patch1:           %{name}-0-daemon.patch
Patch2:           %{name}-0-conf.patch


BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libowfat-static
BuildRequires:	zlib-devel
BuildRequires:	systemd
Requires(pre):	shadow-utils

%description
opentracker is a open and free BitTorrent tracker project. It aims for minimal
resource usage.

%package          common
Summary:          Common-Files for the BitTorrent-Tracker
BuildArch:        noarch

%description common
Filesystem-package which provides the root-dir.


%package          ipv4
Summary:          BitTorrent Tracker using ipv4
Requires:         %{name}-common


%description ipv4
opentracker is a open and free BitTorrent tracker project. It aims for minimal
resource usage.
This package provides IPv4 capability.


%package          ipv6
Summary:          BitTorrent Tracker using ipv6
Requires:         %{name}-common


%description ipv6
opentracker is a open and free BitTorrent tracker project. It aims for minimal
resource usage.
This package provides IPv6 capability.


%prep
%setup -q -n %{name}-%{snapver}

#%patch0 -p1
%patch1 -p1
%patch2 -p1


%build

sed -i 's|INPUTCONFFILEHERE|%{_sysconfdir}/%{name}/%{name}-ipv4.conf|g' \
       opentracker.c

sed -i 's|INPUTINCLUDEDIRHERE|%{_includedir}|g' \
       Makefile

CFLAGS="%{optflags}" make %{name} %{?_smp_mflags}
mv %{name} %{name}-ipv4

make clean

sed -e 's|#FEATURES+=-DWANT_V6|FEATURES+=-DWANT_V6|g' \
    -i Makefile

sed -i 's|%{_sysconfdir}/%{name}/%{name}-ipv4.conf|%{_sysconfdir}/%{name}/%{name}-ipv6.conf|g' \
       opentracker.c

CFLAGS="%{optflags}" make %{name} %{?_smp_mflags}
mv %{name} %{name}-ipv6


%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}/
install -dm0755 %{buildroot}/var/%{name}

# ipv4
install -Dpm0755 %{name}-ipv4 \
        %{buildroot}%{_bindir}/
install -Dpm0644 %{name}.conf.sample \
        %{buildroot}%{_sysconfdir}/%{name}/%{name}-ipv4.conf
install -Dpm0755 %{SOURCE1} \
        %{buildroot}%{_unitdir}/%{name}-ipv4.service
install -Dpm0644 %{SOURCE3} \
        %{buildroot}%{_sysconfdir}/sysconfig/%{name}-ipv4

# ipv6
install -Dpm0755 %{name}-ipv6 \
        %{buildroot}%{_bindir}/
install -Dpm0644 %{name}.conf.sample \
        %{buildroot}%{_sysconfdir}/%{name}/%{name}-ipv6.conf
install -Dpm0755 %{SOURCE2} \
        %{buildroot}%{_unitdir}/%{name}-ipv6.service
install -Dpm0644 %{SOURCE3} \
        %{buildroot}%{_sysconfdir}/sysconfig/%{name}-ipv6


%pre common
getent group %{name}  > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd  -r -g %{name} -d / -s /sbin/nologin -c "Opentracker User" %{name}
exit 0


%post ipv4
%systemd_post opentracker-ipv4.service


%post ipv6
%systemd_post opentracker-ipv6.service


%preun ipv4
%systemd_preun opentracker-ipv4.service

%preun ipv6
%systemd_preun opentracker-ipv6.service

%postun ipv4
%systemd_postun_with_restart opentracker-ipv4.service

%postun ipv6
%systemd_postun_with_restart opentracker-ipv6.service



%files common
%defattr(-,root,opentracker,-)
%dir %{_sysconfdir}/%{name}/
%dir /var/%{name}/

%files ipv4
%doc README
%{_bindir}/%{name}-ipv4
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-ipv4.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-ipv4
%{_unitdir}/opentracker-ipv4.service


%files ipv6
%doc README
%{_bindir}/%{name}-ipv6
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-ipv6.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-ipv6
%{_unitdir}/opentracker-ipv6.service


# thx to Romain Wartel and Matt Domsch and Robert Scheck for the assistance in the review process.  
%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20210823cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Luis Bazan <lbazan@fedoraproject.org> - 0.0.1.20210823cvs
- New upstream version

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0-0.23.20160728cvs
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20160728cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 28 2016 Kevin Fenzi <kevin@scrye.com> - 0.0.12.20160728cvs
- Update to 20160728 snapshot
- Switch to systemd unit files

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20101114cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20101114cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20101114cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20101114cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20101114cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20101114cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20101114cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20101114cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar 11 2011 Simon Wesp <cassmodiah@fedoraproject.org> - 0-0.3.20101114cvs
- Adhere to Static Library Packaging Guidelines RHBZ#678857

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20101114cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Simon Wesp <cassmodiah@fedoraproject.org> - 0-0.1.20101114cvs
- Initial import to the fedora package collection
