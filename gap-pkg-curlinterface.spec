%global pkgname curlinterface
%global upname  curlInterface

# TESTING NOTE: the tests, unsurprisingly, require network access.  Since the
# koji builders have no network access, the tests always fail.  The maintainer
# should run the tests in an environment where testing is possible prior to
# each koji build.
%bcond_with tests

Name:           gap-pkg-%{pkgname}
Version:        2.3.1
Release:        3%{?dist}
Summary:        Simple web access for GAP

License:        GPL-2.0-or-later
ExclusiveArch:  aarch64 ppc64le s390x x86_64
URL:            https://gap-packages.github.io/curlInterface/
Source0:        https://github.com/gap-packages/curlInterface/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)

Requires:       gap-core

%description
This package provides a simple GAP wrapper around libcurl, to allow
downloading files over http, ftp and https.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Curl interface for GAP documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules

# Build the binary interface
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{upname}/doc
cp -a *.g bin gap tst %{buildroot}%{gap_archdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

%if %{with tests}
%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g
%endif

%files
%doc CHANGES README.md
%license GPL LICENSE
%{gap_archdir}/pkg/%{upname}/
%exclude %{gap_archdir}/pkg/%{upname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{upname}/doc/
%{gap_archdir}/pkg/%{upname}/doc/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.3.1-2
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Version 2.3.1
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.2.3-1
- Convert License tag to SPDX

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 2.2.3-1
- Version 2.2.3

* Sat Jul 23 2022 Jerry James <loganjerry@gmail.com> - 2.2.2-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Jerry James <loganjerry@gmail.com> - 2.2.2-1
- Version 2.2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr  3 2020 Jerry James <loganjerry@gmail.com> - 2.2.1-1
- Version 2.2.1
- Drop upstreamed -backtick patch

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 2.1.1-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Initial RPM
