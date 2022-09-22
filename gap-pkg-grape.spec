%global pkgname grape

Name:           gap-pkg-%{pkgname}
Version:        4.8.5
Release:        4%{?dist}
Summary:        GRaph Algorithms using PErmutation groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/grape/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Fedora-only patch: unbundle nauty
Patch0:         %{name}-nauty.patch

BuildArch:      noarch
BuildRequires:  gap-devel
BuildRequires:  nauty
BuildRequires:  tth

Requires:       gap-core%{?_isa}
Requires:       nauty

%description
GRAPE is a package for computing with graphs and groups, and is
primarily designed for constructing and analyzing graphs related to
groups, finite geometries, and designs.

%package doc
Summary:        GRAPE documentation and examples
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

# Remove nauty sources so we use the system version
rm -fr nauty22

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/etc ../../etc
ln -s %{_gap_dir}/doc ../../doc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{doc/make_doc,CHANGES.md,configure,gpl.txt,Makefile.in,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES.md README.md
%license gpl.txt
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 4.8.5-4
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Jerry James <loganjerry@gmail.com> - 4.8.5-1
- Version 4.8.5

* Fri Mar  5 2021 Jerry James <loganjerry@gmail.com> - 4.8.4-1
- Version 4.8.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  9 2019 Jerry James <loganjerry@gmail.com> - 4.8.3-1
- Version 4.8.3
- Add -nauty patch and convert main package to noarch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 4.8.2-1
- New upstream version

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 4.8.1-1
- New upstream version
- New URLs
- Add a -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Jerry James <loganjerry@gmail.com> - 4.7-7
- Build as an archful package instead of noarch because the nauty symlink has
  to be stored in a directory with an arch-specific name

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 4.7-4
- Build for nauty now that it is available

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 4.7-3
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Jerry James <loganjerry@gmail.com> - 4.7-1
- New upstream version
- Drop upstreamed bliss patch

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 4.6.1-2
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures
- New version of bliss patch from upstream

* Mon Oct 19 2015 Jerry James <loganjerry@gmail.com> - 4.6.1-1
- Initial RPM
