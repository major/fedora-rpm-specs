%global _hardened_build 1

Name:           fido
Version:        1.1.5
Release:        23%{?dist}
Summary:        Multi-threaded file watch utility

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.joedog.org/%{name}-home/
Source0:        http://download.joedog.org/%{name}/%{name}-%{version}.tar.gz

#Upstream whants to keep the static library
Patch6:         %{name}-shared-library.patch

%{?el5:BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}

%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:    systemd
%{?systemd_requires}
%else
Requires(post):  /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): initscripts
%endif
BuildRequires:   libtool, libjoedog-devel
BuildRequires: make


%description
A multi-threaded file watch utility. It can monitor files for changes in
content or modification times. If it notices a change, it will kick off a
user-defined script.


%prep
%setup -q

%patch -P6

rm -f *.m4
rm -rf include/joedog/*.h
sed -i -e 's/AC_PROG_SHELL//' configure.ac
autoreconf --install --force


%build
%configure
make %{?_smp_mflags}


%install
%if 0%{?el5}
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%else
%make_install
%endif

%if 0%{?fedora} || 0%{?rhel} >= 7
#systemd
install -D -p -m 0644 utils/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
%else
#SysVinit
install -D -p -m 0644 utils/%{name}-redhat-config %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%{?el6:install -D -p -m 0755 utils/%{name}-redhat-start %{buildroot}%{_initddir}/%{name}}
%{?el5:install -D -p -m 0755 utils/%{name}-redhat-start %{buildroot}%{_initrddir}/%{name}}
%endif

#prepare sample configs for doc
for _file in doc/*.conf
do
    ln -f "${_file}" "${_file}.sample"
done

#provide a reasonable minimal config as starting point
sed -e 's/^verbose  = true/verbose = false/' \
  %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.sample \
  > %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
rm -f %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.sample



%files
%doc ChangeLog README.md COPYING
%doc doc/*.sample
%{_sbindir}/%{name}
%{_mandir}/man*/*
%{_sysconfdir}/%{name}/rules
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf

%if 0%{?fedora} || 0%{?rhel} >= 7
#systemd
%{_unitdir}/%{name}.service


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
%else
#SysVinit
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%{?el6:%{_initddir}/%{name}}
%{?el5:%{_initrddir}/%{name}}

%post
/sbin/chkconfig --add %{name}

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%postun
if [ "$1" -ge "1" ] ; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.5-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.5-13
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Roman Mohr <roman@fenkhuber.at> - 1.1.5-1
- Update to 1.1.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 23 2014 Roman Mohr <roman@fenkhuber.at> - 1.1.2-1
- fix the possibility that fido misses some age tests and fails to fire an alert

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Roman Mohr <roman@fenkhuber.at> - 1.1.1-1
- degraded from alarm to a log entry if monitored files are only sometimes
  locked by another process.

* Tue Nov 19 2013 Roman Mohr <roman@fenkhuber.at> - 1.1.0-1
- upstream 1.1.0
- removing patches 0 to 5, as upstream now includes them
- removing unneeded direct dependency to libjoedog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Roman Mohr <roman@fenkhuber.at> - 1.0.7-6
- Use %%{_initrddir} instead of %%{_initddir} for el5

* Mon Jun 24 2013 Roman Mohr <roman@fenkhuber.at> - 1.0.7-5
- trimmed/rearranged BuildRequires
- nuked explicit Requires: libjoedog
- removed article from Summary

* Mon Jun 24 2013 Roman Mohr <roman@fenkhuber.at> - 1.0.7-4
- Use libjoedog instead of the bundled satic library
- Fixed hardening build
- Added missing Group for EPEL5

* Tue Jun 11 2013 Roman Mohr <roman@fenkhuber.at> - 1.0.7-3
- Refactoring spec to support EPEL builds
- Hunting down some more memory leaks

* Sun Jun 09 2013 Roman Mohr <roman@fenkhuber.at> - 1.0.7-2
- Added systemd unit file
- Fixed some memory leaks
- Fixed a security issue when switching to a non-privileged user

* Mon May 20 2013 Roman Mohr <roman@fenkhuber.at> - 1.0.7-1
- Fixed custom rules in Makefile.in to support DESTDIR
- Fixed incorrect-fsf-address errors
