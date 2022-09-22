Name:           androwarn
Version:        1.6.1
Release:        11%{?dist}
Summary:        Static code analyzer for malicious Android applications

# androwarn is LGPL, Twitter Bootstrap is ASL 2.0 and jQuery MIT
License:        LGPLv3+ and ASL 2.0 and MIT
URL:            https://github.com/maaaaz/androwarn
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Androwarn is a tool whose main aim is to detect and warn the user about
potential malicious behaviors developed by an Android application.

The detection is performed with the static analysis of the application's
Dalvik bytecode, represented as Smali, with the androguard library.

This analysis leads to the generation of a report, according to a technical
detail level chosen from the user.

%prep
%autosetup
rm -rf androwarn/{_SampleApplication,_SampleReports}
chmod -x androwarn/{README.md,COPYING,COPYING.LESSER}
# Handle requirements with dep generator
rm -rf androwarn/requirements.txt
sed -i -e "s/'argparse',//g" setup.py
sed -i -e '/^#!\//, 1d' androwarn/{__init__.py,androwarn.py,warn/*/*.py,warn/*/*/*.py}
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%files
%doc androwarn/README.md
%license androwarn/COPYING androwarn/COPYING.LESSER
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.1-10
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.1-7
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-4
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-3
- Enable dep generator and fix requirements handling

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-2
- Disable dep generator
- Add missing BR (rhbz#1790091)

* Sat Dec 14 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-1
- Initial package for Fedora
