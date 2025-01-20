Name:		perl-Mail-Message
Version:	3.016
Release:	2%{?dist}
Summary:	MIME message handling
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Mail-Message
Source0:	https://www.cpan.org/modules/by-module/Mail/Mail-Message-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Date::Format)
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(Encode) >= 2.26
BuildRequires:	perl(Encode::Alias)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec) >= 0.7
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(HTML::FormatPS)
BuildRequires:	perl(HTML::FormatText) >= 2.01
BuildRequires:	perl(HTML::TreeBuilder) >= 3.13
BuildRequires:	perl(integer)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IO::Lines)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Mail::Address) >= 2.17
BuildRequires:	perl(Mail::Header)
BuildRequires:	perl(Mail::Identity)
BuildRequires:	perl(Mail::Internet) >= 2.01
%if !%{defined perl_bootstrap}
BuildRequires:	perl(Mail::Transport::Send)
%endif
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(MIME::Entity) >= 3.0
BuildRequires:	perl(MIME::Parser)
BuildRequires:	perl(MIME::QuotedPrint)
BuildRequires:	perl(MIME::Types) >= 1.004
BuildRequires:	perl(Net::Domain)
BuildRequires:	perl(overload)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util) >= 1.13
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Text::Autoformat)
BuildRequires:	perl(Time::HiRes) >= 1.51
BuildRequires:	perl(Time::Zone)
BuildRequires:	perl(URI) >= 1.23
BuildRequires:	perl(User::Identity) >= 1.02
BuildRequires:	perl(User::Identity::Collection::Emails)
BuildRequires:	perl(utf8)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Data::Dumper)
# Optional Tests
%if !%{defined perl_bootstrap}
BuildRequires:	perl(Email::Abstract)
%endif
# Dependencies
Requires:	perl(Date::Parse)
%if !%{defined perl_bootstrap}
Requires:	perl(Mail::Transport::Send)
%endif
Requires:	perl(Net::Domain)
Requires:	perl(Time::HiRes) >= 1.51
Requires:	perl(Time::Zone)
Requires:	perl(User::Identity) >= 1.02

# I'm not sure why these provides aren't getting picked up automatically.
Provides:	perl(Mail::Message::Body::Construct) = %{version}
Provides:	perl(Mail::Message::Construct) = %{version}
Provides:	perl(Mail::Message::Construct::Bounce) = %{version}
Provides:	perl(Mail::Message::Construct::Build) = %{version}
Provides:	perl(Mail::Message::Construct::Forward) = %{version}
Provides:	perl(Mail::Message::Construct::Read) = %{version}
Provides:	perl(Mail::Message::Construct::Rebuild) = %{version}
Provides:	perl(Mail::Message::Construct::Reply) = %{version}
Provides:	perl(Mail::Message::Construct::Text) = %{version}

%description
MIME message handling code, formerly part of the Mail::Box package.

%prep
%setup -q -n Mail-Message-%{version}
# The licensing on these test files is unclear.
# They seem to contain content posted publicly to usenet
# so there is an argument that the content is distributable
# but it's not under a Free license.
# We delete these files to resolve the issue.
# https://rt.cpan.org/Public/Bug/Display.html?id=120149
rm -rf t/203-mlfolder.mbox t/204-sgfolder.mbox
rm -rf t/203head-listgroup.t t/204head-spamgroup.t
perl -i -ne 'print $_ unless m{^t/20[34]-(ml|sg)folder\.mbox$}' MANIFEST
perl -i -ne 'print $_ unless m{^t/20[34]head-(list|spam)group\.t$}' MANIFEST

%build
yes y |perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ChangeLog README README.md
%{perl_vendorlib}/Mail/
%{_mandir}/man3/Mail::*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Paul Howarth <paul@city-fan.org> - 3.016-1
- Update to 3.016 (rhbz#2329121)
- Switch source URL from cpan.metacpan.org to www.cpan.org

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Paul Howarth <paul@city-fan.org> - 3.015-1
- Update to 3.015 (rhbz#2253976)

* Wed Oct 18 2023 Paul Howarth <paul@city-fan.org> - 3.014-1
- Update to 3.014 (rhbz#2244805)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Paul Howarth <paul@city-fan.org> - 3.013-1
- Update to 3.013 (rhbz#2217164)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.012-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.012-3
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.012-2
- Perl 5.36 rebuild

* Tue Mar  1 2022 Paul Howarth <paul@city-fan.org> - 3.012-1
- Update to 3.012
- Use author-independent source URL
- Classify buildreqs by usage
- Drop redundant %%{?perl_default_filter}
- Drop recoding of Mail::Message::Field manpage since it has changed to UTF-8
  coding upstream
- Package README.md too (guide for contributors)
- Fix permissions verbosely

* Wed Jan 26 2022 Paul Howarth <paul@city-fan.org> - 3.011-3
- EPEL-9 post-bootstrap rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Tom Callaway <spot@fedoraproject.org> - 3.011-1
- update to 3.011

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.010-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.010-4
- Perl 5.34 re-rebuild of bootstrapped packages

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.010-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Tom Callaway <spot@fedoraproject.org> - 3.010-1
- update to 3.010

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.009-3
- Perl 5.32 re-rebuild of bootstrapped packages

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.009-2
- Perl 5.32 rebuild

* Tue Feb 11 2020 Tom Callaway <spot@fedoraproject.org> - 3.009-1
- update to 3.009

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.008-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.008-2
- Perl 5.30 rebuild

* Mon Feb 11 2019 Tom Callaway <spot@fedoraproject.org> - 3.008-1
- update to 3.008

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep  5 2018 Tom Callaway <spot@fedoraproject.org> - 3.007-1
- update to 3.007

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-4
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-1
- 3.006 bump

* Wed Jan 10 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-1
- 3.005 bump

* Wed Sep 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-1
- 3.002 bump

* Fri Jul 28 2017 Tom Callaway <spot@fedoraproject.org> - 3.001-1
- update to 3.001

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.000-6
- Perl 5.26 re-rebuild of bootstrapped packages

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.000-5
- Added perl_bootstrap to avoid build cycle

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.000-4
- Perl 5.26 rebuild

* Thu Feb  9 2017 Tom Callaway <spot@fedoraproject.org> - 3.000-3
- remove unnecessary requires filtering
- add necessary explicit Requires

* Wed Feb  8 2017 Tom Callaway <spot@fedoraproject.org> - 3.000-2
- fix buildrequires
- remove non-free test cases

* Tue Feb  7 2017 Tom Callaway <spot@fedoraproject.org> - 3.000-1
- initial package
