Name:           perl-Devel-REPL
Version:        1.003029
Release:        10%{?dist}
Summary:        Modern perl interactive shell
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-REPL
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Devel-REPL-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(App::Nopaste)
BuildRequires:  perl(B::Concise) >= 0.62
BuildRequires:  perl(B::Keywords)
BuildRequires:  perl(Data::Dump::Streamer) >= 2.39
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(File::Next)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Lexical::Persistence)
BuildRequires:  perl(Module::Refresh)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.93
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Getopt) >= 0.18
BuildRequires:  perl(MooseX::Object::Pluggable) >= 0.0009
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::SigAction)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Time::HiRes)
# Tests only
BuildRequires:  perl(if)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Moose) >= 0.93
Requires:       perl(Moose::Meta::Role)
Requires:       perl(MooseX::Getopt) >= 0.18
Requires:       perl(MooseX::Object::Pluggable) >= 0.0009
# Require plugins used by default, see Devel::REPL::Profile::Minimal
Requires:       perl(Devel::REPL::Plugin::Commands)
Requires:       perl(Devel::REPL::Plugin::DDS)
Requires:       perl(Devel::REPL::Plugin::History)
Requires:       perl(Devel::REPL::Plugin::LexEnv)
Requires:       perl(Devel::REPL::Plugin::MultiLine::PPI)
Requires:       perl(Devel::REPL::Plugin::Packages)

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Data::Dump::Streamer|Moose)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More\\)

%description
This is an interactive shell for Perl, commonly known as a REPL - Read,
Evaluate, Print, Loop. The shell provides for rapid development or testing
of code without the need to create a temporary source code file.

Through a plugin system, many features are available on demand. These plugins
are available:

    Completion
    CompletionDriver::INC
    CompletionDriver::Keywords
    DDC
    DDS
    Interrupt
    LexEnv
    MultiLine::PPI
    Nopaste
    PPI
    Refresh

The plugins are available in standalone RPM packages. For example the
MultiLine::PPI plugin is delivered within %{name}-MultiLine-PPI package.

%package Plugin-Completion
Summary:        Devel-REPL plugin for tab completion
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-Completion
This Perl interactive shell plugin provides extensible tab completion. By
default, the Completion plugin explicitly does not use the GNU Readline or
Term::ReadLine::Perl fallback file name completion.

%package Plugin-CompletionDriver-INC
Summary:        Devel-REPL plugin for completing module names
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-CompletionDriver-INC
This Perl interactive shell plugin provides module names completion.

%package Plugin-CompletionDriver-Keywords
Summary:        Devel-REPL plugin for completing keywords and operators
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-CompletionDriver-Keywords
This Perl interactive shell plugin provides keyword and operator names
completion.

%package Plugin-DDC
Summary:        Devel-REPL plugin for formatting results with Data::Dumper::Concise
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-DDC
This Perl interactive shell plugin formats results with Data::Dumper::Concise.

%package Plugin-DDS
Summary:        Devel-REPL plugin for formatting results with Data::Dump::Streamer
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Data::Dump::Streamer) >= 2.39

%description Plugin-DDS
This Perl interactive shell plugin formats results with Data::Dump::Streamer.

%package Plugin-Interrupt
Summary:        Devel-REPL plugin for trapping INT signal
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-Interrupt
By default Devel::REPL exits on SIGINT (usually Ctrl-C). If you load this
module, SIGINT will be trapped and used to kill long-running commands
(statements) and also to kill the line being edited (like e.g. BASH do).
(You can still use Ctrl-D to exit.)

%package Plugin-LexEnv
Summary:        Devel-REPL plugin for lexical environments
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-LexEnv
This Perl interactive shell plugin provides environments for lexical variables.

%package Plugin-MultiLine-PPI
Summary:        Devel-REPL plugin for multi-line blocks
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-MultiLine-PPI
This Perl interactive shell plugin will collect lines until you have no
unfinished structures.  This lets you write subroutines, "if" statements,
loops, etc. more naturally.

%package Plugin-Nopaste
Summary:        Devel-REPL plugin for uploading data to a nopaste site
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(App::Nopaste)

%description Plugin-Nopaste
This Perl interactive shell plugin allows you to upload session's input and
output to a nopaste site.

%package Plugin-PPI
Summary:        Devel-REPL plugin for dumping Perl code
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-PPI
This Perl interactive shell plugin provides a "ppi" command that uses
PPI::Dumper to dump PPI-parsed Perl documents.

%package Plugin-Refresh
Summary:        Devel-REPL plugin for reloading libraries
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-Refresh
This Perl interactive shell plugin allows you to reload Perl libraries with
Module::Refresh module.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Devel::REPL)
Requires:       perl(Test::More) >= 0.94

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Devel-REPL-%{version}
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
%license LICENCE
%doc Changes CONTRIBUTING README examples
%{_bindir}/re.pl
%dir %{perl_vendorlib}/Devel
%{perl_vendorlib}/Devel/REPL
%{perl_vendorlib}/Devel/REPL.pm
%{_mandir}/man3/Devel::REPL.*
%{_mandir}/man3/Devel::REPL::*

# Plugin-Completion
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/Completion.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::Completion.*

# Plugin-CompletionDriver-INC
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/CompletionDriver/INC.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::CompletionDriver::INC.*

# Plugin-CompletionDriver-Keywords
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/CompletionDriver/Keywords.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::CompletionDriver::Keywords.*

# Plugin-DDC
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/DDC.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::DDC.*

# Plugin-DDS
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/DDS.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::DDS.*

# Plugin-Interrupt
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/Interrupt.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::Interrupt.*

# Plugin-LexEnv
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/LexEnv.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::LexEnv.*

# Plugin-MultiLine-PPI
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/MultiLine
%exclude %{_mandir}/man3/Devel::REPL::Plugin::MultiLine::*

# Plugin-Nopaste
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/Nopaste.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::Nopaste.*

# Plugin-PPI
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/PPI.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::PPI.*

# Plugin-Refresh
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/Refresh.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::Refresh.*

%files Plugin-Completion
%{perl_vendorlib}/Devel/REPL/Plugin/Completion.pm
%{_mandir}/man3/Devel::REPL::Plugin::Completion.*

%files Plugin-CompletionDriver-INC
%{perl_vendorlib}/Devel/REPL/Plugin/CompletionDriver/INC.pm
%{_mandir}/man3/Devel::REPL::Plugin::CompletionDriver::INC.*

%files Plugin-CompletionDriver-Keywords
%{perl_vendorlib}/Devel/REPL/Plugin/CompletionDriver/Keywords.pm
%{_mandir}/man3/Devel::REPL::Plugin::CompletionDriver::Keywords.*

%files Plugin-DDC
%{perl_vendorlib}/Devel/REPL/Plugin/DDC.pm
%{_mandir}/man3/Devel::REPL::Plugin::DDC.*

%files Plugin-DDS
%{perl_vendorlib}/Devel/REPL/Plugin/DDS.pm
%{_mandir}/man3/Devel::REPL::Plugin::DDS.*

%files Plugin-Interrupt
%{perl_vendorlib}/Devel/REPL/Plugin/Interrupt.pm
%{_mandir}/man3/Devel::REPL::Plugin::Interrupt.*

%files Plugin-LexEnv
%{perl_vendorlib}/Devel/REPL/Plugin/LexEnv.pm
%{_mandir}/man3/Devel::REPL::Plugin::LexEnv.*

%files Plugin-MultiLine-PPI
%{perl_vendorlib}/Devel/REPL/Plugin/MultiLine
%{_mandir}/man3/Devel::REPL::Plugin::MultiLine::*

%files Plugin-Nopaste
%{perl_vendorlib}/Devel/REPL/Plugin/Nopaste.pm
%{_mandir}/man3/Devel::REPL::Plugin::Nopaste.*

%files Plugin-PPI
%{perl_vendorlib}/Devel/REPL/Plugin/PPI.pm
%{_mandir}/man3/Devel::REPL::Plugin::PPI.*

%files Plugin-Refresh
%{perl_vendorlib}/Devel/REPL/Plugin/Refresh.pm
%{_mandir}/man3/Devel::REPL::Plugin::Refresh.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.003029-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.003029-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.003029-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.003029-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.003029-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 06 2023 Petr Pisar <ppisar@redhat.com> - 1.003029-5
- Convert a license tag an SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.003029-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.003029-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.003029-2
- Perl 5.36 rebuild

* Mon May 30 2022 Petr Pisar <ppisar@redhat.com> - 1.003029-1
- 1.003029 bump
- Package the tests

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.003028-18
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 23 2020 Petr Pisar <ppisar@redhat.com> - 1.003028-16
- Modernize a spec file

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.003028-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.003028-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.003028-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Petr Pisar <ppisar@redhat.com> - 1.003028-5
- Require default plugins and reenable building of the DDS plugin (bug #1466106)

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.003028-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.003028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.003028-2
- Perl 5.24 rebuild

* Wed Feb 17 2016 Petr Šabata <contyk@redhat.com> - 1.003028-1
- 1.003028 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.003027-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Petr Šabata <contyk@redhat.com> - 1.003027-1
- 1.003027 bump

* Wed Jun 24 2015 Petr Pisar <ppisar@redhat.com> - 1.003026-3
- Specify all dependencies
- Sub-package plugins
- Disable DDS plugin (bug #1231285)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 20 2014 Petr Šabata <contyk@redhat.com> - 1.003026-1
- 1.003026 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.003015-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 1.003015-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Iain Arnell <iarnell@gmail.com> 1.003015-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 1.003014-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 1.003013-2
- Perl 5.16 rebuild

* Sun May 20 2012 Iain Arnell <iarnell@gmail.com> 1.003013-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.003012-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 03 2010 Iain Arnell <iarnell@gmail.com> 1.003012-1
- update to latest upstream
- clean up spec for modern rpmbuild

* Wed Jun 16 2010 Iain Arnell <iarnell@gmail.com> 1.003011-1
- update to latest upstream

* Fri May 28 2010 Iain Arnell <iarnell@gmail.com> 1.003010-1
- update to latest upstream version
- use perl_default_filter and DESTDIR

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.003009-3
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.003009-2
- Mass rebuild with perl-5.12.0

* Tue Mar 09 2010 Iain Arnell <iarnell@gmail.com> 1.003009-1
- update to latest upstream version
- br perl(Data::Dumper::Concise)
- br perl(Sys::SigAction)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.003007-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Iain Arnell <iarnell@gmail.com> 1.003007-2
- BR perl(CPAN)

* Tue Jul 07 2009 Iain Arnell <iarnell@gmail.com> 1.003007-1
- update to latest version (fixes rt#44919)

* Sat May 02 2009 Iain Arnell <iarnell@gmail.com> 1.003006-2
- remove BR perl

* Sun Apr 19 2009 Iain Arnell <iarnell@gmail.com> 1.003006-1
- Specfile autogenerated by cpanspec 1.77.
- add requires for optional modules
