%global pkgname recog

Name:           gap-pkg-%{pkgname}
Version:        1.4.2
Release:        3%{?dist}
Summary:        Group recognition methods

License:        GPL-3.0-or-later
BuildArch:      noarch
ExclusiveArch:  %{gap_arches} noarch
URL:            https://gap-packages.github.io/recog/
Source0:        https://github.com/gap-packages/recog/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-factint
BuildRequires:  gap-pkg-forms
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-orb
BuildRequires:  gap-pkg-tomlib

Requires:       gap-pkg-atlasrep
Requires:       gap-pkg-factint
Requires:       gap-pkg-forms
Requires:       gap-pkg-genss
Requires:       gap-pkg-orb

%description
This is a GAP package for group recognition.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Recog documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -b 1

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g contrib examples gap tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

# Do not run the very slow tests
gap -l "%{buildroot}%{gap_libdir};" tst/testquick.g
gap -l "%{buildroot}%{gap_libdir};" tst/testslow.g

%files
%doc CHANGES NOTES README.md TODO WISHLIST
%license COPYRIGHT LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/
%exclude %{gap_libdir}/pkg/%{pkgname}/examples/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%docdir %{gap_libdir}/pkg/%{pkgname}/examples/
%{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/examples/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.4.2-2
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- Version 1.4.2
- Update for gap 4.12.0
- Convert License tag to SPDX
- Move TOC data into the testdata tarball

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 1.3.2-9.20200127.168ed62
- Add TOC data to fix the tests with recent versions of atlasrep

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5.20200127.168ed62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 1.3.2-4.20200127.168ed62
- Rebuild for gap 4.11.0
- Add missing gap-pkg-orb dependency

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Jerry James <loganjerry@gmail.com> - 1.3.2-2
- Drop the ctbllib and tomlib dependencies

* Thu Oct 24 2019 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Initial RPM
