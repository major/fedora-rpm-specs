# Enable optional evalutors like Math::Symbolic or Math::Expression::Evaluator
%bcond_without perl_Math_NumSeq_enables_maximum_interoperation
# Perform optional tests
%bcond_without perl_Math_NumSeq_enables_optional_test

Name:           perl-Math-NumSeq
Version:        75
Release:        10%{?dist}
Summary:        Number sequences
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/Math-NumSeq
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-NumSeq-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
# tools/make-oeis-catalogue.pl is executed
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant) >= 1.02
BuildRequires:  perl(constant::defer) >= 1
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Factor::XS) >= 0.40
BuildRequires:  perl(Math::Libm)
BuildRequires:  perl(Math::Prime::XS) >= 0.23
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Safe) >= 2.30
BuildRequires:  perl(SDBM_File)
BuildRequires:  perl(Symbol)
# Tie::Hash::NamedCapture not needed if Safe >= 2.30 is available
# Optional run-time:
BuildRequires:  perl(Encode)
%if %{with perl_Math_NumSeq_enables_maximum_interoperation}
# Language::Expr 0.24 not yet packaged
# Language::Expr::Compiler::perl 0.24 not yet packaged
BuildRequires:  perl(Math::Expression::Evaluator)
BuildRequires:  perl(Math::Symbolic)
%endif
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
%if %{with perl_Math_NumSeq_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Data::Float)
# Devel::FindRef not available because it does not work since Perl 5.22.
BuildRequires:  perl(Devel::StackTrace)
%endif
Recommends:     perl(Encode)
Requires:       perl(File::HomeDir)
Requires:       perl(File::Temp)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::Trig)
Requires:       perl(Module::Load)
Requires:       perl(Safe) >= 2.30
Requires:       perl(SDBM_File)
%if %{with perl_Math_NumSeq_enables_maximum_interoperation}
# Language::Expr 0.24 not yet packaged
# Language::Expr::Compiler::perl 0.24 not yet packaged
Suggests:       perl(Math::Expression::Evaluator)
Suggests:       perl(Math::Symbolic)
%endif

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Math::Factor::XS\\) >= 0.39
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(MyTestHelpers\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(MyTestHelpers\\)

%description
This package contains a base class for number sequences and a collection of
its instances which implements various sequences like prime numbers or
multiples of a constant. Sequence objects can iterate through values and some
sequences have random access or a predicate test.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# Data::Dumper not used
Requires:       perl(File::Spec)
Requires:       perl(Math::Libm)
Requires:       perl(Scalar::Util)
%if %{with perl_Math_NumSeq_enables_optional_test}
# Optional tests:
Requires:       perl(Data::Float)
# Devel::FindRef not available because it does not work since Perl 5.22.
Requires:       perl(Devel::StackTrace)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Math-NumSeq-%{version}
chmod +x t/*.t

%build
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
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license COPYING
%doc Changes examples
%{perl_vendorlib}/Math
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 75-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 75-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 75-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 75-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 75-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 75-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 06 2022 Petr Pisar <ppisar@redhat.com> - 75-2
- Perl 5.36 rebuild

* Mon Jun 06 2022 Petr Pisar <ppisar@redhat.com> - 75-1
- 75 version bump
- Package the tests

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 74-11
- Perl 5.36 rebuild

* Thu May 19 2022 Petr Pisar <ppisar@redhat.com> - 74-10
- Fix handling infinity and adapt to changes in perl-Math-BigInt-1.9998.31
  (bug #2088300)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 74-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 74-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 74-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 74-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Petr Pisar <ppisar@redhat.com> - 74-5
- Modernize a spec file

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 74-3
- Perl 5.32 rebuild

* Thu Mar 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 74-2
- Add perl(Safe) for tests

* Sun Feb 23 2020 Miro Hrončok <mhroncok@redhat.com> - 74-1
- Update to 74 (#1806236)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Miro Hrončok <mhroncok@redhat.com> - 73-1
- Update to 73 (#1737396)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 72-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 72-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 72-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 72-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 72-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 72-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 72-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 26 2016 Miro Hrončok <mhroncok@redhat.com> - 72-1
- New version 72 (#1359443)

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 71-8
- Disable build-time dependency on Devel::FindRef unconditionally

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 71-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 71-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 71-4
- Perl 5.22 rebuild

* Tue Jun 02 2015 Jitka Plesnikova <jplesnik@redhat.com> - 71-3
- Disable optional BR Devel::FindRef for Perl 5.22

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 71-2
- Perl 5.20 rebuild

* Sun Jun 29 2014 Miro Hrončok <mhroncok@redhat.com> - 71-1
- New version 71 (#1114326)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Miro Hrončok <mhroncok@redhat.com> - 70-1
- New version 70 (#1087328)

* Mon Feb 24 2014 Miro Hrončok <mhroncok@redhat.com> - 69-1
- New version 69 (#1066371)

* Thu Jan 30 2014 Miro Hrončok <mhroncok@redhat.com> - 68-1
- New version 68 (#1059636)

* Tue Nov 26 2013 Miro Hrončok <mhroncok@redhat.com> - 67-1
- New version 67 (#1030911)

* Wed Oct 23 2013 Miro Hrončok <mhroncok@redhat.com> - 66-1
- New version 66 (#1022678)

* Sat Oct 12 2013 Miro Hrončok <mhroncok@redhat.com> - 65-1
- New version 65 (#1016246)

* Tue Sep 17 2013 Miro Hrončok <mhroncok@redhat.com> - 64-1
- New version 64 (#1008403)

* Mon Sep 02 2013 Miro Hrončok <mhroncok@redhat.com> - 63-1
- New version 63
- %%{__perl} to perl

* Fri Aug 16 2013 Miro Hrončok <mhroncok@redhat.com> - 62-1
- New version 62
- Language::Expr dependency conditional 

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 55-1
- New release
- Removed shared libs filter, noarch
- Removed deleting empty directories
- PERL_INSTALL_ROOT changed to DESTDIR
- Added some of previously removed BRs
- Sort (B)Rs lexicographically 

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 52-2
- Removed BRs provided by perl package

* Tue Oct 09 2012 Miro Hrončok <miro@hroncok.cz> 52-1
- New release

* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 51-1
- Specfile autogenerated by cpanspec 1.78 and revised.
