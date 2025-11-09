%global pypi_name aioitertools

Name:           python-%{pypi_name}
Version:        0.13.0
Release:        %autorelease
Summary:        Itertools and builtins for AsyncIO and mixed iterables

License:        MIT
URL:            https://github.com/omnilib/aioitertools
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Implementation of itertools, builtins, and more for AsyncIO and mixed-type
iterables.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Implementation of itertools, builtins, and more for AsyncIO and mixed-type
iterables.

%prep
%autosetup -n %{pypi_name}-%{version}
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

%changelog
%autochangelog

