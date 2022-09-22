Name:              ipwatchd
Version:           1.3.0
Release:           11%{?dist}
Summary:           IP conflict detection tool

License:           GPLv2
URL:               http://ipwatchd.sf.net
Source0:           http://sourceforge.net/projects/ipwatchd/files/ipwatchd/%{version}/ipwatchd-%{version}.tar.gz
Patch0:            ipwatchd-service.patch

BuildRequires:     gcc, libpcap-devel, libnet-devel, systemd
BuildRequires: make

Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
IPwatchD is a simple daemon that analyses all incoming ARP packets in order 
to detect IP conflicts on Linux. It can be configured to listen on one or 
more interfaces (alias interfaces are also supported) in active or passive 
mode. In active mode IPwatchD protects your host before IP takeover by 
answering Gratuitous ARP requests received from conflicting system. 
In passive mode it just records information about conflict through standard 
syslog interface.

%prep
%setup -q
%patch0 -p1

%build
make -C src %{?_smp_mflags} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%install
make -C src install DESTDIR=%{buildroot}

%post
%systemd_post ipwatchd.service

%preun
%systemd_preun ipwatchd.service

%postun
%systemd_postun_with_restart ipwatchd.service

%files
%config(noreplace) %{_sysconfdir}/ipwatchd.conf
%{_sbindir}/ipwatchd
%{_sbindir}/ipwatchd-script
%{_mandir}/man8/ipwatchd.8*
%{_mandir}/man5/ipwatchd.conf.5*
%{_mandir}/man1/ipwatchd-script.1*
%{_unitdir}/ipwatchd.service
%doc LICENSE

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.0-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 Jaroslav Imrich <jariq@jariq.sk> 1.3.0-1
- Updated to upstream release 1.3.0

* Fri Jul 20 2018 Jaroslav Imrich <jariq@jariq.sk> 1.2.1-13
- Added gcc to BuildRequires (#1604382)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 09 2013 Jaroslav Imrich <jariq@jariq.sk> 1.2.1-3
- Passing optflags to compiler during build
- Added LICENSE to the files section
- Other minor spec improvements

* Wed Oct 09 2013 Jaroslav Imrich <jariq@jariq.sk> 1.2.1-2
- Removed Group tag as it is no longer required
- Using version macro in URL tag
- Requires systemd instead of systemd-units
- Changed systemd service type to forking (ipwatchd-systemd.patch)

* Sun Jul 31 2011 Jaroslav Imrich <jariq@jariq.sk> 1.2.1-1
- Initial release
