# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     gprconfig_kb
%global upstream_version  23.0.0
%global upstream_gittag   v%{upstream_version}

Name:           gprconfig-kb
Version:        %{upstream_version}
Release:        6%{?dist}
Summary:        GNAT project configuration knowledge base
BuildArch:      noarch

License:        GPL-3.0-or-later WITH GCC-exception-3.1

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# [Fedora specific]
Source1:        fedora_arches.xml
Source2:        fedora_ar.xml

# [Fedora specific]
Patch0:         %{name}-fedora-compilers.patch

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
