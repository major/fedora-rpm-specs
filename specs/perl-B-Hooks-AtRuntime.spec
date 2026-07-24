Name:           perl-B-Hooks-AtRuntime
Version:        8
Release:        16%{?dist}
Summary:        Lower blocks from compile time to runtime
# 2-clause BSD licence
# cf. lib/B/Hooks/AtRuntime.pm
License:        BSD-2-Clause
URL:            https://metacpan.org/dist/B-Hooks-AtRuntime/
Source0:        https://cpan.metacpan.org/authors/id/B/BM/BMORROW/B-Hooks-AtRuntime-%{version}.tar.gz

# build requirements
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::Exception) >= 0.31
BuildRequires:  perl(Test::Exports) >= 1
BuildRequires:  perl(Test::More) >= 1.001002
BuildRequires:  perl(Test::Warn) >= 0.22
BuildRequires:  perl(lib)

# Optional run-time dependency
Recommends:     perl(Filter::Util::Call)


%description
This module allows code that runs at compile-time to do something at
runtime. A block passed to at_runtime gets compiled into the code that's
currently compiling, and will be called when control reaches that point
at runtime. In the example in the SYNOPSIS, the warnings will occur in
order, and if that section of code runs more than once, so will all
three warnings.

%prep
%setup -q -n B-Hooks-AtRuntime-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes
%{perl_vendorarch}/auto/B/Hooks/AtRuntime/AtRuntime.so
%{perl_vendorarch}/B/Hooks/AtRuntime.pm
%{_mandir}/man3/B::Hooks::AtRuntime.3pm*

%changelog
* Wed Jul 22 2026 Jitka Plesnikova <jplesnik@redhat.com> - 8-16
- Perl 5.44 rebuild

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Jul 06 2026 Emmanuel Seyman <emmanuel@seyman.fr> - 8-14
- Recreated for Fedora

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 8-11
- Perl 5.42 rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 8-8
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 8-4
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 8-2
- Convert license to SPDX.

* Sun Aug 14 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 8-1
- Upstream update to 8.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 7-2
- Reflect feedback from review.

* Fri Jul 01 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 7-1
- Update to 7.
- Switch to using metacpan.org URLs.

* Thu Jun 16 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 6-1
- Initial Fedora package.
