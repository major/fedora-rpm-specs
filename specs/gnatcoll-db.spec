# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     gnatcoll-db
%global upstream_version  25.0.0
%global upstream_gittag   v%{upstream_version}

Name:           gnatcoll-db
Epoch:          2
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        The GNAT Components Collection – database packages
Summary(sv):    GNAT Components Collection – databaspaket

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later AND GPL-2.0-or-later WITH GNAT-exception
# The subpackages have different licenses. This is the aggregation of those.

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source:         %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# This patch makes gnatcoll_db2ada run dborm.py in python3, and also corrects
# the location of dborm.py:
Patch:          %{name}-dborm_python3.patch
# [Backport] Refine dependencies on GNATColl (be1a7c6).
Patch:          %{name}-refine-dependencies-to-gnatcoll.patch

BuildRequires:  gcc-gnat gprbuild sed make
# A fedora-gnat-project-common that contains GPRbuild_flags is needed.
BuildRequires:  fedora-gnat-project-common >= 3.17
BuildRequires:  gnatcoll-core-devel     = %{epoch}:%{version}
BuildRequires:  gnatcoll-projects-devel = %{epoch}:%{version}
BuildRequires:  gnatcoll-iconv-devel    = %{epoch}:%{version}
# Although upstream doesn't explicitly say so, I guess it's best to keep all
# the parts of Gnatcoll on the same version number.
BuildRequires:  sqlite-devel libpq-devel

# for adjusting the shebang in dborm.py:
BuildRequires:  python3-devel

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk

# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%description
This is the database module of the GNAT Components Collection.

%description -l sv
Detta är databasmodulen i GNAT Components Collection.


#################
## Subpackages ##
#################

%package devel
Summary:        Development metapackage for the GNAT Components Collection – database packages
Summary(sv):    Metapaket för programmering med GNAT Components Collection – databaspaket
Requires:       gnatcoll-sql-devel      = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sqlite-devel   = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-postgres-devel = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-xref-devel     = %{epoch}:%{version}-%{release}
# This metapackage is marked as deprecated because nothing shall require it.
# Other packages shall require the components they actually need.
Provides:       deprecated()

%description devel
Each database component of the GNAT Components Collection now has its own
development package. This meta-package exists to prevent problems when Fedora
is upgraded. It pulls in the development packages for all of the database
components.

Do not specify this package in any configurations or dependencies. Specify the
packages you actually need.

%description devel -l sv
Varje databaskomponent i GNAT Components Collection har nu ett eget
programmeringspaket. Detta metapaket är till för att undvika problem när Fedora
uppgraderas. Det drar in programmeringspaketen för alla databaskomponenterna.

Ange inte det här paketet i några konfigurationer eller beroenden. Ange paketen
du faktiskt behöver.


%package -n gnatcoll-sql
Summary:        The GNAT Components Collection – SQL component
Summary(sv):    GNAT Components Collection – SQL-komponenten
License:        GPL-3.0-or-later WITH GCC-exception-3.1

%description -n gnatcoll-sql
This is the SQL component of the GNAT Components Collection. It provides an
object-oriented, high-level interface to SQL queries.

%description -n gnatcoll-sql -l sv
Detta är SQL-komponenten i GNAT Components Collection. Den tillhandahåller ett
objektorienterat högnivågränssnitt mot SQL-frågor.


%package -n gnatcoll-sql-devel
Summary:        Development files for the GNAT Components Collection – SQL component
Summary(sv):    Filer för programmering med GNAT Components Collection – SQL-komponenten
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Provides:       gnatcoll_db2ada = %{epoch}:%{version}-%{release}
Provides:       gnatcoll_all2ada = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
# dborm.py needs the Python interpreter:
Requires:       python3
Recommends:     gnatcoll-db-doc

%description -n gnatcoll-sql-devel
This package contains source code and linking information for developing
applications that use the SQL component of the GNAT Components Collection.
It provides an object-oriented, high-level interface to SQL queries.

This package also contains the tool gnatcoll_db2ada, which generates an Ada
package from a description of a database schema.

%description -n gnatcoll-sql-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder SQL-komponenten i GNAT Components Collection.
Den tillhandahåller ett objektorienterat högnivågränssnitt mot SQL-frågor.

Det här paketet innehåller också verktyget gnatcoll_db2ada som genererar ett
adapaket från en beskrivning av en databasstruktur.


%package -n gnatcoll-sqlite
Summary:        The GNAT Components Collection – SQLite support
Summary(sv):    GNAT Components Collection – stöd för SQLite
License:        GPL-3.0-or-later WITH GCC-exception-3.1
# The bundled C files in sqlite/amalgamation don't affect the license
# expression because the sqlite-devel package is used instead.
Requires:       gnatcoll-sql%{?_isa} = %{epoch}:%{version}-%{release}

%description -n gnatcoll-sqlite
This component provides support for SQLite to the SQL component of the GNAT
Components Collection.

%description -n gnatcoll-sqlite -l sv
Den här komponenten tillhandahåller stöd för SQLite till SQL-komponenten i
GNAT Components Collection.


%package -n gnatcoll-sqlite-devel
Summary:        Development files for the GNAT Components Collection – SQLite support
Summary(sv):    Filer för programmering med GNAT Components Collection – stöd för SQLite
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-sqlite%{?_isa}    = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
Recommends:     gnatcoll-db-doc

%description -n gnatcoll-sqlite-devel
This package contains source code and linking information for developing
applications that use SQLite databases through the SQL component of the
GNAT Components Collection.

%description -n gnatcoll-sqlite-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder SQLite-databaser genom SQL-komponenten i GNAT
Components Collection.


%package -n gnatcoll-postgres
Summary:        The GNAT Components Collection – PostgreSQL support
Summary(sv):    GNAT Components Collection – stöd för PostgreSQL
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNAT-exception
# The license is GPLv3+ with the GCC runtime exception, except for:
# - postgres/gnatcoll-sql-postgres-gnade.ad[bs] : GPLv2+ with GNAT runtime exception
Requires:       gnatcoll-sql%{?_isa} = %{epoch}:%{version}-%{release}

%description -n gnatcoll-postgres
This component provides support for PostgreSQL to the SQL component of the GNAT
Components Collection.

%description -n gnatcoll-postgres -l sv
Den här komponenten tillhandahåller stöd för PostgreSQL till SQL-komponenten i
GNAT Components Collection.


%package -n gnatcoll-postgres-devel
Summary:        Development files for the GNAT Components Collection – PostgreSQL support
Summary(sv):    Filer för programmering med GNAT Components Collection – stöd för PostgreSQL
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNAT-exception
# The license is GPLv3+ with the GCC runtime exception, except for:
# - postgres/gnatcoll-sql-postgres-gnade.ad[bs] : GPLv2+ with GNAT runtime exception
Requires:       gnatcoll-postgres%{?_isa}  = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
Recommends:     gnatcoll-db-doc

%description -n gnatcoll-postgres-devel
This package contains source code and linking information for developing
applications that use PostgreSQL databases through the SQL component of the
GNAT Components Collection.

%description -n gnatcoll-postgres-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder PostgreSQL-databaser genom SQL-komponenten i GNAT
Components Collection.


%package -n gnatcoll-xref
Summary:        The GNAT Components Collection – cross-referencing
Summary(sv):    GNAT Components Collection – korshänvisning
License:        GPL-3.0-or-later
# gnatcoll-xref.ads, gnatcoll-xref.adb and gnatinspect.adb do not grant the
# GCC Runtime Library Exception.
Provides:       gnatinspect = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sqlite%{?_isa} = %{epoch}:%{version}-%{release}

%description -n gnatcoll-xref
This is the Xref component of the GNAT Components Collection. It provides
support for parsing the .ali and .gli files that are generated by GNAT and GCC.
In particular, those files contain information that can be used to do cross-
references for entities (going from references to their declaration for
instance).

This package also contains Gnatinspect, a command-line tool for building and
querying a database of cross-reference information.

%description -n gnatcoll-xref -l sv
Detta är komponenten Xref i GNAT Components Collection. Den analyserar .ali-
och .gli-filerna som GNAT och GCC producerar. I de filerna finns uppgifter som
kan användas till korshänvisning (till exempel att hitta en deklaration utifrån
en referens).

Det här paketet innehåller också Gnatinspect, ett kommandoradsverktyg för att
bygga och söka i en databas över korshänvisningar.


%package -n gnatcoll-xref-devel
Summary:        Development files for the GNAT Components Collection – cross-referencing
Summary(sv):    Filer för programmering med GNAT Components Collection – korshänvisning
License:        GPL-3.0-or-later
# gnatcoll-xref.ads, gnatcoll-xref.adb and gnatinspect.adb do not grant the
# GCC Runtime Library Exception.
Requires:       gnatcoll-xref%{?_isa}         = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sql-devel%{?_isa}    = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-sqlite-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel gnatcoll-iconv-devel
Recommends:     gnatcoll-db-doc

%description -n gnatcoll-xref-devel
This package contains source code and linking information for developing
applications that use the Xref component of the GNAT Components Collection.
It provides support for parsing the .ali and .gli files that are generated by
GNAT and GCC. In particular, those files contain information that can be used
to do cross-references for entities (going from references to their declaration
for instance).

%description -n gnatcoll-xref-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder komponenten Xref i GNAT Components Collection.
Den analyserar .ali- och .gli-filerna som GNAT och GCC producerar. I de filerna
finns uppgifter som kan användas till korshänvisning (till exempel att hitta en
deklaration utifrån en referens).


%package doc
Summary:        Documentation for the GNAT Components Collection – database packages
Summary(sv):    Dokumentation till GNAT Components Collection – databaspaket
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1
# License for the documentation is AdaCore-doc. The Javascript and CSS files
# that Sphinx includes with the documentation are BSD 2-Clause and MIT-licensed.
# The example code is licensed under GPLv3+ with the GCC runtime exception.

%description doc
This package contains the documentation for the database and Xref components of
the GNAT Components Collection.

%description doc -l sv
Detta paket innehåller dokumentationen till GNAT Components Collections
databaskomponenter och Xref.


#############
## Prepare ##
#############

%prep
%autosetup -p1

# Delete the bundled SQLite to be extra sure that the packaged version is used.
rm --recursive sqlite/amalgamation


###########
## Build ##
###########

%build

# Version information in this file is used during the build.
echo '%{version}' > ./version_information

export GNATCOLL_VERSION=%{version}
export BUILD=PROD
export LIBRARY_TYPE=relocatable
export GNATCOLL_SQLITE=external

# Most of these components depend on each other and need to be built in
# dependency order. Install the built libraries to a staging directory where
# the later build jobs can find them.
mkdir stage  # without --parents to avoid clobbering any existing directory

for component in sql sqlite postgres xref ; do

    gprbuild %{GPRbuild_flags} \
             -aP stage%{_GNAT_project_dir} \
             -P ${component}/gnatcoll_${component}.gpr

    gprinstall --create-missing-dirs --no-manifest --no-build-var \
               --prefix=${PWD}/stage%{_prefix} \
               --sources-subdir=${PWD}/stage%{_includedir}/gnatcoll-${component} \
               --project-subdir=${PWD}/stage%{_GNAT_project_dir} \
               --ali-subdir=${PWD}/stage%{_libdir}/gnatcoll-${component} \
               --lib-subdir=${PWD}/stage%{_libdir} \
               --no-lib-link \
               -aP stage%{_GNAT_project_dir} \
               -P ${component}/gnatcoll_${component}.gpr

    ln --symbolic --force libgnatcoll_${component}.so.%{version} \
       stage%{_libdir}/libgnatcoll_${component}.so

done

# Compile programs with -fPIE so that redhat-hardened-ld can use -pie.

gprbuild -cargs -fPIE %{GPRbuild_flags} -aP stage%{_GNAT_project_dir} \
         -P gnatinspect/gnatinspect.gpr

# There are four variants of gnatcoll_db2ada that differ in their database
# support. Build the one that supports the most databases.
gprbuild -cargs -fPIE %{GPRbuild_flags} -aP stage%{_GNAT_project_dir} \
         -P gnatcoll_db2ada/gnatcoll_all2ada.gpr

# Make the documentation.
make -C docs html latexpdf


#############
## Install ##
#############

%install
# The libraries have already been staged, so just copy them to the "buildroot"
# staging directory.
# Avoid mv because find-debuginfo will want to collect some files under stage.
cp --archive stage/* --target-directory=%{buildroot}

# Stage the executable files.
mkdir --parents %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/gnatcoll
cp gnatinspect/obj/gnatinspect gnatcoll_db2ada/obj/gnatcoll_all2ada \
   --target-directory=%{buildroot}%{_bindir}
cp --preserve=timestamps gnatcoll_db2ada/dborm.py \
   --target-directory=%{buildroot}%{_libexecdir}/gnatcoll
%{py3_shebang_fix} %{buildroot}%{_libexecdir}/gnatcoll/dborm.py

# Copy the documentation.
mkdir --parents %{buildroot}%{_pkgdocdir}/html
cp --preserve=timestamps --recursive \
   docs/_build/html/* --target-directory=%{buildroot}%{_pkgdocdir}/html

mkdir --parents %{buildroot}%{_pkgdocdir}/pdf
cp --preserve=timestamps \
   docs/_build/latex/*.pdf --target-directory=%{buildroot}%{_pkgdocdir}/pdf

# Preserving the command name "gnatcoll_db2ada" seems like a good idea.
ln --symbolic gnatcoll_all2ada %{buildroot}%{_bindir}/gnatcoll_db2ada

# Make the generated usage project files architecture-independent.
for component in sql sqlite postgres xref ; do
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=/package Linker is/,/end Linker/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'gnatcoll-${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'gnatcoll-${component}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/gnatcoll_${component}.gpr
    # The Sed commands are:
    # 1: Insert a with clause before the first line to import the directories
    #    project.
    # 2: Delete a comment that mentions the architecture.
    # 3: Delete the package Linker, which contains linker parameters that a
    #    shared library normally doesn't need, and can contain architecture-
    #    specific pathnames.
    # 4: Replace the value of Source_Dirs with a pathname based on
    #    Directories.Includedir.
    # 5: Replace the value of Library_Dir with Directories.Libdir.
    # 6: Replace the value of Library_ALI_Dir with a pathname based on
    #    Directories.Libdir.
done

# This readme file may be of some value to developers:
mkdir --parents %{buildroot}%{_pkgdocdir}/xref
cp --preserve=timestamps xref/README.md \
   --target-directory=%{buildroot}%{_pkgdocdir}/xref

# Include the example code:
cp --preserve=timestamps --recursive examples \
   --target-directory=%{buildroot}%{_pkgdocdir}

# Install the license in a directory named after the source package.
mkdir --parents %{buildroot}%{_licensedir}/%{name}
cp --preserve=timestamps COPYING3 COPYING.RUNTIME \
   --target-directory=%{buildroot}%{_licensedir}/%{name}


###########
## Files ##
###########

%files devel
# Empty metapackage.


%files -n gnatcoll-sql
%{_libdir}/libgnatcoll_sql.so.%{version}
%license %{_licensedir}/%{name}
# All the other subpackages depend on gnatcoll-sql, so only this one needs to
# contain the license files.

%files -n gnatcoll-sql-devel
%{_GNAT_project_dir}/gnatcoll_sql.gpr
%{_includedir}/gnatcoll-sql
%dir %{_libdir}/gnatcoll-sql
%attr(444,-,-) %{_libdir}/gnatcoll-sql/*.ali
%{_libdir}/libgnatcoll_sql.so
# Tools.
%{_bindir}/gnatcoll_*2ada
%{_libexecdir}/gnatcoll


%files -n gnatcoll-sqlite
%{_libdir}/libgnatcoll_sqlite.so.%{version}

%files -n gnatcoll-sqlite-devel
%{_GNAT_project_dir}/gnatcoll_sqlite.gpr
%{_includedir}/gnatcoll-sqlite
%dir %{_libdir}/gnatcoll-sqlite
%attr(444,-,-) %{_libdir}/gnatcoll-sqlite/*.ali
%{_libdir}/libgnatcoll_sqlite.so


%files -n gnatcoll-postgres
%{_libdir}/libgnatcoll_postgres.so.%{version}

%files -n gnatcoll-postgres-devel
%{_GNAT_project_dir}/gnatcoll_postgres.gpr
%{_includedir}/gnatcoll-postgres
%dir %{_libdir}/gnatcoll-postgres
%attr(444,-,-) %{_libdir}/gnatcoll-postgres/*.ali
%{_libdir}/libgnatcoll_postgres.so


%files -n gnatcoll-xref
%{_libdir}/libgnatcoll_xref.so.%{version}
%{_bindir}/gnatinspect

%files -n gnatcoll-xref-devel
%{_GNAT_project_dir}/gnatcoll_xref.gpr
%{_includedir}/gnatcoll-xref
%dir %{_libdir}/gnatcoll-xref
%attr(444,-,-) %{_libdir}/gnatcoll-xref/*.ali
%{_libdir}/libgnatcoll_xref.so
%dir %{_pkgdocdir}
%{_pkgdocdir}/xref


%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/html
%{_pkgdocdir}/pdf
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package.
%exclude /%{_pkgdocdir}/html/.buildinfo
%exclude /%{_pkgdocdir}/html/objects.inv


###############
## Changelog ##
###############

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:25.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 27 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:25.0.0-1
- Updated to v25.0.0.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:24.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 31 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:24.0.0-2
- Development package dependencies have been adjusted.

* Wed May 08 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:24.0.0-1
- Updated to v24.0.0.

* Wed May 08 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:23.0.0-1
- Updated to v23.0.0.
- Removed patch gnatcoll-db-operator_ambiguity.patch; has been fixed upstream (commit 3ab81e8).
- Added a package with documentation.

* Tue May 07 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:22.0.0-1
- Updated to v22.0.0.
- License fields now contain SPDX license expressions.
- Re-enabled the build on s390x.
- The devel package has been split up; gnatcoll-db-devel is now a metapackage.
- Parameter values for GPRinstall are now more similar to those in the GPRinstall_flags macro.
- Improved spec file readability.

* Sun Feb 11 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-13
- Rebuilt with XMLada 24 and LibGPR 24.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-10
- Rebuilt with GCC 14 prerelease.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-8
- Rebuilt with XMLada 23 and LibGPR 23.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-6
- Backported a fix for operator ambiguity.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-2
- Corrected the license of gnatcoll-xref.

* Mon Feb 08 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2:21.0.0-1
- Upgraded to version 21.0.0.
- s390x is excluded until GPRinstall can be fixed.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-3
- Added versions to Provides tags.
- Tagged the license file as such.

* Wed Apr 03 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-2
- Added more macro usage and more comments.
- Removed unnecessary duplicates of the license file.

* Sun Mar 24 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2018-1
- new package
