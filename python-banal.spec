%global pypi_name banal

Name:           python-%{pypi_name}
Version:        1.0.6
Release:        %autorelease
Summary:        Commons of stupid, simple Python micro functions

License:        MIT
URL:            https://github.com/pudo/banal
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global common_description %{expand:
Commons of Python micro-functions. This basically an out-sourced, shared utils
module with a focus on functions that buffer type uncertainties in Python.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
