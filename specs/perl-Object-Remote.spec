Name:           perl-Object-Remote
Version:        0.004004
Release:        3%{?dist}
Summary:        Call methods on objects in other processes or on other hosts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Remote
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Object-Remote-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Algorithm::C3)
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::C3)
# Class::C3::next - the part of perl-Class-C3, but it isn't listed in provides
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Future) >= 0.49
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Contextual) >= 0.005
BuildRequires:  perl(Log::Contextual::Role::Router)
BuildRequires:  perl(Method::Generate::BuildAll)
BuildRequires:  perl(Method::Generate::DemolishAll)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.006
BuildRequires:  perl(Moo::HandleMoose::_TypeMap)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strictures) >= 2
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::HiRes)
# Tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
Requires:       perl(Algorithm::C3)
Requires:       perl(Class::C3)
Requires:       perl(Devel::GlobalDestruction)
Requires:       perl(Future) >= 0.49
Requires:       perl(Log::Contextual) >= 0.005
Requires:       perl(Log::Contextual::Role::Router)
Requires:       perl(Method::Generate::BuildAll)
Requires:       perl(Method::Generate::DemolishAll)
Requires:       perl(Moo) >= 1.006
Requires:       perl(Moo::HandleMoose::_TypeMap)
Requires:       perl(MRO::Compat)
Requires:       perl(strictures) >= 2
Requires:       openssh-clients
Requires:       sudo

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Future\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moo\\)$
%global __requires_exclude %__requires_exclude|^perl\\(strictures\\) >= 1$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(maybe\\)$
%global __provides_exclude %__provides_exclude|^perl\\(maybe::start\\)$
%global __provides_exclude %__provides_exclude|^perl\\(start\\)$
%global __provides_exclude %__provides_exclude|^perl\\(then\\)$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %__requires_exclude|^perl\\(ORFeed.*\\)$
%global __requires_exclude %__requires_exclude|^perl\\(ORTest.*\\)$
%global __requires_exclude %__requires_exclude|^perl\\(t::lib::.*\\)$

%description
Object::Remote allows you to create an object in another process - usually
one running on another machine you can connect to via ssh, although there
are other connection mechanisms available.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Object-Remote-%{version}
perl -MConfig -pi -e 's|^#!.*perl|$Config{startperl}|' bin/*

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
%license LICENSE
%doc Changes README
%{_bindir}/object-remote*
%{_bindir}/remoterepl
%dir %{perl_vendorlib}/Object
%{perl_vendorlib}/Object/Remote*
%{_mandir}/man3/Object::Remote*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.004004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.004004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.004004-1
- 0.004004 bump (rhbz#2282899)

* Thu May 23 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.004003-1
- 0.004003 bump (rhbz#2282271)
- Package tests

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.004001-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.004001-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.004001-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.004001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.004001-1
- 0.004001 bump

* Tue Nov 26 2019 Petr Pisar <ppisar@redhat.com> - 0.004000-11
- Adapt to changes in Moo-2.003006 (CPAN RT#130885)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.004000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.004000-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.004000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.004000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.004000-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.004000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.004000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.004000-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.004000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.004000-1
- 0.004000 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.003006-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.003006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.003006-1
- 0.003006 bump

* Thu Jan 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.003005-2
- Update list of dependencies

* Wed Dec 16 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.003005-1
- Initial release
