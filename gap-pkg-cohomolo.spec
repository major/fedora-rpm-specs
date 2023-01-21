%global pkgname cohomolo

Name:           gap-pkg-%{pkgname}
Version:        1.6.11
Release:        3%{?dist}
Summary:        Cohomology groups of finite groups on finite modules

License:        GPL-2.0-or-later
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://gap-packages.github.io/cohomolo/
Source0:        https://github.com/gap-packages/cohomolo/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Add missing shebangs
Patch0:         %{name}-shebang.patch
# Fix all -Wlto-type-mismatch warnings
Patch1:         %{name}-lto.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tth

Requires:       gap-core

%description
This package may be used to perform certain cohomological calculations
on a finite permutation group G.  The following properties of G can be
computed:

1. The p-part Mul_p of the Schur multiplier Mul of G, and a presentation
   of a covering extension of Mul_p by G, for a specified prime p;

2. The dimensions of the first and second cohomology groups of G acting
   on a finite dimensional KG-module M, where K is a field of prime
   order; and

3. Presentations of split and nonsplit extensions of M by G.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Cohomolo documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

# Fix paths
sed -i 's,\.\./\.\./\.\./,%{gap_libdir}/,' doc/make_doc

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{gap_archdir}

# Build the binaries
%make_build

# Build the documentation
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm ../../doc

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/{doc,standalone}
cp -a bin gap htm testdata tst *.g %{buildroot}%{gap_archdir}/pkg/%{pkgname}
cp -a standalone/{data.d,info.d} \
   %{buildroot}%{gap_archdir}/pkg/%{pkgname}/standalone
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/
%exclude %{gap_archdir}/pkg/%{pkgname}/htm/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/htm/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/htm/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.6.11-2
- Update for split GAP directories

* Fri Jan  6 2023 Jerry James <loganjerry@gmail.com> - 1.6.11-1
- Version 1.6.11

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.6.10-4
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.6.10-4
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.6.10-3
- Convert License tag to SPDX

* Sat Jul 23 2022 Jerry James <loganjerry@gmail.com> - 1.6.10-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 30 2022 Jerry James <loganjerry@gmail.com> - 1.6.10-1
- Version 1.6.10
- Drop upstreamed patches 0001 through 0005

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Jerry James <loganjerry@gmail.com> - 1.6.9-1
- Version 1.6.9
- Drop upstreamed -fno-common patch
- Add patch 0006 to fix LTO warnings about mismatched types

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 1.6.8-3
- Rebuild for gap 4.11.0

* Mon Feb  3 2020 Jerry James <loganjerry@gmail.com> - 1.6.8-2
- Add -fno-common patch to fix build with GCC 10
- Add 0001 through 0005 patches to eliminate warnings

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Jerry James <loganjerry@gmail.com> - 1.6.8-1
- Initial RPM
