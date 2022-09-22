Name:		stompclt
Version:	1.8
Release:	4%{?dist}
Summary:	Versatile STOMP client
License:	GPL+ or Artistic
URL:		https://github.com/cern-mig/%{name}
Source0:	https://github.com/cern-mig/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	perl(Net::STOMP::Client) >= 2.0
# the following one is in theory optional but really nice to have everywhere
Requires:	perl(Directory::Queue)

%description
stompclt is a versatile tool to interact with messaging brokers speaking
STOMP and/or message queues (see Messaging::Message::Queue) on disk.

It receives messages (see Messaging::Message) from an incoming module,
optionally massaging them (i.e. filtering and/or modifying), and sends
them to an outgoing module. Depending on which modules are used, the tool
can perform different operations.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.8-3
- Perl 5.36 rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Lionel Cons <lionel.cons@cern.ch> 1.8-1
- Updated to 1.8 (rhbz #2025845)

* Thu Oct 28 2021 Lionel Cons <lionel.cons@cern.ch> 1.7-1
- Updated to 1.7 (rhbz #2018102)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-5
- Perl 5.32 rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-2
- Perl 5.30 rebuild

* Tue Feb 26 2019 Lionel Cons <lionel.cons@cern.ch> 1.6-1
- Update to upstream, rhbz #1683158.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.5-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.5-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Lionel Cons <lionel.cons@cern.ch> 1.5-1
- Update to upstream, rhbz #1395138.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.4-3
- Perl 5.24 rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Lionel Cons <lionel.cons@cern.ch> 1.4-1
- Update to upstream, rhbz #1291167.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.3-2
- Perl 5.22 rebuild

* Tue Apr 28 2015 Adrien Devresse <adevress at cern.ch> - 1.3.0-1
- Update to 1.3.0

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-3
- Perl 5.20 rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Alexandre Beche <alexandre.beche@gmail.com> 1.2-1
- Update to upstream, rhbz #1097055.

* Wed Feb 12 2014 Massimo Paladin <massimo.paladin@gmail.com> 1.1-1
- Update to upstream, rhbz #1061604.

* Tue Dec 17 2013 Massimo Paladin <massimo.paladin@gmail.com> 1.0-1
- Update to upstream, rhbz #1043784.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.9-2
- Perl 5.18 rebuild

* Mon Apr 22 2013 Massimo Paladin <massimo.paladin@gmail.com> 0.9-1
- Update to 0.9, rhbz #954346.

* Tue Feb 26 2013 Massimo Paladin <massimo.paladin@gmail.com> 0.8-1
- Update to 0.8, rhbz #915292.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Massimo Paladin <massimo.paladin@gmail.com> 0.7-1
- Update to 0.7, rhbz #885594.

* Tue Nov 20 2012 Massimo Paladin <massimo.paladin@gmail.com> 0.6-1
- Update to 0.6.

* Mon Oct 08 2012 Massimo Paladin <massimo.paladin@gmail.com> 0.5-2
- Files section more precise.

* Thu Aug 30 2012 Lionel Cons <lionel.cons@cern.ch> 0.5-1
- First version packaged.
