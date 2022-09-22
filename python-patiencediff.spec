%global pypi_name patiencediff
Name:           python-%{pypi_name}
Version:        0.2.3
Release:        1%{?dist}
Summary:        Python implementation of the patiencediff algorithm

License:        GPLv2+
URL:            https://www.breezy-vcs.org/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  gcc

%global _description %{expand:
This package contains the implementation of the patiencediff algorithm, as
first described by Bram Cohen. Like Python's difflib, this module provides
both a convenience unified_diff function for the generation of unified diffs of
text files as well as a SequenceMatcher that can be used on arbitrary
lists. Patiencediff provides a good balance of performance, nice output for
humans, and implementation simplicity.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{pypi_name}
%license COPYING
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Sep 07 2022 Ondřej Pohořelský <opohorel@redhat.com> - 0.2.3-1
- Update to 0.2.3
- Resolves: rhbz#2124925

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.2-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.10

* Mon Mar 29 2021 Ondřej Pohořelský <opohorel@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Ondřej Pohořelský <opohorel@redhat.com> - 0.2.1-1
- Initial package.
