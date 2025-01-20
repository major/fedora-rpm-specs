Summary:       Simple Template Toolkit plugin interfacing to the CGI module
Name:          perl-Template-Plugin-CGI
Version:       3.101
Release:       9%{?dist}
License:       (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
URL:           https://metacpan.org/release/Template-Plugin-CGI
Source:        https://cpan.metacpan.org/modules/by-module/Template/Template-Plugin-CGI-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: make
BuildRequires: perl(base)
BuildRequires: perl(blib)
BuildRequires: perl(CGI) >= 4.44
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::Spec)
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(Template) >= 3.100
BuildRequires: perl(Template::Plugin)
BuildRequires: perl(Template::Test)
BuildRequires: perl(Test::More)
BuildRequires: perl(warnings)

Requires:      perl(CGI) >= 4.44
Conflicts:     perl-Template-Toolkit < 3.010-5

%{?perl_default_filter}


%description
This is a very simple Template Toolkit Plugin interface to the CGI module.


%prep
%autosetup -n Template-Plugin-CGI-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_build pure_install DESTDIR=%{buildroot}


%check
unset AUTHOR_TESTING
%make_build test


%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/Template::Plugin::CGI*3pm*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.101-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.101-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.101-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.101-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 16 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.101-3
- Address comments from review process

* Thu Sep 15 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.101-2
- Address comments from review process

* Wed Sep 14 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.101-1
- Initial RPM release
