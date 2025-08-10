%global pypi_name asysocks

Name:           python-%{pypi_name}
Version:        0.2.17
Release:        %autorelease
Summary:        Socks5/Socks4 client and server library

License:        MIT
URL:            https://github.com/skelsec/asysocks
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
A Python Socks5/Socks4 client and server library.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' asysocks/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/asysock*

%changelog
%autochangelog
