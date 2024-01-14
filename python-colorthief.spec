# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global pypi_name colorthief
%global pypi_version 0.2.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        Grabs the dominant color or a representative color palette from an image

# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/382
# License file provided by Python module, see:
# rpm -q --licensefiles {python3_sitelib}/{name}-{version}.dist-info/LICENSE
License:        BSD-3-Clause
URL:            https://github.com/fengsp/color-thief-py
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
A Python module for grabbing the color palette from an image.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
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
%license LICENSE
%doc README.rst


%changelog
%autochangelog
