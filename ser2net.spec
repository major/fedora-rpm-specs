Name:		ser2net
Summary: 	Proxy that allows tcp connections to serial ports
Version:	3.5
Release:	12%{?dist}
License:	GPLv2+
Source0:	http://download.sourceforge.net/ser2net/%{name}-%{version}.tar.gz
Source1:	%{name}.service
URL:		http://ser2net.sourceforge.net/
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	systemd-units
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
ser2net provides a way for a user to connect from a network connection to a 
serial port. It provides all the serial port setup, a configuration file to 
configure the ports, a control login for modifying port parameters, 
monitoring ports, and controlling ports.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_sysconfdir}
install -m0644 ser2net.conf %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_unitdir}
install %{SOURCE1} %{buildroot}%{_unitdir}

%post
%systemd_post ser2net.service

%preun
%systemd_preun ser2net.service

%postun
%systemd_postun_with_restart ser2net.service 

%triggerun -- ser2net < 2.7-3
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply ser2net
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save ser2net >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del ser2net >/dev/null 2>&1 || :
/bin/systemctl try-restart ser2net.service >/dev/null 2>&1 || :

%files
%doc COPYING ChangeLog AUTHORS README
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5-9
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Tom Callaway <spot@fedoraproject.org> - 3.5-1
- update to 3.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 2.9.1-4
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug  8 2013 Tom Callaway <spot@fedoraproject.org> - 2.9.1-1
- update to 2.9.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar  1 2013 Tom Callaway <spot@fedoraproject.org> - 2.8-1
- update to 2.8 final

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-0.4.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Tom Callaway <spot@fedoraproject.org> - 2.8-0.3.rc2
- update scriptlets for new systemd macros

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-0.2.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Tom Callaway <spot@fedoraproject.org> - 2.8-0.1.rc2
- 2.8-rc2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 06 2011 Tom Callaway <spot@fedoraproject.org> - 2.7-4
- fixed scriptlets

* Wed Feb 09 2011 Tom Callaway <tcallawa@redhat.com> - 2.7-3
- systemd enablement
- rawhide spec cleanup

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.7-1
- Update to 2.7

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6-1
- update to 2.6

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.5-1
- update to 2.5
- fix initscript to not be on by default
- add try-restart

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.4-2.1
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.4-2
- rebuild for BuildID

* Thu Aug  2 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.4-1
- bump to 2.4

* Wed Oct 18 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.3-3
- fix typo

* Wed Oct  4 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.3-2
- fix initscript handling

* Fri Jul 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.3-1
- Initial package for Fedora Extras
