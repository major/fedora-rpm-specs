%global pkgname  cvec

Name:           gap-pkg-%{pkgname}
Version:        2.8.1
Release:        4%{?dist}
Summary:        Compact vectors over finite fields

License:        GPL-2.0-or-later
ExclusiveArch:  %{gap_arches}
URL:            https://gap-packages.github.io/cvec/
Source0:        https://github.com/gap-packages/cvec/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-orb-doc
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}

%description
The CVEC package provides an implementation of compact vectors over
finite fields.  Contrary to earlier implementations no table lookups are
used but only word-based processor arithmetic.  This allows for bigger
finite fields and higher speed.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        CVEC documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-orb-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -b 1

%build
export LC_ALL=C.UTF-8

# This is NOT an autotools-generated configure script; do NOT use %%configure
./configure --with-gaproot=%{gap_archdir}
%make_build V=1

# Build the documentation
make doc

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a bin example gap local test tst *.g %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc CHANGES README.md TIMINGS TODO
%license LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/
%exclude %{gap_archdir}/pkg/%{pkgname}/example/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/example/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/example/

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Jerry James <loganjerry@gmail.com> - 2.8.1-1
- Version 2.8.1

* Fri Mar 24 2023 Jerry James <loganjerry@gmail.com> - 2.8.0-1
- Version 2.8.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 2.7.6-3
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.7.6-2
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.7.6-2
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.7.6-1
- Convert License tag to SPDX

* Sat Aug  6 2022 Jerry James <loganjerry@gmail.com> - 2.7.6-1
- Version 2.7.6
- Move TOC data into the testdata tarball

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 2.7.5-3
- Add TOC data to fix the tests with recent versions of atlasrep

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep  7 2021 Jerry James <loganjerry@gmail.com> - 2.7.5-1
- Version 2.7.5

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 2.7.4-5
- Drop aarch64 workaround

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 2.7.4-4
- Rebuild for gap 4.11.0
- Add atlasrep and tomlib BRs so that all tests can be run

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 2.7.4-1
- New upstream version

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 2.7.2-1
- New upstream version

* Mon Mar  4 2019 Jerry James <loganjerry@gmail.com> - 2.7.1-1
- New upstream version

* Wed Feb 20 2019 Jerry James <loganjerry@gmail.com> - 2.7.0-1
- New upstream version

* Tue Dec 18 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.6.1-1
- Initial package.
