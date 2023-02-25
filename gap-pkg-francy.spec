%global pkgname francy

Name:           gap-pkg-%{pkgname}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Framework for interactive discrete mathematics

License:        MIT
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://gap-packages.github.io/francy/
Source0:        https://github.com/gap-packages/francy/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Fix unknown entity warnings
# https://github.com/gap-packages/francy/pull/90
Patch0:         0001-Fix-unknown-entity-warnings.patch

BuildRequires:  elinks
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-jupyterkernel
BuildRequires:  xdg-utils

Requires:       gap-pkg-jupyterkernel
Requires:       xdg-utils

%description
Francy is a package for GAP and provides a framework for Interactive
Discrete Mathematics.

Unlike xgap, Francy is not linked with any GUI framework and instead,
this package generates a semantic model that can be used to produce a
graphical representation using any other framework / language.

There is a JavaScript implementation of the graphical representation
that works on Jupyter, embedded in a Web page or as a Desktop Application
(e.g. using electron).

%package doc
# The content is MIT.  The remaining licenses cover the various fonts embedded
# in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MIT AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Francy documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

# Call xdg-open instead of open
sed -i.orig 's/"open "/"xdg-open "/' gap/canvas.gi
touch -r gap/canvas.gi.orig gap/canvas.gi
rm gap/canvas.gi.orig

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g examples gap notebooks schema tst \
   %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
# The canvas test always fails.  One test in graph.tst always fails.
# https://github.com/gap-packages/francy/issues/91
rm %{buildroot}%{gap_libdir}/pkg/francy/tst/canvas.tst
sed -i '/GetLinks/,+1d' %{buildroot}%{gap_libdir}/pkg/francy/tst/graph.tst
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g
cp -p tst/{canvas,graph}.tst %{buildroot}%{gap_libdir}/pkg/francy/tst

%files
%doc README.md
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/examples/
%exclude %{gap_libdir}/pkg/%{pkgname}/notebooks/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%docdir %{gap_libdir}/pkg/%{pkgname}/notebooks/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/notebooks/

%changelog
* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Version 2.0.0
- Add patch to fix unknown entity warnings
- Package the notebooks and scheme directories
- Work around tests that expect an exact value for a random UUID

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.2.5-2
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Version 1.2.5
- Drop upstreamed -test patch
- Update for gap 4.12.0

* Mon Jul 25 2022 Jerry James <loganjerry@gmail.com> - 1.2.4-8
- Add -test patch to fix the tests
- Invoke xdg-open instead of open
- BR elinks for the tests

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 1.2.4-1
- New upstream version

* Wed Mar 27 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- Initial RPM
