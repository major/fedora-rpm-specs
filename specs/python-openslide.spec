Name:           python-openslide
Version:        1.4.2
Release:        %autorelease
Summary:        Python bindings for the OpenSlide library

License:        LGPL-2.1-only
URL:            https://openslide.org/
Source0:        https://github.com/openslide/openslide-python/releases/download/v%{version}/openslide_python-%{version}.tar.xz

# Disable Intersphinx so it won't download inventories at build time
Patch0:         disable-intersphinx.patch
# Allow older setuptools and pytest 6
Patch1:         widen-versions.patch

BuildRequires:  gcc
BuildRequires:  openslide
BuildRequires:  python3dist(sphinx)
# There's a 'test' dependency group but %%pyproject_buildrequires isn't
# picking it up
BuildRequires:  python3dist(pytest)

%global _description %{expand:
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.  This package allows Python
programs to use OpenSlide.}

%description %_description


%package -n python3-openslide
Summary:        %{summary}
Requires:       openslide

%description -n python3-openslide %{_description}


%prep
%autosetup -n openslide_python-%{version} -p1

# Examples include bundled jQuery and OpenSeadragon
rm -rf examples


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
sphinx-build doc build/html
rm -r build/html/.buildinfo build/html/.doctrees


%install
%pyproject_install
%pyproject_save_files -l openslide


%check
%if 0%{?rhel} == 9
# pytest 6; no support for pythonpath setting
%pytest --import-mode append
%else
%pytest
%endif


%files -n python3-openslide -f %{pyproject_files}
%doc CHANGELOG.md build/html


%changelog
%autochangelog
