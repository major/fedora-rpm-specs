%global srcname sphinx-issues

Name:           python-%{srcname}
Version:        3.0.1
Release:        %autorelease
Summary:        Sphinx extension for linking to your project's issue tracker

License:        MIT
URL:            https://github.com/sloria/sphinx-issues
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%description
A Sphinx extension for linking to your project's issue tracker. Includes roles
for linking to issues, pull requests, user profiles, with built-in support for
GitHub (though this works with other services).


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
A Sphinx extension for linking to your project's issue tracker. Includes roles
for linking to issues, pull requests, user profiles, with built-in support for
GitHub (though this works with other services).


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_issues

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
