# TODO adjust once this is implemented:
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%global modname  jaraco
%global projname %{modname}.logging
%global pkgname  %{modname}-logging
%global srcname  %{modname}_logging

# pytest fails with some weird import path error in EPEL 9
%bcond tests %[0%{?epel} != 9]
# Change the build backend in EPEL because `setuptools>=77` is needed
%bcond hatch %[0%{?epel} && 0%{?epel} <= 10]

Name:           python-%{pkgname}
Version:        3.4.0
Release:        %autorelease
Summary:        Support for Python logging facility

License:        MIT
URL:            https://github.com/jaraco/%{projname}
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with hatch}
BuildRequires:  tomcli
%endif

%global _description %{expand:
Support for Python logging facility.}

%description %_description

%package     -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%if %{with hatch}
tomcli set pyproject.toml lists str "build-system.requires" "hatchling" "hatch-vcs" "coherent.licensed"
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
%pyproject_check_import
%endif

%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.rst NEWS.rst

%changelog
%autochangelog
