%bcond testcoverage 0

Name:           rpmspectool
Version:        1.100.0
Release:        %autorelease
Summary:        Utility for dealing with RPM spec files

License:        GPL-3.0-or-later
URL:            https://github.com/nphilipp/rpmspectool
Source0:        %{pypi_source %{name}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  sed
# The dependencies needed for testing don’t get auto-generated.
BuildRequires:  python3dist(pytest)
%if %{with testcoverage}
BuildRequires:  python3dist(pytest-cov)
%endif

Requires:       python3-%{name} = %{version}-%{release}

%generate_buildrequires
%{pyproject_buildrequires}

%global _description %{expand:
The rpmspectool utility lets users expand and download sources and patches in
RPM spec files.}

%description %_description

%package -n python3-%{name}
Summary:        %{summary}

%description -n python3-%{name} %_description

This package contains the Python package used by the rpmspectool CLI.

%prep
%autosetup

%if %{without testcoverage}
cat << PYTESTINI > pytest.ini
[pytest]
addopts =
PYTESTINI
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}
sed -i -e 's|^\(.*/COPYING\)|%%license \1|g' %{pyproject_files}

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp shell-completions/bash/rpmspectool %{buildroot}%{_datadir}/bash-completion/completions/

%check
%pytest -v

%files
%license COPYING
%doc README.md
%{_bindir}/rpmspectool
%{_datadir}/bash-completion/

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
