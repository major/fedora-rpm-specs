%global forgeurl https://github.com/platformio/platformio-core
%global pypi_name platformio
%global srcname platformio-core

# Tests require Internet access
%bcond_with tests

Name:           python-%{pypi_name}
Version:        6.1.16
Release:        %autorelease
Summary:        Professional collaborative platform for embedded development

License:        Apache-2.0
URL:            https://platformio.org
# PyPI is missing tests, so use the GitHub tarball instead
Source:         %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Fedora: disable telemetry by default
Patch1:         platformio-default-telemetry-off.patch
# Fedora: neuter update logic for platformio itself
Patch2:         platformio-short-circuit-upgrades.patch
# Allow Starlette 0.40.x
# https://github.com/platformio/platformio-core/pull/5000
# https://github.com/platformio/platformio-core/commit/cade63fba570ffb7381f5e24350fddd41c64c0f4
Patch3:         %{forgeurl}/commit/cade63fba570ffb7381f5e24350fddd41c64c0f4.patch
# Update dependencies.py
# https://github.com/platformio/platformio-core/commit/a4276b4ea63e8701cfa9c05d820d5dfe61c17409
# (Allows Starlette 0.41.x)
Patch4:         %{forgeurl}/commit/a4276b4ea63e8701cfa9c05d820d5dfe61c17409.patch
# Update deps
# https://github.com/platformio/platformio-core/commit/07e7dc47174679fdc6402e899df450a154fd242d
# (Allows uvicorn 0.32.x)
Patch5:         %{forgeurl}/commit/07e7dc47174679fdc6402e899df450a154fd242d.patch
# Update deps
# https://github.com/platformio/platformio-core/commit/90fc36cf2d328309c985af57854e8f59a3aedbb4
# (Allows Starlette 0.42.x and uvicorn 0.34.x)
Patch6:         %{forgeurl}/commit/90fc36cf2d328309c985af57854e8f59a3aedbb4.patch
# Allow starlette versions through 0.45
# https://github.com/platformio/platformio-core/pull/5059
Patch7:         %{forgeurl}/pull/5059.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

%global _description %{expand:
PlatformIO is a cross-platform, cross-architecture, multiple framework,
professional tool for embedded systems engineers and for software developers
who write applications for embedded products.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package -n     %{pypi_name}
Summary:        %{summary}
Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       systemd-udev

%description -n %{pypi_name} %_description

This package contains the PlatformIO command-line utilites and udev rules.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# Replace duplicate binary with symlink
ln -sf platformio %{buildroot}%{_bindir}/pio

# Install udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
ln -s %{python3_sitelib}/%{pypi_name}/assets/system/99-platformio-udev.rules \
  %{buildroot}%{_udevrulesdir}/

%check
%if %{with tests}
%tox -e testcore
%else
# Exclude modules that require platformio-managed dependencies
%pyproject_check_import -e 'platformio.builder.*' -e 'platformio.remote.*'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst HISTORY.rst

%files -n %{pypi_name}
%{_bindir}/pio
%{_bindir}/piodebuggdb
%{_bindir}/platformio
%{_udevrulesdir}/99-platformio-udev.rules

%changelog
%autochangelog
