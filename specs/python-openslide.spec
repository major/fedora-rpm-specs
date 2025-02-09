%global upstream_name openslide-python
%global sdist_name openslide_python

Name:           python-openslide
Version:        1.4.1
Release:        %autorelease
Summary:        Python bindings for the OpenSlide library

License:        LGPL-2.1-only
URL:            https://openslide.org/
Source0:        https://github.com/openslide/%{upstream_name}/releases/download/v%{version}/%{sdist_name}-%{version}.tar.xz

# Disable Intersphinx so it won't download inventories at build time
Patch0:         openslide-python-1.0.1-disable-intersphinx.patch

BuildRequires:  gcc
BuildRequires:  openslide
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pillow
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx

%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.  This package allows Python
programs to use OpenSlide.


%package -n python3-openslide
Summary:        Python 3 bindings for the OpenSlide library
Requires:       openslide
Requires:       python3-pillow
%{?python_provide:%python_provide python3-openslide}


%description -n python3-openslide
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.  This package allows Python 3
programs to use OpenSlide.


%prep
%autosetup -n %{sdist_name}-%{version} -p1

# Examples include bundled jQuery and OpenSeadragon
rm -rf examples


%build
%py3_build
sphinx-build doc build/html
rm -r build/html/.buildinfo build/html/.doctrees


%install
%py3_install


%check
%if 0%{?rhel} == 9
# pytest 6; no support for pythonpath setting
sed -i -e '/^minversion/ d' pyproject.toml
%pytest --import-mode append
%else
%pytest
%endif


%files -n python3-openslide
%doc CHANGELOG.md build/html
%license COPYING.LESSER
%{python3_sitearch}/openslide/
%{python3_sitearch}/*.egg-info/


%changelog
%autochangelog
