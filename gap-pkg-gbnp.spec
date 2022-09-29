%global pkgname gbnp

Name:           gap-pkg-%{pkgname}
Version:        1.0.5
Release:        3%{?dist}
Summary:        Computing Gröbner bases of noncommutative polynomials

License:        LGPL-2.1-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/gbnp/
Source0:        https://github.com/gap-packages/gbnp/archive/v%{version}/GBNP-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  make
BuildRequires:  tex-urlbst

Requires:       gap-core

%description
GBNP provides GAP algorithms for computing Gröbner bases of
non-commutative polynomials with coefficients from a field implemented in
GAP, and some variations, such as a weighted and truncated version and a
tracing facility.

The word algorithm is interpreted loosely: in general one cannot expect
such an algorithm to terminate, as it would imply solvability of the
word problem for finitely presented (semi)groups.

%package doc
Summary:        GBNP documentation and examples
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

# Help GAP find its files
sed -i 's,\\\\\\\(.*\) ,"%{gap_dir}\1",;s/eval //' etc/workspace
sed -i 's,\\\\;,%{gap_dir};,' etc/makedepend etc/workspace
sed -i "s,-r,-l '%{_builddir}/%{pkgname}-%{version}/build;' &,;s/eval //" \
    etc/gapscript

%build
export LC_ALL=C.UTF-8
%make_build doc

%install
# We install test files for use by GAP's internal test suite runner.
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
cp -a doc/{articles,examples,nmo} %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
rm %{buildroot}%{gap_dir}/pkg/%{pkgname}/lib/{gbnp-uses.sed,OPTIONS,STRUCTURE,TODO}
rm %{buildroot}%{gap_dir}/pkg/%{pkgname}/tst/{.depend,GNUmakefile,txt2xml.sed}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc Changelog README.md
%license COPYRIGHT doc/LGPL
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.0.5-3
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.0.5-2
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 10 2022 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- Version 1.0.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  1 2021 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- Version 1.0.4
- New URLs
- Drop upstreamed -doc patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.0.3-9
- Rebuild for gap 4.10.0
- Add -doc patch to fix malformed LaTeX

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul  1 2016 Jerry James <loganjerry@gmail.com> - 1.0.3-3
- Make -doc own the main package directory
- Do not package the .tex source files
- Explain why the test filees are installed

* Mon Jun  6 2016 Jerry James <loganjerry@gmail.com> - 1.0.3-2
- Add a -doc subpackage
- Exclude more files from the binary RPM

* Fri May 27 2016 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Initial RPM
