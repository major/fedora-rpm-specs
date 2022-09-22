Name:		edg-mkgridmap
Version:	4.0.4
Release:	14%{?dist}
Summary:	A tool to build the grid map-file from VO servers
License:	ASL 2.0
Url:		http://svnweb.cern.ch/world/wsvn/curios/edg-mkgridmap

# svn export http://svn.cern.ch/guest/curios/edg-mkgridmap/tags/v4_0_4 edg-mkgridmap-4.0.4
# tar czf edg-mkgridmap-4.0.4.tar.gz edg-mkgridmap-4.0.4
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	perl-generators
BuildRequires: make

Requires:	perl(URI)
Requires:	perl(Net::LDAP)
Requires:	perl(Net::LDAPS)
Requires:	perl(Term::ReadKey)
Requires:	perl(IO::Socket::SSL) >= 0.90
Requires:	perl(Net::SSLeay) >= 1.16
Requires:	perl(LWP)
Requires:	perl(XML::DOM)
Requires:	perl(Date::Manip)
Requires:       perl(LWP::Protocol::https)

%description
edg-mkgridmap is a tool to build the grid map-file from VO servers,
taking into account both VO and local policies.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%files
%doc AUTHORS LICENSE MAINTAINERS
%dir %{_libexecdir}/edg-mkgridmap
%{_libexecdir}/edg-mkgridmap/edg-mkgridmap.pl
%{_sbindir}/edg-mkgridmap
%{_mandir}/man5/edg-mkgridmap.conf.5*
%{_mandir}/man8/edg-mkgridmap.8*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Petr Pisar <ppisar@redhat.com> - 4.0.4-12
- Remove a useless dependency on broken Crypt::SSLeay

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016  Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 4.0.4-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 30 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 4.0.3-1
- Mainly adaptations to changes in underlying libraries on CentOS/EL7

* Wed Jun 24 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 4.0.2-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 03 2014 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 4.0.1-1
- New upstream release

* Fri Nov 21 2014 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 4.0.0-8
- Added Requires perl(LWP::Protocol::https)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.0.0-5
- Perl 5.18 rebuild

* Thu May 23 2013 <aalvarez@cern.ch> - 4.0.0-4
- Added dist to the release number.

* Wed May 08 2013 <aalvarez@cern.ch> - 4.0.0-3
- Marking libexec/edg-mkgridmap as owned

* Mon Apr 29 2013 <aalvarez@cern.ch> - 4.0.0-2
- Preparing for release in Fedora/EPEL

* Sun Apr  3 2011 <Maarten.Litmaath@cern.ch> - 4.0.0-1
- Adaptations for EMI.
- Removed obsolete components.
- Version 4.0.0

