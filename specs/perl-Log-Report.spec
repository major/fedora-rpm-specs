# Run optional test
%bcond_without perl_Log_Report_enables_optional_test

Name:           perl-Log-Report
Version:        1.39
Release:        2%{?dist}
Summary:        Report a problem with exceptions and translation support
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Report
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Log-Report-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.09
# Dancer::Logger::Abstract not used at tests
BuildRequires:  perl(Dancer2::Core::Role::Logger)
BuildRequires:  perl(Dancer2::Core::Types)
BuildRequires:  perl(Dancer2::Plugin) >= 0.207
# DBIx::Class::Storage::Statistics not used at tests
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.09
BuildRequires:  perl(Encode) >= 2.00
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Dispatch) >= 2.00
BuildRequires:  perl(Log::Log4perl)
# Makefile.PL states Log::Report::Optional 1.07 for contained
# Log::Report::{Minimal::Domain,Util}
BuildRequires:  perl(Log::Report::Minimal::Domain) >= 1.07
BuildRequires:  perl(Log::Report::Util) >= 1.07
%if %{with perl_Log_Report_enables_optional_test}
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Log)
%endif
BuildRequires:  perl(Moo)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# String::Print 0.91 is not used
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Syslog) >= 0.27
# Time::HiRes not used at tests
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.86
%if %{with perl_Log_Report_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Dancer2) > 0.166001
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Log4perl) >= 1.00
BuildRequires:  perl(Mojolicious) >= 2.16
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::Error)
%endif
Requires:       perl(Devel::GlobalDestruction) >= 0.09
Requires:       perl(Encode) >= 2.00
# Makefile.PL states Log::Report::Optional 1.03 for contained
# Log::Report::{Minimal::Domain,Util}
Requires:       perl(Log::Report::Minimal::Domain) >= 1.07
Requires:       perl(Log::Report::Util) >= 1.07
Requires:       perl(overload)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Dancer2|Devel::GlobalDestruction|Encode|Log::Report::Minimal::Domain|Log::Report::Util|Sys::Syslog|Test::More)\\)$

# Remove private redefinitions
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)

# Remove private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DieTests\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DieTests\\)

%description
Handling messages directed to users can be a hassle, certainly when the same
software is used for command-line and in a graphical interfaces (you may not
know how it is used), or has to cope with internationalization; these modules
try to simplify this.

%package Dancer
Summary:    Reroute Dancer logs into Log::Report
Requires:   perl(Exporter)
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}

%description Dancer
When you use this logger in your Dancer application, it will nicely integrate
with non-Dancer modules which need logging.

%package Dancer2
Summary:    Reroute Dancer2 logs into Log::Report
Requires:   perl(Dancer2::Core::Role::Logger)
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}

%description Dancer2
This logger allows the use of the many logging back-ends available in
Log::Report. It will process all of the Dancer2 log messages, and also allow
any other module to use the same logging facilities. The same log messages can
be sent to multiple destinations at the same time via flexible dispatchers.

%package DBIC
Summary:    Query profiler for DBIx::Class
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}

%description DBIC
Log DBIx::Class queries via Log::Report.

%package Dispatcher-Log4perl
Summary:    Log::Log4perl back-end for Log::Report
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}
# Makefile.PL states Log::Report::Optional 1.03 for contained
# Log::Report::{Minimal::Domain,Util}
Requires:   perl(Log::Report::Util) >= 1.03

%description Dispatcher-Log4perl
This is an optional Log::Log4perl back-end for Log::Report logging framework.

%package Dispatcher-LogDispatch
Summary:    Log::Dispatch back-end for Log::Report
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}
# Makefile.PL states Log::Report::Optional 1.03 for contained
# Log::Report::{Minimal::Domain,Util}
Requires:   perl(Log::Report::Util) >= 1.03

%description Dispatcher-LogDispatch
This is an optional Log::Dispatch back-end for Log::Report logging framework.

%package Dispatcher-Syslog
Summary:    Sys::Syslog back-end for Log::Report
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}
Requires:   perl(Encode) >= 2.00
Requires:   perl(Sys::Syslog) >= 0.27
# Makefile.PL states Log::Report::Optional 1.03 for contained
# Log::Report::{Minimal::Domain,Util}
Requires:   perl(Log::Report::Util) >= 1.03

%description Dispatcher-Syslog
This is an optional Sys::Syslog back-end for Log::Report logging framework.

%package Mojo
Summary:    Divert log messages into Log::Report
Requires:   perl-Log-Report = %{?epoch:%epoch:}%{version}-%{release}
Requires:   perl(Mojo::Log)

%description Mojo
Mojo likes to log messages directly into a file, by default. This is a Mojo
extension that can route Mojo messages into Log::Report logging framework.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.86
Requires:       perl(Log::Report::Dispatcher::Callback)
Requires:       perl(Log::Report::Dispatcher::File)
Requires:       perl(Log::Report::Dispatcher::Log4perl)
Requires:       perl(Log::Report::Dispatcher::LogDispatch)
Requires:       perl(Log::Report::Dispatcher::Perl)
Requires:       perl(Log::Report::Dispatcher::Syslog)
Requires:       perl(Log::Report::Dispatcher::Try)
Requires:       perl(Log::Report::Domain)
Requires:       perl(Log::Report::Exception)
Requires:       perl(Log::Report::Translator)
%if %{with perl_Log_Report_enables_optional_test}
Requires:       perl(Dancer2) > 0.166001
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Request::Common)
Requires:       perl(Log::Dispatch::File)
Requires:       perl(Log::Log4perl) >= 1.00
Requires:       perl(Mojolicious) >= 2.16
Requires:       perl(MojoX::Log::Report)
Requires:       perl(Plack::Test)
Requires:       perl(XML::LibXML)
Requires:       perl(XML::LibXML::Error)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Log-Report-%{version}
%if !%{with perl_Log_Report_enables_optional_test}
rm t/60mojo.t
perl -i -ne 'print $_ unless m{^t/60mojo\.t\b}' MANIFEST
%endif
chmod +x t/*.t

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
# README is a subset of README.md
%doc ChangeLog README.md
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Dancer
%exclude %{perl_vendorlib}/Dancer2
%exclude %{perl_vendorlib}/Log/Report/DBIC
%exclude %{perl_vendorlib}/Log/Report/Dispatcher/Log4perl.*
%exclude %{perl_vendorlib}/Log/Report/Dispatcher/LogDispatch.*
%exclude %{perl_vendorlib}/Log/Report/Dispatcher/Syslog.*
%exclude %{perl_vendorlib}/MojoX
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Dancer::*
%exclude %{_mandir}/man3/Dancer2::*
%exclude %{_mandir}/man3/Log::Report::DBIC::Profiler.*
%exclude %{_mandir}/man3/Log::Report::Dispatcher::Log4perl.*
%exclude %{_mandir}/man3/Log::Report::Dispatcher::LogDispatch.*
%exclude %{_mandir}/man3/Log::Report::Dispatcher::Syslog.*
%exclude %{_mandir}/man3/MojoX::Log::Report.*

%files Dancer
%{perl_vendorlib}/Dancer
%{_mandir}/man3/Dancer::*

%files Dancer2
%{perl_vendorlib}/Dancer2
%{_mandir}/man3/Dancer2::*

%files DBIC
%{perl_vendorlib}/Log/Report/DBIC
%{_mandir}/man3/Log::Report::DBIC::Profiler.*

%files Dispatcher-Log4perl
%{perl_vendorlib}/Log/Report/Dispatcher/Log4perl.*
%{_mandir}/man3/Log::Report::Dispatcher::Log4perl.*

%files Dispatcher-LogDispatch
%{perl_vendorlib}/Log/Report/Dispatcher/LogDispatch.*
%{_mandir}/man3/Log::Report::Dispatcher::LogDispatch.*

%files Dispatcher-Syslog
%{perl_vendorlib}/Log/Report/Dispatcher/Syslog.*
%{_mandir}/man3/Log::Report::Dispatcher::Syslog.*

%files Mojo
%{perl_vendorlib}/MojoX
%{_mandir}/man3/MojoX::Log::Report.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 10 2024 Petr Pisar <ppisar@redhat.com> - 1.39-1
- 1.39 bump

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Petr Pisar <ppisar@redhat.com> - 1.37-1
- 1.37 bump

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 27 2023 Petr Pisar <ppisar@redhat.com> - 1.36-1
- 1.36 bump

* Fri Oct 27 2023 Petr Pisar <ppisar@redhat.com> - 1.35-1
- 1.35 bump

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Petr Pisar <ppisar@redhat.com> - 1.34-1
- 1.34 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Petr Pisar <ppisar@redhat.com> - 1.33-1
- 1.33 bump
- Package the tests

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-2
- Perl 5.34 rebuild

* Tue Jan 26 2021 Petr Pisar <ppisar@redhat.com> - 1.32-1
- 1.32 bump

* Mon Jan 18 2021 Petr Pisar <ppisar@redhat.com> - 1.31-1
- 1.31 bump

* Fri Jan 15 2021 Petr Pisar <ppisar@redhat.com> - 1.30-1
- 1.30 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Petr Pisar <ppisar@redhat.com> - 1.29-1
- 1.29 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-2
- Perl 5.30 rebuild

* Tue May 14 2019 Petr Pisar <ppisar@redhat.com> - 1.28-1
- 1.28 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-2
- Perl 5.28 rebuild

* Mon Jun 04 2018 Petr Pisar <ppisar@redhat.com> - 1.27-1
- 1.27 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Petr Pisar <ppisar@redhat.com> - 1.26-1
- 1.26 bump

* Mon Dec 11 2017 Petr Pisar <ppisar@redhat.com> - 1.25-1
- 1.25 bump

* Mon Nov 06 2017 Petr Pisar <ppisar@redhat.com> - 1.23-1
- 1.23 bump

* Thu Oct 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-1
- 1.22 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Petr Pisar <ppisar@redhat.com> - 1.21-1
- 1.21 bump

* Wed Jun 28 2017 Petr Pisar <ppisar@redhat.com> - 1.20-1
- 1.20 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-2
- Perl 5.26 rebuild

* Fri Feb 10 2017 Petr Pisar <ppisar@redhat.com> - 1.19-1
- 1.19 bump

* Fri Oct 21 2016 Petr Pisar <ppisar@redhat.com> - 1.18-1
- 1.18 bump

* Wed Sep 21 2016 Petr Pisar <ppisar@redhat.com> - 1.17-1
- 1.17 bump

* Fri May 27 2016 Petr Pisar <ppisar@redhat.com> - 1.16-1
- 1.16 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-2
- Perl 5.24 rebuild

* Tue Apr 19 2016 Petr Pisar <ppisar@redhat.com> - 1.15-1
- 1.15 bump

* Thu Feb 04 2016 Petr Pisar <ppisar@redhat.com> - 1.13-1
- 1.13 bump

* Wed Jan 20 2016 Petr Pisar <ppisar@redhat.com> - 1.12-1
- 1.12 bump

* Wed Dec 02 2015 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Tue Oct 20 2015 Petr Pisar <ppisar@redhat.com> - 1.09-1
- 1.09 bump

* Fri Oct 09 2015 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump

* Wed Jul 22 2015 Petr Pisar <ppisar@redhat.com> - 1.07-1
- 1.07 bump

* Tue Jun 16 2015 Petr Pisar <ppisar@redhat.com> - 1.06-1
- 1.06 bump

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-3
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-2
- Perl 5.20 rebuild

* Mon Jun 30 2014 Petr Pisar <ppisar@redhat.com> - 1.05-1
- 1.05 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Petr Pisar <ppisar@redhat.com> - 1.04-1
- 1.04 bump

* Mon May 26 2014 Petr Pisar <ppisar@redhat.com> - 1.03-1
- 1.03 bump

* Tue Mar 11 2014 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Mon Jan 27 2014 Petr Pisar <ppisar@redhat.com> - 1.01-1
- 1.01 bump

* Wed Nov 20 2013 Petr Pisar <ppisar@redhat.com> 0.998-1
- Specfile autogenerated by cpanspec 1.78.
