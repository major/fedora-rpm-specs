%global pkgname atlasrep

# When bootstrapping a new architecture, there is no gap-pkg-ctbllib package
# yet.  We need it to generate documentation, but it needs this package to
# function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-tomlib
# 3. Build gap-pkg-ctbllib
# 4. Build this package in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        2.1.4
Release:        1%{?dist}
Summary:        GAP interface to the Atlas of Group Representations

License:        GPL-3.0-or-later
URL:            https://www.math.rwth-aachen.de/~Thomas.Breuer/%{pkgname}/
Source0:        https://www.math.rwth-aachen.de/~Thomas.Breuer/%{pkgname}/%{pkgname}-%{version}.tar.gz
Source1:        https://www.math.rwth-aachen.de/~Thomas.Breuer/%{pkgname}/%{pkgname}data.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source2:        %{name}-testdata.tar.xz

BuildArch:      noarch
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-browse-doc
%if %{without bootstrap}
BuildRequires:  gap-pkg-ctbllib-doc
BuildRequires:  gap-pkg-tomlib
%endif

Requires:       coreutils
Requires:       gap-pkg-io

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
Summary:        AtlasRep documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-browse-doc
%if %{without bootstrap}
Requires:       gap-pkg-ctbllib-doc
%endif

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1
tar -x --strip-components=1 -f %{SOURCE1}
rm {dataext,datagens,dataword}/dummy
rm -fr dataword/{.cvsignore,CVS}

# Fix permissions
chmod a-x doc/*.xml

%build
# Link to main GAP documentation
cp -a %{_gap_dir}/doc ../../doc
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
ln -s %{_gap_dir}/pkg/GAPDoc ../pkg
ln -s %{_gap_dir}/pkg/Browse ../pkg
%if %{with bootstrap}
mkdir -p ../ctbllib/doc
touch ../ctbllib/doc/manualbib.xml
mkdir -p ../pkg/ctbllib/doc
touch ../pkg/ctbllib/doc/manualbib.xml
%else
ctbllibdir=$(cd %{_gap_dir}/pkg && ls -1d ctbllib-*)
cp -a %{_gap_dir}/pkg/${ctbllibdir} ..
ln -s %{_gap_dir}/pkg/${ctbllibdir} ../pkg
sed -i "s/ctbllib/${ctbllibdir}/" doc/main.xml
%endif
gap -l "$PWD/..;%{_gap_dir}" < makedocrel.g
rm -fr ../../doc ../{ctbllib*,pkg}

# Remove the build directory from the documentation
sed -i "s,$PWD/doc/\.\./\.\./pkg,../..,g" doc/*.html

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{.package_note*,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

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
# FIXME: a few tests fail, but succeed when a network is available.
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
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
