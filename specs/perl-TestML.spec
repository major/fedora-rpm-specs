%global upstream_version 0.54_05
Name:           perl-TestML
Version:        %(echo '%{upstream_version}' | tr _ .)
Release:        21%{?dist}
Summary:        Generic software Testing Meta Language
# src/perl5/pkg/doc/TestML.pod: GPL-1.0-or-later OR Artistic-1.0-Perl
# src/perl5/pkg/dist.ini:       GPL-1.0-or-later OR Artistic-1.0-Perl
## unused and not packaged
# src/testml-compiler-coffee/pkg/package.json:              MIT
# src/testml-compiler-perl5/pkg/doc/TestML/Compiler.pod:    GPL-1.0-or-later OR Artistic-1.0-Perl
# src/python/pkg/setup.py:      MIT
# src/python/pkg/LICENSE:       MIT text
# src/python/pkg/ReadMe.md:     MIT
# src/node/pkg/package.json:    MIT
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/testml-lang/testml/
Source0:        %{url}archive/pkg-perl5-%{upstream_version}.tar.gz
# Upstream build script requires checking out various git trees and
# executing sripts dowloaded from the Internet. Use a trivial Makefile.PL
# instead.
Source1:        Makefile.PL
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
# Carp not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
# Text::Diff not used at tests
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# XXX not used at tests
# Tests:
# bash for bin/getopt.sh
BuildRequires:  bash
# git in bin/getopt.sh not helpful
BuildRequires:  grep
# perl-Test-Harness for /usr/bin/prove
BuildRequires:  perl-Test-Harness
BuildRequires:  perl(constant)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pegex::Base)
BuildRequires:  perl(Pegex::Parser)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  which
Requires:       perl(Carp)
Requires:       perl(List::Util)
Requires:       perl(Text::Diff)
Requires:       perl(warnings)
Requires:       perl(XXX)

# Remove private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(TestML::Compiler.*\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((TestML::Compiler.*|TestMLBridge)\\)

%description
TestML <http://www.testml.org/> is a generic, programming language agnostic,
meta language for writing unit tests. The idea is that you can use the same
test files in multiple implementations of a given programming idea. Then you
can be more certain that your application written in, say, Python matches your
Perl implementation.

In a nutshell you write a bunch of data tests that have inputs and expected
results. Using a simple syntax, you specify what functions the data must pass
through to produce the expected results. You use a bridge class to write the
data functions that pass the data through your application.

In Perl 5, TestML module is the evolution of the Test::Base module. It has
a superset of Test:Base's goals. The data markup syntax is currently exactly
the same as Test::Base.

Currently, TestML is being redesigned. This package contains the new unstable
implementation. The original, production-ready, implementation is available
under TestML1 name in perl-TestML1 package.


%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       grep
Requires:       perl-Test-Harness
Requires:       perl(warnings)
Requires:       which

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n testml-pkg-perl5-%{upstream_version}
cd src/perl5
cp %{SOURCE1} .
mv pkg/doc/TestML.pod lib/
mv pkg/Changes .

%build
cd src/perl5
perl Makefile.PL VERSION=%{upstream_version} INSTALLDIRS=vendor \
    NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
cd src/perl5
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/bin
cp -a ../../bin/{getopt.sh,testml,testml-cli.sh,testml-compiler,testml-perl5-tap} %{buildroot}%{_libexecdir}/%{name}/upstream/bin
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/test
cp -a ../../test/runtime-tml %{buildroot}%{_libexecdir}/%{name}/upstream/test
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/src/perl5
cp -a test %{buildroot}%{_libexecdir}/%{name}/upstream/src/perl5
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/src/perl5/bin
cp -a bin/testml-perl5-tap %{buildroot}%{_libexecdir}/%{name}/upstream/src/perl5/bin
mkdir -p %{buildroot}%{_libexecdir}/%{name}/upstream/src/testml-compiler-perl5
cp -a ../testml-compiler-perl5/{bin,lib} %{buildroot}%{_libexecdir}/%{name}/upstream/src/testml-compiler-perl5
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# bin/testml writes tests compiled with TestML::Compiler into ./.testml.
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"/upstream/src/perl5
unset TESTML_BRIDGE TESTML_DEVEL TESTML_FILEVAR
export PATH=../../bin:$PATH TESTML_ROOT=../.. TESTML_RUN=perl5-tap
prove -I . -j "$(getconf _NPROCESSORS_ONLN)" test/*.tml
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
cd src/perl5
unset TESTML_BRIDGE TESTML_DEVEL TESTML_FILEVAR
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
PATH=../../bin:$PATH TESTML_ROOT=../.. TESTML_RUN=perl5-tap make test

%files
%doc src/perl5/Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 29 2022 Petr Pisar <ppisar@redhat.com> - 0.54.05-15
- Convert a License tag to an SPDX format
- Perform the tests
- Package the tests

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.54.05-13
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.54.05-10
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Petr Pisar <ppisar@redhat.com> - 0.54.05-8
- Modernize a spec file

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.54.05-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.54.05-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Petr Pisar <ppisar@redhat.com> - 0.54.05-1
- 0.54_05 bump
- Upstream moved from CPAN to GitHub
- TestML is now unstable, old TestML Perl modules are now available as TestML1
  Perl modules (install "perl(TestML1)")

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Petr Pisar <ppisar@redhat.com> - 0.54-1
- 0.54 bump

* Mon Jan 09 2017 Petr Pisar <ppisar@redhat.com> - 0.53-1
- 0.53 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-2
- Perl 5.22 rebuild

* Mon Jan 05 2015 Petr Pisar <ppisar@redhat.com> - 0.52-1
- 0.52 bump

* Thu Dec 18 2014 Petr Šabata <contyk@redhat.com> - 0.51-1
- 0.51 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.49-2
- Perl 5.20 rebuild

* Mon Aug 18 2014 Petr Pisar <ppisar@redhat.com> - 0.49-1
- 0.49 bump

* Thu Aug 14 2014 Petr Pisar <ppisar@redhat.com> - 0.44-1
- 0.44 bump

* Tue Aug 12 2014 Petr Pisar <ppisar@redhat.com> - 0.43-1
- 0.43 bump

* Thu Aug 07 2014 Petr Pisar <ppisar@redhat.com> - 0.42-1
- 0.42 bump

* Wed Jul 30 2014 Petr Pisar <ppisar@redhat.com> 0.37-1
- Specfile autogenerated by cpanspec 1.78.
