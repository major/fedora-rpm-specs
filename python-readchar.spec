%global srcname readchar

Name:           python-%{srcname}
Version:        4.0.5
Release:        %autorelease
Summary:        Library to easily read single chars and key strokes

License:        MIT
URL:            https://github.com/magmax/python-readchar
# The PyPI tarball doesn't include tests so use GitHub instead
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov

%global _description %{expand:
This is package provides a library to easily read single chars and keystrokes.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
