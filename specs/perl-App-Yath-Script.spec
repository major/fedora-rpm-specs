Name:           perl-App-Yath-Script
Version:        2.000016
Release:        1%{?dist}
Summary:        Script initialization and utility functions for Test2::Harness
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/App-Yath-Script
Source0:        https://www.cpan.org/authors/id/E/EX/EXODIST/App-Yath-Script-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd) >= 3.75
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Yath) >= 2.000008
BuildRequires:  perl(goto::file)
BuildRequires:  perl(Importer) >= 0.025
# Tests:
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(PerlIO::scalar)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0) >= 1.302199
Requires:       perl(Cwd) >= 3.75
Requires:       perl(Getopt::Yath) >= 2.000008
Requires:       perl(goto::file)
Requires:       perl(Importer) >= 0.025
# /usr/bin/yath moved from perl-Test2-Harness
Conflicts:      perl-Test2-Harness < 1.0.163-2

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Cwd|Getopt::Yath|Importer|Test2::V0)\\)$

%description
This module provides the initial entry point for the yath script. It
handles script discovery, configuration loading, version detection, and
delegation to version-specific script modules (App::Yath::Script::V{X}).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Cwd) >= 3.75
Requires:       perl(Test2::V0) >= 1.302199

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n App-Yath-Script-%{version}
# Help generators to recognize Perl scripts
for F in $(find -type f -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
unset AUTOMATED_TESTING
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/unit/Script.t, writes into CWD, expects ./lib directory.
# t/acceptance/yath.t expects ./scripts/yath file.
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
mkdir lib scripts
ln -s /usr/bin/yath scripts/yath
unset T2_HARNESS_INCLUDES
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset T2_HARNESS_INCLUDES
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# README.md is reduntant to README
%doc Changes README
%{_bindir}/yath
%dir %{perl_vendorlib}/App
%dir %{perl_vendorlib}/App/Yath
%{perl_vendorlib}/App/Yath/Script
%{perl_vendorlib}/App/Yath/Script.pm
# This file shouldn't be there probably
# <https://github.com/Test-More/Test2-Harness/issues/448>
%{perl_vendorlib}/App/Yath/template.pod
%{_mandir}/man1/yath.*
%{_mandir}/man3/App::Yath::Script.*
%{_mandir}/man3/App::Yath::Script::*
%{_mandir}/man3/App::Yath::template.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Wed Apr 29 2026 Petr Pisar <ppisar@redhat.com> 2.000016-1
- 2.000016 packaged
