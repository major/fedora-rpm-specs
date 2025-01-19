# The testsuite is normally run. It can be disabled with "--without=check".
%bcond_without check

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     gprconfig_kb
%global upstream_version  25.0.0
%global upstream_gittag   v%{upstream_version}

Name:           gprconfig-kb
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        GNAT project configuration knowledge base
BuildArch:      noarch

License:        GPL-3.0-or-later WITH GCC-exception-3.1

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# [Fedora specific]
Source1:        fedora_arches.xml
Source2:        fedora_ar.xml

# [specific to recent GCC] Make detection of GCC compilers independent of locale.
Patch1:         %{name}-improve-detection-of-gcc.patch
# Our guess at why Adacore don't do this is that they might want to support old
# versions of GCC that lack -dumpfullversion.

# [Unix-specific] Make detection of GNU ld independent of locale.
Patch2:         %{name}-improve-detection-of-gnu-ld.patch
# Use of env makes this patch specific to Unix-like systems.

# [specific to recent Clang] Make detection of Clang compilers independent of locale.
Patch3:         %{name}-improve-detection-of-clang.patch
# Our guess at why Adacore don't do this is that they might want to support old
# versions of Clang where -dumpversion returns a hardcoded fake version number.

%if %{with check}
# The XML files are checked with XMLlint. Using a tool not written in Ada for
# this avoids a dependency loop that would make bootstrapping GPRbuild even
# more complicated. The checking can be disabled if there should be a problem
# with this dependency.
BuildRequires:  libxml2
%endif

# The contents of this package are split off from the gprbuild package.
Conflicts:      gprbuild <= 2020


%description
The GNAT project configuration knowledge base is used for configuring
GNAT project toolchains.


#############
## Prepare ##
#############

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -p1


###########
## Build ##
###########

%build
%nil


#############
## Install ##
#############

%install
%global inst install --mode=u=rw,go=r,a-s --preserve-timestamps

mkdir --parents %{buildroot}%{_datadir}/gprconfig
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig db/gprconfig.xsd
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig db/*.xml
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig db/*.ent
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig %{SOURCE1} %{SOURCE2}


###########
## Check ##
###########

%if %{with check}
%check
# Check that the XML files are valid according to the XML schema.
xmllint --nonet --noout --noent \
        --schema %{buildroot}%{_datadir}/gprconfig/gprconfig.xsd \
        %{buildroot}%{_datadir}/gprconfig/*.xml
# --schema requires --noent when the XML files contain entity references.
%endif


###########
## Files ##
###########

%files
%license COPYING3 COPYING.RUNTIME
%doc README*
%{_datadir}/gprconfig


###############
## Changelog ##
###############

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 08 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 25.0.0-1
- Updated to v25.0.0.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jan 28 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 24.0.0-1
- Updated to v24.0.0.
- Dropped gprconfig-kb-fedora-compilers.patch. It seemed to have no effect.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 Björn Persson <Bjorn@Rombobjörn.se> - 23.0.0-5
- Split fedora_arches.xml to make it compliant with gprconfig.xsd.

* Sun Jan 14 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 23.0.0-4
- Removed unused patch-file gprconfig-kb-detect-by-major-version.patch.
- Improve detection of GCC compilers; make it independent of locale.
- Improve detection of GNU ld; make it independent of locale.
- Improve detection of Clang compilers; make it independent of locale.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 30 2022 Dennis van Raaij <dvraaij@fedoraproject.org> - 23.0.0-1
- Updated to v23.0.0, using the archive available on GitHub.
- Removed backport patch gprconfig-kb-detect-by-major-version.patch.

* Sun Oct 02 2022 Dennis van Raaij <dvraaij@fedoraproject.org> - 22.0.0-1
- New package. The contents of this package are split off from the gprbuild package.
