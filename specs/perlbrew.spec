Name:           perlbrew
Version:        1.01
Release:        2%{?dist}
Summary:        Manage perl installations in your $HOME
License:        MIT
URL:            https://metacpan.org/release/App-perlbrew
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUGOD/App-perlbrew-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
# Run-time
BuildRequires:  perl(Capture::Tiny) >= 0.48
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN::Perl::Releases) >= 5.20230720
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::PatchPerl) >= 2.08
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.22
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.2304
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(local::lib) >= 2.000014
BuildRequires:  perl(overload)
#BuildRequires:  perl(Pod::Markdown) >= 2.002
BuildRequires:  perl(Pod::Usage) >= 1.69
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(lib)
BuildRequires:  perl(ok)
BuildRequires:  perl(Path::Class) >= 0.33
BuildRequires:  perl(Test2::Plugin::IOEvents)
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Tools::Basic)
BuildRequires:  perl(Test2::Tools::ClassicCompare)
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Mock)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception) >= 0.32
BuildRequires:  perl(Test::More) >= 1.001002
BuildRequires:  perl(Test::NoWarnings) >= 1.04
BuildRequires:  perl(Test::Output) >= 1.03
BuildRequires:  perl(Test::Spec) >= 0.47
#BuildRequires:  perl(Test::TempDir::Tiny) >= 0.016
BuildRequires:  wget
Requires:       perl(Capture::Tiny) >= 0.48
Requires:       perl(CPAN::Perl::Releases) >= 5.20230720
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(Devel::PatchPerl) >= 2.00
Requires:       perl(ExtUtils::MakeMaker) >= 7.22
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
Requires:       perl(FindBin)
Requires:       perl(local::lib) >= 2.000014
Requires:       perl(Pod::Usage) >= 1.68
Requires:       curl

# maybe someone expects to find
Provides:       perl-App-perlbrew = %{version}-%{release}

%{?perl_default_filter}
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(test2_helpers.pl\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(PerlbrewTestHelpers\\)


%description
perlbrew is a program to automate the building and installation of perl in
the users HOME. At the moment, it installs everything to ~/perl5/perlbrew,
and requires you to tweak your PATH by including a bashrc/cshrc file it
provides. You then can benefit from not having to run 'sudo' commands to
install cpan modules because those are installed inside your HOME too. It's
almost like an isolated perl environments.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n App-perlbrew-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
perl -V
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Few tests used ./script/perlbrew
mkdir %{buildroot}%{_libexecdir}/%{name}/script
ln -s %{_bindir}/perlbrew %{buildroot}%{_libexecdir}/%{name}/script
chmod 755 %{buildroot}%{_libexecdir}/%{name}/t/fake-bin/curl
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-1
- 1.01 bump (rhbz#2326977)

* Fri Oct 04 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-1
- 1.00 bump (rhbz#2316412)

* Tue Sep 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-1
- 0.99 bump (rhbz#2310606)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-1
- 0.98 bump (rhbz#2231459)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.97-1
- 0.97 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.96-1
- 0.96 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-2
- Perl 5.36 rebuild

* Mon May 16 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-1
- 0.95 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.94-1
- 0.94 bump

* Wed Nov 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-1
- 0.93 bump

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.92-2
- Perl 5.34 rebuild

* Thu Apr 15 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.92-1
- 0.92 bump
- Package tests

* Sun Jan 31 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.91-1
- 0.91 bump

* Fri Jan 29 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-1
- 0.90 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.89-1
- 0.89 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.88-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-2
- Perl 5.32 rebuild

* Wed Jan 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.88-1
- 0.88 bump

* Tue Oct 29 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.87-1
- 0.87 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.86-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.86-1
- 0.86 bump

* Mon Dec 17 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.85-1
- 0.85 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-2
- Perl 5.28 rebuild

* Sun Jun 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.84-1
- 0.84 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.82-1
- 0.82 bump

* Mon Dec 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.81-1
- 0.81 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-1
- 0.80 bump

* Mon Jun 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.79-1
- 0.79 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-1
- 0.78 bump

* Mon Nov 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.77-1
- 0.77 bump

* Fri Aug 05 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-2
- Remove Perl version 5.3.7 from tests (CPAN RT#116517)

* Wed Jun 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-1
- 0.76 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-2
- Perl 5.24 rebuild

* Thu Mar 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-1
- 0.75 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-1
- 0.74 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.73-2
- Perl 5.22 rebuild

* Wed Feb 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.73-1
- 0.73 bump

* Tue Nov 11 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.72-1
- 0.72 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 10 2013 Iain Arnell <iarnell@gmail.com> 0.66-1
- update to latest upstream version
- patch to include vendorarch/vendorlib in "special" handling of Cwd (RT#87897)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.64-2
- Perl 5.18 rebuild

* Fri Jun 07 2013 Iain Arnell <iarnell@gmail.com> 0.64-1
- update to latest upstream version
- explicitly require CPAN::Perl::Releases

* Fri May 17 2013 Iain Arnell <iarnell@gmail.com> 0.63-1
- update to latest upstream version

* Sun Apr 14 2013 Johan Vromans <jvromans@squirrel.nl> 0.62-1
- update to latest upstream version
- add dependency for perl-Test-NoWarnings
- depend on perl-local-lib at least version 1.008008

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Iain Arnell <iarnell@gmail.com> 0.46-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 0.44-2
- Perl 5.16 rebuild

* Sun Jul 08 2012 Iain Arnell <iarnell@gmail.com> 0.44-1
- update to latest upstream version

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.43-2
- Perl 5.16 rebuild

* Sat Jun 09 2012 Iain Arnell <iarnell@gmail.com> 0.43-1
- update to latest upstream version

* Tue Mar 13 2012 Iain Arnell <iarnell@gmail.com> 0.42-1
- update to latest upstream version

* Tue Feb 07 2012 Iain Arnell <iarnell@gmail.com> 0.41-1
- update to latest upstream version

* Thu Jan 05 2012 Iain Arnell <iarnell@gmail.com> 0.39-1
- update to latest upstream version

* Mon Nov 14 2011 Iain Arnell <iarnell@gmail.com> 0.33-1
- update to latest upstream version

* Mon Nov 14 2011 Iain Arnell <iarnell@gmail.com> 0.32-1
- update to latest upstream version
- add additional runtime requires

* Sun Oct 09 2011 Iain Arnell <iarnell@gmail.com> 0.29-1
- update to latest upstream version

* Sat Aug 13 2011 Iain Arnell <iarnell@gmail.com> 0.28-1
- update to latest upstream version

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.27-3
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.27-2
- Perl mass rebuild

* Wed Jul 13 2011 Iain Arnell <iarnell@gmail.com> 0.27-1
- update to latest upstream
- BR perl(File::Temp)

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.24-3
- Perl mass rebuild

* Sun Jun 12 2011 Iain Arnell <iarnell@gmail.com> 0.24-2
- BR perl(Test::Spec) and reinstate t/installation2.t

* Wed Jun 08 2011 Iain Arnell <iarnell@gmail.com> 0.24-1
- update to latest upstream version

* Fri Jun 03 2011 Iain Arnell <iarnell@gmail.com> 0.23-1
- update to latest upstream version

* Fri May 27 2011 Iain Arnell <iarnell@gmail.com> 0.22-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed May 11 2011 Iain Arnell <iarnell@gmail.com> 0.20-1
- update to latest upstream version

* Wed Mar 16 2011 Iain Arnell <iarnell@gmail.com> 0.18-1
- update to latest upstream version

* Thu Mar 10 2011 Iain Arnell <iarnell@gmail.com> 0.17-1
- update to latest upstream version

* Sun Feb 20 2011 Iain Arnell <iarnell@gmail.com> 0.16-1
- update to latest upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 09 2010 Iain Arnell <iarnell@gmail.com> 0.15-2
- actually apply the older-Test-More patch

* Thu Dec 09 2010 Iain Arnell <iarnell@gmail.com> 0.15-1
- update to latest upstream version
- no longer requires perl(File::Path::Tiny)
- patch tests to work on older Test::More for EPEL

* Thu Dec 02 2010 Iain Arnell <iarnell@gmail.com> 0.14-1
- update to latest upstream version

* Tue Nov 23 2010 Iain Arnell <iarnell@gmail.com> 0.13-1
- update to latest upstream version

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-3
- Mass rebuild with perl-5.12.0

* Tue May 18 2010 Iain Arnell <iarnell@gmail.com> 0.06-2
- License is MIT, not "same as Perl"

* Sat May 08 2010 Iain Arnell 0.06-1
- Specfile autogenerated by cpanspec 1.78.
