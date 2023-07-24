# Disabled by default, rely on upstream's test
# Requires pytest-qt, not yet packaged in Fedora
%bcond_with tests

%global pypi_name vimiv-qt
%global binname vimiv
%global appdataid org.karlch.vimiv.qt

%global _description %{expand:
Vimiv is an image viewer with vim-like keybindings. It is written in python3
using the Qt5 toolkit and is free software, licensed under the GPL.

The initial GTK3 version of vimiv will no longer be maintained.

- Simple library browser
- Thumbnail mode
- Basic image editing
- Command line with tab completion
- Complete customization with style sheets

Full documentation is available at https://karlch.github.io/vimiv-qt.}


Name:           %{pypi_name}
Version:        0.8.0
Release:        10%{?dist}
Summary:        An image viewer with vim-like keybindings

License:        GPLv3+
URL:            https://karlch.github.io/vimiv-qt/
Source0:        https://github.com/karlch/vimiv-qt/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-qt5-devel
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-bdd}
BuildRequires:  %{py3_dist flaky}
%endif
# Not listed in setup.py
Requires: python3-piexif
# python3-qt5-base is pulled in but SVG requires python3-qt5
Requires: python3-qt5
# For icons
Requires: hicolor-icon-theme


# Replaces the vimiv package now
# Last version of vimiv in Fedora is 0.9.1-13
Provides:   vimiv = 0.9.2
Obsoletes:  vimiv < 0.9.1-14

%py_provides python3-%{binname}

%description %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Don't do the python bit there
mv -v misc/Makefile .
sed -i '/python3 setup.py install/ d' Makefile
sed -i '/LICENSE/ d' Makefile
# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install
%make_install

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appdataid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{binname}.desktop

%check
%if %{with tests}
%pytest
%endif

%files
%license LICENSE
%doc README.md
%{python3_sitearch}/%{binname}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{binname}
%{_bindir}/%{binname}
%{_datadir}/applications/%{binname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{binname}.*
%{_metainfodir}/%{appdataid}.metainfo.xml
%{_mandir}/man1/%{binname}.*

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 0.8.0-9
- Rebuilt for Python 3.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.8.0-4
- A little closer to running tests now that pytest-bdd *is* in Fedora
- Update obsolete macros

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.10

* Sun Mar 28 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.0-1
- Update to latest release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.7.0-1
- Update to new release

* Sat Mar 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.1-1
- Update to new release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-2
- Add python3-qt5 as dependency: required for SVG

* Wed Jan 15 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-1
- Update to 0.5.0

* Sat Nov 09 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.0-1
- Make description for doc package longer than summary
- Remove docs sub package

* Fri Nov 08 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.0-1
- Initial build
