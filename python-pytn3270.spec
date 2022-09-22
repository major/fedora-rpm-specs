%global pypi_name pytn3270

Name:           python-%{pypi_name}
Version:        0.12.0
Release:        %autorelease
Summary:        Python TN3270 library

License:        ISC
URL:            https://github.com/lowobservable/pytn3270
# PyPI is missing tests, so use the GitHub tarball instead
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Inspired by pyte, this is a pure Python TN3270 library providing data stream
parsing and in-memory emulation. It does not include a user interface or
routines to support automation, instead it is designed to be used to build
user-facing emulators and automation libraries.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tn3270

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
