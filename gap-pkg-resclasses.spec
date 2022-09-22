%global pkgname resclasses

Name:           gap-pkg-%{pkgname}
Version:        4.7.3
Release:        1%{?dist}
Summary:        Set-theoretic computations with Residue Classes

License:        GPLv2+
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-utils

Requires:       gap-core
Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-utils

Recommends:     gap-pkg-io

%description
ResClasses is a GAP package for set-theoretic computations with residue
classes of the integers and a couple of other rings.  The class of sets
which ResClasses can deal with includes the open and the closed sets in
the topology on the respective ring which is induced by taking the set
of all residue classes as a basis, as far as the usual restrictions
imposed by the finiteness of computing resources permit this.

%package doc
Summary:        ResClasses documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
gap < makedoc.g
rm -f ../../doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{.package_note*,CHANGES,LICENSE,README}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Mon Aug  1 2022 Jerry James <loganjerry@gmail.com> - 4.7.3-1
- Version 4.7.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Jerry James <loganjerry@gmail.com> - 4.7.2-1
- New upstream version
- Update the source URL again
- Package the license file

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 4.7.1-5
- Rebuild for gap 4.10.0
- New URLs
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 4.7.1-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 17 2017 Jerry James <loganjerry@gmail.com> - 4.6.0-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun  3 2016 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- New upstream version

* Fri May 13 2016 Jerry James <loganjerry@gmail.com> - 4.4.2-1
- Initial RPM
