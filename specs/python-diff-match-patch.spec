%global        projname diff-match-patch
%global        srcname diff_match_patch
%global        desc The Diff Match and Patch libraries offer robust algorithms to perform the \
operations required for synchronizing plain text.

Name:          python-diff-match-patch
Version:       20241021
Release:       2%{?dist}
Summary:       Algorithms for synchronizing plain text

License:       Apache-2.0
URL:           https://pypi.python.org/pypi/diff-match-patch/
Source0:       %{pypi_source %{srcname}}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

%description
%{desc}

%package -n python3-%{projname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{projname}}

%description -n python3-%{projname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%tox
%pytest


%files -n python3-%{projname} -f %{pyproject_files}
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20241021-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 David King <amigadave@amigadave.com> - 20241021-1
- Update to 20241221 (#2320599)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230430-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 20230430-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230430-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230430-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230430-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 David King <amigadave@amigadave.com> - 20230430-1
- Update to 20230430 (#2192250)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200713-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200713-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 20200713-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200713-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200713-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 20200713-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200713-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200713-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 David King <amigadave@amigadave.com> - 20200713-1
- Update to 20200713 (#1856495)

* Wed Jun 24 2020 David King <amigadave@amigadave.com> - 20181111-3
- BuildRequire python3-setuptools explicitly

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20181111-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 20181111-1
- Update to 20181111
- Drop shebang removal steps (fixed upstream)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 20121119-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 20121119-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 David King <amigadave@amigadave.com> - 20121119-6
- Remove Python 2 subpackage (#1629492)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 20121119-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Sep 27 2016 David King <amigadave@amigadave.com> - 20121119-1
- Initial Fedora packaging (#1379778)
