%global pkgname  forms

Name:           gap-pkg-%{pkgname}
Version:        1.2.8
Release:        2%{?dist}
Summary:        Sesquilinear and quadratic forms

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/forms/
Source0:        https://github.com/gap-packages/forms/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core%{?_isa}

%description
This package provides:
- A way to create and use sesquilinear and quadratic forms on finite
  vector spaces.
- An operation which finds an isometry between two forms of the same type
- An operation which returns the forms left invariant by a matrix group.

%package doc
Summary:        Forms documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
ln -s %{_gap_dir}/doc ../../doc
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{*.sh,README}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.2.8-2
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 1.2.8-1
- Version 1.2.8

* Mon Mar 28 2022 Jerry James <loganjerry@gmail.com> - 1.2.7-1
- Version 1.2.7
- New URLs

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul  6 2019 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Initial RPM
