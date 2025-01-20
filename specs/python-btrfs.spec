Name: python-btrfs
Version: 14.1
Release: 5%{?dist}
Summary: Python module to inspect btrfs filesystems
# Automatically converted from old format: LGPLv3+ and MIT - review is highly recommended.
License: LGPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL: https://github.com/knorrie/python-btrfs
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-sphinx

%global _description %{expand:
The primary goal of this module is to be able to inspect the internals of an
existing filesystem for educational purposes.

The python module acts as a wrapper around the low level kernel calls and btrfs
data structures, presenting them as python objects with interesting attributes
and references to other objects.}

%description %_description

%package -n python3-btrfs
Summary: %{summary}
Suggests: %{name}-doc

%description -n python3-btrfs %_description

%package doc
Summary: %{summary}

%description doc %_description

%prep
%autosetup -p1 -n %{name}-%{version}
# Remove dangling symlink
rm -f examples/btrfs
# Don't pull additional dependencies in doc
find examples -type f -print0 | xargs -0 chmod 0644

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs
%make_build html
%make_build text
find build -name .buildinfo -delete
popd

%install
%pyproject_install
%pyproject_save_files -l btrfs
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 bin/btrfs-balance-least-used %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-orphan-cleaner-progress %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-space-calculator %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-usage-report %{buildroot}%{_bindir}
install -m 0644 man/* %{buildroot}%{_mandir}/man1

%files -n python3-btrfs -f %{pyproject_files}
%license COPYING.LESSER
%{_bindir}/*
%{_mandir}/man1/*

%files doc
%doc CHANGES README.md examples
%doc docs/build/html docs/build/text
%license COPYING.LESSER

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 14.1-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 14.1-2
- Rebuilt for Python 3.13

* Tue May 07 2024 Juan Orti Alcaine <jortialc@redhat.com> - 14.1-1
- Version 14.1 (RHBZ#2279616)

* Sat May 04 2024 Juan Orti Alcaine <jortialc@redhat.com> - 14-1
- Version 14 (RHBZ#2277962)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 13-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 13-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Juan Orti Alcaine <jortialc@redhat.com> - 13-4
- Add patch to fix builds with sphinx versions >= 4 (#1990368)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 13-2
- Rebuilt for Python 3.10

* Sat May 01 2021 Juan Orti Alcaine <jortialc@redhat.com> - 13-1
- Version 13 (#1955446)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Juan Orti Alcaine <jortialc@redhat.com> - 12-1
- Version 12 (#1888096)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 11-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 11-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 11-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 11-1
- Version 11

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 10-1
- Version 10
- License changed to LGPLv3+

* Tue Oct 23 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 9.1-2
- Suggests: python-btrfs-doc

* Mon Oct 22 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 9.1-1
- Version 9.1

* Mon Oct 22 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 9-1
- Version 9
- Create doc subpackage
- Use python_provide macro

* Fri Oct 12 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 8-6
- Add patch to support Python3.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 8-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 8-1
- Version 8

* Mon May 29 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 7-1
- Version 7

* Thu Mar 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 6-1
- Version 6
- Drop python2 subpackage

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 5-1
- Version 5

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 4-1
- Version 4

* Wed Nov 16 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.3-1
- Version 0.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.2.1-2
- Remove doc subpackage

* Wed Jul 13 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.2.1-1
- Initial package
