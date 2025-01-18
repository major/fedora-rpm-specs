%global soname 6

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

Name:           crest
Version:        2.12
Release:        9%{?dist}
Summary:        Conformer-Rotamer Ensemble Sampling Tool: a driver for the xtb program
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://xtb-docs.readthedocs.io/en/latest/crest.html
Source0:        https://github.com/grimme-lab/crest/archive/v%{version}/crest-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  %{blaslib}-devel
# To generate man pages
BuildRequires:  rubygem-asciidoctor

# xtb may be required to run tests
BuildRequires:  xtb
Requires:       xtb

# xtb is not available on s390x
ExcludeArch:    s390x

%description
CREST is an utility/driver program for the xtb program. Originally it
was designed as conformer sampling program, hence the abbreviation
Conformer-Rotamer Ensemble Sampling Tool, but now offers also some
utility functions for calculations with the GFNn-xTB
methods. Generally the program functions as an IO based OMP scheduler
(i.e., calculations are performed by the xtb program) and tool for the
creation and analysation of structure ensembles.

The key procedure implemented in CREST is a conformational search
workflow abbreviated as iMTD-GC. The iMTD-GC workflow generates
conformer/rotamer ensembles (CREs) by extensive metadynamic sampling
(MTD) based on, with an additional genetic z-matrix crossing (GC) step
at the end. Other standalone functionalities that are included in
CREST are parallel optimization and screening functions for GFNn–xTB,
the function to sort (e.g. for NMR equivalencies) externally created
ensembles, and some automated procedures for the protonation,
deprotonation and tautomerization of structures.

The main publication for the CREST program can be found at
Phys. Chem. Chem. Phys., 2020, 22, 7169-7192.

%prep
%setup -q

%build
%meson -Dla_backend=custom -Dcustom_libraries=%{blaslib}%{blasvar}
%meson_build

%install
%meson_install

%check
%meson_test -t 2000

%files
%license COPYING COPYING.LESSER
%doc README.md
%{_bindir}/crest
%{_mandir}/man1/crest.1.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.12-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 24 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.12-1
- Update to 2.12.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.11.2-1
- Update to 2.11.2.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 15 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.11-2
- Review fixes.

* Wed May 12 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.11-1
- Initial release.

