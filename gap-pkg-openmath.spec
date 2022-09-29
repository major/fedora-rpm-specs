%global pkgname openmath
%global upname  OpenMath

# When bootstrapping a new architecture, there is no gap-pkg-scscp package yet.
# However, we only need that package to build documentation; it needs this
# package to function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode (the documentation has broken links)
# 2. Build gap-pkg-scscp
# 3. Build this package in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        11.5.1
Release:        3%{?dist}
Summary:        Import and export of OpenMath objects for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/openmath/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{upname}-%{version}.tar.gz

%global _docdir_fmt %{name}

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-io
%if %{without bootstrap}
BuildRequires:  gap-pkg-scscp-doc
%endif

Requires:       gap-pkg-io

%description
This package provides an OpenMath phrasebook for GAP.  It allows GAP
users to import and export mathematical objects encoded in OpenMath, for
the purpose of exchanging them with other OpenMath-enabled applications.
For details about the OpenMath encoding, see https://openmath.org/.

%package doc
Summary:        OpenMath documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%if %{without bootstrap}
Requires:       gap-pkg-scscp-doc
%endif

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{upname}-%{version}

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{gap_dir}/doc ../../doc
mkdir ../pkg
ln -s ../%{upname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{upname}/doc
cp -a *.g cds gap hasse private tst %{buildroot}%{gap_dir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc CHANGES README.md
%license COPYING
%{gap_dir}/pkg/%{upname}/
%exclude %{gap_dir}/pkg/%{upname}/doc/

%files doc
%doc examples
%docdir %{gap_dir}/pkg/%{upname}/doc/
%{gap_dir}/pkg/%{upname}/doc/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 11.5.1-3
- Update for gap 4.12.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 30 2022 Jerry James <loganjerry@gmail.com> - 11.5.1-1
- Version 11.5.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Jerry James <loganjerry@gmail.com> - 11.5.0-1
- Version 11.5.0
- Drop upstreamed -test patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 11.4.2-7
- Rebuild in non-bootstrap mode

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 11.4.2-6
- Rebuild for gap 4.10.0
- Add -test patch
- Add -doc subpackage
- Build in bootstrap mode

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr  1 2017 Jerry James <loganjerry@gmail.com> - 11.4.2-1
- New upstream version
- New URLs

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 21 2016 Jerry James <loganjerry@gmail.com> - 11.3.1-1
- Initial RPM
