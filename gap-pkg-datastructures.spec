%global pkgname  datastructures

Name:           gap-pkg-%{pkgname}
Version:        0.2.7
Release:        4%{?dist}
Summary:        Standard data structures for GAP

License:        GPL-2.0-or-later
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Remove an unused function
Patch0:         %{name}-unused.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
The datastructures package aims at providing standard datastructures,
consolidating existing code and improving on it, in particular in view
of HPC-GAP.

The following data structures are provided:
- queues
- doubly linked lists
- heaps
- priority queues
- hashtables
- dictionaries

%package doc
Summary:        Data structures documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{gap_dir}
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g bin gap tst  %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc CHANGES.md README.md
%license COPYRIGHT.md LICENSE
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 0.2.7-4
- Update for gap 4.12.0
- Add -unused patch to silence compiler warnings

* Wed Aug 17 2022 Jerry James <loganjerry@gmail.com> - 0.2.7-3
- Convert License tag to SPDX

* Sun Jul 24 2022 Jerry James <loganjerry@gmail.com> - 0.2.7-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar  3 2022 Jerry James <loganjerry@gmail.com> - 0.2.7-1
- Version 0.2.7
- Drop upstreamed -doc patch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 14 2021 Jerry James <loganjerry@gmail.com> - 0.2.6-1
- Version 0.2.6
- Add -doc patch to fix a broken reference

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 0.2.5-4
- Drop aarch64 workaround

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 0.2.5-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jerry James <loganjerry@gmail.com> - 0.2.5-1
- Version 0.2.5
- Drop upstreamed -doc patch

* Mon Sep 16 2019 Jerry James <loganjerry@gmail.com> - 0.2.4-1
- Initial RPM
