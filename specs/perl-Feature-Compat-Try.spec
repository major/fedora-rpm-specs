Name:           perl-Feature-Compat-Try
Version:        0.05
Release:        8%{?dist}
Summary:        Make try/catch syntax available
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Feature-Compat-Try
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Feature-Compat-Try-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::AsyncAwait) >= 0.10
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Syntax::Keyword::Try) >= 0.27
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

%if 0%{?fedora} < 37
# https://bugzilla.redhat.com/show_bug.cgi?id=2158742#c2
Requires:       perl(Syntax::Keyword::Try) >= 0.27
%endif


%description
This module makes syntax support for try/catch control flow easily available.


%prep
%autosetup -n Feature-Compat-Try-%{version}


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
%{perl_vendorlib}/Feature/Compat/Try.pm
%{_mandir}/man3/Feature::Compat::Try.*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Sandro Mani <manisandro@gmail.com> - 0.05-2
- Fix license
- Fix source URL
- List files explicitly
- Fix requires/BRs

* Fri Jan 06 2023 Sandro Mani <manisandro@gmail.com> - 0.05-1
- Initial package
