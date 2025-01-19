Name:           perl-Catalyst-Action-REST
Version:        1.21
Release:        23%{?dist}
Summary:        Automated REST Method Dispatching
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Catalyst-Action-REST
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-Action-REST-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Log)
BuildRequires:  perl(Catalyst::Request)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80030
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Class::Inspector) >= 1.13
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Taxi)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.75 
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTTP::Body)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(lib)
BuildRequires:  perl(JSON) >= 2.12
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(LWP::UserAgent) >= 5.00
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose) >= 1.03
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MRO::Compat) >= 0.10
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Validate) >= 0.76
BuildRequires:  perl(PHP::Serialization)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
BuildRequires:  perl(URI::Find)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML::Syck)
Requires:       perl(Catalyst::Runtime) >= 5.80030
Requires:       perl(Class::Inspector) >= 1.13
Requires:       perl(Config::General)
Requires:       perl(Data::Taxi)
Requires:       perl(FreezeThaw)
Requires:       perl(JSON) >= 2.12
Requires:       perl(LWP::UserAgent) >= 5.00
Requires:       perl(Moose) >= 1.03
Requires:       perl(MRO::Compat) >= 0.10
Requires:       perl(Params::Validate) >= 0.76
Requires:       perl(PHP::Serialization)
Requires:       perl(XML::Simple)
Requires:       perl(YAML::Syck)

%{?perl_default_filter}

%description
This Action handles doing automatic method dispatching for REST requests.
It takes a normal Catalyst action, and changes the dispatch to append an
underscore and method name. First it will try dispatching to an action
with the generated name, and failing that it will try to dispatch to a
regular method.

%prep
%setup -q -n Catalyst-Action-REST-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}

%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.21-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-15
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-12
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.21-1
- Update to 1.21

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.20-1
- Update to 1.20

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-2
- Perl 5.22 rebuild

* Sun Feb 08 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.19-1
- Update to 1.19
- Use the %%license macro
- Add NO_PACKLIST=1 as an argument to Makefile.PL

* Sun Feb 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.18-1
- Update to 1.18
- Tighten file listing

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 1.11-1
- 1.11 bump

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 1.06-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 1.06-1
- update to latest upstream version

* Sat Jul 21 2012 Iain Arnell <iarnell@gmail.com> 1.05-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 1.02-2
- Perl 5.16 rebuild

* Sat Jun 09 2012 Iain Arnell <iarnell@gmail.com> 1.02-1
- update to latest upstream version
- BR inc::Module::Install instead of EU::MM

* Tue Apr 17 2012 Iain Arnell <iarnell@gmail.com> 1.00-1
- update to latest upstream version

* Tue Feb 28 2012 Iain Arnell <iarnell@gmail.com> 0.99-1
- update to latest upstream version

* Tue Feb 21 2012 Iain Arnell <iarnell@gmail.com> 0.98-1
- update to latest upstream version

* Wed Feb 01 2012 Iain Arnell <iarnell@gmail.com> 0.96-1
- update to latest upstream (fixes rt#63537)

* Thu Jan 05 2012 Iain Arnell <iarnell@gmail.com> 0.95-1
- update to latest upstream version

* Sat Aug 27 2011 Iain Arnell <iarnell@gmail.com> 0.91-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.90-2
- Perl mass rebuild

* Sat Feb 26 2011 Iain Arnell <iarnell@gmail.com> 0.90-1
- update to latest upstream version

* Sun Feb 20 2011 Iain Arnell <iarnell@gmail.com> 0.89-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Iain Arnell <iarnell@gmail.com> 0.88-1
- update to latest upstream version

* Sat Nov 06 2010 Iain Arnell <iarnell@gmail.com> 0.87-1
- update to latest upstream

* Sun Sep 05 2010 Iain Arnell <iarnell@gmail.com> 0.86-1
- update to latest upstream version

* Sat Jul 17 2010 Iain Arnell <iarnell@gmail.com> 0.85-2
- cleanup spec for modern rpmbuild

* Sun Jun 27 2010 Iain Arnell <iarnell@gmail.com> 0.85-1
- Specfile autogenerated by cpanspec 1.78.
