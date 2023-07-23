%global pypi_name wsgi_intercept

%global common_desc \
It installs a WSGI application in place of a real URI for testing. \
Testing a WSGI application normally involves starting a server at \
a local host and port, then pointing your test code to that address. \
Instead,this library lets you intercept calls to any specific host/port \
combination and redirect them into a `WSGI application`_ importable by \
your test program.


Name:           python-%{pypi_name}
Version:        1.12.0
Release:        3%{?dist}
Summary:        wsgi_intercept installs a WSGI application in place of a real URI for testing

License:        MIT
URL:            https://github.com/cdent/wsgi-intercept
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        wsgi_intercept installs a WSGI application in place of a real URI for testing
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for the wsgi-intercept module

%description -n python-%{pypi_name}-doc
Documentation for the wsgi-intercept module


%prep
%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x testing -x docs

%build
%pyproject_wheel

# generate html docs
# Use tox macro -e docs once https://github.com/cdent/wsgi-intercept/pull/71 is merged
# and contained in a release.
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build docs build/sphinx
# remove the sphinx-build leftovers
rm -rf build/sphinx/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files wsgi_intercept

%check
# Use tox macro once https://github.com/cdent/wsgi-intercept/pull/71 is merged
# and contained in a release.
%{__python3} setup.py test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README
%license LICENSE
%exclude %{python3_sitelib}/%{pypi_name}/tests

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc build/sphinx

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.12.0-2
- Rebuilt for Python 3.12

* Mon Jul 03 2023 Joel Capitao <jcapitao@redhat.com> - 1.12.0-1
- Update to 1.12.0 (#2218071)
- Switch to pyproject-rpm-macros

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.11.0-2
- Rebuilt for Python 3.12

* Tue May 23 2023 Joel Capitao <jcapitao@redhat.com> - 1.11.0-1
- Update to 1.11.0 (#2140362)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Joel Capitao <jcapitao@redhat.com> - 1.10.0-1
- Update to 1.10.0 (#2040722)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.9.2-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-2
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Yatin Karel <ykarel@redhat.com> - 1.9.2-1
- Update to 1.9.2 (Resolves #1429737)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-12
- Subpackage python2-wsgi_intercept has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.2-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.2-7
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-4
- Rebuild for Python 3.6

* Wed May 11 2016 Chandan Kumar <chkumar246@gmail.com> - 1.2.2-3
- Added missing python3 macro in %%check

* Wed May 11 2016 Chandan Kumar <chkumar246@gmail.com> - 1.2.2-2
- Applied python3 Alan Pevec patch

* Wed May 05 2016 Chandan Kumar <chkumar246@gmail.com> - 1.2.2-1
- Bumped to version 1.2.2

* Mon Sep 21 2015 Chandan Kumar <chkumar246@gmail.com> - 0.10.3-2
- Fixed import error
- Removed test folder

* Wed Sep 16 2015 Chandan Kumar <chkumar246@gmail.com> - 0.10.3-1
- Initial package.
