%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}


Name:           mod_qos
Version:        11.75
Release:        4%{?dist}
Summary:        Quality of service module for Apache

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://opensource.adnovum.ch/mod_qos/
Source0:        http://downloads.sourceforge.net/project/mod-qos/%{name}-%{version}.tar.gz
Source1:        10-mod_qos.conf

BuildRequires: automake
BuildRequires: gcc
BuildRequires: httpd-devel
BuildRequires: libpng-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pcre2-devel

Requires: httpd-mmn = %{_httpd_mmn}

%description
The mod_qos module may be used to determine which requests should be served and 
which shouldn't in order to avoid resource over-subscription. The module 
collects different attributes such as the request URL, HTTP request and response
headers, the IP source address, the HTTP response code, history data (based on 
user session and source IP address), the number of concurrent requests to the 
server (total or requests having similar attributes), the number of concurrent 
TCP connections (total or from a single source IP), and so forth.

Counteractive measures to enforce the defined rules are: request blocking, 
dynamic timeout adjustment, request delay, response throttling, and dropping of 
TCP connections. 


%prep
%autosetup 

%build
%{_httpd_apxs} -Wc,"%{optflags}" -c apache2/mod_qos.c -lcrypto

# Tools building
# Need to fix the binaries

pushd .
cd tools/
aclocal
automake --add-missing
%configure
make %{?_smp_mflags}
popd


%install
install -Dpm 755 apache2/.libs/mod_qos.so \
    $RPM_BUILD_ROOT%{_libdir}/httpd/modules/mod_qos.so

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
    # 2.4-style
    install -Dpm 644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}/10-mod_qos.conf
%else
    # 2.2-style
    install -Dpm 644 %{SOURCE1} %{buildroot}%{_httpd_confdir}/mod_qos.conf
%endif

cd tools/
%make_install
install -d %{buildroot}%{_mandir}/man1/
install -Dpm 644 man1/*  %{buildroot}%{_mandir}/man1/



%files
%{_bindir}/*
%{_mandir}/man1/*
%doc doc README.TXT
%{_libdir}/httpd/modules/mod_qos.so
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
    # 2.4-style
    %config(noreplace)  %{_httpd_modconfdir}/10-mod_qos.conf
%else
    # 2.2-style
    %config(noreplace) %{_httpd_confdir}/mod_qos.conf
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 11.75-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 19 2024 Neil Hanlon <neil@shrug.pw> - 11.75-1
- Update to 11.75 (#2276050)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 09 2023 Neil Hanlon <neil@shrug.pw> - 11.74-2
- don't link against pcre-1
- remove httpd conditionals (el6 cruft)

* Mon Oct 09 2023 Neil Hanlon <neil@shrug.pw> - 11.74-1
- Update to 11.74

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 23 2022 athmane - 11.70-1
- Update to 11.70 (rhbz #2020776)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 17 2021 Othman Madjoudj <athmane@fedoraproject.org> - 11.68-1
- Update to 11.68 (rhbz #1991139)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 11.66-5
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Othman Madjoudj <athmane@fedoraproject.org> - 11.66-1
- Update to 11.66 (rhbz #1838788)

* Sun Mar 08 2020 Othman Madjoudj <athmane@fedoraproject.org> - 11.65-1
- Update to 11.65 (rhbz #1783661)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Othman Madjoudj <athmane@fedoraproject.org> - 11.64-1
- Update to 11.64 (rhbz #1686127)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 11.55-1
- Update to 11.55 (rhbz #1596429)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 11.54-1
- Update to 11.54 (rhbz #1564114)

* Mon Mar 26 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 11.53-1
- Update to 11.53 (rhbz #1560122)

* Sun Mar 11 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 11.52-1
- Update to 11.52 (rhbz #1550754)

* Sun Mar 11 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 1550754-1
- Update to 1550754 (rhbz #11.52)

* Sun Feb 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 11.51-1
- Update to 11.51 (rhbz #1544061)
- Add gcc and make as BR (minimal buildroot change)
- Remove deprecated bits

* Thu Feb 08 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 11.47-1
- Update to 11.47 (rhbz #1542474)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 11.46-1
- Update to 11.46 (rhbz #1536898)

* Sat Dec 16 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 11.45-1
- Update to 11.45 (rhbz #1525284)

* Wed Nov 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 11.44-1
- Update to 11.44 (rhbz #1508207)

* Sun Sep 24 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 11.43-1
- Update to 11.43 (rhbz #1494763)

* Sat Sep 16 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 11.42b-1
- Update to 11.42b (rhbz #1491067)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 11.41-1
- Update to 11.41

* Sun Jul 02 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 11.40-1
- Update to 11.40

* Fri Mar 24 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 11.39-1
- Update to the new release

* Tue Mar 07 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 11.37-1
- Update to 11.37
- Remove upstreamed patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.36-2
- Add a patch to fix rawhide build (wrong .h)

* Sat Dec 03 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.36-1
- Update to 11.36

* Thu Nov 24 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.34-1
- Update to 11.34

* Tue Nov 01 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.32-1
- Update to 11.32

* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.31-1
- Update to 11.31

* Sat Jun 25 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.30-1
- Update to 11.30

* Fri Jun 10 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.29-1
- Update to 11.29

* Fri Apr 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.26-1
- Update to 11.26

* Tue Apr 12 2016 Athmane Madjoudj <athmane@fedoraproject.org> 11.24-1
- Update to 11.24

* Fri Feb 26 2016 Athmane Madjoudj <athmane@fedoraproject.org> 11.22-1
- Update to 11.22

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Athmane Madjoudj <athmane@fedoraproject.org> 11.21-1
- Update to 11.21

* Sat Jan 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> 11.19-1
- Update to 11.19

* Fri Nov 20 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.18-1
- Update to 11.18
- Enable all tools

* Fri Oct 02 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.17-1
- Update to 11.17

* Sat Aug 15 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.16-1
- Update to 11.16

* Mon Jul 20 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.15-1
- Update to 11.15

* Sat Jun 20 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.14-1
- Update to 11.14

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.13-1
- Update to 11.13

* Thu Mar 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.12-1
- Update to 11.12

* Sat Feb 21 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.11-1
- Update to 11.11

* Fri Jan 30 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.9-1
- Update to 11.9

* Thu Nov 27 2014 Athmane Madjoudj <athmane@fedoraproject.org> 11.7-1
- Update to 11.7

* Fri Nov 14 2014  Athmane Madjoudj <athmane@fedoraproject.org> 11.6-1
- Update to 11.6

* Fri Oct 10 2014 Athmane Madjoudj <athmane@fedoraproject.org> 11.5-1
- Update to 11.5
- Include the tools
- Exclude some utilities util they get audited because of suid/guid related calls
- Follow the new httpd 2.4.x module packaging guidelines.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 10.24-2
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Nov  2 2013 Christof Damian <christof@damian.net> - 10.24-1
- upstream 10.24

* Thu Jul 25 2013 Christof Damian <christof@damian.net> - 10.16-1
- upstream 10.16

* Sat Apr 27 2013 Christof Damian <christof@damian.net> - 10.15-1
- upstream 10.15

* Sat Feb 23 2013 Christof Damian <christof@damian.net> - 10.13-4
- add crypto requirement

* Tue Jan  8 2013 Christof Damian <christof@damian.net> - 10.13-3
- update build requires

* Tue Jan  8 2013 Christof Damian <christof@damian.net> - 10.13-2
- add conf file

* Tue Jan  8 2013 Christof Damian <christof@damian.net> - 10.13-1
- initial package

