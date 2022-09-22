%global pypi_name surt

%global forgeurl https://github.com/internetarchive/surt
# Using a commit here as the release isn't tagged
# https://github.com/internetarchive/surt/issues/26
%global commit 6934c321b3e2f66af9c001d882475949f00570c5
%forgemeta

%global common_description %{expand:
SURT is a Python package to implement a Sort-friendly URI Reordering Transform,
which is a transformation applied to URIs which makes their left-to-right
representation better match the natural hierarchy of domain names.}

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        %autorelease
Summary:        Sort-friendly URI Reordering Transform (SURT) python package

License:        AGPLv3+
URL:            %{forgeurl}
# PyPI doesn't include tests so use the GitHub tarball instead
Source0:        %{forgesource}
# PR#27: Remove unnecessary shebangs
Patch0:         %{forgeurl}/pull/27.patch
BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files surt

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
