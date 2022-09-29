%global pkgname fining

Name:           gap-pkg-%{pkgname}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Finite incidence geometry

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://www.fining.org/
Source0:        https://github.com/gap-packages/FinInG/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-cvec
BuildRequires:  gap-pkg-design
BuildRequires:  gap-pkg-forms
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-orb
BuildRequires:  tex(makecell.sty)

Requires:       gap-pkg-cvec
Requires:       gap-pkg-forms
Requires:       gap-pkg-genss
Requires:       gap-pkg-grape
Requires:       gap-pkg-orb

Recommends:     gap-pkg-design

%description
FinInG is a GAP package for computation in Finite Incidence Geometry
developed by John Bamberg, Anton Betten, Philippe Cara, Jan De Beule,
Michel Lavrauw and Max Neunhoeffer.  It provides functionality:
- to create and explore finite incidence structures, such as finite
  projective spaces, finite classical polar spaces, generalized
  polygons, coset geometries, finite affine spaces, and many more;
- to explore algebraic varieties in finite projective and finite affine
  spaces;
- that deals with the automorphism groups of incidence structures, and
  functionality integrating these automorphism groups with the group
  theoretical capabilities of GAP;
- to explore various morphisms between finite incidence structures.

%package doc
Summary:        FinInG documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g examples lib tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc README.md
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/
%exclude %{gap_dir}/pkg/%{pkgname}/examples/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%docdir %{gap_dir}/pkg/%{pkgname}/examples/
%{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/examples/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- Version 1.5.1
- Drop upstreamed patches
- New source URL
- Add dependency on gap-pkg-orb
- Update for gap 4.12.0

* Wed Aug 17 2022 Jerry James <loganjerry@gmail.com> - 1.4.1-7
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Initial RPM
