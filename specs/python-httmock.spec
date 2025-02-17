Name:           python-httmock
Version:        1.4.0
Release:        %autorelease
Summary:        A mocking library for requests
License:        Apache-2.0
URL:            https://github.com/patrys/httmock

# Switch to github at next release to avoid the extra Source1
Source0:        https://files.pythonhosted.org/packages/source/h/httmock/httmock-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/patrys/httmock/%{version}/tests.py

# Add a tox file.
# https://bugzilla.redhat.com/show_bug.cgi?id=2019409
Patch0:         https://patch-diff.githubusercontent.com/raw/patrys/httmock/pull/64.diff
BuildArch:      noarch
 
%global _description %{expand:
A mocking library for requests for Python.
You can use it to mock third-party APIs and test libraries 
that use requests internally}


%description %_description

%package -n     python3-httmock
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-httmock %_description


%prep
%autosetup -p1 -n httmock-%{version}
cp %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files httmock


%check
%{tox}


%files -n python3-httmock -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
