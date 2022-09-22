Name:           python-ovh
Version:        1.0.0
Release:        2%{?dist}
Summary:        Lightweight wrapper around OVHcloud's APIs

License:        BSD
URL:            https://github.com/ovh/python-ovh
Source:         %{url}/archive/v%{version}/python-ovh-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# For building man pages
BuildRequires:  make
BuildRequires:  python3dist(sphinx)

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
# Manual testing (see: https://github.com/ovh/python-ovh/issues/111):
# 1. Install the package
# 2. cd to [sources]/tests
# 3. Install pytest and mock using pip
# 4. Run: pytest .


%files -n python3-ovh -f %{pyproject_files}
%doc examples/ README.rst
%{_mandir}/man1/python-ovh.1*


%changelog
* Fri Aug 12 2022 Roman Inflianskas <rominf@aiven.io> - 1.0.0-2
- Add documentation

* Mon Jul 11 2022 Roman Inflianskas <rominf@aiven.io> - 1.0.0-1
- Initial package (rhbz#2106063)

