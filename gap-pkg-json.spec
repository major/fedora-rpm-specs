%global pkgname  json

Name:           gap-pkg-%{pkgname}
Version:        2.1.1
Release:        3%{?dist}
Summary:        JSON reading and writing for GAP

License:        BSD-2-Clause
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://gap-packages.github.io/json/
Source0:        https://github.com/gap-packages/json/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

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
# The content is BSD-2-Clause.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        BSD-2-CLause AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
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
./configure %{gap_archdir}
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc HISTORY README
%license LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.1.1-2
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Clarify license of the doc subpackage

* Thu Oct 20 2022 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Version 2.1.1

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-4
- Update for gap 4.12.0

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
