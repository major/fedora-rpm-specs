%global pkgname  profiling

Name:           gap-pkg-%{pkgname}
Version:        2.5.2
Release:        2%{?dist}
Summary:        Line by line profiling and code coverage for GAP

# The project as a whole is MIT.
# rapidjson, which is a header-only package, is also MIT.
# src/md5.{cc,h} is Public Domain.
License:        MIT AND LicenseRef-Fedora-Public-Domain
ExclusiveArch:  %{gap_arches}
URL:            https://gap-packages.github.io/profiling/
Source0:        https://github.com/gap-packages/profiling/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Adapt to rapidjson 1.1.0
Patch0:         %{name}-rapidjson.patch

BuildRequires:  elinks
BuildRequires:  flamegraph
BuildRequires:  flamegraph-stackcollapse
BuildRequires:  gcc-c++
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  which
BuildRequires:  xdg-utils

Requires:       flamegraph
Requires:       flamegraph-stackcollapse
Requires:       gap-pkg-io%{?_isa}
Requires:       which
Requires:       xdg-utils

# See https://fedoraproject.org/wiki/Bundled_Libraries_Virtual_Provides
Provides:       bundled(md5-plumb)

%description
This package provides line-by-line profiling of GAP, allowing both
discovering which lines of code take the most time, and which lines of
code are even executed.

The main function provided by this package is
OutputAnnotatedCodeCoverageFiles, which takes a previously generated
profile (using ProfileLineByLine or CoverageLineByLine, both provided by
the GAP library), and outputs human-readable HTML files.

There is also OutputFlameGraph, which outputs a graphical diagram
showing which functions took the most time during execution.

%package doc
# The content is MIT.  The remaining licenses cover the various fonts embedded
# in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MIT AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Profiling documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not use the bundled rapidjson
rm -fr src/rapidjson
sed -i.orig 's,"\(rapidjson/.*h\)",<\1>,' src/json_parse_rapidjson.h
fixtimestamp src/json_parse_rapidjson.h

# Do not use the bundled FlameGraph
rm -fr FlameGraph
sed -i.orig '/Flame/s,DirectoriesPackageLibrary([^)]*),Directory("%{_bindir}"),' gap/profiling.gi
fixtimestamp gap/profiling.gi

%build
export LC_ALL=C.UTF-8

# This is not an autoconf-generated configure script; do not use %%configure
./configure %{gap_archdir}
%make_build V=1

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin data gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
export BROWSER=elinks
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc AUTHORS HISTORY.md README.md
%license COPYRIGHT
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.5.2-1
- Version 2.5.2
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- Clarify license of the doc subpackage

* Tue Oct 11 2022 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- Version 2.5.1

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.5.0-4
- Update for gap 4.12.0
- Convert License tag to SPDX

* Sun Jul 24 2022 Jerry James <loganjerry@gmail.com> - 2.5.0-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 23 2022 Jerry James <loganjerry@gmail.com> - 2.5.0-1
- Version 2.5.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 14 2021 Jerry James <loganjerry@gmail.com> - 2.4.1-1
- Version 2.4.1

* Wed Feb  3 2021 Jerry James <loganjerry@gmail.com> - 2.4-1
- Version 2.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr  3 2020 Jerry James <loganjerry@gmail.com> - 2.3-1
- Version 2.3

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 2.2.1-5.20190319.7a582bd
- Drop aarch64 workaround

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 2.2.1-4.20190319.7a582bd
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3.20190319.7a582bd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2.20190319.7a582bd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul  6 2019 Jerry James <loganjerry@gmail.com> - 2.2.1-1.20190319.7a582bd
- Initial package
