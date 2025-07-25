Name:           perl-UUID
Version:        0.37
Release:        3%{?dist}
Summary:        Universally Unique Identifier library for Perl
# README:       Artistic-2.0
# ulib/md5.c:   (GPL-1.0-or-later OR Artistic-1.0-Perl) AND RSA-MD
# ulib/sha1.c:  LicenseRef-Fedora-Public-Domain
# UUID.pm:      Artistic-2.0
# RSA-MD was raplaced by 2000 RSA grant and should not be enumerated
# <https://docs.fedoraproject.org/en-US/legal/misc/#_licensing_of_rsa_implementations_of_md5>.
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/UUID
Source0:        https://cpan.metacpan.org/authors/id/J/JR/JRM/UUID-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.5.63
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::CheckLib) >= 1.14
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.06
BuildRequires:  perl(File::Temp) >= 0.10
BuildRequires:  perl(List::Util) >= 1.29
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(version) >= 0.77
# Optional tests:
BuildRequires:  perl(Digest::SHA1)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::Temp|Test::More)\\)$
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(MyNote\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(MyNote\\)

%description
The UUID library is used to generate unique identifiers for objects that may
be accessible beyond the local system. The generated UUIDs are compatible with
those created by the Open Software Foundation (OSF) Distributed Computing
Environment (DCE).

All generated UUIDs are either version 1, 3, 4, 5, 6, or version 7. And all
are variant 1, meaning compliant with the OSF DCE standard as described in
RFC 4122. Versions 6 and 7 are not standardized. They are presented here as
proposed in RFC 4122bis, version 14, and may change in the future.

%package tests
Summary:        Tests for %{name}
License:        Artistic-2.0
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Digest::SHA1)
Requires:       perl(File::Temp) >= 0.10

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n UUID-%{version}
# Remove always skipped tests
for T in t/0gen.t t/5persist/symlink.t t/9benchmark/*.t; do
    rm -- "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done

%build
unset AUTOMATED_TESTING NONINTERACTIVE_TESTING PERL_CPAN_REPORTER_CONFIG
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -r -I t/0LIB -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes NOTES README
%{perl_vendorarch}/auto/UUID
%{perl_vendorarch}/UUID.pm
%{_mandir}/man3/UUID.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-2
- Perl 5.42 rebuild

* Mon Feb 24 2025 Petr Pisar <ppisar@redhat.com> - 0.37-1
- 0.37 bump

* Mon Feb 10 2025 Petr Pisar <ppisar@redhat.com> - 0.36-4
- Fix building with GCC 15 (bug #2341040)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Petr Pisar <ppisar@redhat.com> - 0.36-1
- 0.36 bump

* Thu Jun 13 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-2
- Perl 5.40 rebuild

* Fri May 31 2024 Petr Pisar <ppisar@redhat.com> 0.35-1
- Specfile autogenerated by cpanspec 1.78.
