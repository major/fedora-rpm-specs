# Enable C++ support
%bcond_without perl_FFI_Platypus_enables_cpp
# Enable Fortran support
%bcond_without perl_FFI_Platypus_enables_fortran
# Perform optional tests
%bcond_without perl_FFI_Platypus_enables_optional_test

Name:           perl-FFI-Platypus
Version:        2.10
Release:        2%{?dist}
Summary:        Write Perl bindings to non-Perl libraries with FFI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://pl.atypus.org/
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/FFI-Platypus-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.4
BuildRequires:  perl(Alien::Base::Wrapper)
# Alien::FFI || Alien::FFI::pkgconfig
BuildRequires:  perl(Alien::FFI) >= 0.20
# Alien::FFI::PkgConfigPP not used on Linux
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.12
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(lib)
# Math::Int64 0.34 used only on perls without long integers
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
%if %{with perl_FFI_Platypus_enables_cpp}
BuildRequires:  gcc-c++
%endif
# gcc-gfortran not used at tests
BuildRequires:  perl(autodie)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(constant) >= 1.32
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FFI::CheckLib) >= 0.05
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util) >= 1.45
# Math::Complex not used because the distribution does not enables
# long doubles in perl
# Math::LongDouble not used because the distribution does not enables
# long doubles in perl
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(if)
BuildRequires:  perl(open)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(utf8)
%if %{with perl_FFI_Platypus_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Acme::Alien::DontPanic) >= 1.03
BuildRequires:  perl(Devel::Hide) >= 0.0010
# forks is not packaged
# gcc used by FFI::Build::Platform
# Sub::Identify is not helpful
%endif
Requires:       gcc
%if %{with perl_FFI_Platypus_enables_cpp}
# gcc-c++ used by FFI::Build::Platform
Recommends:     gcc-c++
%endif
%if %{with perl_FFI_Platypus_enables_fortran}
# gcc-gfortran used by FFI::Build::Platform
Recommends:     gcc-gfortran
%endif
Requires:       perl(bytes)
Requires:       perl(FFI::CheckLib) >= 0.05
Requires:       perl(IPC::Cmd)

# Do not export a SONAME of a private plfill library used by
# FFI::Platypus::Memory as a fallback
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^libplfill.so\\(\\)
# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test2::API|Test2::V0)\\)$
# Filter private modules
%global __provides_exclude %{__provides_exclude}|^perl\\((FFI::Build::Plugin::Foo(1|2)|Test::Cleanup|Test::FauxAttach|Test::Platypus)\\)
%global __requires_exclude %{__requires_exclude}|^perl\\((Test::Cleanup|Test::FauxAttach|Test::Platypus)\\)
# Do not expport test libraries
%global __provides_exclude %{__provides_exclude}|^libtest\\.so\\(\\)
# Do not export private redefinitions
%global __provides_exclude %{__provides_exclude}|^perl\\(FFI::Platypus\\)$

%description
Platypus is a Perl library for creating interfaces to machine code libraries
written in languages like C, C++, Fortran, Rust, Pascal. Essentially anything
that gets compiled into machine code. This implementation uses libffi to
accomplish this task. libffi is battle tested by a number of other scripting
and virtual machine languages, such as Python and Ruby to serve a similar
role. There are a number of reasons why you might want to write an extension
with Platypus instead of XS.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Test2::API) >= 1.302015
Requires:       perl(Test2::V0) >= 0.000121
%if %{with perl_FFI_Platypus_enables_optional_test}
Requires:       perl(Acme::Alien::DontPanic) >= 1.03
Requires:       perl(Devel::Hide) >= 0.0010
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n FFI-Platypus-%{version}
# Remove bundled modules,
# forks is not packaged
for F in \
    inc/Alien/Base inc/Alien/FFI \
    t/forks.t \
%if !%{with perl_FFI_Platypus_enables_optional_test}
    t/type_longdouble__hide.t \
%endif
; do
    rm -r "$F"
    perl -i -n -e 'print unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
unset FFI_PLATYPUS_DEBUG_FAKE32 FFI_PLATYPUS_NO_ALLOCA \
    FFI_PLATYPUS_NO_EXTRA_TYPES FFI_PLATYPUS_PROBE_OVERRIDE V
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
# Build the examples for the tests packaged in %%install
%{make_build} ffi-test
chmod 0755 t/ffi/_build

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{blib/lib}{%{perl_vendorarch}}' \
    %{buildroot}%{_libexecdir}/%{name}/t/ffi_probe.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# FFF::Temp writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset FFI_PLATYPUS_DLERROR FFI_PLATYPUS_MEMORY_STRDUP_IMPL PERL5LIB V
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset FFI_PLATYPUS_DLERROR FFI_PLATYPUS_MEMORY_STRDUP_IMPL PERL5LIB V
# Parallel tests randomly fail because of a known race in FFI::Temp
# <https://github.com/PerlFFI/FFI-Platypus/issues/344>
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes* CONTRIBUTING examples README SUPPORT
%dir %{perl_vendorarch}/auto/FFI
%{perl_vendorarch}/auto/FFI/Platypus
%dir %{perl_vendorarch}/auto/share
%dir %{perl_vendorarch}/auto/share/dist
%{perl_vendorarch}/auto/share/dist/FFI-Platypus
%dir %{perl_vendorarch}/FFI
%{perl_vendorarch}/FFI/Build
%{perl_vendorarch}/FFI/Build.pm
%{perl_vendorarch}/FFI/Platypus
%{perl_vendorarch}/FFI/Platypus.pm
%{perl_vendorarch}/FFI/Probe
%{perl_vendorarch}/FFI/Probe.pm
%{perl_vendorarch}/FFI/Temp.pm
%{perl_vendorarch}/FFI/typemap
%{_mandir}/man3/FFI::Build.*
%{_mandir}/man3/FFI::Build::*
%{_mandir}/man3/FFI::Platypus.*
%{_mandir}/man3/FFI::Platypus::*
%{_mandir}/man3/FFI::Probe.*
%{_mandir}/man3/FFI::Probe::*
%{_mandir}/man3/FFI::Temp.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 19 2024 Petr Pisar <ppisar@redhat.com> - 2.10-1
- 2.10 bump

* Tue Aug 20 2024 Petr Pisar <ppisar@redhat.com> - 2.09-1
- 2.09 bump

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-6
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-2
- Perl 5.38 rebuild

* Mon May 15 2023 Petr Pisar <ppisar@redhat.com> - 2.08-1
- 2.08 bump

* Wed Mar 15 2023 Petr Pisar <ppisar@redhat.com> - 2.07-1
- 2.07 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Petr Pisar <ppisar@redhat.com> - 2.05-2
- Do not provide a test library libtest.so()

* Wed Nov 16 2022 Petr Pisar <ppisar@redhat.com> - 2.05-1
- 2.05 bump

* Mon Nov 07 2022 Petr Pisar <ppisar@redhat.com> - 2.04-1
- 2.04 bump

* Mon Oct 31 2022 Petr Pisar <ppisar@redhat.com> - 2.03-1
- 2.03 bump

* Tue Oct 25 2022 Petr Pisar <ppisar@redhat.com> - 2.02-1
- 2.02 bump

* Wed Aug 31 2022 Petr Pisar <ppisar@redhat.com> - 2.01-1
- 2.01 bump

* Thu Aug 18 2022 Petr Pisar <ppisar@redhat.com> - 2.00-1
- 2.00 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Petr Pisar <ppisar@redhat.com> - 1.58-1
- 1.58 bump

* Thu Jun 16 2022 Petr Pisar <ppisar@redhat.com> - 1.57-1
- 1.57 bump

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Fri Oct 29 2021 Petr Pisar <ppisar@redhat.com> - 1.56-1
- 1.56 bump

* Fri Jul 30 2021 Petr Pisar <ppisar@redhat.com> - 1.55-1
- 1.55 bump

* Fri Jul 30 2021 Petr Pisar <ppisar@redhat.com> - 1.54_01-1
- 1.54_01 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Petr Pisar <ppisar@redhat.com> - 1.53-1
- 1.53 bump

* Thu Jul 01 2021 Petr Pisar <ppisar@redhat.com> - 1.52-1
- 1.52 bump

* Thu Jul 01 2021 Petr Pisar <ppisar@redhat.com> - 1.50-1
- 1.50 bump

* Tue Jun 22 2021 Petr Pisar <ppisar@redhat.com> - 1.46-1
- 1.46 bump

* Mon Jun 21 2021 Petr Pisar <ppisar@redhat.com> - 1.44-1
- 1.44 bump

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-2
- Perl 5.34 rebuild

* Thu Mar 18 2021 Petr Pisar <ppisar@redhat.com> - 1.43-1
- 1.43 bump

* Tue Mar 16 2021 Petr Pisar <ppisar@redhat.com> - 1.42-1
- 1.42 bump

* Tue Mar 09 2021 Petr Pisar <ppisar@redhat.com> - 1.38-1
- 1.38 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Petr Pisar <ppisar@redhat.com> - 1.34-1
- 1.34 bump

* Tue Sep 29 2020 Petr Pisar <ppisar@redhat.com> - 1.33-1
- 1.33 bump

* Mon Sep 21 2020 Petr Pisar <ppisar@redhat.com> - 1.32-1
- 1.32 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Petr Pisar <ppisar@redhat.com> - 1.31-1
- 1.31 bump

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-2
- Perl 5.32 rebuild

* Wed Jun 17 2020 Petr Pisar <ppisar@redhat.com> - 1.30-1
- 1.30 bump

* Mon Jun 08 2020 Petr Pisar <ppisar@redhat.com> - 1.29-1
- 1.29 bump

* Wed May 20 2020 Petr Pisar <ppisar@redhat.com> - 1.28-1
- 1.28 bump

* Thu May 07 2020 Petr Pisar <ppisar@redhat.com> - 1.26-1
- 1.26 bump

* Wed May 06 2020 Petr Pisar <ppisar@redhat.com> - 1.25-1
- 1.25 bump

* Mon May 04 2020 Petr Pisar <ppisar@redhat.com> - 1.24-1
- 1.24 bump

* Thu Apr 16 2020 Petr Pisar <ppisar@redhat.com> - 1.11-1
- 1.11 bump

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Petr Pisar <ppisar@redhat.com> - 1.09-1
- 1.09 bump

* Thu Jan 02 2020 Petr Pisar <ppisar@redhat.com> - 1.07-1
- 1.07 bump

* Tue Dec 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-1
- 1.06 bump

* Tue Dec 10 2019 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Mon Nov 18 2019 Petr Pisar <ppisar@redhat.com> - 1.01-1
- 1.01 bump

* Tue Oct 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-1
- 0.98 bump

* Tue Aug 20 2019 Petr Pisar <ppisar@redhat.com> - 0.96-1
- 0.96 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Petr Pisar <ppisar@redhat.com> - 0.94-1
- 0.94 bump

* Thu Jul 18 2019 Petr Pisar <ppisar@redhat.com> - 0.92-1
- 0.92 bump

* Tue Jul 02 2019 Petr Pisar <ppisar@redhat.com> - 0.90-1
- 0.90 bump

* Wed Jun 19 2019 Petr Pisar <ppisar@redhat.com> - 0.88-1
- 0.88 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.87-2
- Perl 5.30 rebuild

* Tue Apr 23 2019 Petr Pisar <ppisar@redhat.com> - 0.87-1
- 0.87 bump

* Mon Mar 11 2019 Petr Pisar <ppisar@redhat.com> - 0.86-1
- Specfile autogenerated by cpanspec 1.78.
