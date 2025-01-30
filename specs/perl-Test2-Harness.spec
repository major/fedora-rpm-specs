# Enable a coverage plugin
%bcond_without perl_Test2_Harness_enables_coverage

Name:           perl-Test2-Harness
%global cpan_version 1.000156
Version:        1.0.156
Release:        1%{?dist}
Summary:        Test2 Harness designed for the Test2 event system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Harness
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Harness-%{cpan_version}.tar.gz
# Help generators to recognize a Perl code
Patch99:        Test2-Harness-1.000114-Adapt-tests-to-shebangs.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# git not used by App::Yath::Plugin::Git at the tests
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Devel::Cover)
# Devel::NYTProf not used at tests
# Email::Stuffer 0.016 not used at tests
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.11
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(goto::file) >= 0.005
# HTTP::Tiny 0.070 not used at tests
# HTTP::Tiny::Multipart not used at tests
BuildRequires:  perl(Importer) >= 0.025
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Handle) >= 1.27
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Linux::Inotify2)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Long::Jump) >= 0.000001
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::ANSIColor) >= 4.03
BuildRequires:  perl(Term::Table) >= 0.015
BuildRequires:  perl(Test::Builder::Formatter) >= 1.302170
BuildRequires:  perl(Test2::API) >= 1.302170
BuildRequires:  perl(Test2::Event) >= 1.302170
BuildRequires:  perl(Test2::Formatter) >= 1.302170
BuildRequires:  perl(Test2::Hub)
%if %{with perl_Test2_Harness_enables_coverage}
%define test2_plugin_cover_min_version 0.000025
BuildRequires:  perl(Test2::Plugin::Cover) >= %{test2_plugin_cover_min_version}
%endif
# Test2::Plugin::DBIProfile not used at tests
BuildRequires:  perl(Test2::Plugin::IOEvents) >= 0.001001
BuildRequires:  perl(Test2::Plugin::MemUsage) >= 0.002003
BuildRequires:  perl(Test2::Plugin::UUID) >= 0.002001
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Util) >= 1.302170
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(Test2::Util::Table)
BuildRequires:  perl(Test2::Util::Term) >= 0.000127
BuildRequires:  perl(Test2::Util::Times)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::HiRes)
# Win32::Console::ANSI not used on Linux
BuildRequires:  perl(YAML::Tiny)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(ok)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::Bundle::Extended) >= 0.000127
BuildRequires:  perl(Test2::Require::AuthorTesting)
BuildRequires:  perl(Test2::Tools::AsyncSubtest) >= 0.000127
BuildRequires:  perl(Test2::Tools::GenTemp)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(Test2::Tools::Subtest) >= 0.000127
BuildRequires:  perl(Test2::Tools::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000127
BuildRequires:  perl(Test::Builder) >= 1.302170
BuildRequires:  perl(Test::More) >= 1.302170
BuildRequires:  perl(utf8)
# Optional tests:
%if %{with perl_Test2_Harness_enables_coverage}
%define test2_require_module_min_version 0.000127
BuildRequires:  perl(Test2::Require::Module) >= %{test2_require_module_min_version}
%endif
# t2/lib/App/Yath/Plugin/SelfTest.pm tries building a C code using a gcc and
# to run a bash script. But SelfTest.pm itself is never executed.
# bash not used
# gcc not used
# App::Yath::Plugin::Git tries "git" command
Suggests:       git-core
Suggests:       perl(Cpanel::JSON::XS)
Requires:       perl(Data::Dumper)
Suggests:       perl(Devel::Cover)
Suggests:       perl(Devel::NYTProf)
Suggests:       perl(Email::Stuffer) >= 0.016
Requires:       perl(Exporter)
Requires:       perl(File::Path) >= 2.11
Suggests:       perl(FindBin)
Requires:       perl(goto::file) >= 0.005
Suggests:       perl(HTTP::Tiny) >= 0.070
Suggests:       perl(HTTP::Tiny::Multipart) >= 0.08
Requires:       perl(Importer) >= 0.025
Requires:       perl(IO::Compress::Bzip2)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::Uncompress::Bunzip2)
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(IO::Handle) >= 1.27
Suggests:       perl(IO::Pager) >= 1.00
Suggests:       perl(JSON::MaybeXS)
Requires:       perl(JSON::PP)
Suggests:       perl(Linux::Inotify2)
Requires:       perl(Long::Jump) >= 0.000001
Suggests:       perl(Term::ANSIColor) >= 4.03
Requires:       perl(Term::Table) >= 0.015
Requires:       perl(Test2::API) >= 1.302170
Requires:       perl(Test2::Event) >= 1.302170
Requires:       perl(Test2::Formatter) >= 1.302170
Requires:       perl(Test2::Hub)
%if %{with perl_Test2_Harness_enables_coverage}
Suggests:       perl(Test2::Plugin::Cover) >= %{test2_plugin_cover_min_version}
%endif
Suggests:       perl(Test2::Plugin::DBIProfile) >= 0.002002
Requires:       perl(Test2::Plugin::IOEvents) >= 0.001001
Requires:       perl(Test2::Plugin::MemUsage) >= 0.002003
Requires:       perl(Test2::Plugin::UUID) >= 0.002001
Requires:       perl(Test2::Util) >= 1.302170
Requires:       perl(Test2::Util::Term) >= 0.000127
Requires:       perl(Test::Builder::Formatter) >= 1.302170

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::Path|goto::file|Importer|IO::Handle|List::Util|Long::Jump|Term::Table|Test2::API|Test2::Formatter|Test2::Util|Test2::Util::Term|Test2::V0|Test::Builder|Test::More|Test2::Plugin::Cover|Test2::Require::Module)\\)$
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\((Ax|Bar|Baz|Bx|Cx|Foo|main::HBase|main::HBase::Wrapped)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((AAA|Ax|App::Yath::Command::(Broken|Fake|fake)|App::Yath::Plugin::(Options|SelfTest|Test|TestPlugin)|Bar|Baz|Bx|BBB|Broken|CCC|Cx|FAST|Foo|Manager|Plugin|Preload|Preload::[^)]*|Resource|SmokePlugin|TestPreload|TestSimplePreload)\\)

%description
This is a test harness toolkit for Perl Test2 system. It provides a yath tool,
a command-line tool for executing the tests under the Test2 harness.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(FindBin)
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Test::Builder) >= 1.302170
Requires:       perl(Test::More) >= 1.302170
%if %{with perl_Test2_Harness_enables_coverage}
Requires:       perl(Test2::Plugin::Cover) >= %{test2_plugin_cover_min_version}
Requires:       perl(Test2::Require::Module) >= %{test2_require_module_min_version}
%endif
Requires:       perl(Test2::V0) >= 0.000127

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Test2-Harness-%{cpan_version}
chmod -x t2/non_perl/test.c
%if !%{with perl_Test2_Harness_enables_coverage}
for T in t/integration/coverage{,2,3,4}.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{\A\Q'"$T"'\E\b' MANIFEST
done
%endif
# Help generators to recognize a Perl code
%patch -P 99 -p 1
for F in test.pl $(find t t2 -name '*.t' -o -name '*.tx') t/unit/App/Yath/Plugin/Git.script; do
    perl -i -MConfig -pe 'print qq{$Config{startperl}\n} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
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
cp -a test.pl t t2 %{buildroot}%{_libexecdir}/%{name}
# Remove tests which enumerate files in ./lib
for F in t/0-load_all.t t/1-pod_name.t; do
    rm %{buildroot}%{_libexecdir}/%{name}/"$F"
done
# Use /usr/bin/yath
ln -s $(realpath --relative-to %{buildroot}%{_libexecdir}/%{name} \
    %{buildroot}%{_bindir}) \
    %{buildroot}%{_libexecdir}/%{name}/scripts
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/integration/test.t writes into CWD,
# <https://github.com/Test-More/Test2-Harness/issues/259>
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset AUTHOR_TESTING AUTOMATED_TESTING DBI_PROFILE FAIL_ALWAYS FAIL_ONCE \
    FAILURE_DO_PASS GIT_BRANCH GIT_COMMAND GIT_LONG_SHA GIT_SHORT_SHA GIT_STATUS \
    HARNESS_IS_VERBOSE NESTED_YATH RESOURCE_TEST \
    T2_HARNESS_IS_VERBOSE T2_HARNESS_JOB_IS_TRY T2_HARNESS_JOB_FILE \
    T2_HARNESS_MY_JOB_CONCURRENCY T2_HARNESS_MY_JOB_COUNT \
    T2_HARNESS_MY_MAX_JOB_CONCURRENCY T2_HARNESS_STAGE \
    T2_HARNESS_JOB_CONCURRENCY TEST2_HARNESS_ACTIVE TEST2_HARNESS_LOG_FORMAT \
    TEST2_HARNESS_NO_WRITE_TEST_INFO \
    YATH_INTERACTIVE YATH_LOG_FILE_FORMAT YATH_SELF_TEST
export AUTOMATED_TESTING=1
T2_HARNESS_JOB_COUNT="$(getconf _NPROCESSORS_ONLN)" ./test.pl
prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r ./t
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING AUTOMATED_TESTING DBI_PROFILE FAIL_ALWAYS FAIL_ONCE \
    FAILURE_DO_PASS GIT_BRANCH GIT_COMMAND GIT_LONG_SHA GIT_SHORT_SHA GIT_STATUS \
    HARNESS_IS_VERBOSE NESTED_YATH RESOURCE_TEST \
    T2_HARNESS_IS_VERBOSE T2_HARNESS_JOB_IS_TRY T2_HARNESS_JOB_FILE \
    T2_HARNESS_MY_JOB_CONCURRENCY T2_HARNESS_MY_JOB_COUNT \
    T2_HARNESS_MY_MAX_JOB_CONCURRENCY T2_HARNESS_STAGE \
    T2_HARNESS_JOB_CONCURRENCY TEST2_HARNESS_ACTIVE TEST2_HARNESS_LOG_FORMAT \
    TEST2_HARNESS_NO_WRITE_TEST_INFO \
    YATH_INTERACTIVE YATH_LOG_FILE_FORMAT YATH_SELF_TEST
export AUTOMATED_TESTING=1
export T2_HARNESS_JOB_COUNT=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; $j=1 unless $j; print "$j"' -- \
    %{?_smp_mflags})
export HARNESS_OPTIONS=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; print "j$j" if $j' -- \
    %{?_smp_mflags})
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/yath
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/Yath
%{perl_vendorlib}/App/Yath.pm
%dir %{perl_vendorlib}/Test2
%{perl_vendorlib}/Test2/Formatter
%{perl_vendorlib}/Test2/Harness
%{perl_vendorlib}/Test2/Harness.pm
%dir %{perl_vendorlib}/Test2/Tools
%{perl_vendorlib}/Test2/Tools/HarnessTester.pm
%{_mandir}/man1/yath.*
%{_mandir}/man3/App::Yath.*
%{_mandir}/man3/App::Yath::*
%{_mandir}/man3/Test2::Formatter*
%{_mandir}/man3/Test2::Harness.*
%{_mandir}/man3/Test2::Harness::*
%{_mandir}/man3/Test2::Tools::HarnessTester.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Jan 28 2025 Petr Pisar <ppisar@redhat.com> - 1.0.156-1
- 1.000156 bump

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.155-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.155-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.155-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.155-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 04 2023 Petr Pisar <ppisar@redhat.com> - 1.0.155-1
- 1.000155 bump

* Tue Oct 03 2023 Petr Pisar <ppisar@redhat.com> - 1.0.154-1
- 1.000154 bump

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.152-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 04 2023 Petr Pisar <ppisar@redhat.com> - 1.0.152-1
- 1.000152 bump

* Thu Mar 09 2023 Petr Pisar <ppisar@redhat.com> - 1.0.151-1
- 1.000151 bump

* Thu Mar 02 2023 Petr Pisar <ppisar@redhat.com> - 1.0.150-1
- 1.000150 bump

* Wed Mar 01 2023 Petr Pisar <ppisar@redhat.com> - 1.0.149-1
- 1.000149 bump

* Mon Feb 27 2023 Petr Pisar <ppisar@redhat.com> - 1.0.148-1
- 1.000148 bump

* Wed Feb 22 2023 Petr Pisar <ppisar@redhat.com> - 1.0.147-1
- 1.000147 bump

* Tue Feb 21 2023 Petr Pisar <ppisar@redhat.com> - 1.0.146-1
- 1.000146 bump

* Thu Feb 16 2023 Petr Pisar <ppisar@redhat.com> - 1.0.145-1
- 1.000145 bump

* Thu Jan 26 2023 Petr Pisar <ppisar@redhat.com> - 1.0.142-1
- 1.000142 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.141-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Petr Pisar <ppisar@redhat.com> - 1.0.141-1
- 1.000141 bump

* Wed Dec 07 2022 Petr Pisar <ppisar@redhat.com> - 1.0.138-1
- 1.000138 bump

* Tue Dec 06 2022 Petr Pisar <ppisar@redhat.com> - 1.0.137-1
- 1.000137 bump

* Wed Nov 30 2022 Petr Pisar <ppisar@redhat.com> - 1.0.136-1
- 1.000136 bump

* Thu Sep 08 2022 Petr Pisar <ppisar@redhat.com> - 1.0.133-1
- 1.000133 bump

* Wed Sep 07 2022 Petr Pisar <ppisar@redhat.com> - 1.0.131-1
- 1.000131 bump

* Mon Sep 05 2022 Petr Pisar <ppisar@redhat.com> - 1.0.128-1
- 1.000128 bump

* Thu Sep 01 2022 Petr Pisar <ppisar@redhat.com> - 1.0.127-1
- 1.000127 bump

* Wed Aug 31 2022 Petr Pisar <ppisar@redhat.com> - 1.0.126-1
- 1.000126 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Petr Pisar <ppisar@redhat.com> - 1.0.125-1
- 1.000125 bump

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.124-2
- Perl 5.36 rebuild

* Mon Apr 11 2022 Petr Pisar <ppisar@redhat.com> - 1.0.124-1
- 1.000124 bump

* Thu Apr 07 2022 Petr Pisar <ppisar@redhat.com> - 1.0.123-1
- 1.000123 bump

* Wed Apr 06 2022 Petr Pisar <ppisar@redhat.com> - 1.0.119-1
- 1.000119 bump

* Tue Apr 05 2022 Petr Pisar <ppisar@redhat.com> - 1.0.117-1
- 1.000117 bump

* Mon Apr 04 2022 Petr Pisar <ppisar@redhat.com> - 1.0.116-1
- 1.000116 bump

* Fri Apr 01 2022 Petr Pisar <ppisar@redhat.com> - 1.0.115-1
- 1.000115 bump

* Fri Mar 25 2022 Petr Pisar <ppisar@redhat.com> - 1.0.114-1
- 1.000114 bump

* Thu Mar 24 2022 Petr Pisar <ppisar@redhat.com> - 1.0.113-2
- Fix Test2::Harness::Runner::Reloader::reset() not to call blocking() method
  in case of no Linux::Inotify2 (bug #2067332)

* Thu Mar 24 2022 Petr Pisar <ppisar@redhat.com> - 1.0.113-1
- 1.000113 bump

* Wed Mar 16 2022 Petr Pisar <ppisar@redhat.com> - 1.0.112-1
- 1.000112 bump

* Thu Mar 10 2022 Petr Pisar <ppisar@redhat.com> - 1.0.111-1
- 1.000111 bump

* Fri Feb 25 2022 Petr Pisar <ppisar@redhat.com> - 1.0.110-1
- 1.000110 bump

* Wed Feb 23 2022 Petr Pisar <ppisar@redhat.com> - 1.0.109-1
- 1.000109 bump

* Mon Feb 14 2022 Petr Pisar <ppisar@redhat.com> - 1.0.108-1
- 1.000108 bump

* Fri Feb 11 2022 Petr Pisar <ppisar@redhat.com> - 1.0.107-1
- 1.000107 bump

* Wed Feb 09 2022 Petr Pisar <ppisar@redhat.com> - 1.0.106-1
- 1.000106 bump

* Mon Feb 07 2022 Petr Pisar <ppisar@redhat.com> - 1.0.104-1
- 1.000104 bump

* Fri Feb 04 2022 Petr Pisar <ppisar@redhat.com> - 1.0.102-1
- 1.000102 bump

* Thu Feb 03 2022 Petr Pisar <ppisar@redhat.com> - 1.0.101-1
- 1.000101 bump

* Wed Feb 02 2022 Petr Pisar <ppisar@redhat.com> - 1.0.100-1
- 1.000100 bump

* Fri Jan 28 2022 Petr Pisar <ppisar@redhat.com> - 1.0.99-2
- Adapt tests to slow CI (bug #2046568)

* Fri Jan 28 2022 Petr Pisar <ppisar@redhat.com> - 1.0.99-1
- 1.000099 bump

* Fri Jan 28 2022 Petr Pisar <ppisar@redhat.com> - 1.0.98-1
- 1.000098 bump

* Thu Jan 27 2022 Petr Pisar <ppisar@redhat.com> - 1.0.96-1
- 1.000096 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Petr Pisar <ppisar@redhat.com> - 1.0.95-1
- 1.000095 bump

* Mon Dec 20 2021 Petr Pisar <ppisar@redhat.com> - 1.0.93-1
- 1.000093 bump

* Fri Dec 17 2021 Petr Pisar <ppisar@redhat.com> - 1.0.92-1
- 1.000092 bump

* Thu Dec 16 2021 Petr Pisar <ppisar@redhat.com> - 1.0.91-1
- 1.000091 bump

* Tue Dec 14 2021 Petr Pisar <ppisar@redhat.com> - 1.0.88-1
- 1.000088 bump

* Fri Nov 19 2021 Petr Pisar <ppisar@redhat.com> - 1.0.82-1
- 1.000082 bump

* Tue Nov 16 2021 Petr Pisar <ppisar@redhat.com> - 1.0.81-1
- 1.000081 bump

* Fri Nov 05 2021 Petr Pisar <ppisar@redhat.com> - 1.0.80-1
- 1.000080 bump

* Mon Nov 01 2021 Petr Pisar <ppisar@redhat.com> - 1.0.79-1
- 1.000079 bump

* Fri Oct 29 2021 Petr Pisar <ppisar@redhat.com> - 1.0.78-1
- 1.000078 bump

* Mon Oct 25 2021 Petr Pisar <ppisar@redhat.com> - 1.0.76-2
- Fix running tests from /tmp (bug #2016544)

* Mon Oct 25 2021 Petr Pisar <ppisar@redhat.com> - 1.0.76-1
- 1.000076 bump

* Thu Oct 21 2021 Petr Pisar <ppisar@redhat.com> - 1.0.74-1
- 1.000074 bump

* Wed Sep 22 2021 Petr Pisar <ppisar@redhat.com> - 1.0.73-1
- 1.000073 bump

* Tue Sep 14 2021 Petr Pisar <ppisar@redhat.com> - 1.0.72-1
- 1.000072 bump

* Mon Sep 06 2021 Petr Pisar <ppisar@redhat.com> - 1.0.71-1
- 1.000071 bump

* Thu Sep 02 2021 Petr Pisar <ppisar@redhat.com> - 1.0.70-1
- 1.000070 bump

* Wed Sep 01 2021 Petr Pisar <ppisar@redhat.com> - 1.0.69-1
- 1.000069 bump

* Mon Aug 16 2021 Petr Pisar <ppisar@redhat.com> - 1.0.66-1
- 1.000066 bump

* Mon Aug 09 2021 Petr Pisar <ppisar@redhat.com> - 1.0.65-1
- 1.000065 bump

* Tue Aug 03 2021 Petr Pisar <ppisar@redhat.com> - 1.0.64-1
- 1.000064 bump

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Petr Pisar <ppisar@redhat.com> - 1.0.63-1
- 1.000063 bump

* Thu Jul 08 2021 Petr Pisar <ppisar@redhat.com> - 1.0.62-1
- 1.000062 bump

* Wed Jul 07 2021 Petr Pisar <ppisar@redhat.com> - 1.0.60-1
- 1.000060 bump

* Fri Jul 02 2021 Petr Pisar <ppisar@redhat.com> - 1.0.59-1
- 1.000059 bump

* Wed Jun 16 2021 Petr Pisar <ppisar@redhat.com> - 1.0.58-1
- 1.000058 bump

* Tue Jun 08 2021 Petr Pisar <ppisar@redhat.com> - 1.0.57-1
- 1.000057 bump

* Tue May 25 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.56-2
- Perl 5.34 re-rebuild updated packages

* Tue May 25 2021 Petr Pisar <ppisar@redhat.com> - 1.0.56-1
- 1.000056 bump

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.55-2
- Perl 5.34 rebuild

* Wed May 19 2021 Petr Pisar <ppisar@redhat.com> - 1.0.55-1
- 1.000055 bump

* Wed May 05 2021 Petr Pisar <ppisar@redhat.com> - 1.0.54-1
- 1.000054 bump

* Mon May 03 2021 Petr Pisar <ppisar@redhat.com> - 1.0.53-1
- 1.000053 bump

* Thu Apr 29 2021 Petr Pisar <ppisar@redhat.com> - 1.0.51-1
- 1.000051 bump

* Wed Apr 28 2021 Petr Pisar <ppisar@redhat.com> - 1.0.50-1
- 1.000050 bump

* Tue Apr 27 2021 Petr Pisar <ppisar@redhat.com> - 1.0.49-1
- 1.000049 bump

* Mon Apr 26 2021 Petr Pisar <ppisar@redhat.com> - 1.0.48-2
- Correct a minimal Test2::Plugin::Cover version

* Mon Apr 26 2021 Petr Pisar <ppisar@redhat.com> - 1.0.48-1
- 1.000048 bump

* Wed Apr 21 2021 Petr Pisar <ppisar@redhat.com> - 1.0.47-1
- 1.000047 bump

* Fri Mar 12 2021 Petr Pisar <ppisar@redhat.com> - 1.0.44-1
- 1.000044 bump

* Wed Mar 10 2021 Petr Pisar <ppisar@redhat.com> - 1.0.43-2
- A test needs FindBin

* Mon Mar 08 2021 Petr Pisar <ppisar@redhat.com> - 1.0.43-1
- 1.000043 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Petr Pisar <ppisar@redhat.com> - 1.0.42-1
- 1.000042 bump

* Tue Nov 03 2020 Petr Pisar <ppisar@redhat.com> - 1.0.38-1
- 1.000038 bump

* Fri Oct 30 2020 Petr Pisar <ppisar@redhat.com> - 1.0.35-1
- 1.000035 bump

* Thu Oct 29 2020 Petr Pisar <ppisar@redhat.com> - 1.0.34-1
- 1.000034 bump

* Thu Oct 29 2020 Petr Pisar <ppisar@redhat.com> - 1.0.33-1
- 1.000033 bump

* Mon Oct 26 2020 Petr Pisar <ppisar@redhat.com> - 1.0.32-1
- 1.000032 bump

* Fri Oct 23 2020 Petr Pisar <ppisar@redhat.com> - 1.0.31-1
- 1.000031 bump

* Thu Oct 22 2020 Petr Pisar <ppisar@redhat.com> - 1.0.30-1
- 1.000030 bump

* Mon Oct 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.29-1
- 1.000029 bump

* Tue Sep 29 2020 Petr Pisar <ppisar@redhat.com> - 1.0.28-1
- 1.000028 bump

* Tue Sep 22 2020 Petr Pisar <ppisar@redhat.com> - 1.0.27-1
- 1.000027 bump

* Wed Sep 09 2020 Petr Pisar <ppisar@redhat.com> - 1.0.26-1
- 1.000026 bump

* Tue Aug 25 2020 Petr Pisar <ppisar@redhat.com> - 1.0.24-1
- 1.000024 bump

* Tue Aug 18 2020 Petr Pisar <ppisar@redhat.com> - 1.0.23-1
- 1.000023 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Petr Pisar <ppisar@redhat.com> - 1.0.20-1
- 1.000020 bump

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.19-2
- Perl 5.32 rebuild

* Mon Jun 01 2020 Petr Pisar <ppisar@redhat.com> - 1.0.19-1
- 1.000019 bump

* Tue Apr 14 2020 Petr Pisar <ppisar@redhat.com> - 1.0.18-1
- 1.000018 bump

* Wed Apr 08 2020 Petr Pisar <ppisar@redhat.com> - 1.0.16-1
- 1.000016 bump

* Tue Mar 24 2020 Petr Pisar <ppisar@redhat.com> - 1.0.15-1
- 1.000015 bump

* Mon Mar 23 2020 Petr Pisar <ppisar@redhat.com> - 1.0.14-1
- 1.000014 bump

* Thu Mar 19 2020 Petr Pisar <ppisar@redhat.com> - 1.0.13-1
- 1.000013 bump

* Tue Mar 10 2020 Petr Pisar <ppisar@redhat.com> - 1.0.11-1
- 1.000011 bump

* Mon Mar 09 2020 Petr Pisar <ppisar@redhat.com> - 1.0.10-1
- 1.000010 bump

* Mon Mar 02 2020 Petr Pisar <ppisar@redhat.com> - 1.0.3-1
- 1.000003 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001099-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Petr Pisar <ppisar@redhat.com> - 0.001099-1
- 0.001099 bump

* Mon Sep 09 2019 Petr Pisar <ppisar@redhat.com> - 0.001097-1
- 0.001097 bump

* Thu Sep 05 2019 Petr Pisar <ppisar@redhat.com> - 0.001095-1
- 0.001095 bump

* Wed Sep 04 2019 Petr Pisar <ppisar@redhat.com> - 0.001093-1
- 0.001093 bump

* Mon Sep 02 2019 Petr Pisar <ppisar@redhat.com> - 0.001091-1
- 0.001091 bump

* Fri Aug 30 2019 Petr Pisar <ppisar@redhat.com> - 0.001088-1
- 0.001088 bump

* Thu Aug 29 2019 Petr Pisar <ppisar@redhat.com> - 0.001086-1
- 0.001086 bump

* Thu Aug 22 2019 Petr Pisar <ppisar@redhat.com> - 0.001085-1
- 0.001085 bump

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> - 0.001084-1
- 0.001084 bump

* Wed Aug 14 2019 Petr Pisar <ppisar@redhat.com> - 0.001081-1
- 0.001081 bump

* Thu Aug 01 2019 Petr Pisar <ppisar@redhat.com> 0.001080-1
- Specfile autogenerated by cpanspec 1.78.
