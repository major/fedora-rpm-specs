%global pypi_name baseconv

Name:          python-%{pypi_name}
Version:       1.2.2
Release:       %autorelease
BuildArch:     noarch
Summary:       A basic baseconv implementation in python
License:       PSF-2.0
URL:           https://github.com/semente/%{name}
VCS:           git:%{url}.git
Source0:       %{pypi_source %{name}}
BuildSystem:   pyproject
BuildOption(prep):    -n %{name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
