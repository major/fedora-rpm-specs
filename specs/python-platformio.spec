%global forgeurl https://github.com/platformio/platformio-core
%global pypi_name platformio
%global srcname platformio-core

# Tests require Internet access
%bcond tests 0

Name:           python-%{pypi_name}
Version:        6.1.17
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
# Fedora: drop linters from test dependencies
Patch3:         platformio-no-linters.patch
# Update deps (allow starlette versions through 0.46)
# https://github.com/platformio/platformio-core/commit/145142ea6c1d97c92a62999d424c0dd712fbb9f5
Patch4:         %{forgeurl}/commit/145142ea6c1d97c92a62999d424c0dd712fbb9f5.patch
# Allow starlette versions through 0.47
# https://github.com/platformio/platformio-core/pull/5172
Patch5:         %{forgeurl}/pull/5172.patch

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
