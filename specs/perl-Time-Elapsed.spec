Name:           perl-Time-Elapsed
Version:        0.34
Release:        1%{?dist}
Summary:        Convert elapsed seconds into a human readable string
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Time-Elapsed
Source0:        https://www.cpan.org/authors/id/B/BU/BURAK/Time-Elapsed-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(parent)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(subs)
# Test::CPAN::Meta not helpful
BuildRequires:  perl(Test::More)
Requires:       perl(File::Spec)
Requires:       perl(Symbol)

%description
This module transforms the elapsed seconds into a human readable string. It
can be used for (for example) rendering uptime values into a human readable
form. The resulting string will be an approximation.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Time-Elapsed-%{version}
# Remove always skipped tests
for F in t/author-distmeta.t t/author-pod-coverage.t t/author-pod-syntax.t; do
    rm -- "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
# Correct shell bangs
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
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes
%license LICENSE
%dir %{perl_vendorlib}/Time
%{perl_vendorlib}/Time/Elapsed
%{perl_vendorlib}/Time/Elapsed.pm
%{_mandir}/man3/Time::Elapsed.*
%{_mandir}/man3/Time::Elapsed::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Apr 07 2026 Petr Pisar <ppisar@redhat.com> 0.34-1
- 0.34 version packaged
