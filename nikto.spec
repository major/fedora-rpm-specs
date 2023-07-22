Name:           nikto

# Handle the old versioning system 2.01, 2.02, 2.03 ...
Epoch:          1
Version:        2.1.6
Release:        13%{?dist}
Summary:        Web server scanner


# We consider the nikto database to be content.
License:        GPLv2+ and Redistributable, no modification permitted
URL:            https://www.cirt.net/Nikto2
Source0:        https://github.com/sullo/nikto/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        nikto-database-license.txt

# use system libwhisker2
Patch0:         nikto-libwhisker2.patch

# Patch CVE-2018-11652 
# https://github.com/sullo/nikto/commit/e759b3300aace5314fe3d30800c8bd83c81c29f7
# https://nvd.nist.gov/vuln/detail/CVE-2018-11652
Patch1:         nikto-CVE-2018-11652.patch



BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       nmap

# Requires potentially not found by the auto dependency search
Requires:       perl(Time::HiRes)
Requires:       perl(bignum)
Requires:       perl(List::Util)


# We don't provide any perl modules
%global __provides_exclude_from %{_datadir}/nikto/plugins/JSON-PP.pm

%description
Nikto is a web server scanner which performs comprehensive tests against web
servers for multiple items, including over 3300 potentially dangerous
files/CGIs, versions on over 625 servers, and version specific problems
on over 230 servers. Scan items and plugins are frequently updated and
can be automatically updated (if desired).

%prep
%autosetup -p 1

#change configfile path
sed -i "s:/etc/nikto.conf:%{_sysconfdir}/nikto/config:" program/nikto.pl

#enable nmap by default and set plugindir path
sed -i "s:# EXECDIR=/opt/nikto:EXECDIR=%{_datadir}/nikto:;
        s:# PLUGINDIR=/opt/nikto/plugins:PLUGINDIR=%{_datadir}/nikto/plugins:;
        s:# TEMPLATEDIR=/opt/nikto/templates:TEMPLATEDIR=%{_datadir}/nikto/templates:;
        s:# DOCDIR=/opt/nikto/docs:DOCDIR=%{_datadir}/nikto/docs:" program/nikto.conf

#Disable RFIURL by default - let users configure it themselves to trustworthy source
sed -i "s:^RFIURL=:#RFIURL=:" program/nikto.conf

cp %{SOURCE1} program/docs/database-license.txt

%build
#no build required


%install
rm -rf %{buildroot}
install -pD program/nikto.pl %{buildroot}%{_bindir}/nikto
install -pD program/replay.pl %{buildroot}%{_bindir}/nikto-replay
install -m 0644 -pD program/docs/nikto.1 %{buildroot}%{_mandir}/man1/nikto.1
mkdir -p %{buildroot}%{_datadir}/nikto/databases/
install -m 0644 -p program/databases/* %{buildroot}%{_datadir}/nikto/databases/
mkdir -p %{buildroot}%{_datadir}/nikto/plugins/
install -m 0644 -p program/plugins/* %{buildroot}%{_datadir}/nikto/plugins/
mkdir -p %{buildroot}%{_datadir}/nikto/templates/
install -m 0644 -p program/templates/* %{buildroot}%{_datadir}/nikto/templates/
install -m 0644 -pD program/nikto.conf %{buildroot}%{_sysconfdir}/nikto/config

#remove unneeded files
rm -f %{buildroot}%{_datadir}/nikto/plugins/LW2.pm


%files
%license program/docs/LICENSE.txt program/docs/database-license.txt
%doc program/docs/CHANGES.txt program/docs/manual.xml program/docs/nikto.dtd program/docs/nikto_manual.html
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/nikto
%{_datadir}/nikto
%{_mandir}/man?/*


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 Michal Ambroz <rebus AT seznam.cz> - 1:2.1.6-4
- #1651845 - add dependencies not detected automatically during build

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Michal Ambroz <rebus AT seznam.cz> - 1:2.1.6-1
- bump to upstream version
- fix weekdays in changelog
- cherry pick patch from upstream for CVE-2018-11652 - bugs 1585612,1585614

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 24 2014 Michal Ambroz <rebus AT seznam.cz> - 1:2.1.5-10
- updated link to the upstream package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:2.1.5-7
- Perl 5.18 rebuild

* Thu Apr 25 2013 Tom Callaway <spot@fedoraproject.org> - 1:2.1.5-6
- treat nikto database files as content, update license

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Paul Howarth <paul@city-fan.org> - 1:2.1.5-4
- don't rpm-provide perl JSON modules (#885143)

* Thu Oct 04 2012 Michal Ambroz <rebus AT seznam.cz> - 1:2.1.5-3
- add databases directory
- omit initialization of SSL untill it is pushed to libwhiskers
  beware this can result in usage of Net::SSLeay and memory leaks

* Tue Sep 18 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1:2.1.5-2
- Rewrite libwiskers patch

* Mon Sep 17 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1:2.1.5-1
- New upstream release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 9 2011 Michal Ambroz <rebus AT seznam.cz> - 1:2.1.4-2
- Fix the default config file

* Mon Mar 28 2011 Michal Ambroz <rebus AT seznam.cz> - 1:2.1.4-1
- Version bump

* Sun Sep 12 2010 Michal Ambroz <rebus AT seznam.cz> - 1:2.1.3-1
- Version bump

* Mon Mar 22 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1:2.1.1-3
- Add missing changelog
- Version bump

* Mon Mar 22 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1:2.1.1-2
- Update version to 2.1.1 and fix version collisions, 
  based on SPEC provided by Michal Ambroz <rebus at, seznam.cz> 

* Mon Feb 08 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 2.03-3
- Resolve rhbz #515871

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 2.03-1
- New upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.36-4
- fix license tag

* Wed May 30 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 1.36-3
- Add sed magic to really replace nikto-1.36-config.patch
* Mon May 28 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 1.36-2
- Remove libwhisker Requires
- Replace configfile patch with sed magic
- Update License
- Add database-license.txt to %%doc
* Fri May 04 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 1.36-1
- Initial build
