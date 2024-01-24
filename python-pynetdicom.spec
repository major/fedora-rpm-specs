%global forgeurl https://github.com/pydicom/pynetdicom

%global  commit      1511488ac60c45fedd457d82ff23675f4c3f6758
%global  date        20230720
%global  shortcommit %(c=%{commit}; echo ${c:0:8})

%global _description %{expand:
pynetdicom is a pure Python package that implements the DICOM
networking protocol. Working with pydicom, it allows the easy creation of 
DICOM Service Class Users (SCUs) and Service Class Providers (SCPs).}

Name:           python-pynetdicom
Version:        2.0.2^%{date}git%{shortcommit}

%forgemeta

Release:        2%{?dist}
Summary:        A Python implementation of the DICOM networking protocol

License:        MIT and (BSD or ASL 2.0)
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-pynetdicom
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command
BuildRequires:  make
BuildRequires:  %{py3_dist setuptools} %{py3_dist pytest}
BuildRequires:  %{py3_dist sphinx} %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist pydicom} >= 2
%if 0%{?fedora}
BuildRequires:  %{py3_dist pyfakefs}
BuildRequires:  %{py3_dist sphinx-copybutton}
BuildRequires:  %{py3_dist sphinx-issues}
BuildRequires:  %{py3_dist sqlalchemy}
%endif
%{?python_provide:%python_provide python3-pynetdicom}

%description -n python3-pynetdicom %_description

%prep
%forgeautosetup -p1

rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

#%check
# test_tls_yes_server_yes_client and test_tls_transfer are disabled. Upstream is investigating.
# https://github.com/pydicom/pynetdicom/issues/406 and https://github.com/pydicom/pynetdicom/issues/364
#PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest -k "not test_tls_yes_server_yes_client and not test_tls_transfer"

# tests in the apps/ part not reliable, upstream advice to disable them
# https://github.com/pydicom/pynetdicom/issues/498
# tls tests are still failing intermittently
# PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest --deselect=pynetdicom/apps/tests -vvv -k "not test_tls_yes_server_yes_client and not test_tls_transfer and not test_typical"
%if 0%{?fedora}
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest --deselect=pynetdicom/apps/tests -k "not test_tls_yes_server_yes_client and not test_tls_transfer and not test_typical"
%else
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m pytest --deselect=pynetdicom/apps/tests -k "not test_tls_yes_server_yes_client and not test_tls_transfer and not test_typical and not test_scp_handler_dataset_path"
%endif


%files -n python3-pynetdicom
%license LICENCE.txt
%doc README.rst
%{python3_sitelib}/pynetdicom-*-py*.egg-info
%{python3_sitelib}/pynetdicom

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2^20230720git1511488a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Alessio <alciregi AT fedoraproject DOT org> - 2.0.2-2
- Fixes for Python 3.12
- Remove documentation

* Mon Nov 21 2022 Alessio <alciregi AT fedoraproject DOT org> - 2.0.2-1
- Update to 2.0.2

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

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Alessio <alciregi AT fedoraproject DOT org> - 1.4.1-1
- Initial package
