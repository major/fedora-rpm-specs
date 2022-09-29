%global pkgname tomlib

Name:           gap-pkg-%{pkgname}
Version:        1.2.9
Release:        8%{?dist}
Summary:        GAP Table of Marks package

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  parallel

Requires:       gap-pkg-atlasrep

Recommends:     gap-pkg-ctbllib

%description
This package provides access to several hundred tables of marks of
almost simple groups and their maximal subgroups.

%package doc
Summary:        Table of Marks documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
# Build the documentation
export LC_ALL=C.UTF-8
gap makedoc.g

# Compress large tables of marks
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/*.tom

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g data gap htm tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc README.md
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
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.2.9-8
- Update for gap 4.12.0
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Jerry James <loganjerry@gmail.com> - 1.2.9-1
- New upstream version
- Drop upstreamed -doc patch
- Use the %%license macro

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 1.2.8-2
- Remove unneeded hidden files

* Thu May 16 2019 Jerry James <loganjerry@gmail.com> - 1.2.8-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.2.7-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov  9 2016 Jerry James <loganjerry@gmail.com> - 1.2.6-1
- New upstream version

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.2.5-7
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.2.5-5
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 29 2015 Jerry James <loganjerry@gmail.com> - 1.2.5-3
- Compress with _smp_mflags

* Thu Jan 29 2015 Jerry James <loganjerry@gmail.com> - 1.2.5-2
- Compress the tables in parallel

* Fri Jan 16 2015 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Initial RPM
