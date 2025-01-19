Name:           perl-HTML-Mason
Version:        1.60
Release:        7%{?dist}
Epoch:          1
Summary:        Powerful Perl-based web site development and delivery engine
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://www.masonhq.com/
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/HTML-Mason-%{version}.tar.gz
Source1:        perl-HTML-Mason.conf
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Stick to Apache2, ignore Apache 1 modules
BuildRequires:  perl(Apache2::Directive)
BuildRequires:  perl(Apache2::Log)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::ServerUtil)
BuildRequires:  perl(APR::Table)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Cache::Cache) >= 1
BuildRequires:  perl(CGI) >= 2.46
BuildRequires:  perl(CHI) >= 0.21
BuildRequires:  perl(Class::Container) >= 0.07
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exception::Class) >= 1.15
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Log::Any) >= 0.08
BuildRequires:  perl(mod_perl2)
BuildRequires:  perl(Params::Validate) >= 0.70
BuildRequires:  perl(Scalar::Util) >= 1.01
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(vars)
BuildRequires:  perl(YAML)
# Tests:
# Apache not used
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Config)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(Module::Build)
# Pod::Wordlist not used
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More) >= 0.88
# Test::NoTabs not used
# Test::Pod 1.41 not used
# Test::Spelling 0.12 not used
# Optional tests:
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Output)
Requires:       httpd-filesystem
# Stick to Apache2, ignore Apache 1 modules
Requires:       perl(Apache2::Directive)
Requires:       perl(Apache2::Log)
Requires:       perl(Apache2::RequestIO)
Requires:       perl(Apache2::RequestRec)
Requires:       perl(Apache2::RequestUtil)
Requires:       perl(Apache2::ServerUtil)
Requires:       perl(APR::Table)
Requires:       perl(Cache::Cache) >= 1
Requires:       perl(CHI) >= 0.21
Requires:       perl(Class::Container) >= 0.07
Requires:       perl(Exception::Class) >= 1.15
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(mod_perl2)
Requires:       perl(Params::Validate) >= 0.70
Requires:       perl(Scalar::Util) >= 1.01
Requires:       perl(YAML)

%{?perl_default_filter}

# Filter out under-specified Requires:
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::Container|Exception::Class|File::Spec|Params::Validate)\\)$

%description
Mason is a powerful Perl-based web site development and delivery
engine. With Mason you can embed Perl code in your HTML and construct
pages from shared, reusable components.  Mason solves the common
problems of site development: caching, debugging, templating,
maintaining development and production sites, and more.

%prep
%setup -q -n HTML-Mason-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

rm -f $RPM_BUILD_ROOT%{_bindir}/*.README
for file in $RPM_BUILD_ROOT%{_bindir}/convert*.pl ; do
    mv -f $file $( echo $file | sed 's,/\(convert.*\)\.pl$,/mason_\1,' )
done
mv -f $RPM_BUILD_ROOT%{_bindir}/mason.pl $RPM_BUILD_ROOT%{_bindir}/mason

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/

# Apache:: (Apache1) module
# Not applicable on Fedora.
rm -rf $RPM_BUILD_ROOT%{perl_vendorlib}/HTML/Mason/Apache

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/www/mason
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/mason

%check
%{make_build} test

%files
%doc Changes CREDITS README.md UPGRADE
%license LICENSE
%doc eg/ samples/
%{_bindir}/mason*
%{perl_vendorlib}/*
%{_mandir}/man3/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/perl-HTML-Mason.conf
%dir %attr(775,root,apache) %{_localstatedir}/cache/mason
%dir %{_localstatedir}/www/mason

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 1:1.60-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 12 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 1:1.60-1
- Update to 1.60

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.59-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.59-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.59-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.59-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.59-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.59-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.59-2
- Perl 5.32 rebuild

* Sun May 17 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 1:1.59-1
- Update to 1.59
- Replace %%{__perl} with /usr/bin/perl
- Replace make pure_install with %%{make_install}
- Pass NO_PERLLOCAL to Makefile.PL

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.58-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.58-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.58-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.58-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.58-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 04 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1:1.58-1
- Update to 1.58

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.56-9
- Perl 5.26 rebuild

* Sun Feb 12 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1:1.56-8
- switch Requires from /etc/httpd/conf.d to httpd-filesystem

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.56-6
- Perl 5.24 re-rebuild of bootstrapped packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.56-4
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.56-2
- Perl 5.22 rebuild

* Fri Nov 21 2014 Petr Pisar <ppisar@redhat.com> - 1:1.56-1
- 1.56 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.54-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 02 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.54-1
- Upstream update.
- Filter duplicate Requires:.

* Tue Oct 15 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.52-1
- Upstream update.

* Fri Aug 16 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.51-1
- Upstream update.

* Fri Aug 09 2013 Petr Pisar <ppisar@redhat.com> - 1:1.50-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 21 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.50-1
- Upstream update.
- Reflect Source0-URL having changed.
- Reflect upstream having switched to make.
- Reflect upstream having dropped htdocs.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Petr Pisar <ppisar@redhat.com> - 1:1.48-2
- Perl 5.16 rebuild

* Sun Feb 05 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.48-1
- Upstream update.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1:1.47-1
- Upstream update.
- Spec file cleanup.

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1:1.45-7
- Perl mass rebuild

* Fri Apr 08 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1:1.45-6
- Add optional testsuite requirement perl(CHI). 

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1:1.45-4
- Fix spec-file typo.
- Add commented-out BR: perl(CHI).

* Fri Feb 04 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1:1.45-3
- Remove %%{perl_vendorlib}/HTML/Mason/Apache/.
- Re-activate testsuite.

* Thu Feb 03 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 1:1.45-2
- Rebuild package (Was missing in rawhide).
- Switch to using perl_default_filter.
- Add explicit Require:/Provides: config(perl-HTML-Mason) to work-around
  https://bugzilla.redhat.com/show_bug.cgi?id=674765.

* Fri Dec 17 2010 Steven Pritchard <steve@kspei.com> 1:1.45-1
- Update to 1.45.
- Drop build.patch (now in the upstream release).
- BR CGI, Log::Any, and Test::Deep.

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.42-6
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.42-5
- switch off test for meantime, before update of this package

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.42-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:1.42-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Steven Pritchard <steve@kspei.com> 1:1.42-1
- Update to 1.42.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 02 2008 Steven Pritchard <steve@kspei.com> 1:1.40-1
- Update to 1.40.
- BR Test::Builder.

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:1.39-2
- rebuild for new perl

* Wed Jan 30 2008 Steven Pritchard <steve@kspei.com> 1:1.39-1
- Update to 1.39.

* Mon Jan 07 2008 Steven Pritchard <steve@kspei.com> 1:1.38-1
- Update to 1.38.
- Update License tag.

* Mon Sep 17 2007 Steven Pritchard <steve@kspei.com> 1:1.37-1
- Update to 1.37.

* Tue Jun 26 2007 Steven Pritchard <steve@kspei.com> 1:1.36-1
- Update to 1.36.
- BR Test::Pod.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 1:1.35-2
- Rebuild.

* Tue Oct 17 2006 Steven Pritchard <steve@kspei.com> 1:1.35-1
- Update to 1.35.
- BR Test::Memory::Cycle for better test coverage.

* Mon Oct 16 2006 Steven Pritchard <steve@kspei.com> 1:1.34-1
- Update to 1.34.
- Use fixperms macro instead of our own chmod incantation.
- Reformat a bit to more closely resemble current cpanspec output.
- Rename filter-*.sh to HTML-Mason-filter-*.sh.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 1:1.33-3
- Fix find option order.

* Thu Jun 08 2006 Steven Pritchard <steve@kspei.com> 1:1.33-2
- Add explicit dependency on HTML::Entities

* Mon May 29 2006 Steven Pritchard <steve@kspei.com> 1:1.33-1
- Update to 1.33
- Switch to Module::Build-based build
- Add various bindir mason scripts

* Thu Jan 19 2006 Steven Pritchard <steve@kspei.com> 1:1.32-2
- Epoch bump to resolve rpm thinking 1.3101 > 1.32

* Tue Jan 10 2006 Steven Pritchard <steve@kspei.com> 1.32-1
- Update to 1.32

* Thu Sep 15 2005 Steven Pritchard <steve@kspei.com> 1.3101-3
- Filter bogus provides/requires introduced by eg/ and samples/

* Thu Sep 15 2005 Steven Pritchard <steve@kspei.com> 1.3101-2
- More spec cleanup (jpo)

* Mon Aug 29 2005 Steven Pritchard <steve@kspei.com> 1.3101-1
- Update to 1.3101
- Spec cleanup (jpo)
- Include sample config file from Chris Grau

* Wed Aug 24 2005 Steven Pritchard <steve@kspei.com> 1.31-3
- Use /var/www/mason instead of /var/www/comp
- Spec cleanup

* Tue Aug 23 2005 Steven Pritchard <steve@kspei.com> 1.31-2
- Add some missing dependencies

* Tue Aug 23 2005 Steven Pritchard <steve@kspei.com> 1.31-1
- Update to 1.31
- Use /var/cache/mason instead of /var/www/mason
- Fix perl-HTML-Mason.conf
- Fix URL

* Thu Aug 11 2005 Steven Pritchard <steve@kspei.com> 1.30-1
- Specfile autogenerated.
- Add perl-HTML-Mason.conf and /var/www/*
