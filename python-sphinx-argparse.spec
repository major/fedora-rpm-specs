%global srcname sphinx-argparse
%global sum Sphinx extension that automatically documents argparse commands and options

Name:           python-%{srcname}
Version:        0.4.0
Release:        %autorelease
Summary:        %{sum}
BuildArch:      noarch

License:        MIT
Url:            https://github.com/ashb/sphinx-argparse
Source0:        %{url}/releases/download/v%{version}/sphinx_argparse-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)

%description
Sphinx extension that automatically documents argparse commands and options

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
Sphinx extension that automatically documents argparse commands and options

%prep
%autosetup -n sphinx_argparse-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxarg

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
