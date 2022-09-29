%global pkgname smallgrp

Name:           gap-pkg-%{pkgname}
Version:        1.5
Release:        3%{?dist}
Summary:        Small groups library

License:        Artistic-2.0
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  parallel

Requires:       gap-core

%description
The Small Groups library gives access to all groups of certain "small"
orders.  The groups are sorted by their orders and they are listed up to
isomorphism; that is, for each of the available orders a complete and
irredundant list of isomorphism type representatives of groups is given.

%package doc
Summary:        Small groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Fix permissions
chmod a-x id9/idgrp9.g id10/idgrp10.g

%build
export LC_ALL=C.UTF-8
gap makedoc.g

# Compress large group files
parallel %{?_smp_mflags} --no-notice gzip --best -f ::: id*/* small*/*

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g gap id* small* tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc CHANGES.md README README.md
%license COPYRIGHT.md LICENSE
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.5-3
- Update for gap 4.12.0
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr  7 2022 Jerry James <loganjerry@gmail.com> - 1.5-1
- Version 1.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- Version 1.4.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- New upstream version
- Drop upstreamed -ref patch

* Sat Sep 21 2019 Jerry James <loganjerry@gmail.com> - 1.4-1
- New upstream version
- The -ref patch now fixes a different bad reference

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Jerry James <loganjerry@gmail.com> - 1.3-2
- Remove spurious executable bits

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.3-1
- Initial RPM
