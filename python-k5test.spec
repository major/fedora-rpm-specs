Name:           python-k5test
Version:        0.10.3
Release:        %autorelease
Summary:        Library for testing Python apps in self-contained Kerberos 5 environments
# main source code is ISC
# k5test/realm.py is HPND-export-US-modify
License:        ISC AND HPND-export-US-modify
URL:            https://github.com/pythongssapi/k5test
Source:         %{pypi_source k5test}
# https://github.com/pythongssapi/k5test/pull/26
Patch:          0001-Include-both-license-files.patch
BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
k5test is a library for setting up self-contained Kerberos 5 environments, and
running Python unit tests inside those environments.  It is based on the file
of the same name found alongside the MIT Kerberos 5 unit tests.}


%description %{common_description}


%package -n python3-k5test
Summary:        %{summary}


%description -n python3-k5test %{common_description}


%prep
%autosetup -n k5test-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files k5test


%check
%pyproject_check_import


%files -n python3-k5test -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
