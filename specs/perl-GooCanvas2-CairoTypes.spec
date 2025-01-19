%global tarname GooCanvas2-CairoTypes

Name:           perl-GooCanvas2-CairoTypes
Version:        0.001
Release:        18%{?dist}
Summary:        Bridge between GooCanvas2 and Cairo types

# lib/GooCanvas2/CairoTypes.pm file is "GPL+ or Artistic"
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/GooCanvas2-CairoTypes
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASOKOLOV/GooCanvas2-CairoTypes-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-Glib-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Cairo::Install::Files)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(goocanvas-2.0)

# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)

%description
There is an issue in the interaction between GooCanvas, GObject
Introspection, Cairo, and their Perl bindings, which causes some
functionality to be unusable from Perl side. This is better described
here
<https://stackoverflow.com/questions/64625955/cairosolidpattern-is-not-o
f-type-goocanvas2cairopattern>, and there was an attempt
<https://gitlab.gnome.org/GNOME/goocanvas/-/merge_requests/9> to fix it
upstream. Until it's fixed, this can serve as a workaround for it.

Currently this module only "fixes"
"Cairo::Pattern/GooCanvas2::CairoPattern" interop. For certain calls it
just works if this module was included; for some other calls you need to
explicitly convert the type.

If you have any idea how to fix those cases to not require such call, or
need to bridge more types, pull requests
<https://github.com/DarthGandalf/GooCanvas2-CairoTypes> are welcome!

%prep
%setup -q -n %{tarname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README Changes
%{perl_vendorarch}/auto/GooCanvas2/
%{perl_vendorarch}/GooCanvas2*
%{_mandir}/man3/GooCanvas2::CairoTypes.3pm.gz

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.001-17
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-15
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-11
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.001-5
- Remove the parenthesis from the License value
- Remove Provides it's is created automatically
- Do not create a devel subpackage

* Fri Jul 09 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.001-4
- Dropped %%filter_provides_in macro
- Fixed %%description must be sentence
- Fixed license value to "GPL+ or Artistic"
- Include unpacked directory %%dir %%{perl_vendorarch}/auto/
- Do not do %%exclude %%{perl_vendorarch}/perllocal.pod
  That's achieved with "Makefile.PL NO_PERLLOCAL=1"
- Include %%{_mandir}/man3/GooCanvas2::CairoTypes.3pm.gz file
  in devel subpackage
- Remove BR perl-macros
- Add BR perl(strict)
- Add BR perl(warnigs)
- Add BR perl(File::Spec)
- Remove BR perl(lib)
- Corrected Requires to %%{name}%%{?_isa}

* Tue Jun 29 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.001-3
- Rename package to perl-GooCanvas2-CairoTypes

* Thu Jun 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.001-2
- Rename package to perl-goocanvas2-cairotypes

* Thu Jun 10 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.001-1
- Initial package
