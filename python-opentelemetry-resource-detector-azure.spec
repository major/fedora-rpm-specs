Name:           python-opentelemetry-resource-detector-azure
Version:        0.1.3
Release:        %autorelease
Summary:        OpenTelemetry Resource detectors for Azure

License:        Apache-2.0
URL:            https://pypi.org/project/opentelemetry-resource-detector-azure
Source:         %{pypi_source opentelemetry_resource_detector_azure}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

# README.rst has CRLF line terminators in the PyPI sdist, but not in the GitHub
# repository at https://github.com/open-telemetry/opentelemetry-python-contrib/
BuildRequires:  dos2unix

%global common_description %{expand:
This library contains OpenTelemetry Resource Detectors for the following Azure
resources:

  • Azure App Service
  • Azure Virtual Machines}

%description %{common_description}


%package -n python3-opentelemetry-resource-detector-azure
Summary:        %{summary}

%description -n python3-opentelemetry-resource-detector-azure %{common_description}


%prep
%autosetup -n opentelemetry_resource_detector_azure-%{version}

dos2unix --keepdate README.rst


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
# The opentelemetry and opentelemetry/sdk directies are shared
# namespace package directories; they are co-owned with other opentelemetry
# packages, including subpackages of python-opentelemetry and/or
# python-opentelemetry-contrib. See RHBZ#1935266.
%pyproject_save_files -l opentelemetry


%check
# Test failure regression in TestAzureVMResourceDetector
# https://github.com/open-telemetry/opentelemetry-python-contrib/issues/2102
k="${k-}${k+ and }not (TestAzureVMResourceDetector and test_linux)"
k="${k-}${k+ and }not (TestAzureVMResourceDetector and test_windows)"

%pytest -k "${k-}" -v


%files -n python3-opentelemetry-resource-detector-azure -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
