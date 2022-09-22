%global srcname SysMonTask
%global uuid com.github.camelneeraj.%{name}

Name: sysmontask
Version: 1.3.9
Release: 6%{?dist}
Summary: Linux system monitor with the compactness and usefulness of WTM
BuildArch: noarch

# The entire source code is BSD except:
#  * LGPLv2+:   sysmontask/gi_composites.py
License: BSD and LGPLv2+

URL: https://github.com/KrispyCamel4u/SysMonTask
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: gtk3
Requires: hicolor-icon-theme

# For Log Plot utility
Recommends: python3-matplotlib

%description
Linux system monitor with the compactness and usefulness of Windows Task
Manager to allow higher control and monitoring.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build


%install
%py3_install

sed -i 's|/usr/bin/env python3|%{__python3}|' \
    %{buildroot}%{python3_sitelib}/%{name}/*.py

# E: non-executable-script
chmod +x %{buildroot}%{python3_sitelib}/%{name}/{disk,gpu,mem,%{name}}.py

# Remove duplicate LICENSE file
rm %{buildroot}%{_docdir}/%{name}/LICENSE


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc AUTHORS
%doc README.md
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{srcname}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.9-5
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.9-2
- Rebuilt for Python 3.10

* Fri Apr 16 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.9-1
- build(update): 1.3.9

* Fri Apr 16 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.7-2
- build: python3-matplotlib dep

* Fri Apr 16 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.7-1
- build(update): 1.3.7

* Thu Mar 11 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.1-0.5.beta.b
- build(update): 1.1.1-0.5.beta.b

* Thu Mar 04 2021 Alessio <alessio AT fedoraproject DOT org> - 1.1.1-0beta
- Initial RPM Release
