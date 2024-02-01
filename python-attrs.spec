%global modname attrs

%if 0%{?rhel}
# Avoid unwanted/unavailable dependencies in RHEL builds
%bcond_with tests
%else
# Turn the tests off when bootstrapping Python, because pytest requires attrs
%bcond_without tests
%endif

Name:           python-attrs
Version:        23.2.0
Release:        %autorelease
Summary:        Python attributes without boilerplate

# SPDX
License:        MIT
URL:            http://www.attrs.org/
BuildArch:      noarch
Source0:        https://github.com/python-attrs/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel

%description
attrs is an MIT-licensed Python package with class decorators that
ease the chores of implementing the most common attribute-related
object protocols.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

%description -n python%{python3_pkgversion}-%{modname}
attrs is an MIT-licensed Python package with class decorators that
ease the chores of implementing the most common attribute-related
object protocols.

%prep
%setup -q -n %{modname}-%{version}
# Remove undesired/optional test dependency on pympler
sed -i '/"pympler",/d' pyproject.toml

# Remove tests-mypy extra from tests-no-zope extra
sed -i "/attrs\[tests-mypy\]/d" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files attr attrs

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
