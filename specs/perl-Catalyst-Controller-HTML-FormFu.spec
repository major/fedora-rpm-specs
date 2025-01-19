Name:           perl-Catalyst-Controller-HTML-FormFu
Version:        2.04
Release:        22%{?dist}
Summary:        HTML::FormFu controller for Catalyst
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Catalyst-Controller-HTML-FormFu
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIGELM/Catalyst-Controller-HTML-FormFu-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst::Action)
BuildRequires:  perl(Catalyst::Component::InstancePerContext)
BuildRequires:  perl(Catalyst::Controller)
# This is a plug-in for Catalyst::Runtime
BuildRequires:  perl(Catalyst::Runtime) >= 5.71001
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::FormFu) >= 2.06
BuildRequires:  perl(HTML::FormFu::Deploy)
BuildRequires:  perl(HTML::FormFu::MultiForm)
BuildRequires:  perl(HTML::FormFu::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Attribute::Chained) >= 1.0.1
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
# Task::Weaken for Scalar::Util, see Makefile.PL
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::Plugin::ConfigLoader) >= 0.23
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::File)
BuildRequires:  perl(Catalyst::View::TT)
# Config::General not used
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
# Template not used
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
# Test::WWW::Mechanize 1.16 for post_ok()
BuildRequires:  perl(Test::WWW::Mechanize) >= 1.16
Requires:       perl(Catalyst::Component::InstancePerContext)
Requires:       perl(Catalyst::Controller)
Requires:       perl(Catalyst::Runtime) >= 5.71001
Requires:       perl(HTML::FormFu) >= 2.06
Requires:       perl(MooseX::Attribute::Chained) >= 1.0.1
# Task::Weaken for Scalar::Util, see Makefile.PL
Requires:       perl(Task::Weaken)

%description
This base controller merges the functionality of HTML::FormFu with Catalyst.

# Filter unde-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((HTML::FormFu|MooseX::Attribute::Chained)\\)$

%prep
%setup -q -n Catalyst-Controller-HTML-FormFu-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 2.04-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-14
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-11
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-2
- Perl 5.28 rebuild

* Sun Apr 22 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.04-1
- Update to 2.04

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Petr Pisar <ppisar@redhat.com> - 2.02-1
- Update to 2.02
- Remove upstreamed patch

* Tue Jul 25 2017 Petr Pisar <ppisar@redhat.com> - 2.01-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 03 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.01-1
- Update to 2.01

* Sat Jun 04 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.00-1
- Update to 2.00
- Pass NO_PACKLIST to Makefile.PL

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Petr Pisar <ppisar@redhat.com> - 1.00-4
- Do not use Test::Aggregate::Nested for tests because it's not available
  anymore (bug #1231204)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-2
- Perl 5.22 rebuild

* Fri Nov 21 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.00
- Update to 1.00
- Drop unused tags
- Use %%license tag

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09004-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Petr Pisar <ppisar@redhat.com> - 0.09004-5
- Specify all dependencies (bug #1085432)

* Wed Aug 07 2013 Petr Pisar <ppisar@redhat.com> - 0.09004-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Iain Arnell <iarnell@gmail.com> 0.09004-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Petr Pisar <ppisar@redhat.com> - 0.09003-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.09003-2
- Perl mass rebuild

* Wed May 18 2011 Iain Arnell <iarnell@gmail.com> 0.09003-1
- update to latest upstream version

* Sat Apr 09 2011 Iain Arnell <iarnell@gmail.com> 0.09000-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08002-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Sep 25 2010 Iain Arnell <iarnell@gmail.com> 0.08002-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06001-2
- Mass rebuild with perl-5.12.0

* Fri Dec 18 2009 Iain Arnell <iarnell@gmail.com> 0.06001-1
- update to latest upstream version

* Wed Dec 09 2009 Iain Arnell <iarnell@gmail.com> 0.06000-1
- update to latest upstream version

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.05000-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Iain Arnell <iarnell@gmail.com> 0.05000-1
- update to latest upstream version
- BR perl(namespace::autoclean)

* Wed Apr 22 2009 Iain Arnell <iarnell@gmail.com> 0.04003-1
- update to 0.04003
- BR perl(MRO::Compat)

* Fri Apr 17 2009 Iain Arnell <iarnell@gmail.com> 0.04001-1
- update to latest upstream version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Iain Arnell <iarnell@gmail.com> 0.03007-2
- temporarily change source url to use search.cpan.org

* Mon Dec 08 2008 Iain Arnell 0.03007-1
- Specfile autogenerated by cpanspec 1.77.
