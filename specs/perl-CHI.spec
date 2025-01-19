Name:           perl-CHI
Version:        0.61
Release:        11%{?dist}
Summary:        Unified cache handling interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CHI
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/CHI-%{version}.tar.gz

# RHBZ#1275936
Patch1:         perl-CHI-0.60-Adapt-to-changes-in-Cache-FastMmap-1.45.patch

BuildArch:      noarch

%bcond_with author_tests

%bcond_without smoke_tests

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(Carp::Assert) >= 0.20
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::JHash)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(Hash::MoreUtils)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(List::MoreUtils) >= 0.13
BuildRequires:  perl(Log::Any) >= 0.08
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(MooX::Types::MooseLike) >= 0.23
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(MooX::Types::MooseLike::Numeric)
BuildRequires:  perl(Storable)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Log::Dispatch)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Time::Duration) >= 1.06
BuildRequires:  perl(Time::Duration::Parse) >= 0.03
BuildRequires:  perl(Time::HiRes) >= 1.30
BuildRequires:  perl(Try::Tiny) >= 0.05

%if %{with author_tests}
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Module::Mask)
%endif

%if %{with smoke_tests}
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Cache::FastMmap)
%endif


# Filter out bogus provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Bar\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Baz\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DummySerializer\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Foo\\)

# Filter out unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp::Assert\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::MoreUtils\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Log::Any\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Time::Duration\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Time::Duration::Parse\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Time::HiRes\\)$

# ... replace filtered requires with versioned requires
Requires: perl(Carp::Assert) >= 0.20
Requires: perl(List::MoreUtils) >= 0.13
Requires: perl(Log::Any) >= 0.06
Requires: perl(Time::Duration) >= 1.06
Requires: perl(Time::Duration::Parse) >= 0.03
Requires: perl(Time::HiRes) >= 1.30

%description
CHI provides a unified caching API, designed to assist a developer in
persisting data for a specified period of time.

%package Test
Summary:        CHI::Test module
Requires:       perl-CHI = %{version}-%{release}

# rpm misses these:
Requires: perl(Test::Deep)
Requires: perl(Test::Exception)

# ... replace filtered requires with versioned requires
Requires: perl(List::MoreUtils) >= 0.13
Requires: perl(Time::HiRes) >= 1.30

%description Test
CHI::Test and CHI::t perl modules

%prep
%setup -q -n CHI-%{version}
%patch -P1 -p1

# Fix bogus permissions
find lib \( -type f -a -executable \) -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test %{?with_author_tests:AUTHOR_TESTING=1} %{?with_smoke_tests:AUTOMATED_TESTING=1}

%files
%doc Changes
%license LICENSE
%dir %{perl_vendorlib}/CHI
%{perl_vendorlib}/CHI.pm
%{perl_vendorlib}/CHI/Benchmarks.pod
%{perl_vendorlib}/CHI/CacheObject.pm
%{perl_vendorlib}/CHI/Constants.pm
%{perl_vendorlib}/CHI/Driver*
%{perl_vendorlib}/CHI/Serializer
%{perl_vendorlib}/CHI/Stats.pm
%{perl_vendorlib}/CHI/Types.pm
%{perl_vendorlib}/CHI/Util.pm
%{_mandir}/man3/*

%files Test
%dir %{perl_vendorlib}/CHI
%{perl_vendorlib}/CHI/t
%{perl_vendorlib}/CHI/Test*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.61-5
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.61-1
- Update to 0.61.
- Drop perl-CHI-0.60-perl-5.22-regex.diff.
- Modernize spec.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-24
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-21
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-15
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.60-12
- Add perl-CHI-0.60-Adapt-to-changes-in-Cache-FastMmap-1.45.patch
  (https://bugzilla.redhat.com/attachment.cgi?id=1275936, RHBZ#1435166).
- Modernize spec.

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-11
- Perl 5.26 rebuild

* Tue Feb 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.60-10
- Remove BR: perl(Log::Any::Adapter::Dispatch) (Unused).

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-8
- Perl 5.24 re-rebuild of bootstrapped packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.60-6
- Rework filtering.
- Modernize spec.

* Sat Aug 15 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.60-5
- BR: perl(Time::HiRes) (RHBZ#1253321).

* Thu Jun 18 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.60-4
- Add perl-CHI-0.60-perl-5.22-regex.diff (Work-around to 
  "Unescaped left brace in regex is deprecated" with perl-5.22).

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.60-1
- Upstream update.
- Reflect upstream having switched from JSON to JSON::MaybeXS.
- Introduce %%license.

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-2
- Perl 5.22 rebuild

* Thu Jan 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.59-1
- Upstream update.
- Reflect upstream URL having changed.

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-2
- Perl 5.20 rebuild

* Sun Jun 22 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.58-1
- Upstream update (Fixes FTBFS RHBZ #1105958).
- Reflect Source0: having changed.
- Reflect dep changes.
- Spec file cosmetics.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 09 2013 Petr Pisar <ppisar@redhat.com> - 0.56-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.56-1
- Upstream update.
- Disable author-tests (Broken, Fedora_19_Mass_Rebuild FTBFS).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Petr Pisar <ppisar@redhat.com> - 0.55-2
- Perl 5.16 rebuild

* Tue Jul 10 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.55-1
- Upstream update.

* Wed Jul 04 2012 Petr Pisar <ppisar@redhat.com> - 0.54-2
- Perl 5.16 rebuild

* Wed Jun 06 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.54-1
- Upstream update.

* Wed Jun 06 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.53-1
- Upstream update.
- Cleanup perl module filters.

* Mon Mar 19 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.52-1
- Upstream update.

* Sat Jan 14 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.50-1
- Abandon fedora < 15.
- Add BR: perl(Digest::MD5).
- Upstream update.
- Reflect upstream having abandoned htdocs.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 0.44-6
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.44-5
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.44-4
- Perl mass rebuild

* Thu Mar 31 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.44-3
- Add R: perl(Test::Deep) and R: perl(Test::Exception).

* Tue Mar 29 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.44-2
- Change %%bcond_with author_tests into %%bcond_without author_tests.

* Tue Mar 29 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.44-1
- Upstream update.
- Extend provides-filter to filter versioned perl(Foo), 
  perl(Bar), perl(Baz), perl(DummySerializer).
- Add %%bcond_with author_tests and %%bcond_without smoke_tests.
- Split out CHI::Test and CHI::t into separate sub-package.

* Mon Mar 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.42-1
- Upstream update.

* Mon Feb 07 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.36-1
- Initial Fedora package.
