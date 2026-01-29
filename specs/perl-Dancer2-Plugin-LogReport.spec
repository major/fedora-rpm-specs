# Run optional test
%bcond_without perl_Dancer2_Plugin_LogReport_enables_optional_test

Name:           perl-Dancer2-Plugin-LogReport
Version:        2.02
Release:        1%{?dist}
Summary:        Logging, exceptions and translations in Dancer2 via Log::Report
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Dancer2-Plugin-LogReport
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Dancer2-Plugin-LogReport-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Dancer2::Core::Role::Logger)
BuildRequires:  perl(Dancer2::Core::Role::Template)
BuildRequires:  perl(Dancer2::Core::Types)
BuildRequires:  perl(Dancer2::FileUtils)
# Dancer2::Plugin from Dancer2 in META
BuildRequires:  perl(Dancer2::Plugin) >= 0.207
BuildRequires:  perl(Dancer::Logger::Abstract)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Log::Report) >= 1.42
BuildRequires:  perl(Log::Report::Dispatcher)
BuildRequires:  perl(Log::Report::Message)
BuildRequires:  perl(Log::Report::Template)
BuildRequires:  perl(Log::Report::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Test::More) >= 1
%if %{with perl_Dancer2_Plugin_LogReport_enables_optional_test}
# Optional tests:
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(Dancer2) >= 0.207
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Test)
%endif
Requires:       perl(Dancer2::Core::Role::Logger)
Requires:       perl(Dancer2::Core::Role::Template)
Requires:       perl(Dancer2::Plugin) >= 0.207
Requires:       perl(Log::Report) >= 1.42
# Dancer2::Logger::LogReport etc. moved here from perl-Log-Report/perl-Log-Report-Dancer2
Conflicts:      perl-Log-Report-Dancer2 < 1.42
Provides:       perl-Log-Report-Dancer2 = %{?epoch:%{epoch}:}%{version}-%{release}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Dancer2|Dancer2::Plugin|Log::Report)\\)$
# Hide private modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(DB\\)

%description
This logger allows the use of the many logging backends available in
Log::Report. It will process all of the Dancer2 log messages, and also allow
any other module to use the same logging facilities. The same log messages can
be sent to multiple destinations at the same time via flexible dispatchers.

%package -n perl-Dancer-Logger-LogReport
Summary:    Reroute Dancer logs into Log::Report
Requires:   perl(Exporter)
Requires:   perl(Log::Report) >= 1.42
# Log::Report::Dancer moved here from perl-Log-Report/perl-Log-Report-Dancer
Conflicts:  perl-Log-Report-Dancer < 1.42
Provides:   perl-Log-Report-Dancer = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n perl-Dancer-Logger-LogReport
When you use this logger in your Dancer application, it will nicely integrate
with non-Dancer modules which need logging.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Dancer-Logger-LogReport = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Dancer2_Plugin_LogReport_enables_optional_test}
# Optional tests:
Requires:       perl(HTTP::Cookies)
Requires:       perl(Dancer2) >= 0.207
Requires:       perl(HTTP::Request::Common)
Requires:       perl(Plack::Test)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Dancer2-Plugin-LogReport-%{version}
%if %{without perl_Dancer2_Plugin_LogReport_enables_optional_test}
rm t/70dancer2.t
perl -i -ne 'print $_ unless m{^t/70dancer2.t\b}' MANIFEST
%endif
# Correct shebangs
for F in t/*.t; do
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
# License text requested in CPAN RT#171436 and
# <https://github.com/markov2/perl5-Dancer2-Plugin-LogReport/issues/1>.
%doc ChangeLog README.md
%dir %{perl_vendorlib}/Dancer2
%dir %{perl_vendorlib}/Dancer2/Logger
%{perl_vendorlib}/Dancer2/Logger/LogReport.pm
%{perl_vendorlib}/Dancer2/Logger/LogReport.pod
%{perl_vendorlib}/Dancer2/Plugin/LogReport
%{perl_vendorlib}/Dancer2/Plugin/LogReport.pm
%{perl_vendorlib}/Dancer2/Plugin/LogReport.pod
%dir %{perl_vendorlib}/Dancer2/Template
%{perl_vendorlib}/Dancer2/Template/TTLogReport.pm
%{perl_vendorlib}/Dancer2/Template/TTLogReport.pod
%{_mandir}/man3/Dancer2::Logger::LogReport.*
%{_mandir}/man3/Dancer2::Plugin::LogReport.*
%{_mandir}/man3/Dancer2::Plugin::LogReport::*
%{_mandir}/man3/Dancer2::Template::TTLogReport.*

%files -n perl-Dancer-Logger-LogReport
# License text requested in CPAN RT#171436 and
# <https://github.com/markov2/perl5-Dancer2-Plugin-LogReport/issues/1>.
%doc ChangeLog examples README.md
%dir %{perl_vendorlib}/Dancer
%dir %{perl_vendorlib}/Dancer/Logger
%{perl_vendorlib}/Dancer/Logger/LogReport.pm
%{perl_vendorlib}/Dancer/Logger/LogReport.pod
%{_mandir}/man3/Dancer::Logger::LogReport.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Jan 27 2026 Petr Pisar <ppisar@redhat.com> 2.02-1
- Specfile autogenerated by cpanspec 1.78.
