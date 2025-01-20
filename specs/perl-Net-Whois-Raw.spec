%global cpan_version 2.99040

Name:           perl-Net-Whois-Raw
# Keep 2-digit precision
Version:        %(echo '%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Release:        2%{?dist}
Summary:        Get Whois information for domains
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Whois-Raw
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Whois-Raw-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{_bindir}/iconv
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Data::Dumper not used at tests
BuildRequires:  perl(Encode)
# HTTP::Headers not used at tests
# HTTP::Request not used at tests
BuildRequires:  perl(IO::Socket::IP)
# LWP::UserAgent not used at tests
BuildRequires:  perl(Regexp::IPv6)
# URI::URL not used at tests
BuildRequires:  perl(utf8)

# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
Requires:       perl(Data::Dumper)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::UserAgent)
Requires:       perl(URI::URL)

%description
Net::Whois::Raw queries WHOIS servers about domains. The module supports
recursive WHOIS queries. Also queries via HTTP is supported for some TLDs.

%prep
%setup -q -n Net-Whois-Raw-%{cpan_version}
perl -pi -e 's/^#!.*perl/#!\/usr\/bin\/perl/' bin/pwhois

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE COPYRIGHT
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n pwhois
Summary:        Perl written whois client
# Getopt::Long not used at tests
# Net::IDN::Punycode 1 not used at tests
# Win32API::Registry not used on Linux
Requires:       perl(Getopt::Long) >= 2
Requires:       perl(Net::IDN::Punycode) >= 1
# Win32API::Registry not used on Linux

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Getopt::Long\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Net::IDN::Punycode\\)$

%description -n pwhois
Command line whois client.  Invoke with a domain name, optionally with a whois
server name.

%files -n pwhois
%license LICENSE COPYRIGHT
%doc README
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.040-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 18 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.040-1
- Update to 2.99.040

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.039-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 27 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.039-1
- Update to 2.99.039

* Sun Apr 07 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.038-1
- Update to 2.99.038
- Migrate to SPDX license

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.037-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.037-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.037-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.037-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 14 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.037-2
- Bump to rebuild

* Sun Aug 14 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.037-1
- Update to 2.99.037

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.036-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.036-1
- Update to 2.99.036
- Use /usr/bin/perl instead of %%{__perl}

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.034-2
- Perl 5.36 rebuild

* Sun Apr 24 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.034-1
- Update to 2.99.034

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 29 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.032-1
- Update to 2.99.032

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.031-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.031-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.031-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 20 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.031-1
- Update to 2.99.031

* Sun Aug 16 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.030-1
- Update to 2.99.030

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.029-1
- Update to 2.99.029

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.028-2
- Perl 5.32 rebuild

* Sun May 17 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.028-1
- Update to 2.99.028

* Sun Mar 01 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.99.027-1
- Update to 2.99.027
- Use %%{make_install} instead of make "pure_install"
- Use %%{make_build} instead of make

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.026-1
- 2.99026 bump

* Thu Oct 24 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.025-1
- 2.99025 bump

* Wed Oct 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.024-1
- 2.99024 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.022-1
- 2.99022 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.021-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.021-1
- 2.99021 bump

* Tue Sep 25 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.020-1
- 2.99020 bump

* Thu Aug 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.018-1
- 2.99018 bump

* Mon Aug 06 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.016-1
- 2.99016 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.015-2
- Perl 5.28 rebuild

* Mon Jun 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.015-1
- 2.99015 bump

* Wed May 09 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.014-1
- 2.99014 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.013-1
- 2.99013 bump

* Mon Nov 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.011-1
- 2.99011 bump

* Mon Aug 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.010-1
- 2.99010 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.009-1
- 2.99009 bump

* Tue Jun 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.008-1
- 2.99008 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.006-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.99.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.006-1
- 2.99006 bump

* Thu Aug 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.99.001-1
- 2.99001 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.94-2
- Perl 5.24 rebuild

* Thu Mar 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.94-1
- 2.94 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.91-1
- 2.91 bump

* Wed Sep 23 2015 Petr Pisar <ppisar@redhat.com> - 2.86-1
- 2.86 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.82-2
- Perl 5.22 rebuild

* Sat Feb 14 2015 David Dick <ddick@cpan.org> - 2.82-1
- New TLDs for .MOSCOW and fix encoding for whois.jprs.jp

* Tue Jan 20 2015 David Dick <ddick@cpan.org> - 2.80-1
- New TLDs

* Mon Jul 07 2014 David Dick <ddick@cpan.org> - 2.76-1
- Initial release
