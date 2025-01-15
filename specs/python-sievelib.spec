%global srcname sievelib

Name:           python-%{srcname}
Version:        1.4.2
Release:        1%{?dist}
Summary:        Client-side SIEVE library
License:        MIT
URL:            https://github.com/tonioo/sievelib
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Client-side Sieve and Managesieve library written in Python.
* Sieve : An Email Filtering Language (RFC 5228).
* ManageSieve : A Protocol for Remotely Managing Sieve Scripts (RFC 5804).}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
# remove bundled egg-info
rm -rf %{srcname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sievelib

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license COPYING

%changelog
* Mon Jan 13 2025 Juan Orti Alcaine <jortialc@redhat.com> - 1.4.2-1
- Version 1.4.2 (RHBZ#2336381)
- nose replaced by pytest

* Wed Sep 04 2024 Juan Orti Alcaine <jortialc@redhat.com> - 1.4.1-1
- Version 1.4.1 (RHBZ#2298639)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.13

* Sat May 04 2024 Juan Orti Alcaine <jortialc@redhat.com> - 1.4.0-1
- Version 1.4.0 (RHBZ#2272060)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 1.2.1-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.2.1-1
- Version 1.2.1 (#1904992)

* Tue Nov 17 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.2.0-1
- Version 1.2.0 (#1890926)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.1.1-11
- Fix build with pip >= 20.1 (#1838484)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.1-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-1
- Version 1.1.1
- Github's tarball doesn't build, use Pypi instead.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.0-1
- Version 1.0.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.2-8
- Python3 changes

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.2-3
- Use python_provide macro

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 21 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9.2-1
- New version 0.9.2

* Mon Jun 29 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-5.20150629gite34fb54
- Add python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-3
- Use license macro

* Wed Dec 03 2014 Juan Orti <jorti@fedoraproject.org> - 0.8-2
- Remove python shebang from libraries
- Change URL to GitHub
- Include license file

* Tue Dec 02 2014 Juan Orti <jorti@fedoraproject.org> - 0.8-1
- Spec file cleanup

* Sat May 24 2014 Didier Fabert <didier.fabert@gmail.com> 0.0.4-1
- Initial RPM release
