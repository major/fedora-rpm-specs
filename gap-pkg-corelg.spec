%global pkgname corelg

Name:           gap-pkg-%{pkgname}
Version:        1.56
Release:        2%{?dist}
Summary:        Computation with real Lie groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-singular
BuildRequires:  gap-pkg-sla

Requires:       gap-pkg-sla

Recommends:     gap-pkg-singular

%description
The main object of the CoReLG package is to provide functionality for
computing with real (semi-)simple Lie algebras.

%package doc
Summary:        CoReLG documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Remove spurious executable bits
chmod a-x gap/*

%build
export LC_ALL=C.UTF-8
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{LICENSE,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.56-2
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Jerry James <loganjerry@gmail.com> - 1.56-1
- Version 1.56

* Fri Feb 11 2022 Jerry James <loganjerry@gmail.com> - 1.55-1
- Version 1.55

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Jerry James <loganjerry@gmail.com> - 1.54-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Jerry James <loganjerry@gmail.com> - 1.54-1
- Version 1.54
- Change gap-pkg-singular from Requires to Recommends

* Wed Oct  2 2019 Jerry James <loganjerry@gmail.com> - 1.52-1
- New upstream version
- Add a %%check script

* Thu Sep 19 2019 Jerry James <loganjerry@gmail.com> - 1.51-1
- Initial RPM
