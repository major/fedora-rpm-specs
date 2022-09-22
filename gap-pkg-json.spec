%global pkgname  json

Name:           gap-pkg-%{pkgname}
Version:        2.1.0
Release:        3%{?dist}
Summary:        JSON reading and writing for GAP

License:        BSD-2-Clause
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

# We cannot use the system version of picojson-devel.  The version used by this
# package has had https://github.com/kazuho/picojson/pull/52 merged into it.
# Until upstream merges that and produces a new release, we are stuck with the
# bundled version.
Provides:       bundled(picojson-devel) = 1.1.1

%description
This package defines a mapping between the JSON markup language and GAP.
The built-in datatypes of GAP provide an easy mapping to and from JSON.
This package uses the following mapping between GAP and JSON.

- JSON lists are mapped to GAP lists
- JSON dictionaries are mapped to GAP records
- JSON strings are mapped to GAP strings
- Integers are mapped to GAP integers, non-integer numbers are mapped to
  Floats
- true, false and null are mapped to true, false and fail respectively

Note that this library will not map any other GAP types, such as groups,
permutations, to or from JSON.  If you wish to map between more complex
types, look at the gap-pkg-openmath package, or IO_Pickle in the
gap-pkg-io package.

%package doc
Summary:        JSON documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{_gap_dir}
%make_build

# Build the documentation
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
cp -a bin doc gap tst *.g %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/*/{.libs,*.la}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc HISTORY README
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-3
- Convert License tag to SPDX

* Sun Jul 24 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 23 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- Version 2.1.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr  3 2020 Jerry James <loganjerry@gmail.com> - 2.0.2-1
- Version 2.0.2

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 2.0.1-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Jerry James <loganjerry@gmail.com> - 2.0.1-1
- Version 2.0.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 2.0.0-2
- Rebuild for changed bin dir name in gap 4.10.1

* Tue Feb 26 2019 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Initial RPM
