%global pkgname qpa

Name:           gap-pkg-%{pkgname}
Version:        1.34
Release:        5%{?dist}
Summary:        GAP package for quivers and path algebras

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://folk.ntnu.no/oyvinso/QPA/
Source0:        https://github.com/gap-packages/qpa/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-gbnp
BuildRequires:  tex(beamer.cls)
BuildRequires:  tex(pcrr8t.tfm)
BuildRequires:  tex(textpos.sty)
BuildRequires:  tex(xy.sty)

Requires:       gap-pkg-gbnp

%description
This package carries out computations for finite dimensional quotients
of path algebras over the fields that are available in GAP.  QPA stands
for "Quivers and Path Algebras".

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
# XY: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        QPA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

cd doc/gap-days-lectures
pdflatex lecture1
pdflatex lecture1
pdflatex lecture2
pdflatex lecture2
pdflatex lecture3
pdflatex lecture3
pdflatex lecture4a
pdflatex lecture4a

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g examples lib tst version %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs
%gap_copy_docs -d doc/gap-days-lectures

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGES README
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/examples/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.34-3
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.34-2
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.34-2
- Update for gap 4.12.0
- Convert License tag to SPDX

* Wed Aug  3 2022 Jerry James <loganjerry@gmail.com> - 1.34-1
- Version 1.34

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Jerry James <loganjerry@gmail.com> - 1.33-1
- Version 1.33

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 2021 Jerry James <loganjerry@gmail.com> - 1.32-1
- Version 1.32
- Drop upstreamed -issymmetricalgebra patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Jerry James <loganjerry@gmail.com> - 1.31-1
- Version 1.31
- Drop upstreamed -doc patch
- Add -issymmetricalgebra patch

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 Jerry James <loganjerry@gmail.com> - 1.30-2
- Drop broken "gap-pkg-core" Requires

* Sat Mar 14 2020 Jerry James <loganjerry@gmail.com> - 1.30-1
- Initial RPM
