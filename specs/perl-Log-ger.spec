Name:           perl-Log-ger
Version:        0.042
Release:        3%{?dist}
Summary:        Lightweight, flexible logging framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-ger
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Log-ger-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Data::Dmp) >= 0.241
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(parent)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Data::Dmp) >= 0.21

%description
The Log::ger Perl module provides another lightweight, flexible logging
framework.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Log-ger-%{version}
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
rm %{buildroot}%{_libexecdir}/%{name}/t/author-*.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Log/ger*
%{_mandir}/man3/Log::ger*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.042-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.042-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.042-1
- 0.042 bump (rhbz#2265610)

* Mon Feb 05 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.041-1
- 0.041 bump (rhbz#2262717)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.040-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.040-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.040-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.040-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.040-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.040-1
- 0.040 bump
- Package tests

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.038-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.038-2
- Perl 5.34 rebuild

* Sun Jan 31 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.038-1
- 0.038 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-2
- Perl 5.32 rebuild

* Wed Mar 11 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-1
- 0.037 bump

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.036-1
- 0.036 bump

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-1
- 0.034 bump

* Mon Mar 09 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.033-1
- 0.033 bump

* Wed Mar 04 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.031-1
- 0.031 bump

* Tue Feb 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.029-1
- 0.029 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.028-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.028-2
- Perl 5.30 rebuild

* Tue May 07 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.028-1
- 0.028 bump

* Mon Apr 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.027-1
- 0.027 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.025-1
- 0.025 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.023-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.023-1
- 0.023 bump

* Wed Aug 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-1
- 0.021 bump

* Wed Jul 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-1
- Initial release
