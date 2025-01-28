%global srcname referencing

Name:           python-%{srcname}
Version:        0.36.2
Release:        %autorelease
Summary:        An implementation-agnostic implementation of JSON reference resolution
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %{pypi_source referencing}

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


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import -e referencing.tests*
%pytest referencing/tests


%files -n python3-%{srcname} -f %{pyproject_files}


%changelog
%autochangelog
