Name:           python-ovh
Version:        1.2.0
Release:        %autorelease
Summary:        Lightweight wrapper around OVHcloud's APIs

License:        BSD
URL:            https://github.com/ovh/python-ovh
Source:         %{url}/archive/v%{version}/python-ovh-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-requests-oauthlib >= 2.0.0
# For building man pages
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Lightweight wrapper around OVHcloud's APIs. Handles all the hard work
including credential creation and requests signing.
}

%description %_description

%package -n python3-ovh
Summary:        %{summary}

%description -n python3-ovh %_description


%prep
%autosetup -p1 -n python-ovh-%{version}

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel
cd docs/ && make man


%install
%pyproject_install
%pyproject_save_files ovh

mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 0644 docs/_build/man/python-ovh.1* %{buildroot}/%{_mandir}/man1/


%check
# Deselect network-dependent tests
%pytest --deselect tests/test_client.py::TestClient::test_endpoints


%files -n python3-ovh -f %{pyproject_files}
%doc examples/ README.rst
%{_mandir}/man1/python-ovh.1*


%changelog
%autochangelog
