%global srcname affine

Name:           python-%{srcname}
Version:        3.0.1
Release:        %autorelease
Summary:        Matrices describing affine transformation of the plane

License:        BSD-3-Clause
URL:            https://github.com/rasterio/affine
Source:         %pypi_source %{srcname}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Matrices describing affine transformation of the plane. The Affine package is
derived from Casey Duncan's Planar package.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1
%pyproject_patch_dependency pytest-cov:ignore

%generate_buildrequires
%pyproject_buildrequires -g tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} -v

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
