%{!?username:%global username	ip-sentinel}
%global service		ip-sentinel
%global homedir		%{_var}/lib/ip-sentinel

Summary:	Tool to prevent unauthorized usage of IP addresses
Name:		ip-sentinel
Version:	0.12
Release:	1932%{?dist}
License:	GPL-2.0-only
URL:		http://www.nongnu.org/ip-sentinel/
Source0:	http://savannah.nongnu.org/download/ip-sentinel/%{name}-%{version}.tar.bz2
Source1:	http://savannah.nongnu.org/download/ip-sentinel/%{name}-%{version}.tar.bz2.sig
Source2:	ip-sentinel.service
Patch0:		ip-sentinel-0.12-pidfile.patch
Patch1:		ip-sentinel-0.12-glibc.patch
Provides:	user(%username) = 1
Provides:	group(%username) = 1
BuildRequires:  gcc
BuildRequires:	which systemd
BuildRequires: make
Obsoletes: ip-sentinel-sysvinit < %{version}-%{release}
Provides: ip-sentinel-sysvinit = %{version}-%{release}
Obsoletes: ip-sentinel-minit < %{version}-%{release}
Provides: ip-sentinel-minit = %{version}-%{release}
Obsoletes: ip-sentinel-upstart < %{version}-%{release}
Provides: ip-sentinel-upstart = %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
IP Sentinel is a tool that tries to prevent unauthorized usage of
IP addresses within an ethernet broadcast domain by answering ARP
requests. After receiving faked replies, requesting parties store
the MAC in their ARP tables and will send future packets to this
invalid MAC, rendering the IP unreachable.


%prep
%setup -q
%patch -P0 -p0 -b .pidfile
%patch -P1 -p0

# Create a sysusers.d config file
cat >ip-sentinel.sysusers.conf <<EOF
u ip-sentinel - 'IP sentinel user' %{homedir} -
EOF

%build
%configure --enable-release \
	   --with-initrddir=%{_initrddir} \
	   --with-username=%username \
           --disable-dietlibc
make %{?_smp_mflags} all


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install-contrib
install -m750 -d $RPM_BUILD_ROOT%homedir
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/minit/
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/ip-sentinel


install -Dpm 755 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/ip-sentinel.service

install -m0644 -D ip-sentinel.sysusers.conf %{buildroot}%{_sysusersdir}/ip-sentinel.conf

%check
make check




%post
%systemd_post ip-sentinel.service

%preun
%systemd_preun ip-sentinel.service

%postun
%systemd_postun_with_restart ip-sentinel.service 

%triggerun -- ip-sentinel-sysvinit < 0.12-1909
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply ip-sentinel
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save ip-sentinel >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del ip-sentinel >/dev/null 2>&1 || :
/bin/systemctl try-restart ip-sentinel.service >/dev/null 2>&1 || :


%files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%{_mandir}/*/*
%{_sbindir}/*
%{_unitdir}/ip-sentinel.service
%{_sysconfdir}/sysconfig/ip-sentinel
%attr(-,root,%username) %homedir
%{_sysusersdir}/ip-sentinel.conf

%changelog
* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.12-1932
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1931
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1928
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1927
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.12-1926
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1925
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1924
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1923
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1922
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.12-1921
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1920
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1919
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1918
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1917
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1916
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1915
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1914
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1913
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1912
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-1910
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Jon Ciesla <limburgher@gmail.com> - 0.12-1909
- Remove unused upstart subpackage.
- Migrate to systemd.

* Wed Oct 14 2015 Adam Jackson <ajax@redhat.com> 0.12-1908
- Drop -minit subpackage, which Requires things not packaged in Fedora.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-1907
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-1906
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-1905
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-1904
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> - 0.12-1903
- Migrate from fedora-usermgmt to guideline scriptlets.

* Thu Feb 28 2013 Jon Ciesla <limburgher@gmail.com> - 0.12-1902
- Spec cleanup.
- Switch from dietlibc to glibc.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-1901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-1900
- conditionalized upstart and disabled it by default

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-1303
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-1302
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-1301
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec  6 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-1300
- updated -upstart to upstart 0.6.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar  1 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-14
- added -upstart subpackage
- renamed -sysv subpackage to -sysvinit to let -upstart win the
  default dependency resolving

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.12-12
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.12-11
- Autorebuild for GCC 4.3

* Thu Jan 18 2007 David Woodhouse <dwmw2@infradead.org> 0.12-10
- rebuilt with PPC support

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.12-9
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-8
- rebuilt

* Sun Jul  9 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-7
- rebuilt with dietlibc-0.30
- use new fedora-usermgmt code
- use %%bcond_* macros

* Mon Feb 20 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-6
- exclude PPC arch because dietlibc is not available there anymore

* Fri Jul  8 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-5
- fixed named of pidfile (reported by Razvan Sandu)

* Wed Jun  8 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-4
- rebuilt

* Wed Jun  8 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-3
- added 'BuildRequires: which'
- do not use dietlibc on non-i386 archs running FC3

* Thu May 19 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-2
- use %%dist instead of %%disttag

* Wed Mar 30 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.12-1
- updated to 0.12

* Thu Aug 19 2004 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.10.2-0
- added support for 'fedora-usermgmt' (enabled with '--with fedora' switch)

* Thu Jun 17 2004 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.10.1-0
- conditionalized building of -minit subpackage

* Wed Jun 16 2004 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.9.2-0
- updated minit filelist
- moved /etc/sysconfig/* files into -sysv subpackage; they are not
  used for 'minit' anymore

* Sat Mar 20 2004 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.9-0
- workaround https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=118773

* Thu Dec  4 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.8-0
- use 'install-contrib'

* Tue Sep  9 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.7-1
- removed more unneeded curlies

* Tue Aug  5 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.6-1
- version 0.6
- added minit support
- removed unneeded curlies

* Thu Jul 17 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.5-2
- removed %%doc attribute from %%mandir-entries

* Thu Jul 10 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.5-1
- moved 'make check' into the %%check section

* Sat May 24 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4-1
- removed dependencies on /sbin/service
- removed packager tag
- create and remove group explicitely

* Wed May 21 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.3-1
- applied fedora.us naming scheme
- cleanups

* Fri Nov 15 2002 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.1-1
- initial build
