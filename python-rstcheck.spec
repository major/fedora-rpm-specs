Name:       python-rstcheck
Version:    3.3.1
Release:    %autorelease
Summary:    Checks syntax of reStructuredText and code blocks nested within it

License:    MIT
URL:        https://github.com/myint/rstcheck
Source0:    %{pypi_source rstcheck}


BuildArch:  noarch
%description
Checks syntax of reStructuredText and code blocks nested within it.

%package -n python3-rstcheck
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Summary:        %{summary}

%description -n python3-rstcheck
Checks syntax of reStructuredText and code blocks nested within it.


%prep
%autosetup -n rstcheck-%{version}
# remove shebang
sed -i '1d' rstcheck.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files rstcheck

%check
%pyproject_check_import

%files -n python3-rstcheck -f %{pyproject_files}
%doc README.rst AUTHORS.rst
%{_bindir}/rstcheck

%changelog
%autochangelog
