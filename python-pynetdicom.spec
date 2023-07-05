# Disable test with --without=tests
%bcond_without tests

%global forgeurl https://github.com/pydicom/pynetdicom

%global _description %{expand:
pynetdicom is a pure Python package that implements the DICOM
networking protocol. Working with pydicom, it allows the easy creation of 
DICOM Service Class Users (SCUs) and Service Class Providers (SCPs).}

Name:           python-pynetdicom
Version:        2.0.2

%forgemeta

Release:        5%{?dist}
Summary:        A Python implementation of the DICOM networking protocol

License:        MIT and (BSD or ASL 2.0)
URL:            %{forgeurl}
Source0:        %{forgesource}

# [MRG] Fix AttributeError tests for Python 3.11
# https://github.com/pydicom/pynetdicom/pull/754
#
# Fixes:
#
# Tests expecting an AttributeError fail on Python 3.11
# https://github.com/pydicom/pynetdicom/issues/753
#
# python-pynetdicom fails to build with Python 3.11: AssertionError: Regex
# pattern "can't set attribute" does not match "property 'as_scu' of
# 'PresentationContext' object has no setter"
# https://bugzilla.redhat.com/show_bug.cgi?id=2062104
Patch0:         %{forgeurl}/pull/754.patch
# [MRG] Make decoding error tests endian-independent
# https://github.com/pydicom/pynetdicom/pull/756
#
# Fixes:
#
# Certain decoding error tests fail on big-endian platforms
# https://github.com/pydicom/pynetdicom/issues/755
#
# Test failures on s390x: endianness bug
# https://bugzilla.redhat.com/show_bug.cgi?id=2064737
Patch1:         %{forgeurl}/pull/756.patch
# [MRG] Fix test missed when updating for pydicom changes
#
# Fixes:
#
# TestPrimitive_N_GET::test_assignment failed
# https://github.com/pydicom/pynetdicom/issues/773
Patch2:		774.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-pynetdicom
Summary:        %{summary}

BuildRequires: python3-devel
BuildRequires: python-unversioned-command
BuildRequires: make
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist pydicom} >= 2
BuildRequires: %{py3_dist sqlalchemy}

%if 0%{?fedora}
BuildRequires: %{py3_dist pytest}
BuildRequires: %{py3_dist pyfakefs}
BuildRequires: %{py3_dist sphinx}
BuildRequires: %{py3_dist sphinx-rtd-theme}
BuildRequires: %{py3_dist sphinx-copybutton}
BuildRequires: %{py3_dist sphinx-issues}
BuildRequires: %{py3_dist sqlalchemy}
%endif

%{?python_provide:%python_provide python3-pynetdicom}

%description -n python3-pynetdicom %_description
	
%if 0%{?fedora}
%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.
%endif

%prep
%forgeautosetup -p1

rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'
# Fix for sphinx 4.0
sed -i 's/add_stylesheet/add_css_file/' docs/conf.py

%build
%py3_build

%if 0%{?fedora}
export PYTHONPATH=../
make -C docs SPHINXBUILD=sphinx-build-3 html 
rm -rf docs/_build/html/{.doctrees,.buildinfo,.nojekyll} -vf
%endif

%install
%py3_install

# tests in the apps/ part not reliable, upstream advice to disable them
# https://github.com/pydicom/pynetdicom/issues/498
# tls tests are still failing intermittently
# PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest --deselect=pynetdicom/apps/tests -vvv -k "not test_tls_yes_server_yes_client and not test_tls_transfer and not test_typical"
%if 0%{?fedora}
%if %{with tests}
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest --deselect=pynetdicom/apps/tests -k "not test_tls_yes_server_yes_client and not test_tls_transfer and not test_typical and not test_scp_handler_dataset_path"
%endif
%endif

%files -n python3-pynetdicom
%license LICENCE.txt
%doc README.rst
%{python3_sitelib}/pynetdicom-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/pynetdicom

%if 0%{?fedora}
%files doc
%license LICENCE.txt
%doc docs/_build/html
%endif

%changelog
* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 2.0.2-5
- Rebuilt for Python 3.12

* Sat Jan 28 2023 Alessio <alciregi AT fedoraproject DOT org> - 2.0.2-4
- Fix spec file for EPEL9

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-2
- Drop support for i686

* Fri Aug 05 2022 Alessio <alciregi AT fedoraproject DOT org> - 2.0.2-1
- Update to 2.0.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.0.1-4
- Rebuilt for Python 3.11

* Wed Mar 16 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.1-3
- Python 3.11 patch (fix RHBZ#2062104)
- Endianness patch (fix RHBZ#2064737)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Alessio <alciregi AT fedoraproject DOT org> - 2.0.1-1
- Update to 2.0.1

* Mon Dec 27 2021 Alessio <alciregi AT fedoraproject DOT org> - 2.0.0-1
- Update to 2.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.7-3
- Add fix for sphinx 4.0
- https://bugzilla.redhat.com/show_bug.cgi?id=1977627

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.7-2
- Rebuilt for Python 3.10

* Tue Apr 20 2021 Alessio <alciregi AT fedoraproject DOT org> - 1.5.7-1
- Update to 1.5.7

* Thu Jan 28 2021 Alessio <alciregi AT fedoraproject DOT org> - 1.5.6-1
- Update to 1.5.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Alessio <alciregi AT fedoraproject DOT org> - 1.5.5-1
- Update to 1.5.5

* Thu Dec 17 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.4-1
- Update to 1.5.4

* Mon Aug 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.3-2
- Re-enable test_fsm in pytest

* Mon Aug 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.3-1
- 1.5.3 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.2-1
- 1.5.2 release

* Wed Jun 24 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.1-1
- 1.5.1 release

* Fri Jun 05 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.0-2
- Fixed dependecy with pydicom

* Mon Jun 01 2020 Alessio <alciregi AT fedoraproject DOT org> - 1.5.0-1
- 1.5.0 release

* Tue May 26 2020 Miro HronÄ¨ok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Alessio <alciregi AT fedoraproject DOT org> - 1.4.1-1
- Initial package

