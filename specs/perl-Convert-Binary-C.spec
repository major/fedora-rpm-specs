Name:           perl-Convert-Binary-C
Version:        0.85
Release:        3%{?dist}
Summary:        Binary data conversion using C types
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Binary-C
Source0:        https://cpan.metacpan.org/modules/by-module/Convert/Convert-Binary-C-%{version}.tar.gz
Patch1:         Convert-Binary-C-0.85-c23.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.10
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Pod) >= 0.95
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Thread)
BuildRequires:  perl(threads)

%description
Convert::Binary::C is a preprocessor and parser for C type definitions. It
is highly configurable and supports arbitrarily complex data structures.
Its object-oriented interface has pack and unpack methods that act as
replacements for Perl's pack and unpack and allow to use C types instead of
a string representation of the data structure for conversion of binary data
from and to Perl's complex data structures.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Data::Dumper)
Requires:       perl(Scalar::Util)
Requires:       perl(threads)
Requires:       perl(Time::HiRes)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Convert-Binary-C-%{version}
%patch -P1 -p0

# Help generators to recognize Perl scripts
for F in tests/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/%{name}
cp -a examples tests $RPM_BUILD_ROOT/%{_libexecdir}/%{name}
rm $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/tests/80*pod*
cat > $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/test


%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README.md TODO
%{_bindir}/ccconfig*
%{perl_vendorarch}/auto/Convert*
%dir %{perl_vendorarch}/Convert
%{perl_vendorarch}/Convert/Binary*
%{_mandir}/man1/ccconfig*
%{_mandir}/man3/Convert::Binary::C*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 24 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.85-3
- Fix C23 issues in old hash code (rhbz#2341022)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 02 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.85-1
- 0.85 bump (rhbz#2315937)
- Package tests

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-13
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-9
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-1
- 0.84 bump

* Fri Nov 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.83-1
- 0.83 bump

* Thu Nov 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.81-1
- 0.81 bump

* Wed Nov 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-1
- 0.80 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.79-2
- Perl 5.32 rebuild

* Tue May 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.79-1
- 0.79 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.78-8
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-2
- Perl 5.24 rebuild

* Thu Mar 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-1
- 0.78 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.77-1
- 0.77 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-11
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-10
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.76-6
- Perl 5.18 rebuild
- Fix POD syntax (CPAN RT#85264)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.76-3
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Iain Arnell <iarnell@gmail.com> 0.76-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.74-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.74-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.74-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.74-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.74-1
- Update to latest upstream (0.74)
- Drop GCC 4.4 patch (fixed upstream)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.71-2
- Add patch to fix #elif directives for new GCC 4.4

* Wed Jun  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.71-1
- Update to latest upstream (0.71)

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.70-5
- rebuild for new perl (again)

* Sat Feb 23 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.70-4
- Bump release to fix koji problem that prevented tagging the previous
  (correct) build.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.70-3
- Autorebuild for GCC 4.3

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.70-2
- rebuild for new perl

* Sun Jan  6 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.70-1
- Update to latest upstream (0.70)

* Thu Aug 23 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.68-2
- License tag to GPL+ or Artistic as per new guidelines.

* Sat Aug 18 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.68-1
- Update to latest upstream

* Mon Apr 02 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-4
- Remove '%%{?_smp_mflags}', package does not support parallel make.

* Thu Mar 29 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-3
- Add BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)

* Tue Mar 27 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-2
- Add perl(ExtUtils::MakeMaker) BR.

* Fri Mar 23 2007 Alex Lancaster <alexlan[AT]fedoraproject org> 0.67-1
- Specfile autogenerated by cpanspec 1.69.1.
