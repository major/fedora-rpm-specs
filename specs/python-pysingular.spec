Name:           python-pysingular
Version:        0.9.7
Release:        22%{?dist}
Summary:        Python interface to Singular

License:        GPL-2.0-or-later
URL:            https://github.com/sebasguts/PySingular
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/PySingular-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Singular)
BuildRequires:  python3-devel

%global _description %{expand:
This package contains a basic interface to call Singular from python.
It is meant to be used in the Jupyter interface to Singular.}

%description %_description

%package     -n python3-pysingular
Summary:        Python 3 interface to Singular

%description -n python3-pysingular %_description

%prep
%autosetup -n PySingular-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l PySingular

%check
%pyproject_check_import

%files -n python3-pysingular -f %{pyproject_files}
%doc README
%license GPLv2

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Jerry James <loganjerry@gmail.com> - 0.9.7-21
- Rebuild for Singular 4.4.0p2

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.7-20
- Rebuilt for Python 3.13

* Fri Feb 23 2024 Jerry James <loganjerry@gmail.com> - 0.9.7-19
- Rebuild for Singular 4.3.2p8

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0.9.7-16
- Stop building for 32-bit x86

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.7-15
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.9.7-14
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Jerry James <loganjerry@gmail.com> - 0.9.7-13
- Rebuild for Singular 4.3.1p1

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.9.7-12
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.7-11
- Rebuilt for Python 3.11

* Mon Mar 21 2022 Jerry James <loganjerry@gmail.com> - 0.9.7-10
- Rebuild for Singular 4.2.1p3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 0.9.7-7
- Rebuild for Singular 4.2.0p2

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.7-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 0.9.7-1
- Initial RPM
