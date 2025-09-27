# When bootstrapping a new architecture, there is no gap-pkg-ctbllib package
# yet.  We need it to generate documentation and run tests, but it needs this
# package to function at all.  Therefore, do the following:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-tomlib
# 3. Build gap-pkg-ctbllib
# 4. Build this package in non-bootstrap mode.
%bcond bootstrap 0

%global gap_pkgname atlasrep
%global gap_makedoc makedocrel.g

Name:           gap-pkg-%{gap_pkgname}
Version:        2.1.9
Release:        %autorelease
Summary:        GAP interface to the Atlas of Group Representations

License:        GPL-3.0-or-later
URL:            https://www.math.rwth-aachen.de/~Thomas.Breuer/atlasrep/
Source0:        %{url}/%{gap_upname}-%{version}.tar.gz
Source1:        %{url}/%{gap_upname}data.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source2:        %{name}-testdata.tar.xz

# The makedocrel script determines that the package being built is outside of
# the normal GAP install directories and refuses to do anything with it.
Patch:          %{name}-makedocrel.patch

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): *.json bibl dataext datagens datapkg dataword gap tst
BuildOption(check): tst/testall.g

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
The aim of the AtlasRep package is to provide an interface between GAP and the
Atlas of Group Representations, a database that comprises representations of
many almost simple groups and information about their maximal subgroups.  This
database is available independent of GAP.

The AtlasRep package consists of this database and a GAP interface.  The
latter allows the user to get an overview of the database, and to access the
data in GAP format.

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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version} -p1

%conf
tar -x --strip-components=1 -f %{SOURCE1}
rm {dataext,datagens,dataword}/dummy
rm -fr dataword/{.cvsignore,CVS}

# Fix permissions
chmod a-x doc/*.xml

%build -a
# Put the upstream makedocrel.g back before installation
tar -x --strip-components=1 -f %{SOURCE0} \
    %{gap_upname}-%{version}/makedocrel.g

# Remove the build directory from the documentation
sed -i "s,$PWD/doc/\.\./\.\./pkg,../..,g" doc/*.html

%check
%if %{without bootstrap}
# Add the files needed for testing to the starter set
tar -xf %{SOURCE2}

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "$PWD/" );
EOF

# Test
gap --packagedirs .. tst/testall.g
%endif

%files
%doc README.md
%license GPL
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/*.json
%{gap_libdir}/pkg/%{gap_upname}/bibl/
%{gap_libdir}/pkg/%{gap_upname}/dataext/
%{gap_libdir}/pkg/%{gap_upname}/datagens/
%{gap_libdir}/pkg/%{gap_upname}/datapkg/
%{gap_libdir}/pkg/%{gap_upname}/dataword/
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
