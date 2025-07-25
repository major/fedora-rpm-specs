# Enable debugging with Devel::MAT
%bcond_with perl_Future_AsyncAwait_enables_Devel_MAT
# Perform optional tests
%bcond_without perl_Future_AsyncAwait_enables_optional_test
# Declare a role with Role::Tiny
%bcond_without perl_Future_AsyncAwait_enables_role

# A build cycle: perl-Syntax-Keyword-Try → perl-Future-AsyncAwait
%if %{with perl_Future_AsyncAwait_enables_optional_test} && !%{defined perl_bootstrap}
%global optional_tests 1
%else
%global optional_tests 0
%endif

Name:           perl-Future-AsyncAwait
Version:        0.70
Release:        5%{?dist}
Summary:        Deferred subroutine syntax for futures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Future-AsyncAwait
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-AsyncAwait-%{version}.tar.gz
Source1:        macros.perl-Future-AsyncAwait
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.18
BuildRequires:  perl(Config)
%if %{with perl_Future_AsyncAwait_enables_Devel_MAT}
BuildRequires:  perl(Devel::MAT::Dumper::Helper) >= 0.44
%endif
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%define xs_parse_keyword_min_ver 0.13
BuildRequires:  perl(XS::Parse::Keyword::Builder) >= %{xs_parse_keyword_min_ver}
%define xs_parse_sublike_min_ver 0.31
BuildRequires:  perl(XS::Parse::Sublike::Builder) >= %{xs_parse_sublike_min_ver}
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
%define future_min_ver 0.50
BuildRequires:  perl(Future) >= %{future_min_ver}
BuildRequires:  perl(Test2::V0) >= 0.000148
# lib/Future/AsyncAwait.xs includes XSParseKeyword.h generated by
# XS::Parse::Keyword::Builder which loads XS::Parse::Keyword of version
# specified by boot_xs_parse_keyword() argument in AsyncAwait.xs
BuildRequires:  perl(XS::Parse::Keyword) >= %{xs_parse_keyword_min_ver}
# lib/Future/AsyncAwait.xs includes XSParseSublike.h generated by
# XS::Parse::Sublike::Builder which loads XS::Parse::Sublike of version
# specified by boot_xs_parse_sublike() argument in AsyncAwait.xs
BuildRequires:  perl(XS::Parse::Sublike) >= %{xs_parse_sublike_min_ver}
BuildRequires:  perl(XSLoader)
%if %{with perl_Future_AsyncAwait_enables_role}
# Optional run-time:
BuildRequires:  perl(Role::Tiny)
%endif
# Test:
BuildRequires:  perl(attributes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(List::Util)
%if %{with perl_Future_AsyncAwait_enables_role}
BuildRequires:  perl(Role::Tiny::With)
%endif
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Future::Deferred)
%if %{optional_tests}
# Optional tests:
%if %{with perl_Future_AsyncAwait_enables_Devel_MAT}
BuildRequires:  perl(Devel::MAT)
BuildRequires:  perl(Devel::MAT::Dumper)
%endif
# Some tests are skipped with Future::XS < 0.08
BuildRequires:  perl(IO::Async::Loop)
%define object_pad_min_ver 0.800
BuildRequires:  perl(Object::Pad) >= %{object_pad_min_ver}
%define sublike_extended_min_ver 0.29
BuildRequires:  perl(Sublike::Extended) >= %{sublike_extended_min_ver}
BuildRequires:  perl(Syntax::Keyword::Defer) >= 0.02
%define syntax_keyword_dynamically_min_ver 0.02
BuildRequires:  perl(Syntax::Keyword::Dynamically) >= %{syntax_keyword_dynamically_min_ver}
BuildRequires:  perl(Syntax::Keyword::Match)
BuildRequires:  perl(Syntax::Keyword::MultiSub) >= 0.01
BuildRequires:  perl(Syntax::Keyword::Try) >= 0.22
BuildRequires:  perl(Test::MemoryGrowth)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test2::Require::Module)
%endif
Requires:       perl(Future) >= %{future_min_ver}
%if %{with perl_Future_AsyncAwait_enables_role}
Recommends:     perl(Role::Tiny)
%endif
# lib/Future/AsyncAwait.xs includes XSParseKeyword.h generated by
# XS::Parse::Keyword::Builder which loads XS::Parse::Keyword of version
# specified by boot_xs_parse_keyword() argument in AsyncAwait.xs
Requires:       perl(XS::Parse::Keyword) >= %{xs_parse_keyword_min_ver}
%if %{defined perl_XS_Parse_Keyword_ABI}
# XS::Parse::Keyword maintains multiple ABIs whose compatibility is checked at
# run-time by S_boot_xs_parse_keyword() compiled into this package.
# The ABI is defined in XSPARSEKEYWORD_ABI_VERSION of XSParseKeyword.h
Requires:       %{perl_XS_Parse_Keyword_ABI}
%endif
# lib/Future/AsyncAwait.xs includes XSParseSublike.h generated by
# XS::Parse::Sublike::Builder which loads XS::Parse::Sublike of version
# specified by boot_xs_parse_sublike() argument in AsyncAwait.xs
Requires:       perl(XS::Parse::Sublike) >= %{xs_parse_sublike_min_ver}
%if %{defined perl_XS_Parse_Sublike_ABI}
# XS::Parse::Sublike maintains multiple ABIs whose compatibility is checked at
# run-time by S_boot_xs_parse_sublike() compiled into this package.
# The ABI is defined in XSPARSESUBLIKE_ABI_VERSION of XSParseSublike.h
Requires:       %{perl_XS_Parse_Sublike_ABI}
%endif
# This module maintains an ABI compiled into the users of this module and
# checked at run-time in boot_future_asyncawait().
# The ABI range is defined with Future::AsyncAwait/ABIVERSION_MIN and
# Future::AsyncAwait/ABIVERSION_MAX in Future/AsyncAwait.xs.
Provides:       perl(:Future_AsyncAwait_ABI) = 1
Provides:       perl(:Future_AsyncAwait_ABI) = 2

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Future|Object::Pad|Sublike::Extended|Syntax::Keyword::Dynamically|Syntax::Keyword::Try)\\)$

%description
This Perl module provides syntax for deferring and resuming subroutines while
waiting for Futures to complete. This syntax aims to make code that performs
asynchronous operations using futures look neater and more expressive than
simply using then chaining and other techniques on the futures themselves.

%package ExtensionBuilder
Summary:        Build script for Future::AsyncAwait extensions
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# An RPM macro executes perl
Requires:       perl-interpreter
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(File::Spec)
Requires:       perl(Future::AsyncAwait)
# For the macro file
Requires:       rpm

%description ExtensionBuilder
These Perl modules support building XS extensions for Future::AsyncAwait
module.

%package Test
Summary:        Conformance tests for Future::AsyncAwait::Awaitable role
BuildArch:      noarch
# Detected Test2::V0 without a version is correct.

%description Test
This Perl module provides a single test function, which runs a suite of
subtests to check that a given class provides a usable implementation of the
Future::AsyncAwait::Awaitable role. It runs tests that simulate various ways
in which Future::AsyncAwait will try to use an instance of this class, to
check that the implementation is valid.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Test = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(experimental)
Requires:       perl(Future) >= %{future_min_ver}
%if %{with perl_Future_AsyncAwait_enables_role}
Requires:       perl(Role::Tiny)
Requires:       perl(Role::Tiny::With)
%endif
%if %{optional_tests}
%if %{with perl_Future_AsyncAwait_enables_Devel_MAT}
Requires:       perl(Devel::MAT)
Requires:       perl(Devel::MAT::Dumper)
%endif
Requires:       perl(IO::Async::Loop)
Requires:       perl(Object::Pad) >= %{object_pad_min_ver}
Requires:       perl(Sublike::Extended) >= %{sublike_extended_min_ver}
Requires:       perl(Syntax::Keyword::Defer) >= 0.02
Requires:       perl(Syntax::Keyword::Dynamically) >= %{syntax_keyword_dynamically_min_ver}
Requires:       perl(Syntax::Keyword::Match)
Requires:       perl(Syntax::Keyword::MultiSub) >= 0.01
Requires:       perl(Syntax::Keyword::Try) >= 0.22
Requires:       perl(Test::Pod) >= 1.00
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Future-AsyncAwait-%{version}
for F in \
%if !%{optional_tests} || !%{with perl_Future_AsyncAwait_enables_Devel_MAT}
    t/82devel-mat-dumper-helper.t \
%endif
%if !%{optional_tests}
    t/80await+defer.t t/80await+dynamically.t t/80await+matchcase.t \
    t/80await+SKT.t t/80async-method.t t/80extended+async.t \
    t/81async-method+dynamically.t t/81memory-growth.t t/99pod.t \
%endif
%if !%{with perl_Future_AsyncAwait_enables_role}
    t/51awaitable-role.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
chmod +x t/*.t

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
install -D -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE1}
# Move Test subpackage content to a noarch location
install -m 0755 -d %{buildroot}%{perl_vendorlib}
mv %{buildroot}%{perl_vendorarch}/Test %{buildroot}%{perl_vendorlib}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{optional_tests}
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
%dir %{perl_vendorarch}/auto/Future
%{perl_vendorarch}/auto/Future/AsyncAwait
%dir %{perl_vendorarch}/Future
%{perl_vendorarch}/Future/AsyncAwait.pm
%dir %{perl_vendorarch}/Future/AsyncAwait
%{perl_vendorarch}/Future/AsyncAwait/Awaitable.pm
%{_mandir}/man3/Future::AsyncAwait.*
%{_mandir}/man3/Future::AsyncAwait::Awaitable.*

%files ExtensionBuilder
%{perl_vendorarch}/Future/AsyncAwait/ExtensionBuilder.pm
%dir %{perl_vendorarch}/auto/share
%dir %{perl_vendorarch}/auto/share/module
%{perl_vendorarch}/auto/share/module/Future-AsyncAwait
%{_mandir}/man3/Future::AsyncAwait::ExtensionBuilder.*
%{_rpmmacrodir}/macros.%{name}

%files Test
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Test
%dir %{perl_vendorlib}/Test/Future
%{perl_vendorlib}/Test/Future/AsyncAwait
%{_mandir}/man3/Test::Future::AsyncAwait::Awaitable.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 08 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-4
- Perl 5.42 re-rebuild of bootstrapped packages

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-3
- Perl 5.42 rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Petr Pisar <ppisar@redhat.com> - 0.70-1
- 0.70 bump

* Thu Sep 19 2024 Petr Pisar <ppisar@redhat.com> - 0.69-1
- 0.69 bump

* Mon Sep 02 2024 Petr Pisar <ppisar@redhat.com> - 0.68-1
- 0.68 bump

* Wed Aug 21 2024 Petr Pisar <ppisar@redhat.com> - 0.67-1
- 0.67 bump

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-7
- Perl 5.40 re-rebuild of bootstrapped packages

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-6
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 11 2023 Petr Pisar <ppisar@redhat.com> - 0.66-3
- Finish bootstrapping for perl-XS-Parse-Sublike ABI change

* Mon Sep 11 2023 Petr Pisar <ppisar@redhat.com> - 0.66-2
- Bootstrap for perl-XS-Parse-Sublike ABI change

* Mon Sep 11 2023 Petr Pisar <ppisar@redhat.com> - 0.66-1
- 0.66 bump

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-3
- Perl 5.38 re-rebuild of bootstrapped packages

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.65-2
- Perl 5.38 rebuild

* Mon Mar 20 2023 Petr Pisar <ppisar@redhat.com> - 0.65-1
- 0.65 bump

* Wed Feb 15 2023 Petr Pisar <ppisar@redhat.com> - 0.64-1
- 0.64 bump

* Mon Feb 13 2023 Petr Pisar <ppisar@redhat.com> - 0.63-1
- 0.63 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Petr Pisar <ppisar@redhat.com> - 0.62-1
- 0.62 bump

* Tue Nov 22 2022 Petr Pisar <ppisar@redhat.com> - 0.61-2
- perl-Future-AsyncAwait-ExtensionBuilder requires perl-interpreter

* Tue Nov 22 2022 Petr Pisar <ppisar@redhat.com> - 0.61-1
- 0.61 bump

* Mon Sep 26 2022 Petr Pisar <ppisar@redhat.com> - 0.59-1
- 0.59 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-3
- Perl 5.36 re-rebuild of bootstrapped packages

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-2
- Perl 5.36 rebuild

* Fri Apr 29 2022 Petr Pisar <ppisar@redhat.com> - 0.58-1
- 0.58 bump

* Tue Mar 22 2022 Adam Williamson <awilliam@redhat.com> - 0.57-2
- Rebuild with no changes to fix update mess on F36

* Thu Mar 17 2022 Petr Pisar <ppisar@redhat.com> - 0.57-1
- 0.57 bump

* Wed Jan 26 2022 Petr Pisar <ppisar@redhat.com> - 0.56-1
- 0.56 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Petr Pisar <ppisar@redhat.com> - 0.55-2
- Enable optional Syntax::Keyword::MultiSub tests (bug #2033300)

* Thu Dec 16 2021 Petr Pisar <ppisar@redhat.com> - 0.55-1
- 0.55 bump

* Wed Oct 27 2021 Petr Pisar <ppisar@redhat.com> - 0.54-1
- 0.54 bump

* Fri Aug 27 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-2
- Finish bootstrap against perl-XS-Parse-Keyword-0.13

* Thu Aug 26 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-1
- 0.53 bump; Bootstrap against perl-XS-Parse-Keyword-0.13

* Tue Aug 17 2021 Petr Pisar <ppisar@redhat.com> - 0.52-4
- Finish bootstrap against perl-XS-Parse-Keyword-0.12 (bug #1994077)

* Tue Aug 17 2021 Petr Pisar <ppisar@redhat.com> - 0.52-3
- Bootstrap against perl-XS-Parse-Keyword-0.12 (bug #1994077)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Petr Pisar <ppisar@redhat.com> - 0.52-1
- 0.52 bump

* Tue Jul 13 2021 Petr Pisar <ppisar@redhat.com> - 0.51-4
- Adapt a test to changes in XS-Parse-Keyword-Builder-0.09 (bug #1981565)

* Wed Jun 02 2021 Petr Pisar <ppisar@redhat.com> - 0.51-3
- Rebuild against perl-XS-Parse-Keyword-0.06 (bug #1966787)

* Tue Jun 01 2021 Petr Pisar <ppisar@redhat.com> - 0.51-2
- Build-require Syntax::Keyword::Defer for optional tests

* Tue Jun 01 2021 Petr Pisar <ppisar@redhat.com> - 0.51-1
- 0.51 bump

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-3
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-2
- Perl 5.34 rebuild

* Fri Apr 30 2021 Petr Pisar <ppisar@redhat.com> - 0.50-1
- 0.50 bump

* Thu Apr 29 2021 Petr Pisar <ppisar@redhat.com> - 0.49-3
- Build-require perl(experimental) for the tests (bug #1955172)

* Fri Mar 26 2021 Petr Pisar <ppisar@redhat.com> - 0.49-2
- Add a missing dependency on XS::Parse::Sublike

* Thu Feb 25 2021 Petr Pisar <ppisar@redhat.com> - 0.49-1
- 0.49 bump
- Package tests

* Wed Feb 03 2021 Petr Pisar <ppisar@redhat.com> - 0.48-1
- 0.48 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.47-1
- 0.47 bump

* Mon Nov 09 2020 Petr Pisar <ppisar@redhat.com> - 0.46-1
- 0.46 bump

* Fri Oct 23 2020 Petr Pisar <ppisar@redhat.com> - 0.45-1
- 0.45 bump

* Mon Oct 12 2020 Petr Pisar <ppisar@redhat.com> - 0.44-1
- 0.44 bump

* Wed Jul 15 2020 Petr Pisar <ppisar@redhat.com> 0.43-1
- Specfile autogenerated by cpanspec 1.78.
