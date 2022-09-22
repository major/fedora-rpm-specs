Name:           perl-Plack-Middleware-Deflater
Version:        0.12
Release:        26%{?dist}
Summary:        Compress response body with Gzip or Deflate
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Plack-Middleware-Deflater
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Plack-Middleware-Deflater-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  sed
# requires from Makefile.PL
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Module::Install::WriteAll)
# for run time
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# for tests
# AnyEvent does not make sense without Plack::Test::AnyEvent
#BuildRequires:  perl(AnyEvent) >= 5.34
BuildRequires:  perl(FindBin)
# required for a test case but not available in Fedora
#BuildRequires:  perl(Furl)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle::Util)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Test)
# Plack::Test::AnyEvent not available in Fedora
#BuildRequires:  perl(Plack::Test::AnyEvent) >= 0.03
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
# Test::TCP does not make sense without Furl
#BuildRequires:  perl(Test::TCP)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Plack::Middleware::Deflater is a middleware to encode your response body in
gzip or deflate, based on Accept-Encoding HTTP request header. It would
save the bandwidth a little bit but should increase the Plack server load,
so ideally you should handle this on the front end reverse proxy servers.

%prep
%setup -q -n Plack-Middleware-Deflater-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-25
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-22
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-19
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-13
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-10
- Perl 5.26 rebuild

* Wed May 24 2017 Petr Pisar <ppisar@redhat.com> - 0.12-9
- Fix building on Perl without "." in @INC (CPAN RT#121850)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct  1 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.12-1
- Update to 0.12
- Requires/BR perl(IO::Compress::Deflater) and perl(IO::Compress::Gzip) removed,
  perl(Compress::Zlib) added

* Fri Aug  9 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.11-1
- Update to 0.11

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.09-3
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.09-1
- Update to 0.09

* Wed May 15 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.08-2
- BuildRequires more Perl modules: parent, Plack::Middleware, Plack::Util,
  Plack::Util::Accessor, File::Spec, Spiffy, Test::Base::Filter,
  Test::Builder, Test::Builder::Module
- 'frontend' changed to 'front end'

* Fri May 03 2013 Robin Lee <cheeselee@fedoraproject.org> 0.08-1
- Specfile autogenerated by cpanspec 1.78.
