Name:           perl-String-License
Version:        0.0.11
Release:        2%{?dist}
Summary:        Detect source code license statements in a text string
License:        AGPL-3.0-or-later

BuildArch:      noarch
URL:            https://metacpan.org/pod/String::License
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/String-License-v%{version}.tar.gz
# Fix failing test
# Patch0:         test.patch
# Fix build with perl-5.38
# See https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1042847
# Patch1:         perl538.patch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Array::IntSpan)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Feature::Compat::Class)
BuildRequires:  perl(File::BaseDir)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(re::engine::RE2)
BuildRequires:  perl(Regexp::Pattern)
BuildRequires:  perl(Regexp::Pattern::License)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Compare)
BuildRequires:  perl(Test2::Require)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Todo)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)


%description
String::License identifies license statements in a string and serializes them
in a normalized format.


%prep
%autosetup -p1 -n String-License-v%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/String::License*.*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 22 2024 Sandro Mani <manisandro@gmail.com> - 0.0.11-1
- Update to 0.0.11

* Wed Aug 21 2024 Sandro Mani <manisandro@gmail.com> - 0.0.10-1
- Update to 0.0.10

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 28 2024 Sandro Mani <manisandro@gmail.com> - 0.0.9-5
- Add test-software-license.patch

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Sandro Mani <manisandro@gmail.com> - 0.0.9-1
- Update to 0.0.9

* Tue Jul 04 2023 Sandro Mani <manisandro@gmail.com> - 0.0.7-1
- Update to 0.0.7

* Sun Jun 04 2023 Sandro Mani <manisandro@gmail.com> - 0.0.6-1
- Update to 0.0.6

* Tue May 30 2023 Sandro Mani <manisandro@gmail.com> - 0.0.5-1
- Update to 0.0.5

* Tue May 30 2023 Sandro Mani <manisandro@gmail.com> - 0.0.4-3
- Fix failing test

* Sun Jan 29 2023 Sandro Mani <manisandro@gmail.com> - 0.0.4-2
- License is AGPL-3.0-or-later
- Split long description

* Sun Jan 29 2023 Sandro Mani <manisandro@gmail.com> - 0.0.4-1
- Initial package
