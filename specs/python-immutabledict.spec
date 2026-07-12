%bcond_without check

Name:           python-immutabledict
Version:        4.3.1
Release:        %autorelease
Summary:        Drop-in replacement for dictionaries where immutability is desired

License:        MIT
URL:            https://github.com/corenting/immutabledict
Source0:        %{url}/archive/v%{version}/immutabledict-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with check}
BuildRequires:  python3-pytest
%endif


%global _description %{expand:
Implements the complete mapping interface and can be used as a drop-in
replacement for dictionaries where immutability is desired. The immutabledict
constructor mimics dict, and all of the expected dictionary interfaces (such as
iteration, length, representation, hash, and item retrieval) are provided.}

%description %{_description}

%package -n python3-immutabledict
Summary:        %{summary}

%description -n python3-immutabledict %{_description}


%prep
%autosetup -p1 -n immutabledict-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l immutabledict


%if %{with check}
%check
%pyproject_check_import

%pytest
%endif


%files -n python3-immutabledict -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
