%global srcname crochet

%global desc Crochet is an MIT-licensed library that makes it easier to use \
Twisted from regular blocking code. Some use cases include easily using Twisted \
from a blocking framework like Django or Flask, write a library that provides a \
blocking API, but uses Twisted for its implementation, port blocking code to \
Twisted more easily, by keeping a backwards compatibility layer, or allow \
normal Twisted programs that use threads to interact with Twisted more cleanly \
from their threaded parts

Name:           python-%{srcname}
Version:        1.10.0
Release:        13%{?dist}
Summary:        A library that makes it easier to use Twisted from blocking code

# With Python 3.10 test_shutdown leads to timeout. This is just temporary and
# can be removed once it is fixed.
Patch1:         0001-disable-failing-test.patch

License:        MIT
URL:            https://github.com/itamarst/crochet
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description
%{desc}


%package doc
Summary: Documentation for python-crochet

BuildRequires: make
BuildRequires:  python3-sphinx

%description doc
Documentation for python-crochet.


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-twisted
BuildRequires:  python3-wrapt


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build
make %{?_smp_mflags} -C docs html
rm docs/_build/html/.buildinfo


%install
%py3_install


%check
%{__python3} -m unittest discover -v crochet.tests


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/crochet/
%{python3_sitelib}/crochet-*.egg-info/


%files doc
%license LICENSE
%doc docs/_build/html


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.10.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.0-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Jeremy Cline <jcline@redhat.com> - 1.10.0-1
- Initial package.
