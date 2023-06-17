# Perform optional tests
%bcond_without perl_XS_Parse_Keyword_enables_optional_test

Name:           perl-XS-Parse-Keyword
Version:        0.34
Release:        1%{?dist}
Summary:        XS functions to assist in parsing keyword syntax
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XS-Parse-Keyword
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Keyword-%{version}.tar.gz
Source1:        macros.perl-XS-Parse-Keyword
BuildRequires:  coreutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CChecker) >= 0.11
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(XSLoader)
# Tests:
# perl(:VERSION) >= 5.16 not yet used in t/70infix.t
BuildRequires:  perl(B::Deparse)
# Some t/*.xs tests need a newer ExtUtils::ParseXS
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.16
BuildRequires:  perl(overload)
BuildRequires:  perl(utf8)
BuildRequires:  perl(Test2::V0)
%if %{with perl_XS_Parse_Keyword_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
# This module maintains multiple ABIs whose compatibility is checked at
# run-time by S_boot_xs_parse_keyword() compiled into the users of this module.
# This ABI range is defined with XS::Parse::Keyword/ABIVERSION_MIN and
# XS::Parse::Keyword/ABIVERSION_MAX in lib/XS/Parse/Keyword.xs.
Provides:       perl(:XS_Parse_Keyword_ABI_1)
Provides:       perl(:XS_Parse_Keyword_ABI_2)
# This module maintains multiple ABIs whose compatibility is checked at
# run-time by S_boot_xs_parse_infix() compiled into the users of this module.
# This ABI range is defined with XS::Parse::Infix/ABIVERSION_MIN and
# XS::Parse::Infix/ABIVERSION_MAX in lib/XS/Parse/Keyword.xs.
Provides:       perl(:XS_Parse_Infix_ABI_1)
Provides:       perl(:XS_Parse_Infix_ABI_2)

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(testcase\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(testcase\\)

%description
This module provides some XS functions to assist in writing syntax modules
that provide new perl-visible syntax, primarily for authors of keyword plugins
using the PL_keyword_plugin hook mechanism.

%package Builder
Summary:        Build-time support for XS::Parse::Keyword
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-interpreter
# Subpackaged in 0.06
Conflicts:      %{name}%{?_isa} < 0.06

%description Builder
This module provides a build-time helper to assist authors writing XS modules
that use XS::Parse::Keyword. It prepares a Module::Build-using distribution to
be able to make use of XS::Parse::Keyword.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# ExtUtils::ParseXS is not needed at run-time because the XS tests are
# packaged precompiled.
Requires:       perl(XSLoader)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n XS-Parse-Keyword-%{version}
%if !%{with perl_XS_Parse_Keyword_enables_optional_test}
rm t/99pod.t
perl -i -ne 'print $_ unless m{\A\Qt/99pod.t\E\b}' MANIFEST
%endif
chmod +x t/*.t

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
# Build object files for tests now. They are installed into tests subpackage.
./Build testlib

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
install -D -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE1}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
find %{buildroot}%{_libexecdir}/%{name} -type f \
    \( -name '*.bs' -o -name '*.c' -o -name '*.o' \) -delete
%if %{with perl_XS_Parse_Keyword_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorarch}/auto/XS
%dir %{perl_vendorarch}/auto/XS/Parse
%{perl_vendorarch}/auto/XS/Parse/Keyword
%dir %{perl_vendorarch}/XS
%dir %{perl_vendorarch}/XS/Parse
%{perl_vendorarch}/XS/Parse/Infix.pm
%{perl_vendorarch}/XS/Parse/Keyword.pm
%{_mandir}/man3/XS::Parse::Infix.*
%{_mandir}/man3/XS::Parse::Keyword.*

%files Builder
%{perl_vendorarch}/XS/Parse/Infix
%{perl_vendorarch}/XS/Parse/Keyword
%{_mandir}/man3/XS::Parse::Infix::*
%{_mandir}/man3/XS::Parse::Keyword::*
%{_rpmmacrodir}/macros.%{name}

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Jun 15 2023 Petr Pisar <ppisar@redhat.com> - 0.34-1
- 0.34 bump

* Mon Feb 20 2023 Petr Pisar <ppisar@redhat.com> - 0.33-1
- 0.33 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Petr Pisar <ppisar@redhat.com> - 0.32-1
- 0.32 bump

* Thu Jan 05 2023 Petr Pisar <ppisar@redhat.com> - 0.31-1
- 0.31 bump

* Mon Dec 05 2022 Petr Pisar <ppisar@redhat.com> - 0.30-1
- 0.30 bump

* Fri Dec 02 2022 Petr Pisar <ppisar@redhat.com> - 0.29-1
- 0.29 bump

* Wed Nov 30 2022 Petr Pisar <ppisar@redhat.com> - 0.28-1
- 0.28 bump

* Tue Nov 01 2022 Petr Pisar <ppisar@redhat.com> - 0.27-1
- 0.27 bump

* Tue Oct 25 2022 Petr Pisar <ppisar@redhat.com> - 0.26-1
- 0.26 bump

* Tue Jul 26 2022 Petr Pisar <ppisar@redhat.com> - 0.25-1
- 0.25 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Petr Pisar <ppisar@redhat.com> - 0.24-1
- 0.24 bump

* Tue Jun 14 2022 Petr Pisar <ppisar@redhat.com> - 0.23-1
- 0.23 bump

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-2
- Perl 5.36 rebuild

* Tue Feb 22 2022 Petr Pisar <ppisar@redhat.com> - 0.22-1
- 0.22 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Petr Pisar <ppisar@redhat.com> - 0.21-1
- 0.21 bump (bug #2013044)

* Tue Oct 05 2021 Petr Pisar <ppisar@redhat.com> - 0.19-1
- 0.19 bump (bug #2010550)

* Wed Sep 29 2021 Petr Pisar <ppisar@redhat.com> - 0.18-1
- 0.18 bump

* Fri Sep 24 2021 Petr Pisar <ppisar@redhat.com> - 0.17-1
- 0.17 bump
- Fix a test failure on non-x86 platforms (bug #2007391)

* Wed Sep 22 2021 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump

* Tue Sep 07 2021 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Wed Sep 01 2021 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Tue Aug 31 2021 Petr Pisar <ppisar@redhat.com> - 0.13-2
- Return ABI 1

* Thu Aug 26 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-1
- 0.13 bump

* Tue Aug 17 2021 Petr Pisar <ppisar@redhat.com> - 0.12-2
- Bump ABI because XSParseKeywordPieceType changed size (bug #1994077)

* Tue Aug 17 2021 Petr Pisar <ppisar@redhat.com> - 0.12-1
- 0.12 bump

* Mon Aug 09 2021 Petr Pisar <ppisar@redhat.com> - 0.11-2
- Fix perl_XS_Parse_Keyword_ABI macro

* Tue Aug 03 2021 Petr Pisar <ppisar@redhat.com> - 0.11-1
- 0.11 bump

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Tue Jul 13 2021 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump

* Fri Jun 18 2021 Petr Pisar <ppisar@redhat.com> - 0.08-1
- 0.08 bump

* Wed Jun 02 2021 Petr Pisar <ppisar@redhat.com> - 0.06-1
- 0.06 bump
- Subpackage XS::Parse::Keyword::Builder

* Tue Jun 01 2021 Petr Pisar <ppisar@redhat.com> - 0.05-1
- 0.05 bump

* Tue May 25 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-2
- Perl 5.34 re-rebuild updated packages

* Tue May 25 2021 Petr Pisar <ppisar@redhat.com> - 0.04-1
- 0.04 bump

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-3
- Perl 5.34 rebuild

* Tue May 04 2021 Petr Pisar <ppisar@redhat.com> - 0.03-2
- Require XSLoader for the tests

* Fri Apr 30 2021 Petr Pisar <ppisar@redhat.com> 0.03-1
- Specfile autogenerated by cpanspec 1.78.
