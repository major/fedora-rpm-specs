Summary:	Sends fully customized ICMP packets from command line
Name:		sing
Version:	1.1
Release:	25%{?dist}
License:	GPLv2+
URL:		http://www.sourceforge.net/projects/%{name}/
Source:		http://downloads.sourceforge.net/%{name}/SING-%{version}.tgz
Patch0:		sing-1.1-fedora.patch
Patch1:		sing-1.1-suid_log.patch
Patch2:		sing-1.1-sys_errlist.patch
BuildRequires: make
BuildRequires:	gcc, libpcap-devel, libnet10-devel, automake, autoconf

%description
Sing is a little tool that sends fully customized ICMP packets from command
line. The main purpose is to replace/complement the nice ping command with
certain enhancements as:

 - Send fragmented and monster packets > 65534 bytes
 - Send/read spoofed packets
 - Send many ICMP Information types in addition to the echo request type,
   sent by default as address mask request, timestamp, information request,
   router solicitation and router advertisement
 - Send many ICMP error types: redirect, source quench, time exceeded,
   destination unreach and parameter problem
 - Send to host with loose or strict source routing
 - Use little fingerprinting techniques to discover Windows or Solaris boxes
 - Send ICMP packets emulating certain OS: Cisco, Solaris, Linux, Shiva,
   Unix and Windows at the moment

%prep
%setup -q -n SING-%{version}
%patch0 -p1 -b .fedora
%patch1 -p1 -b .sing_suid
%patch2 -p1 -b .sys_errlist

# Rebuilding of configure file is needed for Patch0
autoconf

# Automake can't be run because of missing Makefile.am
cp -f %{_datadir}/automake-*/config.* .

%build
%configure --bindir=%{_sbindir}
%make_build

%install
%make_install

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o LEEME.utf8 LEEME
touch -c -r LEEME LEEME.utf8
mv -f LEEME.utf8 LEEME

%files
%license COPYING
%doc AUTHORS ChangeLog README THANKS
%lang(es) %doc LEEME
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 02 2020 Robert Scheck <robert@fedoraproject.org> 1.1-21
- Replace deprecated sys_errlist array by strerror function

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Robert Scheck <robert@fedoraproject.org> 1.1-1
- Upgrade to 1.1
- Initial spec file for Fedora and Red Hat Enterprise Linux
