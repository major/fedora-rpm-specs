
%global pypi_name zopfli

Name:           python-zopfli
Version:        0.2.1
Release:        3%{?dist}
Summary:        Zopfli module for python
License:        ASL 2.0
URL:            https://github.com/obp/py-zopfli
Source0:        %{pypi_source %{pypi_name} %{version} zip}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  zopfli-devel


%description
cPython bindings for zopfli.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
cPython bindings for zopfli.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# remove vendored zopfli
rm -rf zopfli

%generate_buildrequires
%pyproject_buildrequires -r -x test


%build
export USE_SYSTEM_ZOPFLI=1
%pyproject_wheel


%install
%pyproject_install


%check
export PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}}"
%{python3} tests/test_zopfli.py


%files -n  python3-%{pypi_name}
%license COPYING
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.11

* Thu Mar 03 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2.1-1
- update to 0.2.1

* Wed Mar 02 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2.0-1
- update to 0.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 17 2021 Parag Nemade <pnemade@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9 release

* Wed Aug 04 2021 Felix Schwarz <fschwarz@fedoraproject.org> 0.1.8-1
- initial package

