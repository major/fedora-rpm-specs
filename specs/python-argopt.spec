%{?python_enable_dependency_generator}
%global srcname argopt
%global _description \
Define your command line interface (CLI) from a docstring\
(rather than the other way around). Because it’s easy. It’s quick.\
Painless. Then focus on what’s actually important - using the arguments\
in the rest of your program.

Name:           python-%{srcname}
Version:        0.9.1
Release:        %autorelease
Summary:        Doc to argparse driven by docopt

License:        MPL-2.0
URL:            https://github.com/casperdcl/argopt
Source0:        %{pypi_source}

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENCE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
