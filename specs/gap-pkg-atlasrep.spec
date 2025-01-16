%global pkgname atlasrep

# When bootstrapping a new architecture, there is no gap-pkg-ctbllib package
# yet.  We need it to generate documentation and run tests, but it needs this
# package to function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-tomlib
# 3. Build gap-pkg-ctbllib
# 4. Build this package in non-bootstrap mode.
%bcond bootstrap 0

Name:           gap-pkg-%{pkgname}
Version:        2.1.9
Release:        %autorelease
Summary:        GAP interface to the Atlas of Group Representations

License:        GPL-3.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://www.math.rwth-aachen.de/~Thomas.Breuer/atlasrep/
Source0:        %{url}/%{pkgname}-%{version}.tar.gz
Source1:        %{url}/%{pkgname}data.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source2:        %{name}-testdata.tar.xz

# The makedocrel script determines that the package being built is outside of
# the normal GAP install directories and refuses to do anything with it.
Patch:          %{name}-makedocrel.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
%if %{without bootstrap}
BuildRequires:  gap-pkg-browse-doc
BuildRequires:  gap-pkg-ctbllib-doc
BuildRequires:  gap-pkg-standardff-doc
BuildRequires:  gap-pkg-tomlib
%endif
BuildRequires:  gap-pkg-utils-doc

Requires:       coreutils
Requires:       gap-pkg-io
Requires:       gap-pkg-utils

Recommends:     gap-pkg-browse
Recommends:     gap-pkg-ctbllib
Recommends:     gap-pkg-recog
Recommends:     gap-pkg-standardff
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
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        AtlasRep documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-browse-doc
%if %{without bootstrap}
Requires:       gap-pkg-ctbllib-doc
Requires:       gap-pkg-standardff-doc
%endif
Requires:       gap-pkg-utils-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

%conf
tar -x --strip-components=1 -f %{SOURCE1}
rm {dataext,datagens,dataword}/dummy
rm -fr dataword/{.cvsignore,CVS}

# Fix permissions
chmod a-x doc/*.xml

%build
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
sed -i '/SetPackagePath/d' makedocrel.g
gap -l "$PWD/..;" makedocrel.g
rm -fr ../pkg
tar -x --strip-components=1 -f %{SOURCE0} %{pkgname}-%{version}/makedocrel.g

# Remove the build directory from the documentation
sed -i "s,$PWD/doc/\.\./\.\./pkg,../..,g" doc/*.html

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g *.json bibl dataext datagens datapkg dataword gap tst \
   %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%if %{without bootstrap}
%check
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
%license GPL
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/*.json
%{gap_libdir}/pkg/%{pkgname}/bibl/
%{gap_libdir}/pkg/%{pkgname}/dataext/
%{gap_libdir}/pkg/%{pkgname}/datagens/
%{gap_libdir}/pkg/%{pkgname}/datapkg/
%{gap_libdir}/pkg/%{pkgname}/dataword/
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
