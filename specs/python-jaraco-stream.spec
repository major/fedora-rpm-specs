# TODO adjust once this is implemented:
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%global modname  jaraco
%global projname %{modname}.stream
%global pkgname  %{modname}-stream
%global srcname  %{modname}_stream

%bcond_without tests
# Change the build backend in EPEL9 because `setuptools>=61.2`
# is needed for PEP621
%if 0%{?epel} == 9
%bcond_without hatch
%else
%bcond_with    hatch
%endif

Name:           python-%{pkgname}
Version:        3.0.4
Release:        %autorelease
Summary:        Routines for dealing with data streams

License:        MIT
URL:            https://github.com/jaraco/%{projname}
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with hatch}
BuildRequires:  tomcli
%endif

%global _description %{expand:
Routines for handling streaming data, including a set of generators for
loading gzip data on the fly.}

%description %_description

%package     -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%if %{with hatch}
tomcli set pyproject.toml lists str "build-system.requires" "hatchling" "hatch-vcs"
tomcli set pyproject.toml str "build-system.build-backend" "hatchling.build"
tomcli set pyproject.toml str "tool.hatch.version.source" "vcs"
tomcli set pyproject.toml lists str "tool.hatch.build.targets.wheel.packages" %{modname}
%endif

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -x test
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import -e jaraco.stream.test_gzip
%endif

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.rst NEWS.rst

%changelog
%autochangelog
