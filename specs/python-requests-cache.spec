%global pypi_name requests-cache
%global mod_name requests_cache

Name:           python-%{pypi_name}
Version:        1.3.2
Release:        %autorelease
Summary:        Persistent cache for requests library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/reclosedev/requests-cache
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/requests_cache-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

%description
requests-cache is a persistent HTTP cache that provides an easy way
to get better performance with the python requests library.

%package -n     python3-%{pypi_name}
Summary:        Persistent cache for requests library
Requires:       python3-requests

%description -n python3-%{pypi_name}
requests-cache is a persistent HTTP cache that provides an easy way
to get better performance with the python requests library.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n requests_cache-%{version}
%pyproject_patch_dependency url-normalize:drop_lower

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{mod_name}

%check
%pyproject_check_import -t

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
