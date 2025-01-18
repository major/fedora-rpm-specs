%global _hardened_build 1

%define beanstalkd_user      beanstalkd
%define beanstalkd_group     %{beanstalkd_user}
%define beanstalkd_home      %{_localstatedir}/lib/beanstalkd
%define beanstalkd_binlogdir %{beanstalkd_home}/binlog

Name:           beanstalkd
Version:        1.10
Release:        24%{?dist}
Summary:        A simple, fast work-queue service

License:        MIT
URL:            http://kr.github.io/%{name}/
Source0:        https://github.com/kr/%{name}/archive/v%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysconfig

Patch1:         beanstalkd-1.10-warnings.patch
Patch2:         beanstalkd-1.10-mkdtemp.patch

BuildRequires:  systemd gcc gcc-c++
BuildRequires: make

Requires(pre):    shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
beanstalkd is a simple, fast work-queue service. Its interface is generic,
but was originally designed for reducing the latency of page views in
high-volume web applications by running most time-consuming tasks
asynchronously.


%prep
%autosetup -p1


%build
make LDFLAGS="%{?__global_ldflags}" CFLAGS="%{optflags}" %{?_smp_mflags}


%check
make check


%install
make install PREFIX=%{buildroot}%{_prefix}
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%{__install} -d -m 0755 %{buildroot}%{beanstalkd_home}
%{__install} -d -m 0755 %{buildroot}%{beanstalkd_binlogdir}
%{__install} -d -m 00755 %{buildroot}%{_mandir}/man1
%{__install} -p -m 0644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/


%pre
getent group %{beanstalkd_group} >/dev/null || groupadd -r %{beanstalkd_group}
getent passwd %{beanstalkd_user} >/dev/null || \
    useradd -r -g %{beanstalkd_user} -d %{beanstalkd_home} -s /sbin/nologin \
    -c "beanstalkd user" %{beanstalkd_user}
exit 0


%post
# make the binlog dir after installation, this is so SELinux does not complain
# about the init script creating the binlog directory
# See RhBug 558310
if [ -d %{beanstalkd_home} ]; then
    %{__install} -d %{beanstalkd_binlogdir} -m 0755 \
        -o %{beanstalkd_user} -g %{beanstalkd_user} \
        %{beanstalkd_binlogdir}
fi
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%doc README doc/protocol.txt
%license LICENSE
%{_unitdir}/%{name}.service
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0755,%{beanstalkd_user},%{beanstalkd_group}) %dir %{beanstalkd_home}
%ghost %attr(0755,%{beanstalkd_user},%{beanstalkd_group}) %dir %{beanstalkd_binlogdir}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.10-15
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Nathanael Noblet <nathanael@gnat.ca> - 1.10-9
- Added missing BR gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 16 2017 Neal Gompa <ngompa@datto.com> - 1.10-6
- Small spec improvements
- Drop legacy EL5-era stuff
- Use the correct systemd macro in post-install scriptlet

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Nathanael Noblet <nathanael@gnat.ca> - 1.10-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 08 2013 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.9-1
- update scriptlets with systemd macros (#850044) - from Václav Pavlín
- add hardened build (#954331)
- update to latests upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.4.6-6
- Add systemd config Bug #754490
- fix user/group creation to be in line with packaging standards
- fix Source URL

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Feb 27 2011 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.4.6-4
- fix f15 build issues with patch from upstream

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 05 2010 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.4.6-1
- update to upstream 1.4.6

* Mon Feb 22 2010 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.4.3-2
- fix binlogdir location initialization for bug #55831

* Sun Feb 21 2010 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.4.3-1
- update to upstream 1.4.3
- change default binlogdir in sysconfig file
- cleanup rpmlint warnings

* Sat Oct 17 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.4.2-1
- update to upstream 1.4.2

* Sun Oct 11 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.4-0
- update to upstream 1.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3-1
- update to upstream 1.3

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.2-1
- update to upstream 1.2
- remove man page source as it was incorporated upstream

* Sat Nov 22 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.1-1
- initial spec creation
