Name: python-pulp-glue
Version: 0.34.0
Release: 2%{?dist}
Summary: The version agnostic Pulp 3 client library in python

License: GPL-2.0-or-later
URL: https://github.com/pulp/pulp-cli
Source: %{url}/archive/%{version}/pulp-cli-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-pytest

%global _description %{expand:
pulp-glue is a library to ease the programmatic communication with the Pulp3
API. It helps to abstract different resource types with so called contexts and
allows to build or even provides complex workflows like chunked upload or
waiting on tasks.
It is built around an openapi3 parser to provide client side validation of http
requests, while accounting for known quirks and incompatibilities between
different Pulp server component versions.}

%description %_description


%package -n python3-pulp-glue
Summary: %{summary}

%description -n python3-pulp-glue %_description


%prep
%autosetup -p1 -n pulp-cli-%{version}/pulp-glue

# Remove the Python version upper bound to enable building with new versions in Fedora
# This will work up until 3.19, which should be enough for now
sed -i '/requires-python =/s/,<3\.[0-9]\+//' pyproject.toml

# Remove upper version bound on setuptools to enable building with new versions in Fedora
sed -i '/requires =.*setuptools/s/<[0-9]\+//' pyproject.toml

# Remove upper version bound on packaging to enable building with new versions in Fedora
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml

# Remove upper version bound on multidict to enable building with new versions in Fedora
sed -i '/"multidict/s/,<[0-9.]\+//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pulp_glue


%check
%pyproject_check_import pulp_glue.common.context
%pytest -m "not live"


%files -n python3-pulp-glue -f %{pyproject_files}
%license ../LICENSE
%doc README.*


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 09 2025 Matthias Dellweg <x9c4@redhat.com> - 0.34.0-1
- new version

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.32.1-4
- Rebuilt for Python 3.14

* Mon May 05 2025 Matthias Dellweg <x9c4@redhat.com> - 0.32.1-3
- Remove version constraint on multidict. (thanks romaingeissler1a)
- rebuilt

* Fri May 02 2025 Matthias Dellweg <x9c4@redhat.com> - 0.32.1-2
- Removed upper bound on required packaging. (thanks lbalhar)

* Mon Apr 07 2025 Matthias Dellweg <x9c4@redhat.com> - 0.32.1-1
- new version

* Mon Apr 07 2025 Matthias Dellweg <x9c4@redhat.com> - 0.32.0-1
- new version

* Thu Mar 20 2025 Matthias Dellweg <x9c4@redhat.com> - 0.31.1-1
- new version
- Removed upper bound on build-required setuptools.

* Sun Jan 26 2025 Matthias Dellweg <x9c4@redhat.com> - 0.30.0-3
- Rebuilt with adding tests.
- Removed upper bound on required Python. (thanks ksurma)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Matthias Dellweg <x9c4@redhat.com> - 0.30.0-1
- new version

* Tue Sep 24 2024 Matthias Dellweg <x9c4@redhat.com> - 0.29.2-1
- new version

* Tue Sep 17 2024 Matthias Dellweg <x9c4@redhat.com> - 0.29.1-1
- new version

* Tue Sep 17 2024 Matthias Dellweg <x9c4@redhat.com> - 0.29.0-1
- Bump version to 0.29.0.

* Wed Sep 11 2024 Matthias Dellweg <x9c4@redhat.com> - 0.28.3-1
- Initial specfile
