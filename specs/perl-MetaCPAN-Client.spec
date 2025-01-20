%bcond_with network_tests

# TODO: BR: perl(HTTP::Tiny::Mech) and perl(WWW::Mechanize::Cached) when available

Name:		perl-MetaCPAN-Client
Version:	2.033000
Release:	2%{?dist}
Summary:	A comprehensive, DWIM-featured client to the MetaCPAN API
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://github.com/CPAN-API/metacpan-client
Source0:	http://www.cpan.org/authors/id/M/MI/MICKEY/MetaCPAN-Client-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(blib) >= 1.01
BuildRequires:	perl(ExtUtils::MakeMaker) > 7.11
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(HTTP::Tiny) >= 0.056
BuildRequires:	perl(IO::Socket::SSL) >= 1.42
BuildRequires:	perl(JSON::MaybeXS)
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl(Moo)
BuildRequires:	perl(Moo::Role)
BuildRequires:	perl(Net::SSLeay) >= 1.49
BuildRequires:	perl(parent)
BuildRequires:	perl(Ref::Util)
BuildRequires:	perl(Safe::Isa)
BuildRequires:	perl(strict)
BuildRequires:	perl(Type::Tiny)
BuildRequires:	perl(Types::Standard)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(warnings)
# Test suite
BuildRequires:	perl(base)
BuildRequires:	perl(File::Spec)
%if %{with network_tests}
BuildRequires:	perl(lib)
BuildRequires:	perl(LWP::Protocol::https)
%endif
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Needs) >= 0.002005
# Optional tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
# Dependencies
Requires:	perl(HTTP::Tiny) >= 0.056
Requires:	perl(IO::Socket::SSL) >= 1.42
Requires:	perl(Net::SSLeay) >= 1.49

# Filter under-specified dependency
%global __requires_exclude ^perl\\(HTTP::Tiny\\)$

%description
This is a hopefully-complete API-compliant interface to MetaCPAN
(https://metacpan.org/) with DWIM capabilities, to make your life easier.

%prep
%setup -q -n MetaCPAN-Client-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
%if !%{with network_tests}
mv t/api/[a-z]*.t t/result_custom.t t/scroll.t ./
%endif

make test

%if !%{with network_tests}
mv ./result_custom.t ./scroll.t t/
mv ./[a-z]*.t t/api/
%endif

%files
%license LICENSE
%doc Changes examples/ README
%{perl_vendorlib}/MetaCPAN/
%{_mandir}/man3/MetaCPAN::Client.3*
%{_mandir}/man3/MetaCPAN::Client::Author.3*
%{_mandir}/man3/MetaCPAN::Client::Cover.3*
%{_mandir}/man3/MetaCPAN::Client::Distribution.3*
%{_mandir}/man3/MetaCPAN::Client::DownloadURL.3*
%{_mandir}/man3/MetaCPAN::Client::Favorite.3*
%{_mandir}/man3/MetaCPAN::Client::File.3*
%{_mandir}/man3/MetaCPAN::Client::Mirror.3*
%{_mandir}/man3/MetaCPAN::Client::Module.3*
%{_mandir}/man3/MetaCPAN::Client::Package.3*
%{_mandir}/man3/MetaCPAN::Client::Permission.3*
%{_mandir}/man3/MetaCPAN::Client::Pod.3*
%{_mandir}/man3/MetaCPAN::Client::Rating.3*
%{_mandir}/man3/MetaCPAN::Client::Release.3*
%{_mandir}/man3/MetaCPAN::Client::Request.3*
%{_mandir}/man3/MetaCPAN::Client::ResultSet.3*
%{_mandir}/man3/MetaCPAN::Client::Role::Entity.3*
%{_mandir}/man3/MetaCPAN::Client::Role::HasUA.3*
%{_mandir}/man3/MetaCPAN::Client::Scroll.3*
%{_mandir}/man3/MetaCPAN::Client::Types.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.033000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Paul Howarth <paul@city-fan.org> - 2.033000-1
- Update to 2.033000
  - Remove backpan_directory option (GH#127)
- Switch upstream source URL from cpan.metacpan.org to www.cpan.org

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.032000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 16 2024 Paul Howarth <paul@city-fan.org> - 2.032000-1
- Update to 2.032000
  - Fix scroller issues (GH#123)
  - Removed rating fetching (GH#124)
  - Fix example script

* Tue Mar 12 2024 Paul Howarth <paul@city-fan.org> - 2.031001-1
- Update to 2.031001
  - Show a real error for internal errors (GH#121)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.031000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.031000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov  1 2023 Paul Howarth <paul@city-fan.org> - 2.031000-1
- Update to 2.031000
  - Fix reverse-dependencies distributions check (GH#119)
  - In examples, 'use Data::Printer' instead of shortened 'use DDP' (GH#120)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.030000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.030000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 22 2022 Paul Howarth <paul@city-fan.org> - 2.030000-1
- Update to 2.030000
  - Set verify_SSL=>1 for default HTTP::Tiny user agent (GH#113)
  - Updated docs (GH#111)
- Use SPDX-format license tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.029000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.029000-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.029000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.029000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.029000-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.029000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Paul Howarth <paul@city-fan.org> - 2.029000-1
- Update to 2.029000
  - Added checksum_sha256 and checksum_md5 fields support (GH#110)
  - Clean up old files
- This release by MICKEY → update source URL
- Drop fav.pl sample script, no longer included in upstream release

* Mon Aug 24 2020 Paul Howarth <paul@city-fan.org> - 2.028000-1
- Update to 2.028000
  - Support specific versions in download_url (GH#107)

* Wed Aug 12 2020 Paul Howarth <paul@city-fan.org> - 2.027000-2
- Package fav.pl as documentation rather than as a module

* Tue Aug 11 2020 Paul Howarth <paul@city-fan.org> - 2.027000-1
- Update to 2.027000
  - Run Travis tests with more Perls (GH#102)
  - Show example of result (GH#105)
  - Bump minimum version of WWW::Mechanize::Cached to 1.54 (GH#104)
- This release by OALDERS → update source URL
- Fix permissions of installed files to silence rpmlint

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.026000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.026000-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.026000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.026000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.026000-2
- Perl 5.30 rebuild

* Thu Mar 14 2019 Paul Howarth <paul@city-fan.org> - 2.026000-1
- Update to 2.026000
  - Added example script top20_favorites.pl
  - Updated SYNOPSIS for Favorite
  - Fixed link to Search Spec (GH#101)
  - Fixed typo in error message (GH#100)
- Simplify spec using %%{make_build} and %%{make_install}

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.025000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.025000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.025000-2
- Perl 5.28 rebuild

* Mon Apr 23 2018 Paul Howarth <paul@city-fan.org> - 2.025000-1
- Update to 2.025000
  - Fix warning on a JSON::PP::Boolean check
  - Added support for the new 'cover' index - cpancover.org info

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.023000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Paul Howarth <paul@city-fan.org> - 2.023000-1
- Update to 2.023000
  - Support the new 'deprecated' field in File and Release types

* Thu Jan  4 2018 Paul Howarth <paul@city-fan.org> - 2.022000-1
- Update to 2.022000
  - Allow user-defined target classes in ResultSet
  - Added test for reverse dependencies
  - Switched ref() checks to Ref::Util::is_ref

* Sun Nov 19 2017 Paul Howarth <paul@city-fan.org> - 2.021000-1
- Update to 2.021000
  - Added support for /search/autocomplete/suggest
  - Scroller fix for page skipping
  - Sorting in scrolled searches
  - Type check cleanup

* Fri Nov 17 2017 Paul Howarth <paul@city-fan.org> - 2.019000-1
- Update to 2.019000
  - Added 'package' type support for scrolled searches

* Tue Oct 17 2017 Paul Howarth <paul@city-fan.org> - 2.018000-1
- Update to 2.018000
  - Fix fetch URL (GH#92)
  - Removed critic author test

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.017000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Paul Howarth <paul@city-fan.org> - 2.017000-1
- Update to 2.017000
  - reverse_dependencies: Update link to new API endpoint (GH#89)

* Fri Jun 09 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.016000-2
- Perl 5.26 rebuild

* Thu Jun  8 2017 Paul Howarth <paul@city-fan.org> - 2.016000-1
- Update to 2.016000
  - Support CSV field list in 'all' requests (GH#87)

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.015000-2
- Perl 5.26 rebuild

* Sun May 14 2017 Paul Howarth <paul@city-fan.org> - 2.015000-1
- Update to 2.015000
  - Fixed single-value case for expected arrayref (GH#84)
  - Added support for new release/contributors endpoint
  - Added 'main_module' field to the Release object
  - Updated documentation (GH#85)

* Fri May 12 2017 Paul Howarth <paul@city-fan.org> - 2.013001-1
- Update to 2.013001
  - Updated endpoint name following API change

* Tue May  9 2017 Paul Howarth <paul@city-fan.org> - 2.013000-1
- Update to 2.013000
  - Added support for new 'package' type

* Thu Apr 27 2017 Paul Howarth <paul@city-fan.org> - 2.012000-1
- Update to 2.012000
  - Fixed 'email' field handling in Author objects (GH#83)

* Wed Apr 19 2017 Paul Howarth <paul@city-fan.org> - 2.011000-1
- Update to 2.011000
  - Added support for scroller time/size params
  - Removed warning of scroller deletion failure (GH#81)

* Tue Apr  4 2017 Paul Howarth <paul@city-fan.org> - 2.010000-1
- Update to 2.010000
  - Added support for new 'permission' type

* Wed Mar 29 2017 Paul Howarth <paul@city-fan.org> - 2.009001-1
- Update to 2.009001
  - Use Test::Needs to force a minimum WWW::Mechanize::Cached version (GH#76)

* Fri Mar 24 2017 Paul Howarth <paul@city-fan.org> - 2.009000-1
- Update to 2.009000
  - Bump WWW::Mechanize::Cached version to 1.50 (GH#76)
  - Require LWP::Protocol::https in tests (GH#79)
  - Added 'changes' method for Release objects (GH#57)
  - Cleaner URLs - removed redundant slashes and 'v1'
  - Created a role for user-agent handling for reuse

* Thu Mar 23 2017 Paul Howarth <paul@city-fan.org> - 2.008001-1
- Update to 2.008001
  - Added metacpan_url method to the entity objects (GH#69)
  - Fixed t/scroll.t

* Wed Mar  8 2017 Paul Howarth <paul@city-fan.org> - 2.007000-1
- Update to 2.007000
  - Update tests for newer Perl versions, to run without '.' in @INC (GH#72)

* Fri Feb 24 2017 Paul Howarth <paul@city-fan.org> - 2.006000-1
- Update to 2.006000
  - Support '_source' filtering (GH#70)
  - Support debug-mode for detailed error messages

* Tue Feb 14 2017 Paul Howarth <paul@city-fan.org> - 2.005000-1
- Update to 2.005000
  - Added the ascii_name and perlmongers fields to the Author object (GH#66)
  - Fixed Author->dir to actually return something (GH#66)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.004000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Paul Howarth <paul@city-fan.org> - 2.004000-2
- Update to non-trial release
  - Speed up own scroller
  - Fixed rev_deps

* Tue Dec 27 2016 Paul Howarth <paul@city-fan.org> - 2.004000-1
- Update to 2.004000
  - Removed dependency: Search::Elasticsearch in favour of an internal scroller
  - Added Types class for 'isa' checks

* Mon Dec 19 2016 Paul Howarth <paul@city-fan.org> - 2.003000-1
- Update to 2.003000
  - Escaped query to autocomplete
  - Removed dependency: Try::Tiny

* Wed Dec 14 2016 Paul Howarth <paul@city-fan.org> - 2.002000-1
- Update to 2.002000
  - Support 'autocomplete' endpoint

* Fri Dec  9 2016 Paul Howarth <paul@city-fan.org> - 2.001000-1
- Update to 2.001000
  - Distribution: added 'rt' and 'github' methods
  - Use Ref::Util for ref checks

* Sat Nov 19 2016 Paul Howarth <paul@city-fan.org> - 2.000000-1
- Update to 2.000000
  - Major version: v1 full support
    - Removed support and default settings for v0
    - Corrected domain, base_url setting, using clientinfo
    - Code/tests updates and cleanup
  - Pinned Search::Elasticsearch version to 2.03
  - Use @Starter in dist.ini + cpanfile cleanup

* Mon Oct 24 2016 Paul Howarth <paul@city-fan.org> - 1.028003-1
- Update to 1.028003
  - Removed AutoPrereqs from dist.ini

* Sun Oct 23 2016 Paul Howarth <paul@city-fan.org> - 1.028002-1
- Update to 1.028002
  - Remove hard-deps for HTTP::Tiny::Mech and WWW::Mechanize::Cached (GH#50)
  - dist.ini: Don't automatically update cpanfile
  - Add eumm_version to dist.ini (GH#51)
  - Stop excluding cpanfile from being copied to build (GH#52)
  - A few small dist.ini tweaks (GH#53)
  - Even more dist.ini tweaks

* Thu Oct 20 2016 Paul Howarth <paul@city-fan.org> - 1.027000-1
- Update to 1.027000
  - Convert values of JSON::PP::Boolean objects in output so they are not
    skipped when expecting scalars (GH#49)

* Thu Oct 20 2016 Paul Howarth <paul@city-fan.org> - 1.026001-1
- Update to 1.026001
  - Moved distini prereqs to cpanfile
  - Limit Search::Elasticsearch version to 2.02
  - Updated docs
- Conflict with Search::Elasticsearch ≥ 5.00
  (https://github.com/metacpan/metacpan-client/issues/48)

* Tue Aug 30 2016 Paul Howarth <paul@city-fan.org> - 1.025000-1
- Update to 1.025000
  - Added some version requirements to improve SSL over HTTP::Tiny
  - Added default values for distribution keys with no content

* Mon Aug 29 2016 Paul Howarth <paul@city-fan.org> - 1.024000-1
- Update to 1.024000
  - Try to fetch clientinfo from https://clientinfo.metacpan.org to get
    default production version

* Sat Aug 27 2016 Paul Howarth <paul@city-fan.org> - 1.023000-1
- Update to 1.023000
  - Added support for version by env METACPAN_VERSION
  - Added tests for version argument

* Sun Aug  7 2016 Paul Howarth <paul@city-fan.org> - 1.022003-1
- Update to 1.022003
  - Fixed a warning in $file->pod

* Sat Aug  6 2016 Paul Howarth <paul@city-fan.org> - 1.022002-1
- Update to 1.022002
  - Added LWP::Protocol::https as test dependency

* Fri Aug  5 2016 Paul Howarth <paul@city-fan.org> - 1.022001-1
- Update to 1.022001
  - Rework type checking - enforce expected types, including single-valued
    array-ref unwrapping; doesn't break types that are expected to be
    array-refs
  - Check user provided UA for 'get' and 'post' methods
  - Documentation updates

* Thu Jul 28 2016 Paul Howarth <paul@city-fan.org> - 1.021000-1
- Update to 1.021000
  - Fix result values in v1 - single valued arrayref in ES result will be
    turned to a scalar

* Tue Jul 12 2016 Paul Howarth <paul@city-fan.org> - 1.020000-1
- Update to 1.020000
  - Added support for Author->release_count and Author->links methods
  - Added support for url_prefix parameter for Pod

* Wed Jul  6 2016 Paul Howarth <paul@city-fan.org> - 1.019000-1
- Update to 1.019000
  - Added missing 'download_url' attribute to file/module result objects

* Wed Jul  6 2016 Paul Howarth <paul@city-fan.org> - 1.018000-1
- Update to 1.018000
  - Added support for download_url endpoint
  - Default domain set by providing 'version' - makes it easy to work with v1
- Use recent EU:MM's NO_PERLLOCAL option
- Drop legacy Group: tag

* Tue Jun 28 2016 Paul Howarth <paul@city-fan.org> - 1.017000-1
- Update to 1.017000
  - Fixed nodes list for Search::Elasticsearch
  - Added support for 'aggregations'
- Use recent EU:MM's NO_PACKLIST option

* Mon Jun 27 2016 Paul Howarth <paul@city-fan.org> - 1.016000-1
- Update to 1.016000
  - Added support for 'all' filters type 'files'
  - http → https
- BR: perl-generators

* Fri Jun  3 2016 Paul Howarth <paul@city-fan.org> - 1.015000-1
- Update to 1.015000
  - Adding 'source' method to MetaCPAN::Client::File
- This release by MICKEY → update source URL

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.014000-2
- Perl 5.24 rebuild

* Fri Apr 29 2016 Paul Howarth <paul@city-fan.org> - 1.014000-1
- Update to 1.014000
  - Fix warning on missing fields param
  - Switch to Search::Elasticsearch 2.0
  - You can test MetaCPAN::Client with a different domain using the
    environment variable "METACPAN_DOMAIN"
- This release by XSAWYERX → update source URL
- Simplify find command using -delete
- POD tests are now author tests rather than release tests, so drop hack for
  running them

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.013000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.013000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.013000-2
- Perl 5.22 rebuild

* Sun Apr 26 2015 Paul Howarth <paul@city-fan.org> - 1.013000-1
- Update to 1.013000
  - Use Travis for CI (GH#34)
  - Improve Kwalitee + test improvements (GH#35)

* Thu Apr  9 2015 Paul Howarth <paul@city-fan.org> - 1.012000-1
- Update to 1.012000
  - Added Mirror type and support for mirrors search in 'all' queries (GH#33)
  - Support 'ratings' search in 'all' queries (GH#33)
  - More example scripts: facets, top favorites, all authors blogs
  - Clean-up and documentation updates

* Tue Jan 27 2015 Paul Howarth <paul@city-fan.org> - 1.011000-1
- Update to 1.011000
  - Support 'favorites' type and 'facets' key param in 'all' queries

* Fri Jan 23 2015 Paul Howarth <paul@city-fan.org> - 1.010000-1
- Update to 1.010000
  - Support wildcard-only value in complex search
  - Support raw Elasticsearch filters in 'all' queries

* Mon Jan 12 2015 Paul Howarth <paul@city-fan.org> - 1.009000-1
- Update to 1.009000
  - Added support for 'fields' filtering (GH#25, CPAN RT#99499)
- This release by MICKEY → update source URL

* Tue Jan  6 2015 Paul Howarth <paul@city-fan.org> - 1.008001-1
- Update to 1.008001
  - Correct Meta resources for the repo
  - Correct link in POD for the Pod element
- This release by XSAWYERX → update source URL

* Sat Nov 22 2014 Paul Howarth <paul@city-fan.org> - 1.008000-1
- Update to 1.008000
  - CPAN RT#99498: added API for 'match_all' queries via all($type)
  - GH#21: make 'domain' and 'version' settable via new()
  - CPAN  RT#94491: document nested queries

* Thu Oct  9 2014 Paul Howarth <paul@city-fan.org> - 1.007001-1
- Update to 1.007001
  - GH#18: HTTP::Tiny::Mech and WWW::Mechanize::Cached downgraded to being
    non-essential for tests
  - GH#19: Include 'metadata' in known_fields for ::Release
- Make the POD tests author tests instead of release tests so we can run them

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.007000-2
- Perl 5.20 rebuild

* Tue Aug 19 2014 Paul Howarth <paul@city-fan.org> - 1.007000-1
- Update to 1.007000
  - Ensure passing user-specified ua values to all parts internally, including
    to Elasticsearch (GH #17, CPAN RT#95796)
  - Entity-consuming roles now have a 'client' attribute that will lazy build,
    or reference the MetaCPAN::Client that created them via new_from_request
    (GH #17)
- Use %%license
- Upstream dropped switching to filters document
- Skip the release tests for now because of missing optional test dependencies
  and failing Pod Coverage test with Moo ≥ 1.005
  (#1124400, https://github.com/CPAN-API/metacpan-client/issues/16)

* Tue Jun 24 2014 Paul Howarth <paul@city-fan.org> - 1.006000-1
- Update to 1.006000
  - Add 'recent' functionality (latest releases)

* Tue Jun 10 2014 Paul Howarth <paul@city-fan.org> - 1.005000-1
- Update to 1.005000
  - Add Pod object to allow direct POD fetching
  - Support single element without wrapping arrayref in structures
  - Updated documents - basic/complex search links and wording
- Package additional documentation file on switching to filters

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.004001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Paul Howarth <paul@city-fan.org> - 1.004001-1
- Update to 1.004001
  - Reworked ResultSet to allow RS in non-scrolled searches
  - Correct rev_deps query
- This release by MICKEY → update source URL

* Sun May  4 2014 Paul Howarth <paul@city-fan.org> - 1.003000-1
- Update to 1.003000
  - Add proper POD fetching from module/file objects.
  - GH #1: Switch from JSON.pm to JSON::MaybeXS
  - GH #2: Remove incorrect and unnecessary check for class names
  - Provide "ua" attribute in the main object to override user agent
  - Add some use-case examples (examples directory)
  - Add 'releases' method to Author (not official so no docs yet)
  - GH #4: Use example with hyphen
  - Related to GH #4, use Data::Printer instead of shortened name "DDP"
- This release by XSAWYERX → update source URL

* Fri Apr 25 2014 Paul Howarth <paul@city-fan.org> - 1.002000-2
- Sanitize for Fedora submission

* Thu Apr 24 2014 Paul Howarth <paul@city-fan.org> - 1.002000-1
- Update to 1.002000
  - Add 'not' support for complex queries
  - Add reverse_dependencies method

* Wed Apr 16 2014 Paul Howarth <paul@city-fan.org> - 1.001001-1
- Update to 1.001001
  - Fix the reading of scroller result when 'fields' param is passed

* Thu Apr 10 2014 Paul Howarth <paul@city-fan.org> - 1.001000-1
- Update to 1.001000
  - Add support for nested either/all queries
  - Add tests for complex queries (two levels deep)
  - Correct documentation on complex queries
  - Update tests to work on older versions of perl

* Thu Apr  3 2014 Paul Howarth <paul@city-fan.org> - 1.000001-1
- Update to 1.000001
  - Changed Elasticsearch (deprecated) to Search::Elasticsearch (official)

* Wed Apr  2 2014 Paul Howarth <paul@city-fan.org> - 1.000000-1
- Initial RPM version
