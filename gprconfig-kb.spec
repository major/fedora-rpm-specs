# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     gprconfig_kb
%global upstream_version  23.0.0
%global upstream_gittag   v%{upstream_version}

Name:           gprconfig-kb
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        GNAT project configuration knowledge base
BuildArch:      noarch

License:        GPL-3.0-or-later WITH GCC-exception-3.1

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# [Fedora specific]
Source1:        fedora_arches.xml

# [Fedora specific]
Patch0:         %{name}-fedora-compilers.patch
# [Fedora specific] Detect major version using `gcc -dumpversion`.
Patch1:         %{name}-use-dumpversion.patch

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
%{inst} --target-directory=%{buildroot}%{_datadir}/gprconfig %{SOURCE1}


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
* Sun Oct 30 2022 Dennis van Raaij <dvraaij@fedoraproject.org> - 23.0.0-1
- Updated to v23.0.0, using the archive available on GitHub.
- Removed backport patch gprconfig-kb-detect-by-major-version.patch.

* Sun Oct 02 2022 Dennis van Raaij <dvraaij@fedoraproject.org> - 22.0.0-1
- New package. The contents of this package are split off from the gprbuild package.
