%global pkgname fr

Name:           gap-pkg-%{pkgname}
Version:        2.4.12
Release:        2%{?dist}
Summary:        Computations with functionally recursive groups

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/fr/
Source0:        https://github.com/gap-packages/fr/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-fga
BuildRequires:  gap-pkg-gbnp
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-lpres
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polycyclic

# "cat" is invoked
Requires:       coreutils
Requires:       gap-pkg-fga
Requires:       gap-pkg-io
Requires:       gap-pkg-polycyclic

Recommends:     gap-pkg-gbnp
Recommends:     gap-pkg-lpres
Recommends:     gap-pkg-nq
Recommends:     graphviz

%description
This package implements Functionally Recursive and Mealy automata in
GAP.  These objects can be manipulated as group elements, and various
specific commands allow their manipulation as automorphisms of infinite
rooted trees.  Permutation quotients can also be created and manipulated
as standard GAP groups or semigroups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        FR documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
# Build the documentation
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap guest tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc BUGS CHANGES README.md TODO
%license COPYING
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.4.12-2
- Update for split GAP directories

* Mon Dec  5 2022 Jerry James <loganjerry@gmail.com> - 2.4.12-1
- Version 2.4.12

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.4.11-1
- Clarify license of the doc subpackage

* Sat Oct 22 2022 Jerry James <loganjerry@gmail.com> - 2.4.11-1
- Version 2.4.11

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.4.10-2
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.4.10-1
- Convert License tag to SPDX

* Wed Aug 10 2022 Jerry James <loganjerry@gmail.com> - 2.4.10-1
- Version 2.4.10

* Mon Aug  1 2022 Jerry James <loganjerry@gmail.com> - 2.4.9-1
- Version 2.4.9

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 16 2022 Jerry James <loganjerry@gmail.com> - 2.4.8-1
- Version 2.4.8

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Jerry James <loganjerry@gmail.com> - 2.4.7-1
- Version 2.4.7
- Drop -noassert patch, underlying issue fixed upstream

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Jerry James <loganjerry@gmail.com> - 2.4.6-1
- Initial RPM
