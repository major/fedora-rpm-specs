%global _description %{expand:
cattrs is an open source Python library for structuring and
unstructuring data. cattrs works best with attrs classes and the usual
Python collections, but other kinds of classes are supported by
manually registering converters.}

Name:           python-cattrs
Version:        22.2.0
Release:        %autorelease
Summary:        Python library for structuring and unstructuring data

License:        MIT
URL:            https://pypi.python.org/pypi/cattrs
BuildArch:      noarch
Source0:        %{pypi_source cattrs}


BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-bson
BuildRequires:  python3-msgpack
BuildRequires:  python3-pyyaml
BuildRequires:  python3-tomlkit
BuildRequires:  python3-ujson

%description %_description

%package -n python3-cattrs
Summary:        %{summary}

%description -n python3-cattrs %_description

%prep
%autosetup -n cattrs-%{version}

# loosen requirement
sed -i 's/poetry-core.*"/poetry-core"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cattrs cattr

%check
# optional dev dep, not in Fedora, requires maturin which is not trivial to package
# https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/message/DBVZOGAQKFHIMK6MMEPX3OUDLBYGE2MY/
%pyproject_check_import -e *orjson*

%files -n python3-cattrs -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
