Name:           perl-Test2-Plugin-Cover
%global cpan_version 0.000027
Version:        0.0.27
Release:        13%{?dist}
Summary:        Collect minimal file coverage data
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Plugin-Cover
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-Cover-%{cpan_version}.tar.gz
# Adjust line numbers after adding shebangs, no suitable for upstream
Patch0:         Test2-Plugin-Cover-0.000027-Adapt-tests-to-added-shebangs.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Path::Tiny) >= 0.048
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test2::API) >= 1.302166
BuildRequires:  perl(Test2::EventFacet) >= 1.302166
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test2::V0) >= 0.000130
Requires:       perl(Path::Tiny) >= 0.048
Requires:       perl(Test2::API) >= 1.302166
Requires:       perl(Test2::EventFacet) >= 1.302166

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Path::Tiny|Test2::API|Test2::V0)\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\((Fake.|OpenXXX)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Fake.|OpenXXX)\\)

%description
This Test2 plugin will collect minimal file coverage data, and will do so with
a minimal performance impact.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Path::Tiny) >= 0.048
Requires:       perl(Test2::V0) >= 0.000130

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Test2-Plugin-Cover-%{cpan_version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
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
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Test2*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.27-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.27-10
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.27-6
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.27-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Petr Pisar <ppisar@redhat.com> - 0.0.27-1
- 0.000027 bump (bug #2020455)

* Thu Nov 04 2021 Petr Pisar <ppisar@redhat.com> - 0.0.26-1
- 0.000026 bump (bug #2020029)

* Wed Sep 22 2021 Petr Pisar <ppisar@redhat.com> - 0.0.25-1
- 0.000025 bump

* Wed Jul 28 2021 Petr Pisar <ppisar@redhat.com> - 0.0.24-1
- 0.000024 bump

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Petr Pisar <ppisar@redhat.com> - 0.0.23-1
- 0.000023 bump

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.22-2
- Perl 5.34 rebuild

* Mon Apr 26 2021 Petr Pisar <ppisar@redhat.com> - 0.0.22-1
- 0.000022 bump

* Thu Apr 22 2021 Petr Pisar <ppisar@redhat.com> - 0.0.19-1
- 0.000019 bump

* Mon Apr 19 2021 Petr Pisar <ppisar@redhat.com> - 0.0.18-1
- 0.000018 bump

* Fri Apr 16 2021 Petr Pisar <ppisar@redhat.com> - 0.0.16-1
- 0.000016 bump

* Thu Apr 15 2021 Petr Pisar <ppisar@redhat.com> - 0.0.15-1
- 0.000015 bump

* Mon Apr 12 2021 Petr Pisar <ppisar@redhat.com> - 0.0.14-1
- 0.000014 bump

* Fri Apr 09 2021 Petr Pisar <ppisar@redhat.com> - 0.0.13-1
- 0.000013 bump
- Package the tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Petr Pisar <ppisar@redhat.com> - 0.0.9-1
- 0.000009 bump

* Thu Jul 09 2020 Petr Pisar <ppisar@redhat.com> 0.0.7-1
- Specfile autogenerated by cpanspec 1.78.
