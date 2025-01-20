# Disable support for Carp-Datum because it is Artistic 1 only, CPAN RT#105332
%bcond_with datum
# Perform optional tests
%bcond_without perl_Log_Agent_enables_optional_test

Name:           perl-Log-Agent
Version:        1.005
Release:        13%{?dist}
Summary:        Logging agent
License:        Artistic-2.0
URL:            https://metacpan.org/release/Log-Agent
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MROGASKI/Log-Agent-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
# Carp::Datum not needed at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
# Mail::Mailer not needed at tests
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
# Sys::Syslog not needed at tests
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
%if %{with perl_Log_Agent_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Callback)
%endif
Requires:       perl(warnings)

# Remove private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(\\.::t/

%description
The Log::Agent Perl module provides an abstract layer for logging and tracing,
which is independent from the actual method used to physically perform those
activities. It acts as an agent (hence the name) that collects the requests
and delegates processing to a logging driver.

%if %{with datum}
%package Carp-Datum
Summary:        Carp::Datum driver for Log::Agent Perl logging framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Carp)
Requires:       perl(Carp::Datum)

%description Carp-Datum
The purpose of this logging driver is to cooperate with Carp::Datum by emitting
traces to the debug channel via Carp::Datum's traces facilities.
%endif

%package mail
Summary:        E-mail driver for Log::Agent Perl logging framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description mail
This logging driver maps the log calls to email messages.  Each call generates
a separate email message.

%package syslog
Summary:        Syslog driver for Log::Agent Perl logging framework
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Carp)

%description syslog
This logging driver delegates log operations to syslog() via the
Sys::Syslog interface.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_Log_Agent_enables_optional_test}
Requires:       perl(Callback)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Log-Agent-%{version}
# Fix end of lines
perl -i -pe 's/\r\n/\n/' CHANGELOG.md README
%if !%{with perl_Log_Agent_enables_optional_test}
rm t/tag_callback.t
perl -i -ne 'print $_ unless m{\A\Qt/tag_callback.t\E}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# The tests are not parallel-safe, they overwrite files in CWD, CPAN RT#113812
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
prove -I . -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# The tests are not parallel-safe, they overwrite files in CWD, CPAN RT#113812
make test

%files
%doc CHANGELOG.md README
%{perl_vendorlib}/*
%{_mandir}/man3/*
# Carp-Datum
%exclude %{perl_vendorlib}/Log/Agent/Driver/Datum.pm
%exclude %{_mandir}/man3/Log::Agent::Driver::Datum.*
# mail
%exclude %{perl_vendorlib}/Log/Agent/Driver/Mail.pm
%exclude %{_mandir}/man3/Log::Agent::Driver::Mail.*
# syslog
%exclude %{perl_vendorlib}/Log/Agent/Channel/Syslog.pm
%exclude %{perl_vendorlib}/Log/Agent/Driver/Syslog.pm
%exclude %{_mandir}/man3/Log::Agent::Channel::Syslog.*
%exclude %{_mandir}/man3/Log::Agent::Driver::Syslog.*

%if %{with datum}
%files Carp-Datum
%{perl_vendorlib}/Log/Agent/Driver/Datum.pm
%{_mandir}/man3/Log::Agent::Driver::Datum.*
%endif

%files mail
%{perl_vendorlib}/Log/Agent/Driver/Mail.pm
%{_mandir}/man3/Log::Agent::Driver::Mail.*

%files syslog
%{perl_vendorlib}/Log/Agent/Channel/Syslog.pm
%{perl_vendorlib}/Log/Agent/Driver/Syslog.pm
%{_mandir}/man3/Log::Agent::Channel::Syslog.*
%{_mandir}/man3/Log::Agent::Driver::Syslog.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.005-11
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-2
- Perl 5.34 rebuild

* Mon Apr 12 2021 Petr Pisar <ppisar@redhat.com> - 1.005-1
- 1.005 bump
- Package the tests

* Mon Feb 15 2021 Petr Pisar <ppisar@redhat.com> - 1.004-1
- 1.004 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.003-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Petr Pisar <ppisar@redhat.com> - 1.003-1
- 1.003 bump

* Mon Oct 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.002-1
- 1.002 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.001-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.001-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Petr Pisar <ppisar@redhat.com> - 1.001-1
- 1.001 bump

* Thu Jun 18 2015 Petr Pisar <ppisar@redhat.com> 1.000-1
- Specfile autogenerated by cpanspec 1.78.
