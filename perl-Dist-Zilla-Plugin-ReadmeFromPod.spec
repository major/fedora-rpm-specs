Name:           perl-Dist-Zilla-Plugin-ReadmeFromPod
Version:        0.37
Release:        13%{?dist}
Summary:        Automatically convert POD to a README for Dist::Zilla
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-ReadmeFromPod
Source0:        https://cpan.metacpan.org/authors/id/F/FA/FAYLAND/Dist-Zilla-Plugin-ReadmeFromPod-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Dist::Zilla::File::InMemory not used at tests
# Dist::Zilla::Role::FilePruner version from Dist::Zilla in META
BuildRequires:  perl(Dist::Zilla::Role::FilePruner) >= 6.000
BuildRequires:  perl(Dist::Zilla::Role::InstallTool) >= 5
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moose)
BuildRequires:  perl(Path::Tiny) >= 0.004
BuildRequires:  perl(Pod::Readme) >= 1.2.0
# Tests:
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
# Test::Kwalitee 1.21 not used
# Test::Pod 1.41 not used
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Dist::Zilla::File::InMemory)
# Dist::Zilla::Role::FilePruner version from Dist::Zilla in META
Requires:       perl(Dist::Zilla::Role::FilePruner) >= 6.000
Requires:       perl(Dist::Zilla::Role::InstallTool) >= 5
Requires:       perl(Pod::Readme) >= 1.2.0
# Module names passed to Module::Load::load() via Pod::Readme::new() from %%FORMAT
Suggests:       perl(Pod::Markdown)
Suggests:       perl(Pod::Markdown::Github)
Suggests:       perl(Pod::Simple::HTML)
Suggests:       perl(Pod::Simple::RTF)
Suggests:       perl(Pod::Simple::Text)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::Readme\\)$

%description
Generate the README file from main_module (or other if specified)
with Pod::Readme.

%prep
%setup -q -n Dist-Zilla-Plugin-ReadmeFromPod-%{version}
# Normalize encoding
iconv -f ISO-8859-1 -t UTF-8 < README.md > README.md.utf8
touch -r README.md README.md.utf8
mv README.md.utf8 README.md

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-12
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-9
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-6
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Petr Pisar <ppisar@redhat.com> - 0.37-1
- 0.37 bump

* Tue Oct 30 2018 Petr Pisar <ppisar@redhat.com> - 0.36-1
- 0.36 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Petr Pisar <ppisar@redhat.com> - 0.35-1
- 0.35 bump

* Mon Oct 10 2016 Petr Pisar <ppisar@redhat.com> - 0.34-1
- 0.34 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Petr Pisar <ppisar@redhat.com> - 0.33-1
- 0.33 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-2
- Perl 5.22 rebuild

* Fri Feb 13 2015 Petr Pisar <ppisar@redhat.com> - 0.32-1
- 0.32 bump

* Wed Dec 10 2014 Petr Pisar <ppisar@redhat.com> - 0.30-1
- 0.30 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-2
- Perl 5.20 rebuild

* Thu Sep 04 2014 Petr Šabata <contyk@redhat.com> 0.21-1
- Initial packaging
