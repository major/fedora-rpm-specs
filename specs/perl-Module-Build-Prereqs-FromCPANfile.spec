Name:           perl-Module-Build-Prereqs-FromCPANfile
Version:        0.02
Release:        7%{?dist}
Summary:        Construct prereq parameters of Module::Build from cpanfile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Build-Prereqs-FromCPANfile
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/Module-Build-Prereqs-FromCPANfile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.132830
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Module::CPANfile) >= 1.0000
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version) >= 0.80
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Module::Build) >= 0.4004

%description
This simple module reads cpanfile and converts its content into valid
prereq parameters for new() method of Module::Build.

%prep
%setup -q -n Module-Build-Prereqs-FromCPANfile-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Module/Build/Prereqs*
%{_mandir}/man3/Module::Build::Prereqs*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 03 2024 Chris Adams <linux@cmadams.net> 0.02-5
- additional spec file cleanups

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.02-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.02-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.02-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.02-1
- initial package
