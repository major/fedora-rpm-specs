Name:           diaser
Version:        1.1.0
Release:        23%{?dist}
Summary:        Geo-data replication long-term archive system (WAN vault)
License:        GPLv3
URL:            http://www.diaser.org.uk
Source0:        http://downloads.sourceforge.net/diaser/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:      perl-generators

%description
An advanced disk based backup volume accumulator, replication and management 
system for HE and SME. A quick and low-cost way to make an environment more 
robust and data more accessible by archiving in multiple places. This 
replication also provides fast retrieval of archived data from all node 
hosting locations. A Perl installer creates the system. Nodes can be dedicated 
to storage or used for existing services over unused bandwidth. DIASER works 
in user space over SSH. The software is based on DIAP/LTASP which is a storage 
architecture designed to structure months to years of long term sustainable 
archiving space including retrospective archiving.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d -m0755 %{buildroot}%{_sbindir}
install -d -m0755 %{buildroot}%{_docdir}
install -d -m0755 %{buildroot}%{_mandir}/man1
cp -av %{name} %{buildroot}%{_sbindir}
cp -av %{name}.1 %{buildroot}%{_mandir}/man1

%files
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%doc README COPYING CREDITS manual.txt manual.html manual.pdf diaser.conf.sample

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.1.0-7
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Damian L Brasher <dlb@interlinux.org.uk> 1.1.0-3
- Red Hat Bugzilla Bug 644711 Review Request, Comment #18. 

* Mon Jul 25 2011 Damian L Brasher <dlb@interlinux.org.uk> 1.1.0-2
- Red Hat Bugzilla Bug 644711 Review Request, Comments #12,#14 & #16. 

* Mon Apr 18 2011 Damian L Brasher <dlb@interlinux.org.uk> 1.1.0-1
- Updated to release 1.1.0. 

* Thu Oct 28 2010 Damian L Brasher <dlb@interlinux.org.uk> 1.0.8-1
- Corrections: Red Hat Bugzilla Bug 644711 Review Request.

* Wed May 20 2010 Damian L Brasher <dlb@interlinux.org.uk> 1.0.1-1
- Initial implementation. 
