%global pkgname singular

Name:           gap-pkg-%{pkgname}
Version:        2022.09.23
Release:        1%{?dist}
Summary:        GAP interface to Singular

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Adapt to changed output in Singular 4.2.x
# https://github.com/gap-packages/singular/issues/7
Patch0:         %{name}-test.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-guava-doc
BuildRequires:  Singular

Requires:       gap-core
Requires:       Singular

%description
This package contains a GAP interface to the computer algebra system
Singular.

%package doc
Summary:        Singular documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-guava-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g contrib gap lib tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
rm %{buildroot}%{gap_dir}/pkg/%{pkgname}/gap/todo
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/
%exclude %{gap_dir}/pkg/%{pkgname}/lib/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%docdir %{gap_dir}/pkg/%{pkgname}/lib/
%{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/lib/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2022.09.23-1
- Version 2022.09.23
- Update for gap 4.12.0
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 28 2021 Jerry James <loganjerry@gmail.com> - 2020.12.18-3
- Add -test patch to adapt to Singular 4.2.x

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Jerry James <loganjerry@gmail.com> - 2020.12.18-1
- Version 2020.12.18
- Drop upstreamed -ref patch

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.10.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.10.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  2 2019 Jerry James <loganjerry@gmail.com> - 2019.10.01-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.02.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun  8 2019 Jerry James <loganjerry@gmail.com> - 2019.02.22-1
- Initial RPM
