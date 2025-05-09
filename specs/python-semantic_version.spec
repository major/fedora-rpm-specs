Name:           python-semantic_version
Version:        2.10.0
Release:        %autorelease
Summary:        Library implementing the 'SemVer' scheme

License:        BSD-2-Clause
URL:            https://github.com/rbarrois/python-semanticversion
Source:         %{url}/archive/%{version}/python-semanticversion-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel

# Test dependencies manually cherry-picked from the [dev] extra
# Upstream uses nose2, but pytest works as well
BuildRequires:  python3-pytest
%if %{undefined rhel} || %{defined epel}
# Optional test dependency
BuildRequires:  python3-django
%endif

%global _description %{expand:
This small python library provides a few tools to handle semantic versioning in
Python.}

%description %{_description}

%package -n     python3-semantic_version
Summary:        %{summary}

%description -n python3-semantic_version %{_description}

%prep
%autosetup -p1 -n python-semanticversion-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l semantic_version

%check
%pytest

%files -n python3-semantic_version -f %{pyproject_files}
%doc README.rst ChangeLog CREDITS

%changelog
%autochangelog
