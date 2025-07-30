%{?python_enable_dependency_generator}
%global srcname frozendict

Name:           python-%{srcname}
Version:        2.4.6
Release:        %autorelease
Summary:        An immutable dictionary

License:        MIT
URL:            https://pypi.python.org/pypi/frozendict
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
frozendict is an immutable wrapper around dictionaries that implements
the complete mapping interface. It can be used as a drop-in
replacement for dictionaries where immutability is desired.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
# Build the python only version (no python 3.11 support)
export FROZENDICT_PURE_PY=1
%pyproject_wheel

%install
export FROZENDICT_PURE_PY=1
%pyproject_install
%pyproject_save_files -l %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
