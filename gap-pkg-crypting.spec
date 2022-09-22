%global pkgname  crypting

Name:           gap-pkg-%{pkgname}
Version:        0.10.1
Release:        5%{?dist}
Summary:        Hashes and Crypto in GAP

License:        BSD-3-Clause
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
This package implements some cryptographic primitives.  At the moment
this is a custom implementation of SHA256 and HMAC, which is needed to
sign messages in the Jupyter kernel.

Bindings to a full crypto library are a possibility for the future, and
pull-requests (after discussion) are appreciated.

%package doc
Summary:        Crypting documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated configure script.  Do NOT use %%configure.
./configure %{_gap_dir}
%make_build

# Build the documentation
ln -s %{_gap_dir}/doc ../../doc
gap < makedoc.g
rm -fr ../../doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -p bin/%{_gap_arch}/.libs/crypting.so \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -a doc gap tst *.g %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license COPYRIGHT.md LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 0.10.1-5
- Convert License tag to SPDX

* Sat Jul 23 2022 Jerry James <loganjerry@gmail.com> - 0.10.1-5
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 24 2021 Jerry James <loganjerry@gmail.com> - 0.10.1-1
- Version 0.10.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 0.10-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Jerry James <loganjerry@gmail.com> - 0.10-1
- New upstream version
- Drop upstreamed -ref and -sha256 patches

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 0.9-2
- Rebuild for changed bin dir name in gap 4.10.1

* Tue Feb 26 2019 Jerry James <loganjerry@gmail.com> - 0.9-1
- Initial RPM
