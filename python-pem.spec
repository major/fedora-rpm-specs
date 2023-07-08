# tests are enabled by default
%bcond_without tests

%global         srcname     pem
%global         forgeurl    https://github.com/hynek/pem
Version:        23.1.0
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Easy PEM file parsing

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pretend)
BuildRequires:  python3dist(pyopenssl)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(service-identity)
BuildRequires:  python3dist(twisted)
%endif


%global _description %{expand:
pem is an MIT-licensed Python module for parsing and splitting of PEM files,
i.e. Base64-encoded DER keys and certificates.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgesetup


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pem


%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%autochangelog
