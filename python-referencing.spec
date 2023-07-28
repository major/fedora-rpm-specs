%global srcname referencing

# For the test suite
%global testcommit fe891e8ae5af7b623ed88db1f48ffb53eba9da21
%global testshortcommit %(c=%{testcommit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0.30.0
Release:        %autorelease
Summary:        An implementation-agnostic implementation of JSON reference resolution
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source referencing}
# Data for running tests
Source1:        https://github.com/python-jsonschema/referencing-suite/archive/%{testcommit}/referencing-suite-%{testshortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-subtests)

%global _description %{expand:
An implementation-agnostic implementation of JSON reference resolution.
In other words, a way for e.g. JSON Schema tooling to resolve the $ref
keyword across all drafts without needing to implement support themselves.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version} -p1

# Unpack the test reference suite
%setup -q -n %{srcname}-%{version} -a1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
export REFERENCING_SUITE="%{_builddir}/%{srcname}-%{version}/referencing-suite-%{testcommit}"
%pyproject_check_import -e referencing.tests*
%pytest referencing/tests


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
%autochangelog
