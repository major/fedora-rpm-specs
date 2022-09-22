%global pkgname lpres

Name:           gap-pkg-%{pkgname}
Version:        1.0.3
Release:        2%{?dist}
Summary:        Nilpotent quotients of L-presented groups

License:        GPLv2+
URL:            https://gap-packages.github.io/lpres/
Source0:        https://github.com/gap-packages/lpres/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-ace-doc
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-fga
BuildRequires:  gap-pkg-nq-doc
BuildRequires:  gap-pkg-polycyclic-doc

Requires:       gap-core
Requires:       gap-pkg-fga
Requires:       gap-pkg-polycyclic

Recommends:     gap-pkg-ace
Recommends:     gap-pkg-autpgrp
Recommends:     gap-pkg-nq

%description
The lpres package provides a first construction of finitely L-presented
groups and a nilpotent quotient algorithm for L-presented groups.  The
features of this package include:
- creating an L-presented group as a new gap object,
- computing nilpotent quotients of L-presented groups and epimorphisms
  from the L-presented group onto its nilpotent quotients,
- computing the abelian invariants of an L-presented group,
- computing finite-index subgroups and if possible their L-presentation,
- approximating the Schur multiplier of L-presented groups.

%package doc
Summary:        LPRES documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-polycyclic-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
ln -s %{_gap_dir}/pkg/ace ../pkg
ln -s %{_gap_dir}/pkg/nq-* ../pkg
ln -s %{_gap_dir}/pkg/polycyclic-* ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

# Remove the build directory from the documentation
sed -i "s,$PWD/\.\./pkg,../..,g" doc/*.html

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{COPYING,README.md,scripts}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license COPYING
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Jerry James <loganjerry@gmail.com> - 0.4.3-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 0.4.2-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar  3 2017 Jerry James <loganjerry@gmail.com> - 0.4.1-1
- New upstream version

* Fri Feb 24 2017 Jerry James <loganjerry@gmail.com> - 0.4.0-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> - 0.3.1-1
- New upstream version

* Fri Sep 16 2016 Jerry James <loganjerry@gmail.com> - 0.3.0-1
- Initial RPM
