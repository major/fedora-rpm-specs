%global project_name sphinxext-opengraph
%global pypi_name    sphinxext_opengraph

Name:           python-%{project_name}
Version:        0.7.5
Release:        %autorelease
Summary:        Sphinx extension to generate unique OpenGraph metadata

License:        BSD
URL:            https://%{project_name}.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/s/%{project_name}/%{project_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
%{summary}.}

%description %_description

%package -n python3-%{project_name}
Summary:        %{summary}

%description -n python3-%{project_name} %_description

%prep
%autosetup -p1 -n %{project_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '*'


%files -n python3-%{project_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md


%changelog
%autochangelog
