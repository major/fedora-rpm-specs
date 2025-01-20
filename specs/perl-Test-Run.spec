Name:           perl-Test-Run
Version:        0.0306
Release:        2%{?dist}
Summary:        Extensible and object-oriented test harness for TAP scripts
# Build.PL:                         MIT
# lib/Test/Run.pm:                  MIT
# lib/Test/Run/Assert.pm:           MIT
# lib/Test/Run/Base.pm:             MIT
# lib/Test/Run/Base/Plugger.pm:     MIT
# lib/Test/Run/Base/PlugHelpers.pm: MIT
# lib/Test/Run/Base/Struct.pm:      MIT
# lib/Test/Run/Class/Hierarchy.pm:  MIT
# lib/Test/Run/Core.pm:             MIT
# lib/Test/Run/Core_GplArt.pm:      GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Test/Run/Iface.pm:            MIT
# lib/Test/Run/Obj:                 MIT
# lib/Test/Run/Obj/CanonFailedObj.pm:       MIT
# lib/Test/Run/Obj/Error.pm:        MIT
# lib/Test/Run/Obj/FailedObj.pm:    MIT
# lib/Test/Run/Obj/IntOrUnknown.pm: MIT
# lib/Test/Run/Obj/TestObj.pm:      MIT
# lib/Test/Run/Obj/TotObj.pm:       MIT
# lib/Test/Run/Output.pm:           MIT
# lib/Test/Run/Plugin/CmdLine/Output.pm:        MIT
# lib/Test/Run/Sprintf/Named/FromAccessors.pm:  MIT
# lib/Test/Run/Straps.pm:           MIT
# lib/Test/Run/Straps/Base.pm:      MIT
# lib/Test/Run/Straps/EventWrapper.pm:      MIT
# lib/Test/Run/Straps/StrapsTotalsObj.pm:   MIT
# lib/Test/Run/Straps_GplArt.pm:    "as perl, ie. GPL-2.0-only OR Artistic-1.0-Perl"
# lib/Test/Run/Trap/Obj.pm:         MIT
# LICENSE:                          MIT
# README:                           documents (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
# t/accumulate.t:                   MIT
# t/base.t:                         MIT
# t/hierarchy.t:                    MIT
# t/output.t:                       MIT
# t/test-failure-report.t           MIT
# t/switches.t:                     MIT
## Unbundled, never used
# t/lib/if.pm                       GPL-1.0-or-later OR Artistic-1.0-Perl
# t/lib/Test/Builder.pm:            GPL-1.0-or-later OR Artistic-1.0-Perl
# t/lib/Test/More.pm:               GPL-1.0-or-later OR Artistic-1.0-Perl
# t/lib/Test/Simple.pm:             GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-only AND MIT
URL:            https://metacpan.org/release/Test-Run
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Test-Run-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec) >= 0.6
BuildRequires:  perl(lib)
# Prefer Module::Build over ExtUtils::Maker because the Test::Run::Builder
# uses Module::Build too
BuildRequires:  perl(Module::Build) >= 0.36
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(IPC::System::Simple) >= 1.21
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(overload)
# POSIX is optional
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(TAP::Parser) >= 3.09
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Text::Sprintf::Named) >= 0.02
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(UNIVERSAL::require)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(if)
BuildRequires:  perl(POSIX)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::TrailingSpace)
Requires:       perl(IPC::System::Simple) >= 1.21
Requires:       perl(TAP::Parser) >= 3.09
Requires:       perl(Text::Sprintf::Named) >= 0.02

# Remove under-specified dependenices
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((IPC::System::Simple|TAP::Parser|Text::Sprintf::Named)\\)$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\((Dev::Null|MyFoo|MyHello)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Dev::Null|MyClass::|MyFoo|MyHello|MyTestRun::)
# Hide intetionally broken shebangs
%global __requires_exclude %{__requires_exclude}|^/usr/bin/perl-latest$

%description
These Perl modules are an improved test harness based on Test::Harness, but
more modular, extensible and object-oriented.

%package tests
Summary:        Tests for %{name}
License:        MIT
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(if)
Requires:       perl(TAP::Parser) >= 3.09

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Test-Run-%{version}
# Remove bundled modules
rm -rf t/lib/Test
rm -rf t/lib/if.pm
perl -i -n -e 'print $_ unless m{^t/lib/Test/}' MANIFEST
perl -i -n -e 'print $_ unless m{^t/lib/if\.pm}' MANIFEST
# Correct shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
# Correct permissions
chmod a+x t/data/interpreters/wrong-mini-ok.pl\
    t/sample-tests/{inc_taint,invalid-perl,leak-file.t,no_output,segfault,shbang_misparse,taint,taint_warn,test_more_fail.t,with-myhello,with-myhello-and-myfoo,skipall}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir="$RPM_BUILD_ROOT" create_packlist=0
%{_fixperms} "$RPM_BUILD_ROOT"/*
# Install tests
mkdir -p "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cp -a t "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
# Remove tests that cannot work out of source tree
rm "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/t/{pod,pod-coverage,style-trailing-space}.t
cat > "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/leaked-dir.t writes to CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes DONE examples NOTES README TODO
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/Run
%{perl_vendorlib}/Test/Run.pm
%{_mandir}/man3/Test::Run.*
%{_mandir}/man3/Test::Run::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0306-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 10 2024 Petr Pisar <ppisar@redhat.com> - 0.0306-1
- 0.0306 bump

* Wed Aug 07 2024 Petr Pisar <ppisar@redhat.com> - 0.0305-13
- Correct a license tag to "(GPL-1.0-or-later OR Artistic-1.0-Perl) AND
  GPL-2.0-only AND MIT"
- Package the tests

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0305-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0305-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0305-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0305-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0305-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0305-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.0305-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0305-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0305-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.0305-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0305-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0305-1
- 0.0305 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0304-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0304-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0304-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0304-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.0304-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0304-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0304-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0304-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0304-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0304-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.0304-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0304-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0304-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0304-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Petr Pisar <ppisar@redhat.com> - 0.0304-1
- 0.0304 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0303-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.0303-2
- Perl 5.22 rebuild

* Mon Jun 01 2015 Petr Pisar <ppisar@redhat.com> - 0.0303-1
- 0.0303 bump

* Fri Feb 27 2015 Petr Pisar <ppisar@redhat.com> 0.0302-1
- Specfile autogenerated by cpanspec 1.78.
