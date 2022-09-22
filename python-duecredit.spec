%global srcname duecredit

%global _description %{expand: \
duecredit is being conceived to address the problem of inadequate citation of
scientific software and methods, and limited visibility of donation requests
for open-source software.

It provides a simple framework (at the moment for Python only) to embed
publication or other references in the original code so they are automatically
collected and reported to the user at the necessary level of reference detail,
i.e. only references for actually used functionality will be presented back if
software provides multiple citeable implementations.}

Name:           python-%{srcname}
Version:        0.9.1
Release:        5%{?dist}
Summary:        Automated collection and reporting of citations

License:        BSD
URL:            https://github.com/%{srcname}/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist citeproc-py}
BuildRequires:  %{py3_dist lxml}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist vcrpy}

Requires:       %{py3_dist six}
Requires:       %{py3_dist citeproc-py}
Requires:       %{py3_dist requests}


%description -n python3-%{srcname}
%{_description}

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}
rm -rfv *egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{pytest} duecredit/tests --ignore=duecredit/tests/test_io.py

%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}*

%files doc
%license LICENSE
%doc examples/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.1-2
- Rebuilt for Python 3.10

* Sat May 22 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-1
- Update to latest release

* Sun Mar 28 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.1-1
- Update to latest release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.0-3
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.0-1
- Update to 0.8.0
- Remove py2 bits

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.7.0-1
- Update to 0.7.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.4-2
- Shorten summary
- Remove stray empty line in description
- Improve description for doc package

* Sat Nov 03 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.4-1
- Update to new version
- Only install py3 bin
- Use macro for description
- use pydist macros
- use pypi_source macro

* Wed Nov 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.4.4.1-1
- Initial package
