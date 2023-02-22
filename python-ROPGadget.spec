%global srcname ROPGadget

Name:           python-%{srcname}
Version:        7.2
Release:        1%{?dist}
Summary:        A tool to find ROP gadgets in program files

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/R/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/JonathanSalwan/ROPgadget/c29c50773ec7fb3df56396ce27fb71c3898c53ae/LICENSE_BSD.txt
Source2:        https://raw.githubusercontent.com/JonathanSalwan/ROPgadget/c29c50773ec7fb3df56396ce27fb71c3898c53ae/README.md

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist capstone}
BuildRequires:  %{py3_dist setuptools}

%description
ROPGadget lets you search your gadgets on your binaries to facilitate
your ROP exploitation. ROPgadget supports ELF, PE and Mach-O format on
x86, x64, ARM, ARM64, PowerPC, SPARC and MIPS architectures.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       %{py3_dist capstone}

%description -n python3-%{srcname}
ROPGadget lets you search your gadgets on your binaries to facilitate
your ROP exploitation. ROPgadget supports ELF, PE and Mach-O format on
x86, x64, ARM, ARM64, PowerPC, SPARC and MIPS architectures.

%prep
%autosetup -n %{srcname}-%{version}
cp -p %SOURCE1 .
cp -p %SOURCE2 .

%build
%py3_build

%install
%py3_install
for lib in $(find %{buildroot}%{python3_sitelib}/ropgadget/ -name "*.py"); do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done

%files -n python3-%{srcname}
%doc LICENSE_BSD.txt README.md
%{python3_sitelib}/ropgadget
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{_bindir}/*

%changelog
* Mon Feb 20 2023 W. Michael Petullo <mike@flyn.org> - 7.2-1
- New upstream version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.7-2
- Rebuilt for Python 3.11

* Fri May 13 2022 W. Michael Petullo <mike@flyn.org> - 6.7-1
- New upstream version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 W. Michael Petullo <mike@flyn.org> - 6.6-1
- New upstream version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.3-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.3-3
- Rebuilt for Python 3.9

* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> - 6.3-2
- Commit copy of README.md and LICENSE_BSD.txt

* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> - 6.3-1
- New upstream version
- Reflect change to license

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 W. Michael Petullo <mike@flyn.org> - 5.8-1
- New upstream version

* Thu Sep 05 2019 Miro Hrončok <mhroncok@redhat.com> - 5.4-6
- Subpackage python2-ROPGadget has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 W. Michael Petullo <mike@flyn.org> - 5.4-1
- Initial package
