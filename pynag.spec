Summary: Python modules and utilities for Nagios plugins and configuration
Name: pynag
Version: 1.1.2
Release: 11%{?dist}
Source0: http://pypi.python.org/packages/source/p/pynag/pynag-%{version}.tar.gz
License: GPLv2
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: /usr/bin/pathfix.py
Url: http://pynag.org/
BuildArch: noarch

%description
Python modules and utilities for pragmatically handling Nagios configuration
file maintenance, status information, log file parsing and plug-in
development.

%package examples
Summary: Example scripts which manipulate Nagios configuration
Requires: pynag

%description examples
Example scripts which manipulate Nagios configuration files. Provided
are scripts which list services, do network discovery among other tasks.

%prep
%setup -q

pathfix.py -pni "%{__python3} %{py3_shbang_opts}" . ./examples/Model/parse-configmain.py

%build
%{__python3} setup.py build

%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install --prefix=/usr --root=$RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples
install -m 755 -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples/Model
install -m 755 -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples/Utils
install -m 755 -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples/Parsers
install -m 755 -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples/Plugins
install -m 755 examples/Model/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples/Model/
install -m 755 examples/Parsers/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples/Parsers/
install -m 755 examples/Plugins/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples/Plugins/


%files
%{python3_sitelib}/pynag*.egg-info
%{python3_sitelib}/pynag/
%{_bindir}/pynag
%{_mandir}/man1/pynag.1.gz

%doc AUTHORS README.md LICENSE CHANGES
%dir %{_datadir}/%{name}

%files examples
%{_datadir}/%{name}/examples
%doc examples/README

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.2-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.2-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 10 2014 Tomas Edwardsson <tommi@tommi.org> 0.9.1-1
- New upstream version

* Thu Jul 24 2014 Tomas Edwardsson <tommi@tommi.org> 0.9.0-1
- New upstream version

* Sun Jun 15 2014 Tomas Edwardsson <tommi@tommi.org> 0.8.9-1
- Updated to latest upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Tomas Edwardsson <tommi@tommi.org> 0.8.5-1
- Updated to latest upstream version

* Mon Jan 06 2014 Tomas Edwardsson <tommi@tommi.org> 0.7.0-2
- Update invalid changelog entries

* Sat Nov 02 2013 Tomas Edwardsson <tommi@tommi.org> 0.7.0-1
- New upstream version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Tomas Edwardsson <tommi@tommi.org> 0.5.0-1
- New upstream version

* Tue Apr 30 2013 Tomas Edwardsson <tommi@tommi.org> 0.4.9-1
- New upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Tomas Edwardsson <tommi@tommi.org> 0.4.8-1
- New upstream version

* Mon Sep 17 2012 Tomas Edwardsson <tommi@tommi.org> 0.4.6-1
- New upstream version
- Removed pynag-* scripts for a new binary, pynag

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  9 2012 Tomas Edwardsson <tommi@tommi.org> 0.4.1-6
- Simplified spec file, threw out lots of legacy conditionals
- Added Requires parent for pynag-examples

* Mon Jul  4 2011 Pall Sigurdsson <palli@opensource.is> - 0.4-1
- New upstream version
- Config refactoring
- New Model module

* Wed Apr 27 2011 Tomas Edwardsson <tommi@tommi.org> - 0.3-3
- Added examples package and moved example files there

* Wed Jan 26 2011 Tomas Edwardsson <tommi@tommi.org> - 0.3-2
- Fixes for spelling and some issues reported by rpmlint

* Sat Jan 22 2011 Tomas Edwardsson <tommi@tommi.org> - 0.3-1
- Initial RPM Creation, based heavily on the func spec file
