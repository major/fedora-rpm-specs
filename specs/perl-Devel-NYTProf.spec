Name:           perl-Devel-NYTProf
Version:        6.14
Release:        6%{?dist}
Summary:        Powerful feature-rich perl source code profiler
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-NYTProf
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/Devel-NYTProf-%{version}.tar.gz
Patch1:         Devel-NYTProf-6.13-Unbundled-flamegraph.patch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  flamegraph
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# Unused BuildRequires:  perl(ActiveState::Browser)
# Unused BuildRequires:  perl(Apache)
BuildRequires:  perl(base)
# Unused BuildRequires:  perl(Browser::Open)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Which)
# Unused BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(AutoSplit)
# Unused BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# Optional tests only
BuildRequires:  perl(Sub::Name) >= 0.11
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# Unneded Requires:       perl(Apache)
# Optional features
Suggests:       perl(Browser::Open)
Suggests:       perl(JSON::MaybeXS)
Requires:       flamegraph

%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(NYTProfTest\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Devel::NYTProf::Test)\s*$

%description
Devel::NYTProf is a powerful feature-rich perl source code profiler.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Devel-NYTProf-%{version}
%patch -P1 -p1

# Remove bundled flamegraph.pl
rm -r bin/flamegraph.pl
perl -i -ne 'print $_ unless m{flamegraph.pl}' MANIFEST

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
# remove duplicate installed lib in wrong location
rm -rf %{buildroot}/%{perl_vendorarch}/Devel/auto/
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# XXX - remove the tests, because it fails only with subpackage
rm %{buildroot}%{_libexecdir}/%{name}/t/test62-subcaller1-b.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
for F in nytprofcalls nytprofcg nytprofcsv nytprofhtml nytprofmerge nytprofpf; do
    ln -s %{_bindir}/"$F" %{buildroot}%{_libexecdir}/%{name}/bin
done
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes HACKING demo README.md
%{perl_vendorarch}/auto/Devel*
%{perl_vendorarch}/Devel*
%{_bindir}/nytprof*
%{_mandir}/man1/nytprof*
%{_mandir}/man3/Devel::MemoryProfiling*
%{_mandir}/man3/Devel::NYTProf*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 6.14-4
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Jitka Plesnikova <jplesnik@redhat.com> - 6.14-1
- 6.14 bump (rhbz#2244960)

* Wed Oct 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 6.13-1
- 6.13 bump (rhbz#2243140)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 6.12-3
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.12-1
- 6.12 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.11-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.11-2
- Update the running tests

* Mon Sep 20 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.11-1
- 6.11 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.10-2
- Perl 5.34 rebuild

* Mon May 10 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.10-1
- 6.10 bump

* Wed Apr 07 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.07-1
- 6.07 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-7
- Unbundle flamegraph (bug #1781251)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-2
- Perl 5.28 rebuild

* Tue Jun 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.06-1
- 6.06 bump

* Tue Mar 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.05-1
- 6.05 bump

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-7
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.04-1
- 6.04 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-2
- Perl 5.24 rebuild

* Tue Mar 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.03-1
- 6.03 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 03 2015 Petr Šabata <contyk@redhat.com> - 6.02-1
- 6.02 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.01-2
- Perl 5.22 rebuild

* Wed Apr 08 2015 Petr Šabata <contyk@redhat.com> - 6.01-1
- 6.01 bump

* Fri Mar 20 2015 Petr Šabata <contyk@redhat.com> - 5.07-1
- 5.07 bump
- Modernize the spec and fix the dependency list

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.06-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.06-1
- 5.06 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Iain Arnell <iarnell@gmail.com> 5.05-1
- update to latest upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 5.00-2
- Perl 5.18 rebuild

* Fri Apr 19 2013 Iain Arnell <iarnell@gmail.com> 5.00-1
- update to latest upstream version

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 4.25-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 4.23-1
- update to latest upstream version

* Sat Oct 20 2012 Iain Arnell <iarnell@gmail.com> 4.09-1
- update to latest upstream version

* Sun Aug 19 2012 Iain Arnell <iarnell@gmail.com> 4.08-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 4.06-7
- Perl 5.16 rebuild

* Tue Jun 12 2012 Iain Arnell <iarnell@gmail.com> 4.06-6
- specify additional build dependencies

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 4.06-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 4.06-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 03 2010 Iain Arnell <iarnell@gmail.com> 4.06-1
- update to latest upstream version

* Wed Sep 29 2010 jkeating - 4.05-2
- Rebuilt for gcc bug 634757

* Sat Sep 25 2010 Iain Arnell <iarnell@gmail.com> 4.05-1
- update to latest upstream
- clean up spec for modern rpmbuild
- reenable t/70-subname.t

* Sun Jul 11 2010 Iain Arnell <iarnell@gmail.com> 4.04-1
- update to latest upstream

* Wed Jun 23 2010 Iain Arnell <iarnell@gmail.com> 4.03-1
- update to latest upstream

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 4.02-2
- perftest.pl has been removed from upstream

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 4.02-1
- update to latest upstream

* Wed Jun 16 2010 Iain Arnell <iarnell@gmail.com> 4.01-1
- update to latest upstream

* Tue Jun 15 2010 Iain Arnell <iarnell@gmail.com> 4.00-1
- update to latest upstream
- enable zlib support

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.11-3
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.11-2
- Mass rebuild with perl-5.12.0

* Wed Mar 17 2010 Iain Arnell <iarnell@gmail.com> 3.11-1
- update to latest upstream version
- BR perl(Sub::Name)

* Sun Mar 07 2010 Iain Arnell <iarnell@gmail.com> 3.02-1
- update to latest upstream version
- requires perl(JSON::Any)

* Mon Jan 04 2010 Iain Arnell <iarnell@gmail.com> 3.01-1
- update to latest upstream version
- use perl_default_filter

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.10-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Iain Arnell <iarnell@gmail.com> 2.10-1
- update to latest upstream version

* Fri Apr 10 2009 Iain Arnell <iarnell@gmail.com> 2.09-1
- update to latest upstream

* Tue Mar 17 2009 Iain Arnell 2.08-1
- Specfile autogenerated by cpanspec 1.77.
- strip private perl libs from provides
- add scripts and man pages to files
