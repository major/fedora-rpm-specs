%global pypi_name spyder-kernels

# Use forge macros for pulling from GitHub
%global forgeurl https://github.com/spyder-ide/spyder-kernels

Name:           python-%{pypi_name}
Version:        3.0.0~b4
Release:        %autorelease
Epoch:          1
Summary:        Jupyter kernels for Spyder's console
%global tag v%{version_no_tilde %{quote:%nil}}
%forgemeta
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Package that provides Jupyter kernels for use with the consoles of
Spyder, the Scientific Python Development Environment.

These kernels can launched either through Spyder itself or in an
independent Python session, and allow for interactive or file-based
execution of Python code inside Spyder.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgesetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files spyder_kernels


%check
# Package doesn't provide any tests
# For the import test a lot of runtime dependencies are required, so we
# skip that as well
#%%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
#%%license LICENSE.txt
%doc README.md


%changelog
%autochangelog
