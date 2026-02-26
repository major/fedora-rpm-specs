%global srcname pathable

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Object-oriented paths

License:        Apache-2.0
URL:            https://github.com/p1c2u/pathable
# The GitHub tarball contains tests; the PyPI sdist does not.
Source:         %{url}/archive/%{version}/pathable-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies; see [tool.poetry.dev-dependencies], but note that this
# contains both test dependencies and unwanted linters etc.
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A python library which provides traverse resources like paths and
access resources on demand with separate accessor layer.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%check
%pyproject_check_import
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
