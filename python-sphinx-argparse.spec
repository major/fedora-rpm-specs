%global srcname sphinx-argparse
%global sum Sphinx extension that automatically documents argparse commands and options

Name:           python-%{srcname}
Version:        0.3.1
Release:        %autorelease
Summary:        %{sum}
BuildArch:      noarch

License:        MIT
Url:            https://github.com/ashb/sphinx-argparse
Source0:        https://github.com/ashb/sphinx-argparse/archive/%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Sphinx extension that automatically documents argparse commands and options

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
Sphinx extension that automatically documents argparse commands and options

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxarg

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
%autochangelog
