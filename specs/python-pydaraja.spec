Name:           python-pydaraja
Version:        0.3.7
Release:        %autorelease
Summary:        Python wrapper for Mpesa's Daraja API

License:        MIT
URL:            https://github.com/raykipkorir/pydaraja
Source:         %{url}/archive/v%{version}/pydaraja-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This Python wrapper allows developers to seamlessly interact with the MPESA's
Daraja API and manage payment requests within their Python applications.

It streamlines and abstracts the complexity of integrating with the MPESA's
Daraja API, providing developers with a convenient and efficient means of
handling payment transactions.}

%description %_description

%package -n     python3-pydaraja
Summary:        %{summary}

%description -n python3-pydaraja %_description



%prep
%autosetup -p1 -n pydaraja-%{version}
# Relax setuptools version
sed -i 's/"setuptools>=80.8.0", "setuptools_scm==8.3.1"/"setuptools", "setuptools_scm"/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pydaraja


%check
%pyproject_check_import
%pytest

%files -n python3-pydaraja -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md

%changelog
%autochangelog
