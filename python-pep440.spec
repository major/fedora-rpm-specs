%bcond_without tests

%global _description %{expand:
A simple package with utils to check whether versions number match PEP 440.}

Name:           python-pep440
Version:        0.1.2
Release:        %{autorelease}
Summary:        A simple package with utils to check whether versions number match Pep 440

License:        MIT
URL:            https://pypi.org/pypi/pep440
Source0:        %{pypi_source pep440}

BuildArch:      noarch

%description %_description

%package -n python3-pep440
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-pep440 %_description


%prep
%autosetup -n pep440-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pep440


%check
%if %{with tests}
# skip test_cli test as they depend on pytest-console-scripts, which
# is not yet packaged to Fedora
%{pytest} -svv -k "not test_cli"
%endif


%files -n python3-pep440 -f %{pyproject_files}
%doc readme.md
%{_bindir}/pep440
%license LICENSE

%changelog
%autochangelog
