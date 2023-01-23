%global pypi_name term-background
%global srcname shell-term-background

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        %autorelease
Summary:        Figure out if a terminal has a dark or light background

License:        GPL-2.0-or-later
URL:            https://github.com/rocky/shell-term-background
# PyPI doesn't have a source tarball uploaded
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Python package to figure out if a terminal has a dark or light background.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files term_background

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING
%doc README.rst NEWS.md ChangeLog

%changelog
%autochangelog
