%global _hardened_build 1

%define tinyproxy_confdir %{_sysconfdir}/tinyproxy
%define tinyproxy_datadir %{_datadir}/tinyproxy
%define tinyproxy_rundir  /run/tinyproxy
%define tinyproxy_logdir  %{_localstatedir}/log/tinyproxy
%define tinyproxy_user    tinyproxy
%define tinyproxy_group   tinyproxy

Name:           tinyproxy
Version:        1.10.0
Release:        14%{?dist}
Summary:        A small, efficient HTTP/SSL proxy daemon

License:        GPLv2+
URL:            https://github.com/tinyproxy/

Source0:        https://github.com/tinyproxy/tinyproxy/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}.service
Source2:        %{name}.conf
Source3:        %{name}.logrotate
Source4:        %{name}.tmpfiles

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  asciidoc
BuildRequires:  systemd

%description
tinyproxy is a small, efficient HTTP/SSL proxy daemon that is very useful in a
small network setting, where a larger proxy like Squid would either be too
resource intensive, or a security risk.  

%prep
%setup -q


%build
%configure --sysconfdir=%{_sysconfdir} \
    --enable-reverse \
    --enable-transparent 

make LDFLAGS="%{?__global_ldflags}" CFLAGS="-DNDEBUG $RPM_OPT_FLAGS" %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{tinyproxy_confdir}/%{name}.conf
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -p -D -m 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%{__install} -p -d -m 0700 %{buildroot}%{tinyproxy_rundir}
%{__install} -p -d -m 0700 %{buildroot}%{tinyproxy_logdir}


%pre
if [ $1 == 1 ]; then
    %{_sbindir}/useradd -c "tinyproxy user" -s /bin/false -r -d %{tinyproxy_rundir} %{tinyproxy_user} 2>/dev/null || :
fi


%post
/bin/systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf
%systemd_post %{name}.service
    

%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service
 


%files
%doc AUTHORS COPYING README README.md NEWS docs/*.txt
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8.gz
%{_mandir}/man5/%{name}.conf.5.gz
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{tinyproxy_datadir}
%dir %{tinyproxy_confdir}
%ghost %dir %{tinyproxy_rundir}
%dir %{tinyproxy_logdir}
%config(noreplace) %{tinyproxy_confdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0700,%{tinyproxy_user},%{tinyproxy_group}) %ghost %dir %{tinyproxy_rundir}
%attr(0700,%{tinyproxy_user},%{tinyproxy_group}) %dir %{tinyproxy_logdir}

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.10.0-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Michael Adam <obnox@samba.org> - 1.10.0-2
- Rebuild rawhide to stay ahead of f29

* Mon Sep 03 2018 Michael Adam <obnox@samba.org> - 1.10.0-1
- Update to the new upstream stable version 1.10

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Michael Adam <obnox@samba.org> - 1.8.4-1
- Update to new upstream version 1.8.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 30 2013 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.8.3-2
- fix missing NDEBUG flag (#1011783)

* Sun Sep 08 2013 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.8.3-1
- update to upstream 1.8.3

* Sun Sep 08 2013 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.8.2-7
- apply patch from Tomas Torcz which provides systemd bits, removing SYSV initscript (#760474)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 05 2010 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.8.2-1
- update to upstream 1.8.2

* Tue Apr 06 2010 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.8.1-1
- update to upstream 1.8.1

* Wed Feb 17 2010 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.8.0-1
- update to upstream 1.8.0
- add logrotate configuration

* Sun Oct 11 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.6.5-1
- update to upstream 1.6.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.6.4-3
- add --enable-transparent-proxy option (#466808)

* Sun Aug 24 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.6.4-2
- update to upstream 1.6.4 final

* Sun Jun 22 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.6.4-1
- update to upstream candidate 1.6.4

* Wed Apr 16 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.6.3-2
- fix spec review issues
- fix initscript

* Sun Mar 09 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.6.3-1
- Initial rpm configuration
