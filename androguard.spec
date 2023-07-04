Name:           androguard
Version:        3.3.5
Release:        13%{?dist}
Summary:        Reverse engineering, mal- or goodware analysis of Android applications

License:        ASL 2.0
URL:            https://github.com/androguard/androguard/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-magic
BuildRequires:  python3-asn1crypto
BuildRequires:  python3-click
BuildRequires:  python3-future
BuildRequires:  python3-lxml
BuildRequires:  python3-ipython
BuildRequires:  python3-networkx
BuildRequires:  python3-pydot
BuildRequires:  desktop-file-utils

Requires:       python3-magic
Requires:       python3-pyperclip
Requires:       python3-qt5

%description
Androguard is a tool to play with Android files.

- DEX, ODEX
- APK
- Android's binary XML
- Android resources
- Disassemble DEX/ODEX bytecodes
- Decompiler for DEX/ODEX files

%package docs
Summary:        Androguard documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-programoutput
BuildRequires:  python3-sphinx_rtd_theme

%description docs
Documentation for Androguard.

%prep
%autosetup
sed -i -e '/^#!\//, 1d' androguard/cli/entry_points.py

%build
%py3_build

%install
%py3_install
PATH=%{buildroot}%{_bindir}:$PATH PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

for file in androarsc.py androaxml.py androcg.py androdd.py androdis.py androgui.py androlyze.py androsign.py; do
  mv %{buildroot}%{_bindir}/$file -T %{buildroot}%{_bindir}/$(echo "$file" | cut -f 1 -d '.')
done


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests \
  -k "not testMagic and not EntryPointsTest"

%files
%doc README.md
%license LICENCE-2.0
%{_bindir}/andro*
%{_datadir}/applications/%{name}.desktop
%{python3_sitelib}/%{name}/
%{python3_sitelib}/*.egg-info/

%files docs
%doc html examples

%changelog
* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 3.3.5-13
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 3.3.5-10
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.5-7
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.5-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.5-3
- Rebuilt for Python 3.9

* Wed Apr 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.5-2
- Add docs subpackage (rhbz#1786653)
- Enable tests
- Fix requirements

* Sat Dec 14 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.5-1
- Initial package for Fedora
