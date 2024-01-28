%global desc IPython features (tab completion, syntax highlighting, better tracebacks,\
better introspection) right in pdb.
%global srcname ipdb
%global sum IPython enabled Python debugger


Name:           python-ipdb
Version:        0.13.13
Release:        6%{?dist}
BuildArch:      noarch

License:        BSD-3-Clause
Summary:        IPython enabled Python debugger
URL:            https://github.com/gotcha/%{srcname}/
Source0:        https://github.com/gotcha/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel


%description
%{desc}


%package -n python3-%{srcname}
Summary:        IPython enabled Python debugger

Requires:       python3-ipython
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-ipdb
%{desc}


%prep
%setup -q -n %{srcname}-%{version}
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ipdb


%check
# ipdb doesn't support using tox nor pytest
%{__python3} setup.py test


%files -n python3-%{srcname} -f %{pyproject_files}
%doc HISTORY.txt README.rst
%license COPYING.txt
%{_bindir}/ipdb3


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 0.13.13-3
- Rebuilt for Python 3.12

* Mon May 01 2023 Troy Curtis, Jr <troy@troycurtisjr.com> - 0.13.13-2
- Update to the newer Python macros to allow for easy EPEL9 support (#2185811)

* Sat Mar 18 2023 Troy Curtis, Jr <troy@troycurtisjr.com> - 0.13.13-1
- Update to 0.13.13

* Thu Jan 26 2023 Troy Curtis, Jr <troy@troycurtisjr.com> - 0.13.11-1
- Update to 0.13.11
- Change license to SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.13.4-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.13.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.13.4-1
- Update to 0.13.4 (#1884339).
- https://github.com/gotcha/ipdb/blob/0.13.4/HISTORY.txt

* Sun Sep 20 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.13.3-1
- Update to 0.13.3 (#1850323).
- https://github.com/gotcha/ipdb/blob/0.13.3/HISTORY.txt

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-2
- Rebuilt for Python 3.9

* Sat May 02 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.13.2-1
- Update to 0.13.2 (#1808623).
- https://github.com/gotcha/ipdb/blob/0.13.2/HISTORY.txt

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.12.3-1
- Update to 0.12.3 (#1779136).
- https://github.com/gotcha/ipdb/blob/0.12.3/HISTORY.txt

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2 (#1742353).
- https://github.com/gotcha/ipdb/blob/0.12.2/HISTORY.txt

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.12-1
- Update to 0.12 (#1690864).
- https://github.com/gotcha/ipdb/blob/0.12/HISTORY.txt

* Sun Feb 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11-5
- Drop Python 2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
