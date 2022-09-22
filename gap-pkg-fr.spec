%global pkgname fr

Name:           gap-pkg-%{pkgname}
Version:        2.4.10
Release:        1%{?dist}
Summary:        Computations with functionally recursive groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-fga
BuildRequires:  gap-pkg-gbnp
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-lpres
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polycyclic

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
Summary:        FR documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
# Build the documentation
export LC_ALL=C.UTF-8
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/scripts
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{.package_note*,BUGS,CHANGES,COPYING,README.md,TODO}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc BUGS CHANGES README.md TODO
%license COPYING
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
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
