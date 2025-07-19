%global srcname pydo

Name: python3-%{srcname}
Summary: PyDo - DigitalOcean python library
Version: 0.13.0
Release: 1%{?dist}

License: ASL 2.0

Url: https://github.com/digitalocean/%{srcname}
Source: https://github.com/digitalocean/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3dist(poetry-core)
BuildRequires: make

%global _description %{expand:
Official DigitalOcean Python Client based on the DO OpenAPIv3 specification.}
%description %_description

Summary: %{summary}

%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
# The tests are not included in their releases, so we cannot run them.
# We might want to think about checking out straight from git to include the
# tests.
# make test-mocked


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
