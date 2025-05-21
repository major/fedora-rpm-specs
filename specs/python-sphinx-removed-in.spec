%global pypi_name sphinx-removed-in

Name:           python-sphinx-removed-in
Version:        0.2.3
Release:        %autorelease
Summary:        versionremoved and removed-in directives for Sphinx
License:        BSD-3-Clause
URL:            https://github.com/MrSenko/sphinx-removed-in
Source:         %{url}/archive/v%{version}/sphinx-removed-in-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%package -n     python3-sphinx-removed-in
Summary:        %{summary}

%description -n python3-sphinx-removed-in
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%prep
%autosetup -p1 -n sphinx-removed-in-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sphinx_removed_in

%check
%pyproject_check_import
%pytest

%files -n python3-sphinx-removed-in -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
