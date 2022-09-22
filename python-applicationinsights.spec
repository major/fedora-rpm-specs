# tests are enabled by default
%bcond_without tests

%global         srcname     applicationinsights

Name:           python-%{srcname}
Version:        0.11.9
Release:        %autorelease
Summary:        Python support for Azure Application Insights API
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-test
%endif

%global _description %{expand:
This project extends the Application Insights API surface to support Python}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Fix incorrect line endings in the README.
sed -i 's/\r$//' README.rst


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files applicationinsights


%if %{with tests}
%check
PYTHONPATH=%{buildroot}/%{python3_sitelib} \
    %{__python3} -m unittest discover ./tests/
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
%autochangelog
