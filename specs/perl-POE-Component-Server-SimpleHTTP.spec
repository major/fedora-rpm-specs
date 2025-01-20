# Run optional test
%bcond_without perl_POE_Component_Server_SimpleHTTP_enables_optional_test

Name:           perl-POE-Component-Server-SimpleHTTP
Version:        2.30
Release:        6%{?dist}
Summary:        Serve HTTP requests in POE
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Server-SimpleHTTP
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Component-Server-SimpleHTTP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Moose) >= 0.9
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::POE) >= 0.205
BuildRequires:  perl(POE) >= 1.0000
BuildRequires:  perl(POE::Component::SSLify) >= 0.04
BuildRequires:  perl(POE::Filter::HTTPD)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POE::Filter::HTTP::Parser) >= 1.06
BuildRequires:  perl(POE::Kernel)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::POE::Client::TCP) >= 1.24
%if %{with perl_POE_Component_Server_SimpleHTTP_enables_optional_test}
# Optional tests only
BuildRequires:  perl(POE::Component::Client::HTTP) >= 0.82
%endif
Requires:       perl(HTTP::Request)
Requires:       perl(Moose) >= 0.9
Requires:       perl(Moose::Object)
Requires:       perl(MooseX::POE) >= 0.205
Requires:       perl(POE) >= 1.0000
Recommends:     perl(POE::Component::SSLify) >= 0.04
Requires:       perl(Storable)
Requires:       perl(Sys::Hostname)

%{?perl_default_filter}
# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Moose|MooseX::POE|POE|POE::Filter::HTTP::Parser|Test::More|Test::POE::Client::TCP)\\)$

%description
This module makes serving up HTTP requests a breeze in POE.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(POE) >= 1.0000
%if %{with perl_POE_Component_Server_SimpleHTTP_enables_optional_test}
Requires:       perl(POE::Component::Client::HTTP) >= 0.82
%endif
Requires:       perl(POE::Filter::HTTP::Parser) >= 1.06
Requires:       perl(POE::Filter::Stream)
Requires:       perl(Test::More) >= 0.47
Requires:       perl(Test::POE::Client::TCP) >= 1.24

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n POE-Component-Server-SimpleHTTP-%{version}
perl -i -pe 's/\r$//g' examples/*
# Remove unused tests
for F in \
    t/author-pod-coverage.t t/author-pod-syntax.t \
%if !%{with perl_POE_Component_Server_SimpleHTTP_enables_optional_test}
    t/06_stream.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
yes | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc README Changes Changes.old examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 09 2023 Petr Pisar <ppisar@redhat.com> - 2.30-1
- 2.30 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Petr Pisar <ppisar@redhat.com> - 2.28-14
- Fix checking a failure after posting to a POE kernel (bug #2109851)
- Package the tests

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.28-12
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.28-9
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.28-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.28-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Petr Pisar <ppisar@redhat.com> - 2.28-1
- 2.28 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-2
- Perl 5.26 rebuild

* Fri Mar 10 2017 Petr Pisar <ppisar@redhat.com> - 2.26-1
- 2.26 bump

* Tue Feb 21 2017 Petr Pisar <ppisar@redhat.com> - 2.24-1
- 2.24 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-2
- Perl 5.24 rebuild

* Thu Feb 25 2016 Petr Šabata <contyk@redhat.com> - 2.22-1
- 2.22 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Petr Šabata <contyk@redhat.com> - 2.20-1
- 2.20 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-6
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 2.18-3
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Petr Šabata <contyk@redhat.com> - 2.18-1
- 2.18 bump, drop the MooseX::AttributeHelpers dependency
- Modernize the spec a little

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Petr Šabata <contyk@redhat.com> - 2.16-1
- 2.16 bump (Module::Install updated)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Petr Pisar <ppisar@redhat.com> - 2.14-2
- Perl 5.16 rebuild

* Tue Jan 17 2012 Petr Šabata <contyk@redhat.com> - 2.14-1
- 2.14 bump
- Spec cleanup
- Filter out underspecified dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.06-5
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 2.06-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.06-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Dec 09 2010 Iain Arnell <iarnell@gmail.com> 2.06-1
- update to latest upstream version
- fixes FTBFS RHBZ#660836
- clean up spec for modern rpmbuild

* Wed Jun 23 2010 Petr Pisar <ppisar@redhat.com> - 2.04-1
- 2.04 bump (bug #602616)
- Clean dependencies up

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.0-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.0-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 2.0-1
- auto-update to 2.0 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(Moose) (version 0.81)
- added a new br on perl(MooseX::AttributeHelpers) (version 0)
- added a new br on perl(MooseX::POE) (version 0.205)
- added a new req on perl(Moose) (version 0.81)
- added a new req on perl(MooseX::AttributeHelpers) (version 0)
- added a new req on perl(MooseX::POE) (version 0.205)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.58-1
- auto-update to 1.58 (by cpan-spec-update 0.01)
- added a new br on perl(Storable) (version 0)
- added a new br on perl(Sys::Hostname) (version 0)
- added a new br on perl(POE::Filter::HTTP::Parser) (version 0.02)
- added a new br on perl(Socket) (version 0)
- added a new br on perl(Test::POE::Client::TCP) (version 0.1)
- altered br on perl(POE) (0 => 1.0000)
- altered br on perl(Test::More) (0 => 0.47)
- added a new br on perl(Carp) (version 0)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.48-1
- update to 1.48

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.23-3
- rebuild for new perl

* Sat Apr 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.23-2
- additional testing BR

* Sat Apr 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.23-1
- update to 1.23
- update source URL (maintainer changed)
- add BR's for potential perl splittage
- add BR's for tests -- note pod coverage fails, so we just leave that one
  commented out

* Fri Sep 29 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.13-1
- update to 1.13
- add examples/ to %%doc; correct encoding in %%prep
- explicitly requires perl(HTTP::Base); was missed due to a use base construct

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.11-3
- bump for mass rebuild

* Fri Aug 18 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.11-2
- bump

* Wed Aug 16 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.11-1
- Specfile autogenerated by cpanspec 1.68.
- Initial spec file for F-E
