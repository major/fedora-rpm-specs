%ifarch %{ix86} x86_64 ia64 ppc64le
%bcond_without libquadmath
%else
%bcond_with libquadmath
%endif

Name: algol68g
Summary: Algol 68 Genie compiler-interpreter
Version: 3.5.12
Release: 2%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://jmvdveer.home.xs4all.nl/en.algol-68-genie.html
Source: https://jmvdveer.home.xs4all.nl/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(gmp)
BuildRequires: pkgconfig(libRmath)
BuildRequires: pkgconfig(mpfr)
BuildRequires: pkgconfig(libpq)
%if %{with libquadmath}
BuildRequires: libquadmath-devel
%endif
BuildRequires: plotutils-devel

%description
Algol 68 Genie (Algol68G) is an Algol 68 compiler-interpreter.
It can be used for executing Algol 68 programs or scripts.
Algol 68 is a rather lean orthogonal general-purpose language
that is a beautiful means for denoting algorithms.
Algol 68 was designed as a general-purpose programming language
by IFIP Working Group 2.1 (Algorithmic Languages and Calculi)
that has continuing responsibility for Algol 60 and Algol 68.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%{_bindir}/a68g
%{_mandir}/man1/a68g.1*
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%exclude %{_includedir}
%exclude %{_pkgdocdir}/COPYING

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 12 2025 Oleg Girko <ol@infoserver.lv> - 3.5.12-1
- Update to 3.5.12

* Fri Jan 03 2025 Oleg Girko <ol@infoserver.lv> - 3.5.11-1
- Update to 3.5.11

* Sat Nov 30 2024 Oleg Girko <ol@infoserver.lv> - 3.5.10-1
- Update to 3.5.10

* Fri Oct 18 2024 Oleg Girko <ol@infoserver.lv> - 3.5.9-1
- Update to 3.5.9

* Thu Oct 10 2024 Oleg Girko <ol@infoserver.lv> - 3.5.6-1
- Update to 3.5.6

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.5.4-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Oleg Girko <ol@infoserver.lv> - 3.5.4-1
- Update to 3.5.4

* Tue Jun 11 2024 Oleg Girko <ol@infoserver.lv> - 3.5.3-1
- Update to 3.5.3
- Don't run autoreconf again: we don't apply any patches

* Tue May 21 2024 Oleg Girko <ol@infoserver.lv> - 3.5.2-1
- Update to 3.5.2

* Wed May 01 2024 Oleg Girko <ol@infoserver.lv> - 3.5.1-2
- Add patch to make configure detect glibc again
- Run autoreconf again: we have patches to configure,ac

* Thu Feb 22 2024 Oleg Girko <ol@infoserver.lv> - 3.5.1-1
- Update to 3.5.1

* Mon Feb 05 2024 Oleg Girko <ol@infoserver.lv> - 3.5.0-1
- Update to 3.5.0

* Mon Jan 22 2024 Oleg Girko <ol@infoserver.lv> - 3.4.7-1
- Update to 3.4.7

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 14 2024 Oleg Girko <ol@infoserver.lv> - 3.4.6-1
- Update to 3.4.6

* Sun Oct 29 2023 Oleg Girko <ol@infoserver.lv> - 3.4.4-1
- Update to 3.4.4

* Mon Oct 23 2023 Oleg Girko <ol@infoserver.lv> - 3.4.3-1
- Update to 3.4.3

* Tue Oct 10 2023 Oleg Girko <ol@infoserver.lv> - 3.4.1-1
- Update to 3.4.1

* Mon Oct 02 2023 Oleg Girko <ol@infoserver.lv> - 3.3.24-1
- Update to 3.3.24
- Don't run autoreconf: we don't apply any patches

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 11 2022 Oleg Girko <ol@infoserver.lv> - 3.1.0-1
- Update to 3.1.0

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.3-4
- Rebuild for gsl-2.7.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Oleg Girko <ol@infoserver.lv> - 3.0.3-2
- Add patch to make configure work on all Linux architectures
* Wed Jan 26 2022 Oleg Girko <ol@infoserver.lv> - 3.0.3-1
- Update to 3.0.3
- Fix download URL to use HTTPS
- Use more specific file names in %%files section
- Don't put license files in docs
- Require gcc for build explicitly
* Mon Jan 24 2022 Oleg Girko <ol@infoserver.lv> - 3.0.2-1
- Update to 3.0.2
* Wed Jan 12 2022 Oleg Girko <ol@infoserver.lv> - 3.0.0-3
- Fix typo (source specified twice)
* Wed Jan 12 2022 Oleg Girko <ol@infoserver.lv> - 3.0.0-2
- Use libquadmath only on architectures that have it
* Wed Jan 12 2022 Oleg Girko <ol@infoserver.lv> - 3.0.0-1
- Initial package
