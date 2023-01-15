%global pkgname ferret

Name:           gap-pkg-%{pkgname}
Version:        1.0.9
Release:        2%{?dist}
Summary:        Backtracking search in permutation groups

# YAPB++/simple_graph/gason is MIT
# YAPB++/source/library/fnv_hash.hpp is Public Domain
# However, none of those files are part of the final binary.
License:        MPL-2.0
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://gap-packages.github.io/ferret/
Source0:        https://github.com/gap-packages/ferret/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
Ferret is a reimplementation of parts of Jeffery Leon's Partition
Backtrack framework in C++, with extensions including:

- Ability to intersect many groups simultaneously.
- Improved refiners based on orbital graphs.

This package currently supports:

- Group intersection.
- Stabilizing many structures including sets, sets of sets, graphs,
  sets of tuples and tuples of sets.

This package can be used by users in two ways:

- When the package is loaded many built-in GAP functions such as
  'Intersection' and 'Stabilizer' are replaced with more optimized
  implementations.  This requires no changes to existing code.

- The function 'Solve' provides a unified interface to accessing
  all the functionality of the package directly.

%package doc
# The content is MPL-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Ferret documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{gap_archdir}
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin lib tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc README
%license LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.0.9-2
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.0.9-1
- Clarify license of the doc subpackage

* Wed Oct 19 2022 Jerry James <loganjerry@gmail.com> - 1.0.9-1
- Version 1.0.9

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.0.8-4
- Update for gap 4.12.0

* Wed Aug 17 2022 Jerry James <loganjerry@gmail.com> - 1.0.8-3
- Convert License tag to SPDX

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 1.0.8-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  1 2022 Jerry James <loganjerry@gmail.com> - 1.0.8-1
- Version 1.0.8

* Wed Mar 30 2022 Jerry James <loganjerry@gmail.com> - 1.0.7-1
- Version 1.0.7
- Make the -doc subpackage noarch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Jerry James <loganjerry@gmail.com> - 1.0.6-1
- Version 1.0.6

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 10 2021 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- Version 1.0.5

* Tue Feb  9 2021 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- Version 1.0.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3
- Replace GPLv2+ with MPLv2.0 in the License field

* Thu Apr 30 2020 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- Initial RPM
