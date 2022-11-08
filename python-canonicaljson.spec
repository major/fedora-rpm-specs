%global modname canonicaljson

Name:           python-%{modname}
Version:        1.6.4
Release:        1%{?dist}
Summary:        Canonical JSON

License:        ASL 2.0
URL:            https://github.com/matrix-org/python-canonicaljson
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description \
Features:\
* Encodes objects and arrays as RFC 7159 JSON.\
* Sorts object keys so that you get the same result each time.\
* Has no inignificant whitespace to make the output as small as possible.\
* Escapes only the characters that must be escaped,\
  U+0000 to U+0019 / U+0022 / U+0056, to keep the output as small as possible.\
* Uses the shortest escape sequence for each escaped character.\
* Encodes the JSON as UTF-8.\
* Can encode frozendict immutable dictionaries.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %{_description}


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires -e py


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{modname}


%check
%tox -e py


%files -n python3-%{modname} -f %{pyproject_files}


%changelog
* Sun Nov 06 2022 Kai A. Hiller <V02460@gmail.com> - 1.6.4-1
- Update to 1.6.4
- Follow new Python packaging guidelines

* Fri Aug 05 2022 Kai A. Hiller <V02460@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-1
- 1.4.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.4-2
- Drop python2 subpackage

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-2
- Rebuilt for Python 3.7

* Thu May 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-1
- Initial package
