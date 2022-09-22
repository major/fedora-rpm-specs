%{?python_enable_dependency_generator}

%global revnum 146
%global commit 861aa67c37bd5939e87ae2d87de62c3ca652258f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           sgmanager
Version:        2.0.0
Release:        13+201801213git+%{revnum}.%{shortcommit}%{?dist}
Summary:        OpenStack Security Groups Management Tool

License:        BSD
URL:            https://github.com/gooddata/sgmanager
Source:         %{url}/archive/%{commit}/%{name}-%{version}~git+%{revnum}.%{shortcommit}.tar.gz

BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3-pip
BuildRequires:  /usr/bin/flit
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(orderedset)
BuildRequires:  python3dist(pyyaml)

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit}

%build
FLIT_NO_NETWORK=1 flit build --format wheel

%install
%py3_install_wheel sgmanager-2.0.0-py3-none-any.whl

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -vv

%files
%license LICENSE
%doc README.md
%{_bindir}/sgmanager
%{python3_sitelib}/sgmanager-*.dist-info/
%{python3_sitelib}/sgmanager/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13+201801213git+146.861aa67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.0-12+201801213git+146.861aa67
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11+201801213git+146.861aa67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10+201801213git+146.861aa67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-9+201801213git+146.861aa67
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8+201801213git+146.861aa67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7+201801213git+146.861aa67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-6+201801213git+146.861aa67
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5+201801213git+146.861aa67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4+201801213git+146.861aa67
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3+201801213git+146.861aa67
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2+201801213git+146.861aa67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-1+201801213git+146.861aa67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-0+201801213git+146.861aa67
- Update to latest snapshot

* Tue Sep 04 2018 Igor Gnatenko <igor@gooddata.com> - 2.0.0-0+20180906git+116.a420e38
- Initial package
