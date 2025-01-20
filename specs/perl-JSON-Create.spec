# Permform optional tests
%bcond_without perl_JSON_Create_enables_optional_tests

Name:           perl-JSON-Create
Version:        0.35
Release:        14%{?dist}
Summary:        Create JSON
# lib/JSON/Create.pod:  GPL+ or Artistic
# ppport.h:             GPL+ or Artistic
# qsort-r.c:            BSD
# unicode.c:            (BSD or GPLv2+ or Artistic) at upstream, but the author
#                       is the same, so he can pick any license, and here it's
#                       a part of JSON-Create
# Automatically converted from old format: (GPL+ or Artistic) and BSD - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/JSON-Create
Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/JSON-Create-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON::Parse) >= 0.60
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Unicode::UTF8) >= 0.62
BuildRequires:  perl(utf8)
BuildRequires:  perl(XSLoader)
# Tests:
# perl-Test-Harness for /usr/bin/prove executed by t/zz-pure-perl.t
BuildRequires:  perl-Test-Harness
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
%if %{with perl_JSON_Create_enables_optional_tests}
# Optional tests:
BuildRequires:  perl(boolean)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::Tiny)
BuildRequires:  perl(Types::Serialiser)
%endif
Requires:       perl(JSON::Parse) >= 0.60
Requires:       perl(Unicode::UTF8) >= 0.62

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Unicode::UTF8\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(JCT\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(JCT\\)

%description
JSON::Create encodes Perl variables into JSON. The basic routine "create_json"
gives common defaults. The stricter version "create_json_strict" accepts only
unambiguous inputs. For more customization, an object created with "new" and
run with "create" allows specifying behavior in more detail.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_JSON_Create_enables_optional_tests}
Requires:       perl(boolean)
Requires:       perl(JSON::PP)
Requires:       perl(JSON::Tiny)
Requires:       perl(Types::Serialiser)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p 1 -n JSON-Create-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 &&
!s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
cd  %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset JSONCreatePP
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/JSON*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.35-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-11
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-7
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Petr Pisar <ppisar@redhat.com> - 0.35-1
- 0.35 bump

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-2
- Perl 5.34 rebuild

* Wed May 05 2021 Petr Pisar <ppisar@redhat.com> - 0.34-1
- 0.34 bump

* Tue Apr 27 2021 Petr Pisar <ppisar@redhat.com> 0.32-1
- Specfile autogenerated by cpanspec 1.78.
