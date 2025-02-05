%global pypi_name hexbytes

Name:          python-%{pypi_name}
Version:       1.3.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python `bytes` subclass that decodes hex, with a readable console output
License:       MIT
URL:           https://github.com/ethereum/hexbytes
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-devel
BuildRequires: python3-eth-utils
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# FIXME requires internet-access
rm -f scripts/release/test_package.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
