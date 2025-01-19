# Name of the plugin
%global plugin check_openmanage

# No binaries here, do not build a debuginfo package
%global debug_package %{nil}

Name:          nagios-plugins-openmanage
Version:       3.7.12
Release:       25%{?dist}
Summary:       Nagios plugin to monitor hardware health on Dell servers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://folk.uio.no/trondham/software/%{plugin}.html
Source0:       http://folk.uio.no/trondham/software/files/%{plugin}-%{version}.tar.gz


# Building requires Docbook XML
BuildRequires: make
BuildRequires: libxslt
BuildRequires: libxml2
BuildRequires: docbook-style-xsl
BuildRequires: perl-generators

# Rpmbuild doesn't find these perl dependencies
Requires:      perl(Config::Tiny)
Requires:      perl(Net::SNMP)

# Owns the nagios plugins directory
Requires: nagios-common

# Make the transition to Fedora/EPEL packages easier for existing
# users of the non-Fedora/EPEL RPM packages
Provides:      nagios-plugins-check-openmanage = %{version}-%{release}
Obsoletes:     nagios-plugins-check-openmanage < 3.7.2-3

%description
check_openmanage is a plugin for Nagios which checks the hardware
health of Dell servers running OpenManage Server Administrator
(OMSA). The plugin can be used remotely with SNMP or locally with
NRPE, check_by_ssh or similar, whichever suits your needs and
particular taste. The plugin checks the health of the storage
subsystem, power supplies, memory modules, temperature probes etc.,
and gives an alert if any of the components are faulty or operate
outside normal parameters.

%prep
%setup -q -n %{plugin}-%{version}
rm -f %{plugin}.exe

%build
pushd man
make clean && make
popd

%install
install -Dp -m 0755 %{plugin} %{buildroot}%{_libdir}/nagios/plugins/%{plugin}
install -Dp -m 0644 man/%{plugin}.8 %{buildroot}%{_mandir}/man8/%{plugin}.8
install -Dp -m 0644 man/%{plugin}.conf.5 %{buildroot}%{_mandir}/man5/%{plugin}.conf.5

%files
%license COPYING
%doc README CHANGES example.conf
%{_libdir}/nagios/plugins/%{plugin}
%{_mandir}/man8/%{plugin}.8*
%{_mandir}/man5/%{plugin}.conf.5*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.7.12-24
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Xavier Bachelot <xavier@bachelot.org> - 3.7.12-14
- Remove obsolete conditionals
- Don't clean buildroot in %%install
- Use %%license for license file

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.12-1
- Upstream release 3.7.12
- Conditionalize building man pages for rhel6+ and fedora19+ (others
  will use pre-built man pages)
- Conditionalize require nagios-common (rhel6+/fedora19+) or
  nagios-plugins (others) for owner of the plugins directory
- Drop perl(Crypt::Rijndael) requirement, as it provides optional and
  very rarely used functionality

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug  6 2013 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.11-1
- Upstream release 3.7.11

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 3.7.10-2
- Perl 5.18 rebuild

* Fri Jul 19 2013 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.10-1
- Upstream release 3.7.10

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.7.9-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.9-1
- Upstream release 3.7.9

* Wed Dec 12 2012 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.8-1
- Upstream release 3.7.8

* Thu Dec  6 2012 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.7-1
- Upstream release 3.7.7

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.6-1
- Upstream release 3.7.6
- Changes to build section and buildrequires for new manpage format

* Fri Apr 13 2012 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.5-1
- Upstream version 3.7.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.3-3
- Provide example config file as documentation rather than installing
  it under /etc/nagios
- Remove win32 binary in prep section

* Tue Nov 15 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.3-2
- Spec file changes which address issues raised in rhbz#743615

* Wed Oct  5 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.3-1
- Version 3.7.3
- RPM name changed to nagios-plugins-openmanage
- Added obsoletes for old name

* Tue Sep 27 2011 Xavier Bachelot <xavier@bachelot.org> - 3.7.2-2
- Add a commented configuration file.
- Add some Requires to have all features out of the box.
- Add Requires on nagios-plugins for %%{_libdir}/nagios/plugins directory.
- Remove some useless command macros.
- Fix Obsoletes/Provides.

* Mon Sep 19 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.2-1
- Version 3.7.2

* Mon Aug 22 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.1-1
- Version 3.7.1

* Mon Aug 15 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.7.0-1
- Version 3.7.0

* Mon Jun 06 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.8-1
- Version 3.6.8

* Thu May 12 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.7-1
- Version 3.6.7

* Thu Apr 28 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.6-1
- Version 3.6.6

* Wed Feb  9 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.5-1
- Version 3.6.5

* Tue Jan  4 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.4-2
- Don't compress the man page, rpmbuild takes care of that. Thanks to
  Jose Pedro Oliveira for a patch that fixes this.

* Tue Jan  4 2011 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.4-1
- Version 3.6.4
- Initial build with new spec file
- Spec file adapted to Fedora/EPEL standards

* Mon Dec 13 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.3-1
- Version 3.6.3

* Thu Nov 25 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.2-1
- Version 3.6.2

* Tue Nov  2 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.1-1
- Version 3.6.1

* Mon Aug 30 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.6.0-1
- Version 3.6.0

* Wed Jul 14 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.10-1
- Version 3.5.10

* Tue Jun 29 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.9-1
- Version 3.5.9

* Thu Jun 17 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.8-1
- Version 3.5.8

* Fri Mar 19 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.7-1
- Version 3.5.7

* Tue Feb 23 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.6-1
- Version 3.5.6

* Fri Jan 22 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.5-1
- Version 3.5.5

* Wed Jan 13 2010 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.4-1
- Version 3.5.4

* Thu Dec 17 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.3-1
- Version 3.5.3

* Tue Nov 17 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.2-1
- Version 3.5.2

* Thu Oct 22 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.1-1
- Version 3.5.1

* Tue Oct 13 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.5.0-1
- Version 3.5.0
- New location for the manual page (section 3 -> 8)

* Fri Aug  7 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.9-1
- Version 3.4.9

* Fri Jul 31 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.8-1
- Version 3.4.8

* Fri Jul 24 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.7-1
- Version 3.4.7

* Tue Jul  7 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.6-1
- Version 3.4.6

* Mon Jun 22 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.5-1
- Version 3.4.5

* Mon Jun 22 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.4-1
- Version 3.4.4

* Thu Jun 11 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.3-1
- Version 3.4.3

* Wed Jun  3 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.2-1
- Version 3.4.2

* Wed May 27 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.1-1
- Version 3.4.1

* Mon May 25 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.4.0-1
- Version 3.4.0

* Tue May  5 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.3.2-1
- Version 3.3.2

* Tue Apr 28 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.3.1-1
- Version 3.3.1

* Tue Apr  7 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.3.0-1
- Version 3.3.0

* Sun Mar 29 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.2.7-1
- Version 3.2.7

* Thu Mar  5 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.2.6-1
- Version 3.2.6

* Tue Feb 24 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.2.5-1
- Version 3.2.5
- take 64bit (other libdir) into consideration

* Tue Feb 17 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.2.4-1
- Version 3.2.4

* Mon Feb  9 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.2.3-1
- Version 3.2.3

* Tue Feb  3 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.2.2-1
- Version 3.2.2

* Tue Feb  3 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.2.1-1
- Version 3.2.1

* Tue Jan 27 2009 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.2.0-1
- Version 3.2.0

* Sat Dec 20 2008 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.0.2-1
- Version 3.0.2

* Thu Dec  4 2008 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 3.0.0-1
- Version 3.0.0

* Wed Nov 19 2008 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 2.1.0-0
- first RPM release
