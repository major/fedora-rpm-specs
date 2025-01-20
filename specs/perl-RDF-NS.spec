Name:           perl-RDF-NS
Version:        20230619
Release:        6%{?dist}
Summary:        Popular RDF name space prefixes from prefix.cc
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RDF-NS
Source0:        https://cpan.metacpan.org/authors/id/V/VO/VOJ/RDF-NS-%{version}.tar.gz
# Fix shell bang
Patch0:         RDF-NS-20160409-Do-not-use-usr-bin-env.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(RDF::Trine::Node::Blank)
BuildRequires:  perl(RDF::Trine::Node::Resource)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
# Optional tests:
BuildRequires:  perl(RDF::Trine)
Requires:       perl(File::ShareDir) >= 1.00

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::ShareDir\\)$

%description
Hard-coding URI name spaces and prefixes for RDF applications is neither
fun nor maintainable. In the end we all use more or less the same
prefix definitions, as collected at <http://prefix.cc/>. This Perl module
includes all these prefixes as defined at specific snapshots in time.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(RDF::NS::Trine)
Requires:       perl(RDF::NS::URIS)
Requires:       perl(RDF::Trine)
Requires:       perl(URI)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n RDF-NS-%{version}
chmod -x lib/App/rdfns.pm
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
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
./Build test

%files
%license LICENSE
%doc Changes README.md
%{_bindir}/rdfns
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/rdfns.pm
%dir %{perl_vendorlib}/RDF
%dir %{perl_vendorlib}/auto
%dir %{perl_vendorlib}/auto/share
%dir %{perl_vendorlib}/auto/share/dist
%{perl_vendorlib}/auto/share/dist/RDF-NS
%{perl_vendorlib}/RDF/NS
%{perl_vendorlib}/RDF/NS.pm
%{perl_vendorlib}/RDF/SN.pm
%{_mandir}/man1/rdfns.*
%{_mandir}/man3/App::rdfns.*
%{_mandir}/man3/RDF::NS.*
%{_mandir}/man3/RDF::NS::*
%{_mandir}/man3/RDF::SN.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20230619-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230619-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230619-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230619-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230619-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Petr Pisar <ppisar@redhat.com> - 20230619-1
- 20230619 bump
- Package the tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20190227-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20190227-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 20190227-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20190227-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190227-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 20190227-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190227-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190227-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 20190227-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190227-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190227-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 20190227-2
- Perl 5.30 rebuild

* Thu Feb 28 2019 Petr Pisar <ppisar@redhat.com> - 20190227-1
- 20190227 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Petr Pisar <ppisar@redhat.com> - 20181102-1
- 20181102 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180227-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 20180227-2
- Perl 5.28 rebuild

* Wed Feb 28 2018 Petr Pisar <ppisar@redhat.com> - 20180227-1
- 20180227 bump

* Tue Feb 13 2018 Petr Pisar <ppisar@redhat.com> - 20180213-1
- 20180213 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170111-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170111-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 20170111-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170111-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Petr Pisar <ppisar@redhat.com> - 20170111-1
- 20170111 bump

* Fri May 27 2016 Petr Pisar <ppisar@redhat.com> - 20160409-1
- 20160409 bump

* Fri Apr 08 2016 Petr Pisar <ppisar@redhat.com> 20150725-1
- Specfile autogenerated by cpanspec 1.78.
