# Add support for DNS resolution
%bcond_without perl_POE_Component_IRC_enables_dns
# Enable IPv6 support
%bcond_without perl_POE_Component_IRC_enables_ipv6
# Enable SSL support
%bcond_without perl_POE_Component_IRC_enables_ssl
# Enable zlib compression
%bcond_without perl_POE_Component_IRC_enables_zlib

Name:           perl-POE-Component-IRC
Summary:        A POE component for building IRC clients
Version:        6.93
Release:        13%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Component-IRC-%{version}.tar.gz 
URL:            https://metacpan.org/release/POE-Component-IRC
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode::Guess)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IRC::Utils) >= 0.12
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(overload)
BuildRequires:  perl(POE) >= 1.311
%if %{with perl_POE_Component_IRC_enables_dns}
BuildRequires:  perl(POE::Component::Client::DNS) >= 0.99
%endif
%if %{with perl_POE_Component_IRC_enables_ssl}
# POE::Component::SSLify not used at tests
%endif
BuildRequires:  perl(POE::Component::Syndicator)
BuildRequires:  perl(POE::Driver::SysRW)
BuildRequires:  perl(POE::Filter)
BuildRequires:  perl(POE::Filter::IRCD) >= 2.42
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Stackable)
BuildRequires:  perl(POE::Filter::Stream)
%if %{with perl_POE_Component_IRC_enables_zlib}
BuildRequires:  perl(POE::Filter::Zlib::Stream) >= 1.96
%endif
BuildRequires:  perl(POE::Wheel::FollowTail)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
# Tests:
BuildRequires:  perl(Crypt::PasswdMD5)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Net::Netmask)
BuildRequires:  perl(POE::Component::Client::Ident::Agent)
# TODO: Unbundle POE::Component::Server::IRC
%if %{with perl_POE_Component_IRC_enables_ipv6}
BuildRequires:  perl(Socket::GetAddrInfo)
%endif
BuildRequires:  perl(Test::Differences) >= 0.61
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(vars)
Requires:       perl(IRC::Utils) >= 0.12
Requires:       perl(List::Util) >= 1.33
Requires:       perl(overload)
Requires:       perl(POE) >= 1.311
%if %{with perl_POE_Component_IRC_enables_dns}
Recommends:     perl(POE::Component::Client::DNS) >= 0.99
%endif
%if %{with perl_POE_Component_IRC_enables_ssl}
Recommends:     perl(POE::Component::SSLify)
%endif
Requires:       perl(POE::Driver::SysRW)
Requires:       perl(POE::Filter::IRCD) >= 2.42
Requires:       perl(POE::Filter::Line)
Requires:       perl(POE::Filter::Stream)
%if %{with perl_POE_Component_IRC_enables_zlib}
Recommends:     perl(POE::Filter::Zlib::Stream) >= 1.96
%endif
Requires:       perl(POE::Wheel::FollowTail)
Requires:       perl(POE::Wheel::ReadWrite)
Requires:       perl(POE::Wheel::SocketFactory)

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((IRC::Utils|List::Util|POE|POE::Filter::IRCD|Test::Differences|Test::More)\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(POE::Component::Server::IRC.*\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((POE::Component::IRC::Test::Plugin|POE::Component::Server::IRC.*)\\)

%description
POE::Component::IRC is a POE component (who'd have guessed?) which acts as an
easily controllable IRC client for your other POE components and sessions. You
create an IRC component and tell it what events your session cares about and
where to connect to, and it sends back interesting IRC events when they
happen. You make the client do things by sending it events. That's all there
is to it. Cool, no?

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(IRC::Utils) >= 0.12
Requires:       perl(List::Util) >= 1.33
Requires:       perl(POE) >= 1.311
%if %{with perl_POE_Component_IRC_enables_dns}
Requires:       perl(POE::Component::Client::DNS) >= 0.99
%endif
Requires:       perl(POE::Filter::IRCD) >= 2.42
Requires:       perl(POE::Filter::Line)
%if %{with perl_POE_Component_IRC_enables_zlib}
Requires:       perl(POE::Filter::Zlib::Stream) >= 1.96
%endif
Requires:       perl(POE::Wheel::ReadWrite)
Requires:       perl(POE::Wheel::SocketFactory)
%if %{with perl_POE_Component_IRC_enables_ipv6}
Requires:       perl(Socket::GetAddrInfo)
%endif
Requires:       perl(Test::Differences) >= 0.61
Requires:       perl(Test::More) >= 0.47
Provides:       bundled(POE-Component-Server-IRC) = 1.52

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n POE-Component-IRC-%{version}
chmod -c -x examples/*
# Remove bundled modules
for D in t/inc/Crypt t/inc/Net; do
    rm -r "$D"
    perl -i -ne 'print $_ unless m{\A\Q'"$D"'\E/}' MANIFEST
done
# Remove online tests
for T in t/02_behavior/06_online.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{\A\Q'"$T"'\E\b}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in $(find t -type f -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a Changes t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/04_plugins/17_dcc/04_send_spaces.t writes to CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes docs/ examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.93-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 6.93-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.93-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.93-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.93-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.93-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.93-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.93-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Michal Josef Špaček <mspacek@redhat.com> - 6.93-2
- Remove obsolete require for Socket6

* Wed Jun 16 2021 Petr Pisar <ppisar@redhat.com> - 6.93-1
- 6.93 bump

* Tue Jun 08 2021 Petr Pisar <ppisar@redhat.com> - 6.92-1
- 6.92 bump

* Mon Jun 07 2021 Petr Pisar <ppisar@redhat.com> - 6.91-1
- 6.91 bump
- Package the tests
- Unbundle Net::Netmask

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.90-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.90-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.90-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.90-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.90-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.90-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.90-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Petr Pisar <ppisar@redhat.com> - 6.90-1
- 6.90 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.88-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.88-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.88-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.88-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.88-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.88-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.88-3
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.88-2
- Perl 5.20 rebuild

* Mon Jun 30 2014 Petr Šabata <contyk@redhat.com> - 6.88-1
- 6.88 bump

* Mon Jun 23 2014 Petr Šabata <contyk@redhat.com> - 6.87-1
- 6.87 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.83-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 6.83-2
- Perl 5.18 rebuild

* Tue May 28 2013 Petr Šabata <contyk@redhat.com> - 6.83-1
- 6.83 enhancement bump

* Mon Mar 11 2013 Petr Šabata <contyk@redhat.com> - 6.82-1
- 6.82 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Petr Šabata <contyk@redhat.com> - 6.81-3
- Correct the Obsoletes tests version to 6.81, thanks to Ralf Corsepius

* Mon Nov 26 2012 Petr Šabata <contyk@redhat.com> - 6.81-2
- Obsolete tests < v2.81 to be more future-proof

* Mon Nov 26 2012 Petr Šabata <contyk@redhat.com> - 6.81-1
- 6.81 bump
- Drop command macros
- Drop the tests subpackage

* Thu Sep 20 2012 Petr Pisar <ppisar@redhat.com> - 6.80-1
- 6.80 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.78-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 6.78-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Petr Šabata <contyk@redhat.com> - 6.78-1
- 6.78 bump (just tests)

* Mon Dec 05 2011 Petr Šabata <contyk@redhat.com> - 6.77-1
- 6.77 bump

* Tue Nov 29 2011 Petr Šabata <contyk@redhat.com> - 6.76-1
- 6.76 bump

* Mon Nov 14 2011 Petr Šabata <contyk@redhat.com> - 6.75-1
- 6.75 bump

* Mon Oct 10 2011 Petr Sabata <contyk@redhat.com> - 6.74-1
- 6.74 bump

* Mon Sep 19 2011 Petr Sabata <contyk@redhat.com> - 6.71-1
- 6.71 bump

* Thu Aug  4 2011 Petr Sabata <contyk@redhat.com> - 6.68-1
- 6.70 bump
- Remove defattr and some forgotten buildroot stuff

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 6.52-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 Marcela Mašláňová <mmaslano@redhat.com> 6.52-2
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- altered br on perl(ExtUtils::MakeMaker) (6.42 => 6.31)
- added a new br on perl(Object::Pluggable) (version 0)
- altered br on perl(POE) (0.3202 => 1.287)
- altered br on perl(POE::Filter::IRCD) (1.7 => 2.42)
- added a new br on perl(POE::Session) (version 0)
- dropped old BR on perl(Encode)
- dropped old BR on perl(Encode::Guess)
- dropped old BR on perl(POE::Component::Client::DNS)
- dropped old BR on perl(POE::Component::Pluggable)
- dropped old BR on perl(POE::Filter::Zlib::Stream)
- dropped old BR on perl(Socket6)
- dropped old BR on perl(Test::Pod)
- dropped old BR on perl(Test::Pod::Coverage)
- added a new req on perl(Object::Pluggable) (version 0)
- altered req on perl(POE) (0.3202 => 1.287)
- altered req on perl(POE::Filter::IRCD) (1.7 => 2.42)
- added a new req on perl(POE::Session) (version 0)
- dropped old requires on perl(Encode)
- dropped old requires on perl(Encode::Guess)
- dropped old requires on perl(POE::Component::Pluggable)

* Thu May 20 2010 Iain Arnell <iarnell@gmail.com> 6.14-4
- apply patch for rhbz#591215

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 6.14-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 6.14-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 6.14-1
- auto-update to 6.14 (by cpan-spec-update 0.01)
- altered br on perl(POE::Component::Pluggable) (1.12 => 1.24)
- altered req on perl(POE::Component::Pluggable) (1.12 => 1.24)

* Wed Aug 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 6.10-1
- auto-update to 6.10 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new req on perl(Encode) (version 0)
- added a new req on perl(Encode::Guess) (version 0)
- added a new req on perl(POE) (version 0.3202)
- added a new req on perl(POE::Component::Pluggable) (version 1.12)
- added a new req on perl(POE::Driver::SysRW) (version 0)
- added a new req on perl(POE::Filter::IRCD) (version 1.7)
- added a new req on perl(POE::Filter::Line) (version 0)
- added a new req on perl(POE::Filter::Stackable) (version 0)
- added a new req on perl(POE::Filter::Stream) (version 0)
- added a new req on perl(POE::Wheel::ReadWrite) (version 0)
- added a new req on perl(POE::Wheel::SocketFactory) (version 0)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Chris Weyl <cweyl@alumni.drew.edu> 6.06-1
- auto-update to 6.06 (by cpan-spec-update 0.01)
- added a new br on perl(Encode) (version 0)
- added a new br on perl(POE::Component::Pluggable) (version 1.12)
- added a new br on perl(POE::Filter::Stream) (version 0)
- added a new br on perl(POE::Filter::Stackable) (version 0)
- added a new br on perl(POE::Wheel::ReadWrite) (version 0)
- added a new br on perl(POE::Wheel::SocketFactory) (version 0)
- altered br on perl(POE::Filter::IRCD) (0 => 1.7)
- altered br on perl(POE) (0 => 0.3202)
- added a new br on perl(POE::Driver::SysRW) (version 0)
- altered br on perl(Test::More) (0 => 0.47)
- added a new br on perl(POE::Filter::Line) (version 0)
- added a new br on perl(Encode::Guess) (version 0)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 5.88-1
- update to 5.88

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.29-2
Rebuild for new perl

* Sat May 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.29-1
- update to 5.29

* Wed May 02 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.28-1
- update to 5.28

* Mon Apr 30 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.26-1
- update to 5.26
- include t/ in %%doc

* Sat Apr 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.24-1
- update to 5.24
- additional splittage BR's
- Additional BR's to handle new tests, ipv6 functionality, etc

* Thu Jan 04 2007 Chris Weyl <cweyl@alumni.drew.edu> 5.18-1
- update to 5.18

* Fri Dec 15 2006 Chris Weyl <cweyl@alumni.drew.edu> 5.17-1
- update to 5.17

* Tue Dec 05 2006 Chris Weyl <cweyl@alumni.drew.edu> 5.14-1
- update to 5.14

* Sun Oct 22 2006 Chris Weyl <cweyl@alumni.drew.edu> 5.07-1
- update to 5.07

* Tue Oct 10 2006 Chris Weyl <cweyl@alumni.drew.edu> 5.05-1
- update to 5.05
- scratched head in confusion at versions in the last few changelogs

* Fri Sep 29 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.54-1
- update to 0.54

* Sun Sep 17 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.53-1
- update to 0.53
- add br: perl(POE::Filter::Zlib::Stream)

* Sun Sep 10 2006 Chris Weyl <cweyl@alumni.drew.edu> 5.02-1
- update to 5.02

* Fri Sep 01 2006 Chris Weyl <cweyl@alumni.drew.edu> 5.00-1
- update to 5.00
- add br on Test::Pod, Test::Pod::Coverage, which are now used
- minor spec tweaks, mostly cosmetic

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 4.99-1
- rebuild per mass rebuild
- update to 4.99

* Tue Aug 22 2006 Chris Weyl <cweyl@alumni.drew.edu> 4.98-1
- update to 4.98

* Tue Jul 25 2006 Chris Weyl <cweyl@alumni.drew.edu> 4.97-1
- update to 4.97

* Sat Jul 22 2006 Chris Weyl <cweyl@alumni.drew.edu> 4.96-3
- Fix typo, add more verbage

* Fri Jul 21 2006 Chris Weyl <cweyl@alumni.drew.edu> 4.96-2
- bump for f-e build
- rework conditionals around testing to... well, work :)

* Thu Jul 20 2006 Chris Weyl <cweyl@alumni.drew.edu> 4.96-1
- snip lines

* Mon Jul 17 2006 Chris Weyl <cweyl@alumni.drew.edu> 4.96-0
- updated to version 4.96
- Dropped the licensing conversation as the documentation (README, pods) were
  updated to include it
- Added optional framework around test suite, rather than just disabling

* Thu Jul 13 2006 Chris Weyl <cweyl@alumni.drew.edu> 4.95-0
- Initial spec file for F-E
