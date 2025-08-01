Name:           perl-Crypt-URandom-Token
Version:        0.005
Release:        2%{?dist}
Summary:        Generate secure strings for passwords, secrets and similar
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Crypt-URandom-Token
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STIGTSP/Crypt-URandom-Token-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::URandom) >= 0.40
BuildRequires:  perl(Exporter)
# Tests
BuildRequires:  perl(Test::Exception) >= 0.43
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
Requires:       perl(Crypt::URandom) >= 0.40

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Crypt::URandom\\)$

%description
This module provides a secure way to generate a random token for passwords
and similar using Crypt::URandom as the source of random bits.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Crypt-URandom-Token-%{version}
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
%doc README SECURITY.md
%license LICENSE
%{perl_vendorlib}/Crypt*
%{_mandir}/man3/Crypt::URandom::Token*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu May 22 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-1
- 0.005 bump (rhbz#2367599)

* Fri Mar 28 2025 Jitka Plesnikova <jplesnik@redhat.com> 0.003-1
- Specfile autogenerated by cpanspec 1.78.
- Package tests
