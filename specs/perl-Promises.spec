Name:           perl-Promises
Version:        1.05
Release:        1%{?dist}
Summary:        Implementation of Promises in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Promises
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Promises-%{version}.tar.gz
BuildArch:      noarch
# Fix numbering of line in test when shebang is added
Patch0:         Promises-1.05-Fix-numbering-of-line-in-test.patch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(AE)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(EV)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Timer::Countdown)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Attribute)
BuildRequires:  perl(Sub::Exporter)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Async)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Warn)
Requires:       perl(Data::Dumper)
Requires:       perl(Module::Runtime)

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(AsyncUtil\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(NoEV\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Promises::Test.*\\)


%description
This module is an implementation of the "Promise/A+" pattern for
asynchronous programming. Promises are meant to be a way to better deal
with the resulting callback spaghetti that can often result in
asynchronous programs.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Promises-%{version}
perl -MConfig -pi -e 's|^#!.*perl|$Config{startperl}|' ./example/*.pl

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

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
%license LICENSE
%doc Changes example README.md
%{perl_vendorlib}/Promises*
%{_mandir}/man3/Promises*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon Jun 30 2025 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-1
- 1.05 bump (rhbz#2375526)
- Package tests

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-3
- Perl 5.32 rebuild

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-2
- Add missing BR

* Mon Feb 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-1
- 1.04 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.02-1
- 1.02 bump

* Tue Jun 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-1
- 1.01 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-2
- Perl 5.30 rebuild

* Tue May 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-1
- 1.00 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-1
- 0.99 bump

* Mon Oct 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-1
- 0.98 bump

* Mon Aug 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.96-1
- 0.96 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.94-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.94-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 26 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.94-1
- 0.94 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-3
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-2
- Perl 5.20 rebuild

* Thu May 22 2014 David Dick <ddick@cpan.org> - 0.93-1
- Initial release
