%global srcname dill

Name: python-%{srcname}
Version: 0.3.7
Release: 3%{?dist}
Summary: Serialize all of Python

License: BSD

URL: https://github.com/uqfoundation/dill
Source0: %{pypi_source}

BuildArch: noarch

%description
Dill extends python's 'pickle' module for serializing and de-serializing 
python objects to the majority of the built-in python types. 
Dill provides the user the same interface as the 'pickle' module, and also 
includes some additional features. In addition to pickling python objects, dill
provides the ability to save the state of an interpreter session in a single 
command. 

%package -n python3-%{srcname}
Summary:  %{summary}
BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
# the test script calls 'python', this is easier than patching it
BuildRequires: python-unversioned-command

%description -n python3-%{srcname}
Dill extends python's 'pickle' module for serializing and de-serializing 
python objects to the majority of the built-in python types. 
Dill provides the user the same interface as the 'pickle' module, and also 
includes some additional features. In addition to pickling python objects, dill
provides the ability to save the state of an interpreter session in a single 
command. 


%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

# Disabled at update to 0.3.6 as they're missing.
#%%check
#export PYTHONPATH=%{buildroot}%{python3_sitelib}
# this is how upstream runs the tests (minus a useless wrapper),
# pytest does not work:
# https://github.com/uqfoundation/dill/issues/460
#%{python3} tests/__main__.py

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%exclude %{_bindir}/undill
%exclude %{_bindir}/get_objgraph
%exclude %{_bindir}/get_gprof
%{python3_sitelib}/%{srcname}*

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.7-1
- New upstream source (0.3.7)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.6-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.3.6-1
- 0.3.6

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Adam Williamson <awilliam@redhat.com> - 0.3.5.1-3
- Backport several patches to fix Python 3.11 issues
- Backport PR #524 to fix test suite invocation
- Re-enable test suite, the way upstream runs it in tox

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.5.1-2
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.5.1-1
- New upstream source (0.3.5.1)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.4-1
- New upstream source (0.3.4)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.3-1
- New upstream source (0.3.3)
- Upstream compressed with zip

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-1
- New upstream source (0.3.2)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Oct 02 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.1.1-1
- New upstream source (0.3.1.1)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.0-1
- New upstream source (0.3.0)

* Wed Feb 13 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.9-1
- New upstream source (0.2.9)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.8.2-2
- Drop python2 subpackage

* Tue Aug 21 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.8.2-1
- New upstream source (0.2.8.2)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.7.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.7.1-2
- New upstream source (0.2.7.1)
- And the sources

* Tue Aug 08 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.6-3
- Fix %%python_provide invocation

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.6-1
- New upstream source (0.2.6)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.5-1
- New upstream source (0.2.5)
- Updated upstream url
- Pypi url updated

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.4-1
- New upstream source (0.2.4)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 12 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-2
- Add license macro
- Run tests
- Add numpy build req for tests

* Thu Sep 11 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-1
- New upstream (0.2.1)

* Fri Dec 13 2013 Sergio Pascual <sergio.pasra@gmail.com> - 0.2-0.1b1
- Initial specfile

