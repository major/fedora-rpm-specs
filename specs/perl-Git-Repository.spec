Name:           perl-Git-Repository
Version:        1.325
Release:        14%{?dist}
Summary:        Perl interface to Git repositories
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Git-Repository
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/Git-Repository-%{version}.tar.gz
# Adapt tests to git-2.38.1, proposed to the upstream,
# <https://github.com/book/Git-Repository/pull/22>
Patch1:         git-2.38.1-compatibility.patch
# Adapt tests to git-2.39.0, bug #2175807, proposed to the upstream,
# <https://github.com/book/Git-Repository/pull/23>
Patch2:         git-var-GIT_EDITOR.patch
# Do not write to CWD by the tests, proposed to the upstream,
# <https://github.com/book/Git-Repository/pull/24>
Patch3:         Git-Repository-1.325-tests-Do-not-write-to-current-working-directory.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  git
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Git::Version::Compare) >= 1.001
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(System::Command) >= 1.118
BuildRequires:  perl(Test::Builder)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires::Git) >= 1.005
Requires:       git
Requires:       perl(Git::Version::Compare) >= 1.001
Requires:       perl(System::Command) >= 1.118

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Git::Version::Compare|Test::Requires::Git|System::Command)\\)$

# Hide private modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}perl\\((Git::Repository::Plugin::Hello(|2)|MyGit::Hello)\\)

%description
Git::Repository is a Perl interface to Git, for scripted interactions with
repositories. It's a low-level interface that allows calling any Git
command, whether porcelain or plumbing, including bidirectional commands
such as git commit-tree.

%package -n perl-Test-Git
Summary:        Helper functions for test scripts using Git
# Bind releases from the same build to minimize a testing matrix
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Git::Version::Compare) >= 1.001
# Test::Git(3pm) manual page moved in from perl-Git-Repository-1.325-11.fc41
Conflicts:      perl-Git-Repository < 1.325-12

%description -n perl-Test-Git
Test::Git provides a number of helpful functions when running test scripts that
require the creation and management of a Git repository.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-interpreter
Requires:       perl-Test-Git = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Requires::Git) >= 1.005

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Git-Repository-%{version}
# Remove always skipped tests
for F in t/author-pod-coverage.t t/author-pod-syntax.t t/release-distmeta.t t/test-all-git.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t t/sudo.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Git
%{perl_vendorlib}/Git/Repository
%{perl_vendorlib}/Git/Repository.pm
%{_mandir}/man3/Git::Repository.*
%{_mandir}/man3/Git::Repository::*

%files -n perl-Test-Git
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/Git.pm
%{_mandir}/man3/Test::Git.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.325-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.325-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Petr Pisar <ppisar@redhat.com> - 1.325-12
- Move Test::Git(3pm) manual page to perl-Test-Git
- Package the tests

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.325-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.325-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.325-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Pazdziora <jpazdziora@redhat.com> - 1.325-8
- 2175807 - address git var GIT_EDITOR related build fail with git 2.39.1.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.325-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 05 2022 Pazdziora <jpazdziora@redhat.com> - 1.325-6
- 2137877 - test compatilibity patch for git 2.38.1.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.325-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.325-4
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.325-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.325-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 01 2021 Jan Pazdziora <jpazdziora@redhat.com> - 1.325-1
- 1966355 - Rebase to upstream version 1.325.

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.324-8
- Perl 5.34 rebuild

* Sat Jan 30 2021 Jan Pazdziora <jpazdziora@redhat.com> - 1.324-7
- 1917453 - Address build fail with git 2.30.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.324-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.324-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.324-4
- Perl 5.32 rebuild

* Thu Mar 19 2020 Petr Pisar <ppisar@redhat.com> - 1.324-3
- Build-require blib for the tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.324-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Jan Pazdziora <jpazdziora@redhat.com> - 1.324-1
- 1747726 - Rebase to upstream version 1.324.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.323-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.323-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.323-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Jan Pazdziora <jpazdziora@redhat.com> - 1.323-1
- 1653175 - Rebase to upstream version 1.323.

* Mon Sep 10 2018 Jan Pazdziora <jpazdziora@redhat.com> - 1.322-4
- 1622996 - Match new error message format in git 2.19.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.322-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.322-2
- Perl 5.28 rebuild

* Mon Apr 23 2018 Jan Pazdziora <jpazdziora@redhat.com> - 1.322-1
- 1570328 - Rebase to upstream version 1.322.

* Tue Apr 03 2018 Jan Pazdziora <jpazdziora@redhat.com> - 1.321-3
- 1560908 - Match new error message format in git 2.17.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.321-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Jan Pazdziora <jpazdziora@redhat.com> - 1.321-1
- 1497525 - Rebase to upstream version 1.321.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.320-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.320-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.320-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Jan Pazdziora <jpazdziora@redhat.com> - 1.320-1
- 1346508 - Rebase to upstream version 1.320.

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.319-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Wed May 18 2016 Jan Pazdziora <jpazdziora@redhat.com> - 1.319-1
- 1336971 - Rebase to upstream version 1.319.

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.318-2
- Perl 5.24 rebuild

* Mon Mar 14 2016 Jan Pazdziora <jpazdziora@redhat.com> - 1.318-1
- 1.318 bump

* Tue Feb 16 2016 Petr Šabata <contyk@redhat.com> - 1.317-1
- 1.317 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.316-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Petr Šabata <contyk@redhat.com> - 1.316-1
- 1.316 bump

* Mon Sep 21 2015 Petr Šabata <contyk@redhat.com> - 1.315-2
- Make the test suite compatible with git 2.5.2+ (rt#107219, rhbz#1264744)

* Thu Jul 30 2015 Petr Šabata <contyk@redhat.com> - 1.315-1
- 1.315 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.314-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.314-2
- Perl 5.22 rebuild

* Fri Jun 05 2015 Petr Šabata <contyk@redhat.com> - 1.314-1
- 1.314 bump

* Mon Dec 01 2014 Petr Šabata <contyk@redhat.com> - 1.312-2
- Fix broken MODULE_COMPAT

* Fri Nov 28 2014 Petr Šabata <contyk@redhat.com> - 1.312-1
- 1.312 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.27-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 1.27-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 21 2012 Iain Arnell <iarnell@gmail.com> 1.27-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.25-3
- Perl 5.16 rebuild

* Fri Feb 10 2012 Iain Arnell <iarnell@gmail.com> 1.25-2
- avoid file dependencies; just require git
- add Changes and README to perl-Test-Git docs
- explicit BuildRequires for dual-lifed modules

* Fri Jan 13 2012 Iain Arnell <iarnell@gmail.com> 1.25-1
- Specfile autogenerated by cpanspec 1.78.
- Separate sub-package for Test::Git
