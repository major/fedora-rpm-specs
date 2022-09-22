# Perform optional tests
%bcond_without perl_XS_Parse_Sublike_enables_optional_tests

Name:           perl-XS-Parse-Sublike
Version:        0.16
Release:        4%{?dist}
Summary:        XS functions to assist in parsing sub-like syntax
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/XS-Parse-Sublike
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Sublike-%{version}.tar.gz
Source1:        macros.perl-XS-Parse-Sublike
# Fix an integer overflow in croak(), CPAN RT#133035
Patch0:         XS-Parse-Sublike-0.16-Fix-type-mismatch-in-croak-format-string-width-argum.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(base)
BuildRequires:  perl(B)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(feature)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_XS_Parse_Sublike_enables_optional_tests}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# This module maintains multiple ABIs whose compatibility is checked at
# run-time by S_boot_xs_parse_sublike() compiled into the users of this module.
# This ABI range is defined with XS::Parse::Sublike/ABIVERSION_MIN and
# XS::Parse::Sublike/ABIVERSION_MAX in lib/XS/Parse/Sublike.xs.
Provides:       perl(:XS_Parse_Sublike_ABI) = 4

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(testcase\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(testcase\\)

%description
This module provides some XS functions to assist in writing parsers for
sub-like syntax, primarily for authors of keyword plugins using the
PL_keyword_plugin hook mechanism.

%package Builder
Summary:        Build-time support for XS::Parse::Sublike
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-interpreter
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# Subpackaged in 0.13
Conflicts:      %{name}%{?_isa} < 0.13

%description Builder
This module provides a build-time helper to assist authors writing XS modules
that use XS::Parse::Sublike. It prepares a Module::Build-using distribution to
be able to make use of XS::Parse::Sublike.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88
Requires:       perl(XSLoader)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n XS-Parse-Sublike-%{version}
%patch0 -p1
%if !%{with perl_XS_Parse_Sublike_enables_optional_tests}
rm t/99pod.t
perl -i -ne 'print $_ unless m{^t/99pod\.t}' MANIFEST
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
%if %{with perl_XS_Parse_Sublike_enables_optional_tests}
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
%{perl_vendorarch}/auto/*
%dir %{perl_vendorarch}/XS
%dir %{perl_vendorarch}/XS/Parse
%{perl_vendorarch}/XS/Parse/Sublike.pm
%{_mandir}/man3/XS::Parse::Sublike.*

%files Builder
%{perl_vendorarch}/XS/Parse/Sublike
%{_mandir}/man3/XS::Parse::Sublike::*
%{_rpmmacrodir}/macros.%{name}

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump

* Thu Dec 16 2021 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Fri Oct 29 2021 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Wed Sep 01 2021 Petr Pisar <ppisar@redhat.com> - 0.13-1
- 0.13 bump
- XS::Parse::Sublike::Builder moved to perl-XS-Parse-Sublike-Builder
  subpackage

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Petr Pisar <ppisar@redhat.com> - 0.12-1
- 0.12 bump
- Package the tests

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Petr Pisar <ppisar@redhat.com> - 0.11-1
- 0.11 bump

* Wed Jul 22 2020 Petr Pisar <ppisar@redhat.com> 0.10-1
- Specfile autogenerated by cpanspec 1.78.
