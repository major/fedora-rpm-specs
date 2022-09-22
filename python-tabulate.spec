%global srcname tabulate

Name:           python-%{srcname}
Version:        0.8.10
Release:        1%{?dist}
Summary:        Pretty-print tabular data in Python, a library and a command-line utility

License:        MIT
URL:            https://pypi.python.org/pypi/tabulate
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch

%global _description %{expand:
The main use cases of the library are:

* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Test deps
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(wcwidth)
BuildRequires:  python3dist(numpy)
%if ! 0%{?el9}
# The pandas backport is not finished yet in EPEL 9. See BZ 2032550.
# The BR is needed only for Pandas integration tests.
BuildRequires:  python3dist(pandas)
%endif
# widechars support
%{?python_extras_subpkg:Recommends: python3-%{srcname}+widechars}
%{!?python_extras_subpkg:Recommends: python%{python3_version}dist(wcwidth)}

%description -n python3-%{srcname} %{_description}

Python 3 version.

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{srcname} -i %{python3_sitelib}/%{srcname}*.egg-info widechars}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{pytest}

%files -n python3-%{srcname}
%license LICENSE
%doc README README.md
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}*.egg-info/
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*

%changelog
* Thu Aug 18 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.10-1
- Update to 0.8.10 (close RHBZ#2099766)
- Drop EPEL9 numpy workaround; the flexiblas-related crashes have been fixed

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.8.9-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 04 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.9-1
- Update to latest release
- replace nose with pytest
- drop no longer needed patch

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.7-3
- Add tabulate[widechars] subpackage

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.7-2
- Rebuilt for Python 3.9

* Sun Mar 29 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.8.7-1
- Update to 0.8.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.8.6-1
- Update to 0.8.6

* Wed Nov 20 12:21:20 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.5-2
- Remove all useless changes in spec

* Fri Oct 25 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.5-1
- Update to 0.8.5

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.3-3
- Remove py2 subpackage

* Sat Jan 26 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.3-2
- Fix FTBFS

* Sat Jan 26 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.3-1
- Update to latest upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Steve Traylen <steve.traylen@cern.ch> - 0.8.2-1
- Update to 0.8.2, Correct source URL.

* Tue Oct 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
- Run more tests

* Sun Oct 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.5-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.5-2
- Drop multiple versions of bins

* Tue Nov 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.5-1
- Initial package
