%global commit0 28e913e7114dae485747ccd8f9fd436ada2195f0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global snapdate 20250121

%global srcname migen

Name:           python-%{srcname}
Version:        0.9.2
Release:        30.%{snapdate}git%{shortcommit0}%{?dist}
Summary:        A Python toolbox for building complex digital hardware

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://m-labs.hk/%{srcname}
Source0:        https://github.com/m-labs/%{srcname}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# for the pdf manual:
BuildRequires:  make
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  python3-sphinx-latex

%description
Migen enables hardware designers to take advantage of the richness of
Python (object oriented programming, function parameters, generators,
operator overloading, libraries, etc.), to build well organized, reusable
and elegant digital hardware designs.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Migen enables hardware designers to take advantage of the richness of
Python (object oriented programming, function parameters, generators,
operator overloading, libraries, etc.), to build well organized, reusable
and elegant digital hardware designs.

%prep
%autosetup -n %{srcname}-%{commit0}
sed -r -i 's/(migen_version = ).*/\1"%{version}-%{release}"/' doc/conf.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
PYTHONPATH=. sphinx-build-3 -M latexpdf doc _build/pdf
PYTHONPATH=. sphinx-build-3 -b man doc _build/man

%install
%pyproject_install
%pyproject_save_files %{srcname}
install -Dpm644 -t %{buildroot}%{_mandir}/man1 _build/man/%{srcname}.1

%check
%tox

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md _build/pdf/latex/Migen.pdf
%{_mandir}/man1/%{srcname}.1*

%changelog
* Tue Jan 21 2025 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-26.20250121git28e913e
- update to newer snapshot

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-29.20240716git66f5963
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.2-28.20240716git66f5963
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-27.20240716git66f5963
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-26.20240716git66f5963
- update to newer snapshot

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.2-25.20231218git50934ad
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-24.20231218git50934ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-23.20231218git50934ad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2.22.20231218git50934ad
- update to newer snapshot
- build using pyproject.toml
- fix Python 3.13 FTBFS (BZ #2246280)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-21.20230215gitccaee68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.9.2-20.20230215gitccaee68
- Rebuilt for Python 3.12

* Wed Feb 15 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-19.20230215gitccaee68
- update to newer snapshot

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18.20230104git12eb563
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-17.20230104git12eb563
- update to newer snapshot

* Thu Oct 06 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-16.20221006git639e66f
- update to newer snapshot

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-15.20220705git0fb9173
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-14.20220705git0fb9173
- update to newer snapshot (incl. fix for Python 3.11, BZ 2069537)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.2-13.20211209git9a0be7a
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-12.20211209git9a0be7a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 09 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-11.20211209git9a0be7a
- update to newer snapshot

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-10.20210307git7014bdc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.2-9.20210307git7014bdc
- Rebuilt for Python 3.10

* Sun Mar 07 2021 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-8.20210307git7014bdc
- add buildrequires make (fix BZ 1935719)
- update to latest snapshot

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7.20201124gita5cc037
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-6.20201124gita5cc037
- fix "python3-sphinx-latex" build dependency name
- update to latest snapshot

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5.20200625gitb1b2b29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-4.20200625gitb1b2b29
- added setuptools build dependency
- updated to latest snapshot

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-3.20191204git4c00f5b
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2.20191204git4c00f5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.9.2-1.20191204git4c00f5b
- Update to 0.9.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-4.20190606git562c046
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3.20190606git562c046
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2.20190606git562c046
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.9.1-1.20190606git562c046
- Update to 0.9.1

* Mon May 20 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.8-0.4.20190520git9031bfe
- Update to newer snapshot.

* Mon Apr 15 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.8-0.3.20190415gitedcadbc
- Update to newer snapshot.

* Wed Feb 27 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.8-0.2.20190227git936732f
- Update to newer snapshot.

* Mon Feb 18 2019 Gabriel Somlo <gsomlo@gmail.com> - 0.8-0.1.20190218gitafe4405
- Initial version.
