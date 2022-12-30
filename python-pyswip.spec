%global srcname pyswip

Name:           python-%{srcname}
Version:        0.2.10
Release:        9%{?dist}
Summary:        Python-SWI-Prolog bridge

License:        MIT
URL:            https://github.com/yuce/pyswip
Source0:        https://github.com/yuce/pyswip/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description
PySWIP is a Python - SWI-Prolog bridge enabling to query SWI-Prolog in your
Python programs. It features an (incomplete) SWI-Prolog foreign language
interface, a utility class that makes it easy querying with Prolog and also a
Pythonic interface.


%package     -n python3-%{srcname}
Summary:        %summary
# we need to require pl-devel because pyswip uses the unversioned libswipl.so
Requires:       pl-devel

# Patch for SWI-Prolog Version > 8.5.2
# See https://github.com/yuce/pyswip/pull/133
Patch0:        pyswip-version.patch

%description -n python3-%{srcname}
PySWIP is a Python - SWI-Prolog bridge enabling to query SWI-Prolog in your
Python programs. It features an (incomplete) SWI-Prolog foreign language
interface, a utility class that makes it easy querying with Prolog and also a
Pythonic interface.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
pytest-3 tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Dec 28 2022 Christoph Karl <pampelmuse [AT] gmx [DOT] at> - 0.2.10-9
- SPDX migration (checked, no change)

* Sun Dec 18 2022 Christoph Karl <pampelmuse [AT] gmx [DOT] at> - 0.2.10-8
- Patch for SWI-Prolog Version > 8.5.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.10-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.10-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Christoph Karl <pampelmuse [AT] gmx [DOT] at> - 0.2.10
- Revive with version 0.2.10

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.2.7-4
- Remove python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7

* Mon Jun 04 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6

* Fri May 25 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5.git72771d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-4.git72771d9
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3.git72771d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Till Hofmann <till.hofmann@posteo.de> - 0.2.3-2.git72771d9
- Don't glob %%{python_sitelib}/* but add files separately instead

* Sun Jan 15 2017 Till Hofmann <till.hofmann@posteo.de> - 0.2.3-1.git72771d9
- Initial package
