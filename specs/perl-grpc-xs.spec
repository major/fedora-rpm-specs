Name:           perl-grpc-xs
Version:        0.38
Release:        7%{?dist}
Summary:        Perl binding to a client part of the gRPC library
# examples/route_guide/route_guide.proto:   BSD-3-Clause
# LICENSE:      Apache-2.0 text
# ppport.h:     GPL-1.0-or-later OR Artistic-1.0-Perl
License:        Apache-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause
URL:            https://metacpan.org/dist/grpc-xs
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JOYREX/grpc-xs-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  grpc-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)

%description
This is a low-level binding to a client part of the gRPC library.

%package tests
Summary:        Tests for %{name}
License:        Apache-2.0
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -n Grpc-XS-%{version} -p1
# Fix shebangs in examples
perl -MConfig -i -p -e 's/^#!perl\b/$Config{startperl}/' examples/*/t/*.t
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS"
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
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc examples README.md
%dir %{perl_vendorarch}/auto/Grpc
%{perl_vendorarch}/auto/Grpc/XS
%dir %{perl_vendorarch}/Grpc
%{perl_vendorarch}/Grpc/Client
%{perl_vendorarch}/Grpc/Constants.pm
%{perl_vendorarch}/Grpc/XS
%{perl_vendorarch}/Grpc/XS.pm
%{_mandir}/man3/Grpc::XS.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-5
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 09 2023 Petr Pisar <ppisar@redhat.com> - 0.38-2
- Update upstream URL

* Thu Nov 02 2023 Petr Pisar <ppisar@redhat.com> - 0.38-1
- 0.38 bump

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-8
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Florian Weimer <fweimer@redhat.com> - 0.37-6
- Do not call undeclared exit function in Makefile.PL for C99 compatibility

* Tue Aug 23 2022 Petr Pisar <ppisar@redhat.com> - 0.37-5
- Rebuilt for abseil-cpp 20220623.0 and grpc 1.48.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-3
- Perl 5.36 rebuild

* Mon May 16 2022 Petr Pisar <ppisar@redhat.com> - 0.37-2
- Rebuild against grpc 1.46.1 (bug #2024386)

* Tue May 10 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.37-1
- Update to 0.37
- Supports grpc 1.45+ with no insecure build (fix RHBZ#2082323)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Petr Pisar <ppisar@redhat.com> - 0.36-2
- Rebuild against grpc 1.41.0 (bug #2008569)

* Wed Sep 01 2021 Petr Pisar <ppisar@redhat.com> - 0.36-1
- 0.36 bump

* Wed Aug 04 2021 Petr Pisar <ppisar@redhat.com> - 0.35-6
- Rebuild for grpc 1.39

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Petr Pisar <ppisar@redhat.com> - 0.35-4
- Rebuild with grpc-1.37 and perl-5.34

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-3
- Perl 5.34 rebuild

* Tue May 11 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.35-2
- Rebuild for grpc 1.37

* Mon Apr 26 2021 Petr Pisar <ppisar@redhat.com> - 0.35-1
- 0.35 bump

* Thu Apr 22 2021 Petr Pisar <ppisar@redhat.com> - 0.34-3
- Adapt to grpc-1.32.0 (CPAN RT#135258)
- Package the tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Petr Pisar <ppisar@redhat.com> - 0.34-1
- 0.34 bump

* Mon Oct 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-1
- 0.33 bump

* Mon Aug 03 2020 Petr Pisar <ppisar@redhat.com> - 0.32-5
- Adjust the tests to a stronger crypto-policy (bug #1862951)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Petr Pisar <ppisar@redhat.com> - 0.32-1
- 0.32 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Petr Pisar <ppisar@redhat.com> - 0.31-3
- Remove fork tests that are not supported in grpc and halt since grpc-1.20.0
  (bug #1715774)

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-2
- Perl 5.30 rebuild

* Mon May 13 2019 Petr Pisar <ppisar@redhat.com> - 0.31-1
- 0.31 bump

* Mon Mar 18 2019 Petr Pisar <ppisar@redhat.com> - 0.30-1
- 0.30 bump

* Thu Mar 14 2019 Petr Pisar <ppisar@redhat.com> 0.20-1
- Specfile autogenerated by cpanspec 1.78.
