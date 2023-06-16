%global srcname sphinx-hoverxref
%global sum Sphinx extension to add tooltips on cross references

Name:           python-%{srcname}
Version:        0.5b1
Release:        11%{?dist}
Summary:        %{sum}
BuildArch:      noarch

License:        MIT
Url:            https://%{srcname}.readthedocs.io/en/latest/
Source0:        https://github.com/readthedocs/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%description
Sphinx extension to show a floating window (tooltips or modal dialogues) on the
cross references of the documentation embedding the content of the linked
section on them. With sphinx-hoverxref, you don’t need to click a link to see
what’s in there.


%package -n python3-%{srcname}
Requires:       python3-sphinx
BuildRequires:  python3-sphinx
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Sphinx extension to show a floating window (tooltips or modal dialogues) on the
cross references of the documentation embedding the content of the linked
section on them. With sphinx-hoverxref, you don’t need to click a link to see
what’s in there.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install
# remove superfluous files
rm -rf %{buildroot}%{python3_sitelib}/tests/


%check
pytest tests/


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/hoverxref/
%{python3_sitelib}/*egg-info/


%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.5b1-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5b1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5b1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5b1-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5b1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5b1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Tim Landscheidt <tim@tim-landscheidt.de> - 0.5b1-5
- Fix mangled URL

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5b1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5b1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5b1-2
- Don't glob sitelib contents

* Tue Aug 25 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5b1-1
- Initial package

