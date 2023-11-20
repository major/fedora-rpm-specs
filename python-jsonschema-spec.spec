%global srcname jsonschema-spec
%global modname jsonschema_spec

Name:           python-%{srcname}
Version:        0.2.4
Release:        %autorelease
Summary:        JSONSchema Spec with object-oriented paths

License:        Apache-2.0
URL:            https://github.com/p1c2u/%{srcname}
# The GitHub archive has the tests; the PyPI sdist does not.
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# A temporary workaround to avoid FTI
# We need to retire jsonschema-spec as soon as openapi-core releases a new version
# which switches to the renamed package jsonschema-path
Patch:          relax-dependencies.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(responses)

%global _description %{expand:
A python library which provides traverse JSON resources like paths and
access resources on demand with separate accessor layer.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version} -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
