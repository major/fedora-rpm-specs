
Summary: Python bindings for QtWebEngine
Name:    pyqtwebengine
Version: 5.15.6
Release: 10%{?dist}

# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
Url:     https://www.riverbankcomputing.com/software/pyqt/
Source0: %{pypi_source PyQtWebEngine}
ExclusiveArch: %{qt5_qtwebengine_arches}

## downstream patches
# may not be needed anymore? -- rdieter
#Patch100: PyQtWebEngine-Timeline.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5WebEngine)

BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}
BuildRequires: python%{python3_pkgversion}-qt5
BuildRequires: python%{python3_pkgversion}-qt5-devel
BuildRequires: %{py3_dist sip} >= 5.3
BuildRequires: %{py3_dist PyQt-builder} >= 1

%description
%{summary}.

%package -n python%{python3_pkgversion}-qt5-webengine
Summary: Python3 bindings for Qt5 WebEngine
Requires:  python%{python3_pkgversion}-qt5%{?_isa}
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-webengine}
%description -n python%{python3_pkgversion}-qt5-webengine
%{summary}.

%package devel
Summary: Development files for %{name}
Conflicts: python%{python3_pkgversion}-qt5-devel < 5.12.1
Requires: %{py3_dist sip} >= 5.3
%description devel
%{summary}.

%package doc
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.


%prep
%setup -q -n PyQtWebEngine-%{version}


%build
PATH=%{_qt5_bindir}:$PATH ; export PATH

# Python 3 build:
sip-build \
  --no-make \
  --qmake=%{_qt5_qmake} \
  --api-dir=%{_qt5_datadir}/qsci/api/python \
  --verbose \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{build_cflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags}"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{build_ldflags}"'

%make_build -C build


%install

%make_install INSTALL_ROOT=%{buildroot} -C build

# ensure .so modules are executable for proper -debuginfo extraction
for i in %{buildroot}%{python3_sitearch}/PyQt5/*.so ; do
test -x $i  || chmod a+rx $i
done


%files -n python%{python3_pkgversion}-qt5-webengine
%doc README
%license LICENSE
%{python3_sitearch}/PyQtWebEngine-%{version}.dist-info/
%{python3_sitearch}/PyQt5/QtWebEngine.*
%{python3_sitearch}/PyQt5/QtWebEngineCore.*
%{python3_sitearch}/PyQt5/QtWebEngineWidgets.*

%files devel
%license LICENSE
%{python3_sitearch}/PyQt5/bindings/QtWebEngine*/

%files doc
# avoid dep on qscintilla-python, own %%_qt5_datadir/qsci/... here for now
%dir %{_qt5_datadir}/qsci/
%dir %{_qt5_datadir}/qsci/api/
%dir %{_qt5_datadir}/qsci/api/python/
%doc %{_qt5_datadir}/qsci/api/python/PyQtWebEngine.api


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 5.15.6-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.15.6-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 5.15.6-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 01 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-1
- Update to 5.15.6

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.15.4-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.15.4-1
- 5.15.4
- drop/simplify conditionals
- drop python2 support

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Scott Talbert <swt@techie.net> - 5.15.2-3
- Update to build with sip 5

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.15.2-2
- Rebuilt for Python 3.10

* Mon Feb 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.15.2-1
- 5.15.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.15.0-1
- 5.15.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.14.0-2
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.14.0-1
- 5.14.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.13.1-1
- 5.13.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.12.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-5
- fix/workaround -debug generation
- +python2 support on f30

* Thu Apr 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-4
- -devel: %%license LICENSE

* Wed Apr 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-3
- %%doc README
- %%license LICENSE
- -devel: Requires: sip
- use %%autosetup

* Wed Apr 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-2
- update Source0 URL
- use ExclusiveArch
- use %%build_cflags %%build_cxxflags %%build_ldflags
- BR: gcc-c++

* Sat Mar 23 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-1
- first try

