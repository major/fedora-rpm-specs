# Test with executing real programs
%bcond_without perl_Test2_Tools_Process_enables_extended_test

Name:           perl-Test2-Tools-Process
Version:        0.07
Release:        7%{?dist}
Summary:        Unit tests for code that calls exit, exec, system or qx()
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Tools-Process
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Test2-Tools-Process-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Return::MultiLevel)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Compare) >= 0.000121
BuildRequires:  perl(Test2::Compare::Array) >= 0.000121
BuildRequires:  perl(Test2::Compare::Custom) >= 0.000121
BuildRequires:  perl(Test2::Compare::Number) >= 0.000121
BuildRequires:  perl(Test2::Compare::String) >= 0.000121
BuildRequires:  perl(Test2::Compare::Wildcard) >= 0.000121
BuildRequires:  perl(Test2::Tools::Compare) >= 0.000121
%if %{with perl_Test2_Tools_Process_enables_extended_test}
BuildRequires:  bash
# coreutils for /usr/bin/true
%endif
# Tests:
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test2::V0) >= 0.000121
Requires:       perl(Config)
Requires:       perl(Test2::API) >= 1.302015
Requires:       perl(Test2::Compare) >= 0.000121
Requires:       perl(Test2::Compare::Array) >= 0.000121
Requires:       perl(Test2::Compare::Custom) >= 0.000121
Requires:       perl(Test2::Compare::Number) >= 0.000121
Requires:       perl(Test2::Compare::String) >= 0.000121
Requires:       perl(Test2::Compare::Wildcard) >= 0.000121
Requires:       perl(Test2::Tools::Compare) >= 0.000121
# Replaces perl-Test-Exec
Provides:       perl-Test-Exec = %{version}-%{release}
Obsoletes:      perl-Test-Exec < 0.04-12

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test::More|Test2::API|Test2::Compare(|::Array|::Custom|::Number|::String|::Wildcard)|Test2::Tools::Compare|Test2::V0)\\)$

%description
This set of testing tools is intended for writing unit tests for code that
interacts with other processes without using real processes that might have
unwanted side effects. It also lets you test code that exits program flow
without actually terminating your test. So far it allows you to test and/or
mock exit, exec, system, readpipe and qx//. Other process related tests
will be added in the future.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.98
Requires:       perl(Test2::V0) >= 0.000121
%if %{with perl_Test2_Tools_Process_enables_extended_test}
Requires:       bash
# coreutils for /usr/bin/true
Requires:       coreutils
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Test2-Tools-Process-%{version}
%if !%{with perl_Test2_Tools_Process_enables_extended_test}
rm t/test2_tools_process__live.t
perl -i -ne 'print $_ unless m{\A\Qt/test2_tools_process__live.t\E\b}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
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
unset CIPSOMETHING RETURN_MULTILEVEL_DEBUG
%if %{with perl_Test2_Tools_Process_enables_extended_test}
export CIPSOMETHING=true
%endif
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset CIPSOMETHING RETURN_MULTILEVEL_DEBUG
%if %{with perl_Test2_Tools_Process_enables_extended_test}
export CIPSOMETHING=true
%endif
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes Changes.Test-Exec README
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/Exec.pm
%dir %{perl_vendorlib}/Test2
%dir %{perl_vendorlib}/Test2/Tools
%{perl_vendorlib}/Test2/Tools/Process.pm
%{_mandir}/man3/Test::Exec.*
%{_mandir}/man3/Test2::Tools::Process.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Petr Pisar <ppisar@redhat.com> - 0.07-1
- 0.07 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Petr Pisar <ppisar@redhat.com> - 0.06-1
- 0.06 bump (bug #2013058)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-2
- Perl 5.34 rebuild

* Mon May 17 2021 Petr Pisar <ppisar@redhat.com> 0.05-1
- Specfile autogenerated by cpanspec 1.78.
