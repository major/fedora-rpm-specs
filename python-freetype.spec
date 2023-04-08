%global pypi_name freetype-py

Name:           python-freetype
Version:        2.3.0
Release:        %autorelease
Summary:        Python binding for the freetype library

License:        BSD
URL:            https://github.com/rougier/freetype-py
Source0:        %{pypi_source %{pypi_name} %{version} zip}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
# tests use tox
BuildRequires:  python3dist(tox-current-env)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(wheel)
BuildRequires:  freetype

%description
Freetype Python provides bindings for the FreeType library. Only the high-level
API is bound.

%package -n     python3-freetype
Summary:        %{summary}
%py_provides python3-freetype

%description -n python3-freetype
%{description}

%prep
%autosetup -n %{pypi_name}-%{version}

%py3_shebang_fix freetype/*.py
%py3_shebang_fix examples/*.py

rm -r freetype_py.egg-info

%build
%py3_build

%install
%py3_install

%check
%tox

%files -n python3-freetype
%doc examples README.rst
%license LICENSE.txt
%{python3_sitelib}/freetype/
%{python3_sitelib}/freetype_py-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
