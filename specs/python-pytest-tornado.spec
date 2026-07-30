%global srcname pytest-tornado
%global srcname_ pytest_tornado

Name:           python-%{srcname}
Version:        0.8.1
Release:        %autorelease
Summary:        Py.test plugin for testing of asynchronous tornado applications
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/eugeniy/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3-pkg-resources
Requires:       python3-pkg-resources

%global _description %{expand:
A py.test plugin providing fixtures and markers to simplify testing of
asynchronous tornado applications.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname_}

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
