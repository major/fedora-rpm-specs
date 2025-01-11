Name:           perl-Log-Dispatchouli
Version:        3.009
Release:        1%{?dist}
Summary:        Simple wrapper around Log::Dispatch
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Dispatchouli
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Log-Dispatchouli-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(Carp)
BuildRequires:  perl(experimental)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Dispatch::Screen)
BuildRequires:  perl(Log::Dispatch::Syslog)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Flogger)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::GlobExporter) >= 0.002
BuildRequires:  perl(Try::Tiny) >= 0.04
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(utf8)
Requires:       perl(Log::Dispatch::Array)
Requires:       perl(Log::Dispatch::File)
Requires:       perl(Log::Dispatch::Screen)
Requires:       perl(Log::Dispatch::Syslog)

%{?perl_default_filter}

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(DDR.*\\)
%global __requires_exclude %{__requires_exclude}|perl\\(SDR.*\\)

%description
Log::Dispatchouli is a thin layer above Log::Dispatch and meant to make it
dead simple to add logging to a program without having to think much about
categories, facilities, levels, or things like that. It is meant to make
logging just configurable enough that you can find the logs you want and
just easy enough that you will actually log things.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Log-Dispatchouli-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Log*
%{_mandir}/man3/Log::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Jan 09 2025 Jitka Plesnikova <jplesnik@redhat.com> - 3.009-1
- 3.009 bump (rhbz#2336328)

* Wed Nov 06 2024 Jitka Plesnikova <jplesnik@redhat.com> - 3.008-1
- 3.008 bump (rhbz#2323382)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 04 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-1
- 3.007 bump (rhbz#2237032)

* Wed Aug 23 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-1
- 3.006 bump (rhbz#2231470)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-1
- 3.005 bump

* Tue Jun 06 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-1
- 3.004 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-1
- 3.002 bump

* Fri Dec 02 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.001-1
- 3.001 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.023-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.023-1
- 2.023 bump
- Package tests

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.022-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.022-1
- 2.022 bump

* Mon Aug 17 2020 Petr Pisar <ppisar@redhat.com> - 2.021-1
- 2.021 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.019-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.019-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.019-1
- 2.019 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.017-2
- Perl 5.30 rebuild

* Wed Mar 13 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.017-1
- 2.017 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.016-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.016-2
- Perl 5.28 rebuild

* Fri Feb 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.016-1
- 2.016 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.015-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.015-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.015-1
- 2.015 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.012-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.012-2
- Perl 5.22 rebuild

* Fri Dec 05 2014 Petr Šabata <contyk@redhat.com> - 2.012-1
- 2.012 bump, various optimizations

* Fri Nov 21 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.010-1
- 2.010 bump
- Modernize spec file

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.005-10
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.005-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.005-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 2.005-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 2.005-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.005-2
- Perl mass rebuild

* Sat Apr 09 2011 Iain Arnell <iarnell@gmail.com> 2.005-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 22 2011 Iain Arnell <iarnell@gmail.com> 2.004-1
- update to latest upstream version

* Thu Jan 20 2011 Iain Arnell <iarnell@gmail.com> 2.002-1
- update to latest upstream version
- remove unnecessary files listed as docs
- clean up spec for modern rpmbuild
- new BR perl(File::Spec)
- new BR perl(Sub::Exporter)
- new BR perl(Sub::Exporter::GlobExporter) >= 0.002
- new BR perl(Test::Fatal)
- update BR perl(Test::More) >= 0.96

* Sun Nov 21 2010 Iain Arnell <iarnell@gmail.com> 1.102350-1
- update to latest upstream version

* Fri Aug 13 2010 Iain Arnell <iarnell@gmail.com> 1.102220-1
- update to latest upstream version

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.100712-2
- Mass rebuild with perl-5.12.0

* Fri Apr 02 2010 Iain Arnell <iarnell@gmail.com> 1.100712-1
- Specfile autogenerated by cpanspec 1.78.
- use perl_default_filter and DESTDIR
