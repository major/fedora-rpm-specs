%global pkgname ace

Name:           gap-pkg-%{pkgname}
Version:        5.6.2
Release:        4%{?dist}
Summary:        Advanced Coset Enumerator

License:        MIT
ExclusiveArch:  %{gap_arches}
URL:            https://gap-packages.github.io/ace/
Source0:        https://github.com/gap-packages/ace/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  tth

Requires:       gap-core%{?_isa}

%description
The ACE package provides a mechanism to replace GAP's usual Todd-Coxeter
coset enumerator by ACE, so that functions that behind the scenes use
coset enumeration will use the ACE enumerator.  The ACE enumerator may
also be used explicitly; both non-interactively and interactively.
However the package is used, a plethora of options and strategies are
available to assist the user in avoiding incomplete coset enumerations.

%package doc
# The content is MIT.  The remaining licenses cover the various fonts embedded
# in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        MIT AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        Advanced Coset Enumerator documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated script.  Do not use %%configure.
./configure %{gap_archdir}
%make_build

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/etc ../../etc
make doc
rm -f ../../{doc,etc}

# Package PDF instead of PostScript
pushd standalone-doc
ps2pdf ace3001.ps ace3001.pdf
popd

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin examples gap htm res-examples tst VERSION \
   %{buildroot}%{gap_archdir}/pkg/%{pkgname}
rm %{buildroot}%{gap_archdir}/pkg/%{pkgname}/gap/CHANGES
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/
%exclude %{gap_archdir}/pkg/%{pkgname}/examples/
%exclude %{gap_archdir}/pkg/%{pkgname}/htm/
%exclude %{gap_archdir}/pkg/%{pkgname}/res-examples/

%files doc
%doc standalone-doc/ace3001.pdf
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/examples/
%docdir %{gap_archdir}/pkg/%{pkgname}/htm/
%docdir %{gap_archdir}/pkg/%{pkgname}/res-examples/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/examples/
%{gap_archdir}/pkg/%{pkgname}/htm/
%{gap_archdir}/pkg/%{pkgname}/res-examples/

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 5.6.2-2
- Update for split GAP directories

* Fri Jan  6 2023 Jerry James <loganjerry@gmail.com> - 5.6.2-1
- Version 5.6.2

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 5.6.1-1
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 5.6.1-1
- Version 5.6.1
- Drop upstreamed patches
- Update for gap 4.12.0

* Tue Aug  2 2022 Jerry James <loganjerry@gmail.com> - 5.5-1
- Version 5.5
- Add -utsname patch to remove coreutils dependency

* Sat Jul 23 2022 Jerry James <loganjerry@gmail.com> - 5.4-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 10 2022 Jerry James <loganjerry@gmail.com> - 5.4-1
- Version 5.4
- Add -noreturn and -uninit patches for code cleanliness

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 5.3-2
- Rebuild for gap 4.11.0

* Wed Feb 12 2020 Jerry James <loganjerry@gmail.com> - 5.3-1
- Version 5.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 5.2-9
- Rebuild for changed bin dir name in gap 4.10.1

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 5.2-8
- Rebuild for gap 4.10.0
- Package PDF documentation instead of PostScript

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Jerry James <loganjerry@gmail.com> - 5.2-1
- Initial RPM
