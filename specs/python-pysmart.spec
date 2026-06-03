Name:           python-pysmart
Version:        1.4.3
Release:        %autorelease
Summary:        Wrapper for smartctl (smartmontools)

License:        LGPL-2.1-or-later
URL:            https://github.com/truenas/py-SMART
Source:         %{pypi_source pysmart}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
pySMART is a simple Python wrapper for the smartctl component of smartmontools.
It is officially compatible with Linux, Windows and FreeBSD, as long as
smartctl is on the system path. Running with administrative rights is strongly
recommended, as smartctl cannot accurately detect all device types or parse all
SMART information without these permissions.}

%description %_description

%package -n     python3-pysmart
Summary:        %{summary}

%description -n python3-pysmart %_description


%prep
%autosetup -p1 -n pysmart-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pySMART


%check
%pyproject_check_import
# These tests work locally but not in mock or a containerized build environment.
%pytest -k "not test_device_creation and not test_generic_checks and not test_device_diagnostics and not test_device_iface_attributes and not test_device_attributes and not test_device_tests"


%files -n python3-pysmart -f %{pyproject_files}
%doc docs/

%changelog
%autochangelog
