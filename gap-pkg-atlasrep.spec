%global pkgname atlasrep

# When bootstrapping a new architecture, there is no gap-pkg-ctbllib package
# yet.  We need it to generate documentation and run tests, but it needs this
# package to function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-tomlib
# 3. Build gap-pkg-ctbllib
# 4. Build this package in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        2.1.6
Release:        1%{?dist}
Summary:        GAP interface to the Atlas of Group Representations

License:        GPL-3.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://www.math.rwth-aachen.de/~Thomas.Breuer/atlasrep/
Source0:        %{url}/%{pkgname}-%{version}.tar.gz
Source1:        %{url}/%{pkgname}data.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source2:        %{name}-testdata.tar.xz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-browse-doc
%if %{without bootstrap}
BuildRequires:  gap-pkg-ctbllib-doc
#BuildRequires:  gap-pkg-standardff-doc
BuildRequires:  gap-pkg-tomlib
%endif
BuildRequires:  gap-pkg-utils-doc

Requires:       coreutils
Requires:       gap-pkg-io
Requires:       gap-pkg-utils

Recommends:     gap-pkg-browse
Recommends:     gap-pkg-ctbllib
Recommends:     gap-pkg-tomlib

%description
The aim of the AtlasRep package is to provide an interface between GAP
and the Atlas of Group Representations, a database that comprises
representations of many almost simple groups and information about their
maximal subgroups.  This database is available independent of GAP.

The AtlasRep package consists of this database and a GAP interface.  The
latter allows the user to get an overview of the database, and to access
the data in GAP format.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN AND LicenseRef-Fedora-Public-Domain
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND LicenseRef-Fedora-Public-Domain AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        AtlasRep documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-browse-doc
%if %{without bootstrap}
Requires:       gap-pkg-ctbllib-doc
#Requires:       gap-pkg-standardff-doc
%endif
Requires:       gap-pkg-utils-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}
tar -x --strip-components=1 -f %{SOURCE1}
rm {dataext,datagens,dataword}/dummy
rm -fr dataword/{.cvsignore,CVS}

# Fix permissions
chmod a-x doc/*.xml

%build
# Link to main GAP documentation
cp -a %{gap_dir}/doc ../../doc
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
%if %{with bootstrap}
mkdir -p ../ctbllib/doc
touch ../ctbllib/doc/manualbib.xml
mkdir -p ../pkg/ctbllib/doc
touch ../pkg/ctbllib/doc/manualbib.xml
%else
cp -a %{gap_dir}/pkg/ctbllib ..
%endif
gap -l "$PWD/..;" makedocrel.g
rm -fr ../../doc ../{ctbllib,pkg}

# Remove the build directory from the documentation
sed -i "s,$PWD/doc/\.\./\.\./pkg,../..,g" doc/*.html

%install
rm tst/*~
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g *.json bibl dataext datagens datapkg dataword gap tst \
   %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
export LC_ALL=C.UTF-8

# Add the files needed for testing to the starter set
tar -xf %{SOURCE2}

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "$PWD/" );
EOF

# Test
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" tst/testall.g
rm -fr ../pkg
%endif

%files
%doc README.md
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Fri Nov  4 2022 Jerry James <loganjerry@gmail.com> - 2.1.6-1
- Version 2.1.6
- Add dependency on gap-pkg-utils
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.1.5-1
- Version 2.1.5
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.1.4-1
- Convert License tag to SPDX

* Sat Aug  6 2022 Jerry James <loganjerry@gmail.com> - 2.1.4-1
- Version 2.1.4

* Thu Aug  4 2022 Jerry James <loganjerry@gmail.com> - 2.1.3-1
- Version 2.1.3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 30 2022 Jerry James <loganjerry@gmail.com> - 2.1.2-1
- Version 2.1.2

* Tue Mar 29 2022 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Version 2.1.1
- Drop upstreamed -bib patch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jerry James <loganjerry@gmail.com> - 2.1.0-6
- Fix cross references to the ctbllib documentation

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 2.1.0-4
- BR gap-pkg-tomlib to eliminate warnings when testing
- Add -bib patch to fix broken citations
- Add check script

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- New upstream version

* Thu Feb 28 2019 Jerry James <loganjerry@gmail.com> - 1.5.1-9
- Do not ship a CVS directory or the dummy files

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.5.1-8
- Rebuild in non-bootstrap mode

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.5.1-7
- Rebuild for gap 4.10.0 in bootstrap mode
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- New upstream version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.5.0-4
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Jerry James <loganjerry@gmail.com> - 1.5.0-2
- Add Requires(post) and Requires(postun)
- Mark documentation as such

* Fri Jan 16 2015 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- Initial RPM
