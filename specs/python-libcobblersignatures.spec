%global srcname libcobblersignatures

Name:           python-libcobblersignatures
Version:        0.4.0
Release:        %autorelease
Summary:        Library for working with cobbler signatures

License:        GPL-2.0-only
URL:            https://github.com/cobbler/libcobblersignatures
Source:         https://github.com/cobbler/libcobblersignatures/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This library should be the interface for all applications using cobbler
signatures.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# disable test that requires network
%pytest -k "not test_importsignatures_url"


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.*
%{_bindir}/cobbler-manage-signatures


%changelog
%autochangelog
