%bcond tests 1

%if 0%{?fedora} == 42
%bcond old_setuptools 1
%else
%bcond old_setuptools 0
%endif

Name:           python-standard-nntplib
Version:        3.13.0
Release:        %autorelease
Summary:        Standard library nntplib redistribution

License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
Source:         %{pypi_source standard_nntplib}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with old_setuptools}
BuildRequires:  sed
%endif
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-test
%endif


%global _description %{expand:
Python is moving forward! Python finally started to remove dead batteries. For
more information, see PEP 594.

If your project depends on nntplib, which has been removed from Python 3.13,
here is the redistribution.}

%description %_description

%package -n     python3-standard-nntplib
Summary:        %{summary}

%description -n python3-standard-nntplib %_description


%prep
%autosetup -p1 -n standard_nntplib-%{version}
%if %{with old_setuptools}
sed -i 's:setuptools>=75.0:setuptools>=74.0:' pyproject.toml
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l nntplib


%check
%pyproject_check_import
%if %{with tests}
# certfile not shipped
%pytest -v \
  --deselect tests/test_nntplib.py::LocalServerTests::test_starttls
%endif


%files -n python3-standard-nntplib -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
