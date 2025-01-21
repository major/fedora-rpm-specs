
Summary:	A daemon to record and keep track of system up times
Name:		uptimed
Version:	0.4.7
Release:	2%{?dist}
License:	GPL-2.0-only
URL:		https://github.com/rpodgorny/uptimed/
Source0:	https://github.com/rpodgorny/%{name}/archive/v%{version}.tar.gz
# https://github.com/rpodgorny/uptimed/pull/6
Patch0:		uptimed-0001-systemd-unit-run-as-daemon-user-not-root.patch
%{?systemd_requires}
BuildRequires: make
BuildRequires: systemd
BuildRequires:	autoconf, automake, libtool

%description
Uptimed is an up time record daemon keeping track of the highest
up times the system ever had.

Uptimed has the ability to inform you of records and milestones
though syslog and e-mail, and comes with a console front end to
parse the records, which can also easily be used to show your
records on your Web page

%package devel
Summary:	Development header and library for uptimed
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development header and library for uptimed.

%prep
%setup -q
# remove bundled getopt
rm -rf src/getopt.[ch]
sed --in-place -e 's/AC_REPLACE_FUNCS(getopt)//' configure.ac
%patch -P0 -p1

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# remove superfluous file
rm %{buildroot}/%{_libdir}/libuptimed.la
# Debian ships urec.h as uptimed.h since 2005
mkdir %{buildroot}%{_includedir}
cp libuptimed/urec.h %{buildroot}%{_includedir}/uptimed.h
install -m 755 -d %{buildroot}%{_pkgdocdir}/sample-cgi
install -m 644 sample-cgi/uprecords.* %{buildroot}%{_pkgdocdir}/sample-cgi
mv %{buildroot}/etc/uptimed.conf-dist %{buildroot}/%{_sysconfdir}/uptimed.conf
mkdir -p %{buildroot}%{_localstatedir}/spool/uptimed

%post
%systemd_post %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%preun
%systemd_preun %{name}.service


%files
%doc AUTHORS CREDITS ChangeLog INSTALL.cgi INSTALL.upgrade README.md README.unsupported TODO sample-cgi/
%license COPYING
%config(noreplace) %{_sysconfdir}/uptimed.conf
%{_sbindir}/uptimed
%{_bindir}/uprecords
%{_mandir}/*/*
%{_libdir}/libuptimed.so.*
%{_unitdir}/uptimed.service
%dir %attr(-,daemon,daemon) %{_localstatedir}/spool/uptimed

%files devel
%{_libdir}/libuptimed.so
%{_includedir}/uptimed.h

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 13 2025 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.4.7-1
- Update to 0.4.7 (#2337462)

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.6-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.4.6-1
- new version, better duplicated detection (rhbz#2023336)

* Mon Aug 02 2021 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.4.4-1
- bump to latest version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 28 2021 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.4.1-8
- remove old trigerun

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.1-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.4.1-1
- update to latest release (rhbz#1592097)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.4.0-2
- switch to running as 'daemon' user

* Wed Apr 29 2015 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.4.0-1
- new upstream release

* Wed Dec 03 2014 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.3.18-1
- new upstream release 0.3.18

* Wed Oct 22 2014 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.3.17.20141021hg29bd8b1eb43d-1
- package snapshot
- use upstream systemd units

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jul 27 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 0.3.17-5
- use _pkgdocdir (https://fedoraproject.org/wiki/Changes/UnversionedDocdirs)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.17-3
- bring systemd unit in-line with upstream (until new version is released)
- use systemd macros
- do not use macros for system executables (rm, sed)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 03 2012 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.17-1
- new upstream version
- do not regenerate auto* stuff

* Sat Feb 11 2012 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.16-9
- remove bundled getopt

* Thu Feb 09 2012 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.16-8
- start Description= in unit file with uppercase
- provide defattr for -devel files

* Sun Jan 29 2012 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.16-7
- remove epoch for -devel Requires

* Sat Jan 14 2012 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.16-6
- add missing percentage sign to -devel Requires

* Sat Jan 14 2012 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.16-5
- add _isa to -devel Requires
- mention header in -devel description and summary

* Mon Jan  9 2012 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.16-4
- ship urec.h as uptimed.h in -devel

* Sun Jan  1 2012 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.16-3
- correct review issues (#770283):
  - dropped BuildRoot:, clean and rm -rf "{buildroot}" from install
  - use defattr(-,root,root,-) instead of defattr(-,root,root)
  - use dir {_localstatedir}/spool/uptimed/ in files
  - don't package uptimed.la

* Wed Dec 28 2011 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.16-2
- added Group: and Requires: to -devel

* Sun Dec 25 2011 Tomasz Torcz <ttorcz@fedoraproject.org> 0.3.16-1
- Initial version based on .spec shipped with source 

