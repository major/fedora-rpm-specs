%global pkgname crime

Name:           gap-pkg-%{pkgname}
Version:        1.6
Release:        2%{?dist}
Summary:        Group cohomology and Massey products

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  perl-generators

Requires:       gap-core

%description
This GAP package computes cohomology rings for finite p-groups using Jon
Carlson's method, both as GAP objects, and also in terms of generators
and relators. It also computes induced homomorphisms on cohomology and
Massey products in the cohomology ring.

%package doc
Summary:        Group cohomology documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{CHANGES,COPYING,README}

%check
export LC_ALL=C.UTF-8

# Do not run the batch.g test.  It never terminates.  The instructions indicate
# it has to be interrupted manually.
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" << EOF
LoadPackage("crime");
GAP_EXIT_CODE(Test("tst/test.tst", rec(compareFunction := "uptowhitespace")));
EOF

%files
%doc CHANGES.md README.md
%license COPYING
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.6-2
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul  7 2022 Jerry James <loganjerry@gmail.com> - 1.6-1
- Remove obsolete character encoding change

* Fri Mar 18 2022 Jerry James <loganjerry@gmail.com> - 1.6-1
- Version 1.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.5-1
- New upstream version with new URLs
- Drop upstreamed -test patch
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Jerry James <loganjerry@gmail.com> - 1.4-2
- Fix License (bz 1583448)

* Sat May 26 2018 Jerry James <loganjerry@gmail.com> - 1.4-1
- Initial RPM
