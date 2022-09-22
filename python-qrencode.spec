%global modname qrencode

%global commit b75219e878f9913514d2f6c0438aaa3e37433382
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        1.2~git.1.%{shortcommit}
Release:        15%{?dist}
Summary:        Simple wrapper for the C qrencode

License:        MIT
URL:            https://github.com/Arachnid/pyqrencode
Source0:        %{url}/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  qrencode-devel

%description
A simple wrapper for the C qrencode.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
Requires:       python3-pillow%{?_isa}

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n py%{modname}-%{commit}

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{modname}/
%{python3_sitearch}/%{modname}-*.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2~git.1.b75219e-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2~git.1.b75219e-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2~git.1.b75219e-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2~git.1.b75219e-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2~git.1.b75219e-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2~git.1.b75219e-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2~git.1.b75219e-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2~git.1.b75219e-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2~git.1.b75219e-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2~git.1.b75219e-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2~git.1.b75219e-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2~git.1.b75219e-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 1.2~git.1.b75219e-3
- Rebuilt (libqrencode.so.4)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2~git.1.b75219e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2~git.1.b75219e-1
- Update to latest git

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.git.a58d28a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0-8.git.a58d28a
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.git.a58d28a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.git.a58d28a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.git.a58d28a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.git.a58d28a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0-3.git.a58d28a
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-2.git.a58d28a
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-1.git.a58d28a
- Initial package
