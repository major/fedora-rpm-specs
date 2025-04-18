%global pypi_name pure-protobuf

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        %autorelease
Summary:        Python implementation of Protocol Buffers data types with dataclasses support

License:        MIT
URL:            https://github.com/eigenein/protobuf

# Using github sources since tests not available on PyPI
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
%if 0%{?el8}
BuildRequires:  python3dist(dataclasses)
%endif

%global _description %{expand:
pure-protobuf allows you to take advantages of the standard dataclasses module
to define message types. It is preferred over the legacy interface for new
projects. The dataclasses interface is available in Python 3.6 and higher.

The legacy interface is deprecated and still available via pure_protobuf.legacy.

This guide describes how to use pure-protobuf to structure your data. It tries
to follow the standard developer guide. It also assumes that you're familiar
with Protocol Buffers.}

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n protobuf-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix shebangs
pushd pure_protobuf
sed -i 's|/usr/bin/env python3|%{_bindir}/python3|' \
    __init__.py dataclasses_.py
popd


%build
%py3_build


%install
%py3_install

# E: non-executable-script
pushd %{buildroot}%{python3_sitelib}/pure_protobuf/
chmod +x __init__.py dataclasses_.py
popd


%check
%{python3} -m pytest -v


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pure_protobuf-%{version}-py*.egg-info
%{python3_sitelib}/pure_protobuf/


%changelog
%autochangelog
