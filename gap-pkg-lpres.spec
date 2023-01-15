%global pkgname lpres

Name:           gap-pkg-%{pkgname}
Version:        1.0.3
Release:        4%{?dist}
Summary:        Nilpotent quotients of L-presented groups

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/lpres/
Source0:        https://github.com/gap-packages/lpres/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-ace-doc
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-fga
BuildRequires:  gap-pkg-nq-doc
BuildRequires:  gap-pkg-polycyclic-doc

Requires:       gap-pkg-fga
Requires:       gap-pkg-polycyclic

Recommends:     gap-pkg-ace
Recommends:     gap-pkg-autpgrp
Recommends:     gap-pkg-nq

%description
The lpres package provides a first construction of finitely L-presented
groups and a nilpotent quotient algorithm for L-presented groups.  The
features of this package include:
- creating an L-presented group as a new gap object,
- computing nilpotent quotients of L-presented groups and epimorphisms
  from the L-presented group onto its nilpotent quotients,
- computing the abelian invariants of an L-presented group,
- computing finite-index subgroups and if possible their L-presentation,
- approximating the Schur multiplier of L-presented groups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        LPRES documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-polycyclic-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
gap -l "$PWD/..;" makedoc.g

# A second BiBTeX run is needed to resolve \cite within a reference
cd doc
bibtex lpres
pdflatex -interaction=batchmode lpres
pdflatex -interaction=batchmode lpres
mv lpres.pdf manual.pdf
cd -

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc README.md
%license COPYING
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.0.3-4
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.0.3-3
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.0.3-3
- Update for gap 4.12.0
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Jerry James <loganjerry@gmail.com> - 0.4.3-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 0.4.2-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar  3 2017 Jerry James <loganjerry@gmail.com> - 0.4.1-1
- New upstream version

* Fri Feb 24 2017 Jerry James <loganjerry@gmail.com> - 0.4.0-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> - 0.3.1-1
- New upstream version

* Fri Sep 16 2016 Jerry James <loganjerry@gmail.com> - 0.3.0-1
- Initial RPM
