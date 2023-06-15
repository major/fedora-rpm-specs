%global modname visionegg-quest
%global srcname Quest

# https://fedoraproject.org/wiki/Packaging:DistTag?rd=Packaging/DistTag#Conditionals
%if 0%{?fedora} < 30
%global with_py2 1
%else
%global with_py2 0
%endif

Name:           python-%{modname}
Version:        1.1
Release:        17%{?dist}
Summary:        QUEST algorithm for finding threshold

License:        BSD
URL:            http://visionegg.readthedocs.org/en/latest/Quest.html
Source0:        http://downloads.sourceforge.net/visionegg/%{srcname}-%{version}.tar.gz
Patch0:         0001-Fix-tab-mixing.patch
Patch1:         0002-py3-print_function.patch
Patch2:         0003-py3-raw_input.patch
Patch3:         0004-rename-to-visionegg-quest.patch
Patch4:         0005-remove-bool-constants-hack.patch

BuildArch:      noarch

%description
%{summary}.

%if %{with_py2}
%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
Requires:       %{py2_dist numpy}

%description -n python2-%{modname}
%{summary}.

Python 2 version.
%endif

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
Requires:       %{py3_dist numpy}

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%if %{with_py2}
%py2_build
%endif

%py3_build

%install
%if %{with_py2}
%py2_install
%endif

%py3_install

%if %{with_py2}
%files -n python2-%{modname}
%{python2_sitelib}/visionegg_quest-*.egg-info
%{python2_sitelib}/%{srcname}.py*
%endif

%files -n python3-%{modname}
%{python3_sitelib}/visionegg_quest-*.egg-info
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1-2
- Initial import
- Use conditional to disable py2 builds on F30+
- Use pyX_dist macro

* Sat Dec 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1-1
- Initial package
