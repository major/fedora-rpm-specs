Name:           python-exceptiongroup
Version:        1.3.0
Release:        %autorelease
Summary:        Backport of PEP 654 (exception groups)

# license clarification in https://github.com/agronholm/exceptiongroup/issues/150
License:        MIT or PSF-2.0
URL:            https://github.com/agronholm/exceptiongroup
Source:         %{pypi_source exceptiongroup}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This is a backport of the BaseExceptionGroup and ExceptionGroup classes
from Python 3.11.}

%description %_description

%package -n     python3-exceptiongroup
Summary:        %{summary}

%description -n python3-exceptiongroup %_description

%prep
%autosetup -p1 -n exceptiongroup-%{version}

# test failure fix
sed -i 's/range(10000)/range(150_000)/g' tests/test_exceptions.py

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l exceptiongroup

%check
%pyproject_check_import
%pytest -vv

%files -n python3-exceptiongroup -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
