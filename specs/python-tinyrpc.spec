%global library tinyrpc
%global module tinyrpc

Name:       python-%{library}
Version:    1.1.7
Release:    4%{?dist}
Summary:    A modular RPC library
License:    MIT
URL:        https://github.com/mbr/%{library}

# tarball in pypy does not include tests
Source0:    https://github.com/mbr/%{library}/archive/%{version}.tar.gz

BuildArch:  noarch

%description
tinyrpc is a library for making and handling RPC calls in python.

%package -n python-%{library}-doc
Summary:   Documentation for tinyrpc library

%description -n python-%{library}-doc
Documentation for tinyrpc library

%package -n python3-%{library}
Summary:    A modular RPC library

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-gevent
BuildRequires:  python3-msgpack
BuildRequires:  python3-pika
BuildRequires:  python3-werkzeug
BuildRequires:  python3-zmq

%description -n python3-%{library}
tinyrpc is a library for making and handling RPC calls in python.


# gevent-websocket and jsonext are old and unmaintained
%pyproject_extras_subpkg -n python3-%{library} gevent
#        'httpclient': ['requests', 'websocket-client', 'gevent-websocket'],
#pyproject_extras_subpkg -n python3-%{library} httpclient
%pyproject_extras_subpkg -n python3-%{library} msgpack
%pyproject_extras_subpkg -n python3-%{library} rabbitmq
%pyproject_extras_subpkg -n python3-%{library} wsgi
%pyproject_extras_subpkg -n python3-%{library} zmq

%package -n python3-%{library}-tests
Summary:    Tests for python3-tinyrpc library

# Requirements are not generated automatically
Requires:  python3-gevent
Requires:  python3-msgpack
Requires:  python3-pika
Requires:  python3-werkzeug
Requires:  python3-zmq
Requires:  python3-%{library} = %{version}-%{release}

%description -n python3-%{library}-tests
Tests for  python3-tinyrpc library

%prep
%autosetup -n %{library}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Fix doc build with latest Sphinx
sed -i "s#'https://docs.python.org/3/': None#'python': ('https://docs.python.org/3', None)#" docs/conf.py
sed -i "s#'https://pyzmq.readthedocs.io/en/latest/': None#'pyzmq': ('https://pyzmq.readthedocs.io/en/latest/', None)#" docs/conf.py
sed -i "s#'http://docs.python-requests.org/en/latest/': None#'python-requests': ('http://docs.python-requests.org/en/latest/', None)#" docs/conf.py
sed -i "s#'http://werkzeug.pocoo.org/docs/': None#'werkzeug': ('http://werkzeug.pocoo.org/docs/', None)#" docs/conf.py
sed -i "s#'http://www.gevent.org/': None#'gevent': ('http://www.gevent.org/', None)#" docs/conf.py

# generate html docs
sphinx-build docs build/sphinx/html
# remove the sphinx-build leftovers
rm -rf build/sphinx/html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{module}
# Move tests
mkdir -p %{buildroot}%%{python3_sitelib}/%{library}/tests
mv %{buildroot}%{python3_sitelib}/tests %{buildroot}%{python3_sitelib}/%{library}/tests

%check
%pytest -rs -v

%files -n python-%{library}-doc
%license LICENSE
%doc build/sphinx/html README.rst

%files -n python3-%{library} -f %{pyproject_files}
%license LICENSE

%files -n python3-%{library}-tests
%license LICENSE
%{python3_sitelib}/%{module}/tests

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jun 07 2025 Python Maint <python-maint@redhat.com> - 1.1.7-3
- Rebuilt for Python 3.14

* Mon Feb 03 2025 Javier Peña <jpena@redhat.com> 1.1.7-2
- Fix doc build (#2329893)
- Fix minor typos

* Mon Feb 03 2025 Orion Poplawski <orion@nwra.com> - 1.1.7-1
- Update to 1.1.7
- Use pyproject macros
- Add extras sub-packages

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.1.4-10
- Rebuilt for Python 3.13

* Sun Feb 18 2024 Orion Poplawski <orion@nwra.com> - 1.1.4-9
- Use sphinx-build to build docs
- Drop obsolete requires

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.1.4-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.1.4-2
- Rebuilt for Python 3.11

* Thu Feb 17 2022 Karolina Kula <kkula@redhat.com> - 1.1.4-1
- Update to 1.1.4
- Remove ignored tests

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.3-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Alfredo Moralejo <amoralej@redhat.xom> - 1.0.1-1
- Update to 1.0.1
- Remove python2 subpackages as tinyrpc > 1 does not support python2.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Alfredo Moralejo <amoralej@redhat.com> - 0.9.1-4
- Remove python2 subpackages from Fedora.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-2
- Rebuilt for Python 3.7

* Wed Jun 06 2018 Alfredo Moralejo <amoralej@redhat.com> - 0.9.1-1
- Update to upstream version 0.9.1.

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5-7.20170523git1f38ac
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6.20170523git1f38ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5.20170523git1f38ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Lumír Balhar <lbalhar@redhat.com> - 0.5-4.20170523git1f38ac
- Move to the latest upstream commit
- Disable non-working tests
- Enable python3 subpackage

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Alfredo Moralejo <amoralej@redhat.com> 0.5-2
- Some fixes applied to spec.

* Thu Jan 12 2017 Alfredo Moralejo <amoralej@redhat.com> 0.5-1
- Initial spec
