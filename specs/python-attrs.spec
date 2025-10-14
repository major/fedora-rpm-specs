# Avoid unwanted/unavailable dependencies in RHEL builds.
# Turn the tests off when bootstrapping Python, because pytest requires attrs
%bcond tests %{undefined rhel}

Name:           python-attrs
Version:        25.4.0
Release:        %autorelease
Summary:        Python attributes without boilerplate

# SPDX
License:        MIT
URL:            http://www.attrs.org/
BuildArch:      noarch
Source:         https://github.com/python-attrs/attrs/archive/%{version}/attrs-%{version}.tar.gz

BuildRequires:  python3-devel

%global _description %{expand:
attrs is an MIT-licensed Python package with class decorators that
ease the chores of implementing the most common attribute-related
object protocols.}

%description %{_description}

%package -n python3-attrs
Summary:        %{summary}

%description -n python3-attrs %{_description}

%prep
%autosetup -p1 -n attrs-%{version}
# Remove undesired/optional test dependency on pympler
sed -i '/"pympler",/d' pyproject.toml

# Remove tests-mypy extra from tests-no-zope extra
sed -i "/attrs\[tests-mypy\]/d" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g tests}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l attr attrs

%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif

%files -n python3-attrs -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
