%global pypi_name jsonstreams

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        %autorelease
Summary:        Python library for writing JSON documents as streams 

# MIT: main library
# BSD-2-Clause-Views AND MIT:
#   - etc/scripts/gen_pypi_simple.py.NOTICE
#   - etc/scripts/gen_pypi_simple.py.ABOUT
#   - etc/scripts/gen_pypi_simple.py
License:        MIT AND (BSD-2-Clause-Views AND MIT)
URL:            https://github.com/dcbaker/jsonstreams
Source:         %url/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%global common_description %{expand:
JSONstreams is a package that attempts to making writing JSON in a streaming
format easier. In contrast to the core json module, this package doesn't require
building a complete tree of dicts and lists before writing, instead it provides
a straightforward way to to write a JSON document without building the whole
data structure ahead of time.

JSONstreams considers there to be two basic types, the JSON array and the JSON
object, which correspond to Python's list and dict respectively, and can encode
any types that the json.JSONEncoder can, or can use an subclass to handle
additional types.

The interface is designed to be context manger centric. The Stream class, and
the Array and Object classes returned by the subarray and subobject methods
(respectively), can be used as context managers or not, but use as context
managers are recommended to ensure that each container is closed properly.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
License:        MIT AND BSD-2-Clause
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-doctools)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog
