Name:           perl-HTTP-OAI
Version:        4.10
Release:        10%{?dist}
Summary:        API for the OAI-PMH
License:        BSD
URL:            https://metacpan.org/release/HTTP-OAI
Source0:        https://cpan.metacpan.org/authors/id/H/HO/HOCHSTEN/HTTP-OAI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode) >= 2.12
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(LWP::MemberMixin)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.6
BuildRequires:  perl(XML::LibXML::SAX) >= 1.04
BuildRequires:  perl(XML::LibXML::SAX::Builder)
BuildRequires:  perl(XML::LibXML::SAX::Parser)
BuildRequires:  perl(XML::LibXML::XPathContext)
BuildRequires:  perl(XML::NamespaceSupport)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base) >= 1
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::SAX::Writer)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is a stub module, you probably want to look at HTTP::OAI::Harvester or
HTTP::OAI::Repository.

%prep
%setup -q -n HTTP-OAI-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
iconv -f iso8859-15 -t utf-8 README > README.conv && mv -f README.conv README
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.10-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.10-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.10-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.10-1
- 4.10 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.08-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.08-1
- 4.08 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.07-2
- Perl 5.28 rebuild

* Mon Jun 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.07-1
- 4.07 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-1
- 4.06 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-1
- 4.05 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-2
- Perl 5.26 rebuild

* Wed Feb 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-1
- 4.04 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.03-4
- Perl 5.24 rebuild

* Fri Feb 05 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.03-3
- Add BR: perl(Test) (Fix F23FTBFS).
- Modernize spec.
- Add %%license.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 4.03-1
- New upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.27-8
- Perl 5.22 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 3.27-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 3.27-1
- tidying of spec file
- new upstream release 3.27
* Thu Apr 28 2011 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 3.24-1
- Specfile autogenerated by cpanspec 1.78.
