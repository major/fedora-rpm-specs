%global soname 6

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

Name:           crest
Version:        3.0.2
Release:        1%{?dist}
Summary:        Conformer-Rotamer Ensemble Sampling Tool: a driver for the xtb program
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://crest-lab.github.io/crest-docs/
Source0:        https://github.com/crest-lab/crest/archive/v%{version}/crest-%{version}.tar.gz

# Do not use "true" as a function name
Patch0:         https://github.com/crest-lab/crest/pull/397.patch
# Upstream forces a fully static executable, which does not work on Fedora
Patch1:         crest-3.0.2-no-static.patch
# gfnff_dump_sasa is not guarded by WITH_GFNFF, so it does not compile when the
# GFN-FF subproject is disabled
Patch2:         crest-3.0.2-no-subprojects.patch
# Upstream disabled the man page build, but the sources are still shipped
Patch3:         crest-3.0.2-manpage.patch
# The unit tests are only wired up in the CMake build; add the missing meson
# recipe, and fix the format statements in the "feature not compiled" stubs
Patch4:         crest-3.0.2-enable-tests.patch
# Don't use hostname
Patch5:         crest-3.0.2-no-git.patch

BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  %{blaslib}-devel
BuildRequires:  toml-f-devel
# For the unit tests
BuildRequires:  test-drive-devel
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
%autosetup -p1

%build
# tblite, gfn0, gfnff and lwoniom are not packaged in Fedora, and upstream only
# ships them as git submodules, so the corresponding features are turned off.
# toml-f is taken from the system.
%meson -Dla_backend=custom -Dcustom_libraries=%{blaslib}%{blasvar} \
    -DWITH_TBLITE=false -DWITH_GFN0=false -DWITH_GFNFF=false \
    -DWITH_LWONIOM=false -DWITH_TOMLF=true
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
* Wed Oct 28 2026 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2.

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 31 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.12-1
- Fix FTBFS on rawhide.

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

