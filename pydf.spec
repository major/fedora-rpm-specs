%global srcname pydf

Summary:        Fully colorized df clone written in python
Name:           pydf
Version:        12
Release:        13%{?dist}
License:        Public Domain
URL:            https://pypi.python.org/pypi/%{srcname}/%{version}
Source0:        http://kassiopeia.juls.savba.sk/~garabik/software/%{srcname}/%{name}_%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
pydf displays the amount of used and available space on your file systems,
just like df, but in colors. The output format is completely customizable.

%prep
%autosetup -n %{srcname}-%{version}

# Change shebang in individual files
sed -i '1s=^#!\s*/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' pydf

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_sysconfdir}/man1
install -p -m 755 pydf %{buildroot}/%{_bindir}
install -p -m 644 pydf.1 %{buildroot}/%{_mandir}/man1
install -p -m 644 pydfrc %{buildroot}/%{_sysconfdir}

%files
%license COPYING
%doc README COPYING
%{_bindir}/pydf
%{_mandir}/man1/pydf.1*
%config(noreplace) %{_sysconfdir}/pydfrc

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 12-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Artem Goncharov <artem.goncharov@gmail.com> 12-1
- Update to version 12
- Switch to Python3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild


* Mon May 2 2011 Clint Savage <herlo@fedoraproject.org> 9-3
- Removing define and properly adding other docs

* Sun May 1 2011 Clint Savage <herlo@fedoraproject.org> 9-2
- Fixing minor packaging issues

* Fri Apr 29 2011 Clint Savage <herlo@fedoraproject.org> 9-1
- Initial package build
