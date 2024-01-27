Name:           perl-Boost-Geometry-Utils
Version:        0.15
Release:        39%{?dist}
Summary:        Bindings for the Boost Geometry library
# README:               GPL+ or Artistic
# src/medial_axis.hpp:  Boost
# src/ppport.h:         GPL+ or Artistic
## Unbundled
# src/boost/type.hpp:   Boost
License:        (GPL+ or Artistic) and Boost
URL:            https://metacpan.org/release/Boost-Geometry-Utils
Source0:        https://cpan.metacpan.org/authors/id/A/AA/AAR/Boost-Geometry-Utils-%{version}.tar.gz
# Fix for RT#96145
Patch0:         Boost-Geometry-Utils-0.15-multi_linestring2perl-only-extend-the-array-if-needed.patch
# Fix building with Boost 1.73.0, CPAN RT#133057
Patch1:         Boost-Geometry-Utils-0.15-Port-Boost-1.73.0.patch
BuildRequires:  boost-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Typemaps::Default) >= 0.05
BuildRequires:  perl(Module::Build::WithXSpp) >= 0.10
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
# List::Util not used
BuildRequires:  perl(Test::More)
# Optional tests:
# Pod::Coverage::TrustPod not used
# Test::Pod not used
# Test::Pod::Coverage not used
# Test::Script not helpful because of no script files

%description
This Perl module provides bindings to perform some geometric operations using
the Boost Geometry library. It does not aim at providing full bindings.

%prep
%setup -q -n Boost-Geometry-Utils-%{version}
%patch0 -p1
%patch1 -p1
# Unbundle Boost
rm -r src/boost
perl -i -ne 'print $_ unless m{^src/boost/}' MANIFEST

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
unset RELEASE_TESTING
./Build test

%files
%license LICENSE
%doc CHANGES README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Boost*
%{_mandir}/man3/*

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-36
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-33
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-30
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Petr Pisar <ppisar@redhat.com> - 0.15-27
- Modernize a spec file
- License corrected to "(GPL+ or Artistic) and Boost"
- Build against a system Boost library

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-26
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-23
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-20
- Perl 5.28 rebuild

* Thu Mar 01 2018 Petr Pisar <ppisar@redhat.com> - 0.15-19
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-15
- Perl 5.26 rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-9
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.15-8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-5
- Fix for Perl 5.20 (RT#96145)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.15-2
- Perl 5.18 rebuild

* Mon Jun 24 2013 Miro Hrončok <mhroncok@redhat.com> - 0.15-1
- New upstream release

* Wed Apr 03 2013 Miro Hrončok <mhroncok@redhat.com> - 0.06-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Miro Hrončok <mhroncok@redhat.com> - 0.05-6
- Added back:  perl(ExtUtils::Typemaps::Default)

* Thu Jan 17 2013 Miro Hrončok <mhroncok@redhat.com> - 0.05-5
- Dropped perl macro in MODULE_COMPAT
- Removed src and xsp from %%doc
- Dropped converting src to UTF-8
- Dropped converting newlines and dos2unix BR
- Dropped BRs: perl(ExtUtils::Typemaps::Default)
               perl(ExtUtils::XSpp)
               perl(Module::Build)
- Added BRs:   perl(File::Temp)
               perl(Exporter)
               perl(XSLoader)

* Thu Jan 17 2013 Miro Hrončok <mhroncok@redhat.com> - 0.05-4
- Using dos2unix instead of sed
- Removed deleting empty dirs
- Dropped perl macro

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 0.05-3
- Removed BRs provided by perl package

* Sun Oct 07 2012 Miro Hrončok <miro@hroncok.cz> 0.05-2
- Rebuilding for 32bit, no spec changes.

* Tue Sep 25 2012 Miro Hrončok <miro@hroncok.cz> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
