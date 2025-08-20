%global pypi_name pure-protobuf

Name:           python-%{pypi_name}
Version:        3.1.4
Release:        %autorelease
Summary:        Python implementation of Protocol Buffers data types with dataclasses support

License:        MIT
URL:            https://github.com/eigenein/protobuf

# Using github sources since tests not available on PyPI
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         poetry-strict.patch

BuildArch:      noarch

BuildRequires:  python3-devel
#BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(pytest-cov)
#BuildRequires:  python3-pydantic
#BuildRequires:  python3-pytest-benchmark
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

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n protobuf-%{version} -p1

sed -i s/0.0.0/%{version}/g pyproject.toml

# Fix shebangs
pushd pure_protobuf
sed -i 's|/usr/bin/env python3|%{_bindir}/python3|' \
    __init__.py
popd


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

# E: non-executable-script
pushd %{buildroot}%{python3_sitelib}/pure_protobuf/
chmod +x __init__.py
popd


#%%check
#%%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pure_protobuf/
%{python3_sitelib}/pure_protobuf-*.dist-info/

%changelog
%autochangelog
