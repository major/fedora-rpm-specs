%global pypi_name Pallets-Sphinx-Themes

Name:           python-%{pypi_name}
Version:        2.5.0
Release:        %autorelease
Summary:        Sphinx themes for Pallets and related projects

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/pallets/pallets-sphinx-themes/
Source0:        %{pypi_source pallets_sphinx_themes}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Pallets Sphinx Themes Themes for the Pallets projects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3-sphinx
%description -n python3-%{pypi_name}
Pallets Sphinx Themes Themes for the Pallets projects.


%prep
%autosetup -n pallets_sphinx_themes-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pallets_sphinx_themes

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md CHANGES.md

%changelog
%autochangelog
