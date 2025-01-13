
%global pypi_name tinyhtml5

Name:           python-tinyhtml5
Version:        2.0.0
Release:        1%{?dist}
Summary:        HTML parser based on the WHATWG HTML specification
License:        MIT
URL:            https://github.com/CourtBouillon/tinyhtml5
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)


%description
tinyhtml5 is a HTML5 parser that transforms a possibly malformed HTML document
into an ElementTree tree. This module is a simplified fork of html5lib.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
tinyhtml5 is a HTML5 parser that transforms a possibly malformed HTML document
into an ElementTree tree. This module is a simplified fork of html5lib.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v -n auto

%files -n  python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Mon Jan 06 2025 Felix Schwarz <fschwarz@fedoraproject.org> 2.0.0-1
- initial package

