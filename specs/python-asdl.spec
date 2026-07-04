Name:           python-asdl
Version:        0.1.5
Release:        %autorelease
Summary:        A copy of the ASDL parser used in CPython 3.5

License:        PSF-2.0
URL:            https://github.com/fpoli/python-asdl
# Sources on PyPI do not have tests
Source:         %{url}/archive/%{version}/asdl-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(nose2)

%global _description %{expand:
A copy of the ASDL parser used in CPython 3.5, cleaned a bit.}

%description %_description

%package -n     python3-asdl
Summary:        %{summary}

%description -n python3-asdl %_description


%prep
%autosetup -p1 -n python-asdl-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l asdl

%check
%pyproject_check_import
%{py3_test_envvars} nose2

%files -n python3-asdl -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
