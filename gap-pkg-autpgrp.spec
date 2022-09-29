%global pkgname autpgrp

Name:           gap-pkg-%{pkgname}
Version:        1.11
Release:        2%{?dist}
Summary:        Compute the automorphism group of a p-Group in GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/autpgrp/
Source0:        https://github.com/gap-packages/autpgrp/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  tth

Requires:       gap-core

%description
The AutPGrp package introduces a new function to compute the
automorphism group of a finite p-group.  The underlying algorithm is a
refinement of the methods described in O'Brien (1995).  In particular,
this implementation is more efficient in both time and space
requirements and hence has a wider range of applications than the ANUPQ
method.  Our package is written in GAP code and it makes use of a
number of methods from the GAP library such as the MeatAxe for matrix
groups and permutation group functions.  We have compared our method to
the others available in GAP.  Our package usually out-performs all but
the method designed for finite abelian groups.  We note that our method
uses the small groups library in certain cases and hence our algorithm
is more effective if the small groups library is installed.

%package doc
Summary:        Automorphism group documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Use the system GAP macro file instead of the bundled version
rm -f doc/gapmacro.tex
ln -s %{gap_dir}/doc/gapmacro.tex doc

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{gap_dir}/etc ../../etc
ln -s %{gap_dir}/doc ../../doc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g gap htm tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc README CHANGES.md
%license LICENSE
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/
%exclude %{gap_dir}/pkg/%{pkgname}/htm/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%docdir %{gap_dir}/pkg/%{pkgname}/htm/
%{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/htm/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.11-2
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.11-1
- Convert License tag to SPDX

* Fri Aug  5 2022 Jerry James <loganjerry@gmail.com> - 1.11-1
- Version 1.11

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Jerry James <loganjerry@gmail.com> - 1.10.2-1
- Version 1.10.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 1.10.1-1
- New upstream version

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.10-3
- Rebuild for gap 4.10.0
- Add a -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.10-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Jerry James <loganjerry@gmail.com> - 1.9-1
- New upstream version
- New URLs
- Add check script

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 26 2016 Jerry James <loganjerry@gmail.com> - 1.8-1
- New upstream version

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.6-5
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.6-3
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Jerry James <loganjerry@gmail.com> - 1.6-1
- Initial RPM (bz 1205777)
