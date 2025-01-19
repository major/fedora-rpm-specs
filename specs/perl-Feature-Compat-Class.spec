Name:           perl-Feature-Compat-Class
Version:        0.07
Release:        3%{?dist}
Summary:        Make class syntax available
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Feature-Compat-Class
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Feature-Compat-Class-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Object::Pad)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

Requires:       perl(Object::Pad)

%description
This module provides the new class keyword and related others (method, field
and ADJUST) in a forward-compatible way.


%prep
%autosetup -n Feature-Compat-Class-%{version}


%build
perl Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*


%check
./Build test


%files
%doc Changes README
%license LICENSE
%dir %{perl_vendorlib}/Feature/
%dir %{perl_vendorlib}/Feature/Compat
%{perl_vendorlib}/Feature/Compat/Class.pm
%{_mandir}/man3/Feature::Compat::Class.*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Sandro Mani <manisandro@gmail.com> - 0.07-1
- Update to 0.07

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Sandro Mani <manisandro@gmail.com> - 0.06-1
- Update to 0.06

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Sandro Mani <manisandro@gmail.com> - 0.05-1
- Update to 0.05

* Fri Jan 06 2023 Sandro Mani <manisandro@gmail.com> - 0.04-2
- Fix license
- Fix source URL
- List files explicitly
- Fix requires/BRs

* Fri Jan 06 2023 Sandro Mani <manisandro@gmail.com> - 0.04-1
- Initial package
