%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%global webkit 1
%endif

%if 0%{?fedora} < 32 && 0%{?rhel} < 8
%global with_python2 1
%endif

%if 0%{?fedora} && 0%{?fedora} < 30
%global qtassistant 1
%endif

%if 0%{?with_python3}
%{!?python3_inc:%global python3_inc %(%{__python3} -c "from distutils.sysconfig import get_python_inc; print(get_python_inc(1))")}
%global python3_dbus_dir %(%{__python3} -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])")
%endif

%if 0%{?with_python2}
%{!?__python2:%global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch:%global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?python2_inc:%global python2_inc %(%{__python2} -c "from distutils.sysconfig import get_python_inc; print get_python_inc(1)")}
%global python2_dbus_dir %(%{__python2} -c "import dbus.mainloop; print(dbus.mainloop.__path__[0])")
%if 0%{?fedora} > 27
%global python2_dbus python2-dbus
%else
%global python2_dbus dbus-python
%endif
%endif

## f29+ no longer using separate sipdir for python3
%global py3_sipdir %{_datadir}/sip/PyQt4
#if 0%{?fedora} < 29
#global py3_sipdir %{_datadir}/python3-sip/PyQt4
#endif

Summary: Python bindings for Qt4
Name: 	 PyQt4
Version: 4.12.3
Release: 26%{?dist}

# GPLv2 exceptions(see GPL_EXCEPTIONS*.txt)
License: (GPLv3 or GPLv2 with exceptions) and BSD
Url:     http://www.riverbankcomputing.com/software/pyqt/
%if 0%{?snap:1}
Source0:  http://www.riverbankcomputing.com/static/Downloads/PyQt4/PyQt-x11-gpl-%{version}%{?snap:-snapshot-%{snap}}.tar.gz
%else
Source0:  http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-%{version}/PyQt4_gpl_x11-%{version}.tar.gz
%endif

Source2: pyuic4.sh

## upstreamable patches
Patch1: PyQt4_gpl_x11-4.12.3-ftbfs.patch

## upstream patches
# fix FTBFS on ARM
Patch60:  qreal_float_support.diff

# Fix Python 3.10 support (rhbz#1895298)
Patch61:  python310-pyobj_ascharbuf.patch

# Fix error: invalid use of undefined type 'struct _frame'
Patch62:  PyQt4-4.12.3-pyframe_getback.patch

# rhel patches
Patch300: PyQt-x11-gpl-4.11-webkit.patch

BuildRequires: make
BuildRequires: chrpath
BuildRequires: findutils
BuildRequires: gcc-c++
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-python)
BuildRequires: pkgconfig(phonon)
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtDeclarative) pkgconfig(QtDesigner)
BuildRequires: pkgconfig(QtGui) pkgconfig(QtHelp) pkgconfig(QtMultimedia)
BuildRequires: pkgconfig(QtNetwork) pkgconfig(QtOpenGL)
BuildRequires: pkgconfig(QtScript) pkgconfig(QtScriptTools)
BuildRequires: pkgconfig(QtSql) pkgconfig(QtSvg) pkgconfig(QtTest)
BuildRequires: pkgconfig(QtXml) pkgconfig(QtXmlPatterns)
%global sip_ver 4.19.12

%if 0%{?with_python3}
BuildRequires: python3-dbus
BuildRequires: python3-devel 
BuildRequires: python3-pyqt4-sip >= %{sip_ver}
BuildRequires: python3-sip-devel >= %{sip_ver}
%endif # with_python3

%if 0%{?with_python2}
BuildRequires: %{python2_dbus}
BuildRequires: python2-devel
BuildRequires: python2-pyqt4-sip >= %{sip_ver}
BuildRequires: python2-sip-devel >= %{sip_ver}

Requires: %{python2_dbus}
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}
%{?_sip_api:Requires: python2-pyqt4-sip-api(%{_sip_api_major}) >= %{_sip_api}}

%if !0%{?qtassistant}
Obsoletes: PyQt4-assistant < %{version}-%{release}
Obsoletes: python3-PyQt4-assistant < %{version}-%{release}
%endif

%if 0%{?webkit}
# when -webkit was split out
Obsoletes: PyQt4 < 4.11.4-8
%endif

Provides: python-qt4 = %{version}-%{release}
Provides: python2-qt4 = %{version}-%{release}
Provides: python2-PyQt4 = %{version}-%{release}
Provides: pyqt4 = %{version}-%{release}
Provides: python%{python2_version}dist(pyqt4) = %{version}
%endif

%global __provides_exclude_from ^(%{?python2_sitearch:%{python2_sitearch}/.*\\.so|}%{?python3_sitearch:%{python3_sitearch}/.*\\.so|}%{_qt4_plugindir}/.*\\.so)$

%description
These are Python bindings for Qt4.

%package devel
Summary: Files needed to build other bindings based on Qt4
%if 0%{?webkit}
Obsoletes: %{name}-webkit-devel < %{version}-%{release}
Provides: %{name}-webkit-devel = %{version}-%{release}
Obsoletes: PyQt4 < 4.11.4-8
%endif
Provides: python-qt4-devel = %{version}-%{release}
Provides: python2-qt4-doc = %{version}-%{release}
Provides: python2-PyQt4-doc = %{version}-%{release}
Provides: pyqt4-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt4-devel
Requires: sip-devel
# when split happened, upgrade path
Obsoletes: PyQt4-devel < 4.10.3-6
%description devel
Files needed to build other bindings for C++ classes that inherit from any
of the Qt4 classes (e.g. KDE or your own).

%package doc
Summary: PyQt4 developer documentation and examples
BuildArch: noarch
# when split happened, upgrade path
Obsoletes: PyQt4-devel < 4.10.3-6
Obsoletes: python3-PyQt4-devel < 4.10.3-6
Provides: python-qt4-doc = %{version}-%{release}
Provides: python2-qt4-doc = %{version}-%{release}
Provides: python2-PyQt4-doc = %{version}-%{release}
%description doc
%{summary}.

# split-out arch'd subpkg, since (currently) %%_qt4_datadir = %%_qt4_libdir
%package qsci-api
Summary: Qscintilla API file support
# when split happened, upgrade path
Obsoletes: PyQt4-devel < 4.10.3-6
Obsoletes: python3-PyQt4-devel < 4.10.3-6
Provides: python-qt4-qsci-api = %{version}-%{release}
Provides: python2-qt4-qsci-api = %{version}-%{release}
Provides: python2-PyQt4-qsci-api = %{version}-%{release}
%description qsci-api
%{summary}.

%if 0%{?qtassistant}
%package assistant
Summary: Python bindings for QtAssistant
BuildRequires: pkgconfig(QtAssistantClient)
Provides: python-qt4-assistant = %{version}-%{release}
Provides: python2-qt4-assistant = %{version}-%{release}
Provides: python2-PyQt4-assistant = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description assistant
%{summary}.

%package -n python3-%{name}-assistant
Summary: Python 3 bindings for QtAssistant
Provides: python3-qt4-assistant = %{version}-%{release}
Requires: python3-%{name}%{?_isa} = %{version}-%{release}
%description -n python3-%{name}-assistant
%{summary}.
%endif

%if 0%{?webkit}
%package webkit
Summary: Python bindings for Qt4 Webkit
BuildRequires: pkgconfig(QtWebKit)
# when -webkit was split out
Obsoletes: PyQt4 < 4.11.4-8
Provides: python-qt4-webkit = %{version}-%{release}
Provides: python2-qt4-webkit = %{version}-%{release}
Provides: python2-PyQt4-webkit = %{version}-%{release}
Provides: pyqt4-webkit = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description webkit
%{summary}.

%package -n python3-%{name}-webkit
Summary: Python3 bindings for Qt4 Webkit
Obsoletes: python3-PyQt4 < 4.11.4-8
Provides: python3-qt4-webkit = %{version}-%{release}
Requires:  python3-PyQt4%{?_isa} = %{version}-%{release}
%description -n python3-%{name}-webkit
%{summary}.
%endif

# The bindings are imported as "PyQt4", hence it's reasonable to name the
# Python 3 subpackage "python3-PyQt4", despite the apparent tautology
%package -n python3-%{name}
Summary: Python 3 bindings for Qt4
Requires: python3-dbus
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}
%{?_sip_api:Requires: python3-pyqt4-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%if 0%{?webkit}
Obsoletes: python3-PyQt4 < 4.11.4-8
%endif
Provides: python3-qt4 = %{version}-%{release}
Provides: python%{python3_version}dist(pyqt4) = %{version}
%description -n python3-%{name}
These are Python 3 bindings for Qt4.

%package -n python3-%{name}-devel
Summary: Python 3 bindings for Qt4
%if 0%{?webkit}
Provides: python3-%{name}-webkit-devel = %{version}-%{release}
%endif
Provides: python3-qt4-devel = %{version}-%{release}
Requires: python3-%{name}%{?_isa} = %{version}-%{release}
Requires: python3-sip-devel
# when split happened, upgrade path
Obsoletes: python3-PyQt4-devel < 4.10.3-6
%description -n python3-%{name}-devel
Files needed to build other Python 3 bindings for C++ classes that inherit
from any of the Qt4 classes (e.g. KDE or your own).


%prep
%setup -q -n PyQt4_gpl_x11-%{version}%{?snap:-snapshot-%{snap}}

# save orig for comparison later
cp -a ./sip/QtGui/opengl_types.sip ./sip/QtGui/opengl_types.sip.orig
%patch1 -p1 -b .ftbfs
%patch60 -p1 -b .arm
%patch61 -p1
%patch62 -p1
%if ! 0%{?webkit}
%patch300 -p1 -b .webkit
%endif

# permissions, mark examples non-executable
find examples/ -name "*.py" | xargs chmod a-x


%build

QT4DIR=%{_qt4_prefix}
PATH=%{_qt4_bindir}:$PATH ; export PATH

%if 0%{?with_python2}
# Python 2 build:
mkdir %{_target_platform}
pushd %{_target_platform}
%{__python2} ../configure.py \
  --assume-shared \
  --confirm-license \
  --no-timestamp \
  --qmake=%{_qt4_qmake} \
  --qsci-api-destdir=%{_qt4_datadir}/qsci \
  --verbose \
  CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LFLAGS="%{?__global_ldflags}"
 
%make_build
popd
%endif

# Python 3 build:
%if 0%{?with_python3}

mkdir %{_target_platform}-python3
pushd %{_target_platform}-python3
%{__python3} ../configure.py \
  --assume-shared \
  --confirm-license \
  --no-timestamp \
  --qmake=%{_qt4_qmake} \
  --qsci-api-destdir=%{_qt4_datadir}/qsci \
  %{?py3_sipdir:--sipdir=%{py3_sipdir}} \
  --verbose \
  CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LFLAGS="%{?__global_ldflags}"

%make_build
popd
%endif # with_python3


%install
# Install Python 3 first, and move aside any executables, to avoid clobbering
# the Python 2 installation:
%if 0%{?with_python3}
make install DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot} -C %{_target_platform}-python3
%if "%py3_sipdir" == "%{_datadir}/sip/PyQt4"
# copy files to old location for compat purposes temporarily
mkdir -p %{buildroot}%{_datadir}/python3-sip
cp -alf %{buildroot}%{py3_sipdir} \
        %{buildroot}%{_datadir}/python3-sip/PyQt4
%endif
mkdir %{buildroot}%{python3_sitearch}/PyQt4/__pycache__/ ||:
%endif

%if 0%{?with_python2}
make install DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%endif

# remove Python 3 code from Python 2.6 directory, fixes FTBFS (#564633)
rm -rfv %{buildroot}%{python2_sitearch}/PyQt4/uic/port_v3/

# likewise, remove Python 2 code from the Python 3.1 directory:
rm -rfv %{buildroot}%{python3_sitearch}/PyQt4/uic/port_v2/

# install pyuic4 wrapper to support both python2/python3
rm -fv %{buildroot}%{_bindir}/pyuic4
install -p -m755 -D %{SOURCE2} \
  %{buildroot}%{_bindir}/pyuic4
sed -i \
  -e "s|@PYTHON3@|%{__python3}|g" \
  -e "s|@PYTHON2@|%{__python2}|g" \
  %{buildroot}%{_bindir}/pyuic4


%check
# verify opengl_types.sip sanity
diff -u ./sip/QtGui/opengl_types.sip.orig \
        ./sip/QtGui/opengl_types.sip ||:


%if 0%{?with_python2}
%files
%doc NEWS README
%license LICENSE
%{python2_dbus_dir}/qt.so
%dir %{python2_sitearch}/PyQt4/
%{python2_sitearch}/PyQt4/__init__.py*
%{python2_sitearch}/PyQt4/pyqtconfig.py*
%{python2_sitearch}/PyQt4/phonon.so
%{python2_sitearch}/PyQt4/Qt.so
%{python2_sitearch}/PyQt4/QtCore.so
%{python2_sitearch}/PyQt4/QtDBus.so
%{python2_sitearch}/PyQt4/QtDeclarative.so
%{python2_sitearch}/PyQt4/QtDesigner.so
%{python2_sitearch}/PyQt4/QtGui.so
%{python2_sitearch}/PyQt4/QtHelp.so
%{python2_sitearch}/PyQt4/QtMultimedia.so
%{python2_sitearch}/PyQt4/QtNetwork.so
%{python2_sitearch}/PyQt4/QtOpenGL.so
%{python2_sitearch}/PyQt4/QtScript.so
%{python2_sitearch}/PyQt4/QtScriptTools.so
%{python2_sitearch}/PyQt4/QtSql.so
%{python2_sitearch}/PyQt4/QtSvg.so
%{python2_sitearch}/PyQt4/QtTest.so
%{python2_sitearch}/PyQt4/QtXml.so
%{python2_sitearch}/PyQt4/QtXmlPatterns.so
%{python2_sitearch}/PyQt4/uic/
%{_qt4_plugindir}/designer/*

%if 0%{?qtassistant}
%files assistant
%{python2_sitearch}/PyQt4/QtAssistant.so
%endif

%if 0%{?webkit}
%files webkit
%{python2_sitearch}/PyQt4/QtWebKit.so
%endif

%files devel
%{_bindir}/pylupdate4
%{_bindir}/pyrcc4
%{_bindir}/pyuic4
%{_datadir}/sip/PyQt4/
%endif

%files doc
%doc doc/*
%doc examples/

%files qsci-api
# avoid dep on qscintilla-python, own %%_qt4_datadir/qsci/... here for now
%dir %{_qt4_datadir}/qsci/
%dir %{_qt4_datadir}/qsci/api/
%dir %{_qt4_datadir}/qsci/api/python/
%{_qt4_datadir}/qsci/api/python/PyQt4.api

%if 0%{?with_python3}
%files -n python3-%{name}
%doc NEWS README
%license LICENSE
%{python3_dbus_dir}/qt.so
%dir %{python3_sitearch}/PyQt4/
%{python3_sitearch}/PyQt4/__init__.py*
%{python3_sitearch}/PyQt4/__pycache__/
%{python3_sitearch}/PyQt4/pyqtconfig.py*
%{python3_sitearch}/PyQt4/phonon.so
%{python3_sitearch}/PyQt4/Qt.so
%{python3_sitearch}/PyQt4/QtCore.so
%{python3_sitearch}/PyQt4/QtDBus.so
%{python3_sitearch}/PyQt4/QtDeclarative.so
%{python3_sitearch}/PyQt4/QtDesigner.so
%{python3_sitearch}/PyQt4/QtGui.so
%{python3_sitearch}/PyQt4/QtHelp.so
%{python3_sitearch}/PyQt4/QtMultimedia.so
%{python3_sitearch}/PyQt4/QtNetwork.so
%{python3_sitearch}/PyQt4/QtOpenGL.so
%{python3_sitearch}/PyQt4/QtScript.so
%{python3_sitearch}/PyQt4/QtScriptTools.so
%{python3_sitearch}/PyQt4/QtSql.so
%{python3_sitearch}/PyQt4/QtSvg.so
%{python3_sitearch}/PyQt4/QtTest.so
%{python3_sitearch}/PyQt4/QtXml.so
%{python3_sitearch}/PyQt4/QtXmlPatterns.so
%{python3_sitearch}/PyQt4/uic/
%if !0%{?with_python2}
%{_qt4_plugindir}/designer/*
%endif

%if 0%{?qtassistant}
%files -n python3-%{name}-assistant
%{python3_sitearch}/PyQt4/QtAssistant.so
%endif

%if 0%{?webkit}
%files -n python3-%{name}-webkit
%{python3_sitearch}/PyQt4/QtWebKit.so
%endif

%files -n python3-%{name}-devel
%{_bindir}/pylupdate4
%{_bindir}/pyrcc4
%{_bindir}/pyuic4
%{py3_sipdir}/
# compat location
%dir %{_datadir}/python3-sip/
%{_datadir}/python3-sip/PyQt4/
%endif


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 4.12.3-25
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Than Ngo <than@redhat.com> - 4.12.3-22
- Fix error: invalid use of undefined type 'struct _frame'

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 4.12.3-21
- Rebuilt for Python 3.11

* Tue May 03 2022 Than Ngo <than@redhat.com> - 4.12.3-20
- Fixed bz#2038921 - PyQt4: FTBFS in Fedora Rawhide

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-18
- rebuild (python 3.11)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 4.12.3-16
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 18:40:28 CET 2020 Victor Stinner <vstinner@redhat.com> - 4.12.3-14
- Fix Python 3.10 support (rhbz#1895298)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.12.3-12
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-10
- drop python2 support for f32+ (#1729577)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.12.3-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 4.12.3-8
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-6
- Provides: Provides: python%%{python?_version}dist(pyqt4) (#1705739)

* Mon May 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-5
- rebuild for python autodeps (#1705739)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-3
- drop -assistant subpkg on f30+ (#1633792)

* Fri Aug 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Fri Aug 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-2
- drop dep on python?-sip
- drop backward-compat py3_sipdir

* Tue Aug 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Sun Jul 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-10
- use %%make_build %%license
- -devel: drop dep on -webkit
- unified sipdir on f29+
- s/dbus-python/python2-dbus/
- update sip-related build deps

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 4.12.1-8
- Rebuilt for Python 3.7

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-7
- BR: gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 Merlin Mathesius <mmathesi@redhat.com> - 4.12.1-5
- Cleanup spec file conditionals

* Mon Jul 31 2017 Than Ngo <than@redhat.com> - 4.12.1-4
- fixed bz#1348514 - Arbitrary code execution due to insecure loading
  of Python module from CWD

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-2
- rebuild (sip)

* Sun Jul 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- PyQt4-4.12.1

* Thu Mar 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.12-4
- rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 4.12-2
- update provides filtering

* Sun Jan 01 2017 Rex Dieter <rdieter@math.unl.edu> - 4.12-1
- PyQt4-4.12

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 4.11.4-16
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11.4-15
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.11.4-14
- rebuild (qt)

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.11.4-13
- Provides: python2-qt4/python2-PyQt4 (#1249422)

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.11.4-12
- rebuild (qt)

* Wed Apr 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.11.4-11
- rebuid (sip)

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 4.11.4-10
- -webkit: add Provides: to match those of main pkg

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 4.11.4-9
- rebase -webkit.patch, use safer subdir builds

* Mon Feb 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.11.4-8
- don't remove anything from uic/widget-plugins (see also #1294307)
- -webkit subpkg

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Rex Dieter <rdieter@fedoraproject.org> 4.11.4-6
- explicitly set CFLAGS,CXXFLAGS,LFLAGS

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 10 2015 Than Ngo <than@redhat.com> - 4.11.4-4
- rebuild

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 4.11.4-3
- Rebuilt for Python3.5 rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Rex Dieter <rdieter@fedoraproject.org> 4.11.4-1
- PyQt4-4.11.4

* Fri Jun 05 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-5
- drop qscintilla conditional
- -python3-devel: include binaries, use pyuic4 wrapper (see also #1193107)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.11.3-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 25 2015 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-3
- rebuild (sip)

* Wed Feb 25 2015 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-2
- rebuild (sip)

* Mon Nov 10 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-1
- PyQt4-4.11.3

* Thu Nov 06 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.2-2
- python2_sitelib should be python2_sitearch (#1161121)

* Mon Sep 15 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.2-1
- PyQt4-4.11.2

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.1-2
- rebuild (qt/phonon)

* Sun Jul 06 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.1-1
- PyQt4-4.11.1

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11.1-0.3.9d5a6843b580
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11.1-0.2.9d5a6843b580
- rebuild for new qscintilla (#1104559)

* Sun Jun 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-0.1.9d5a6843b580
- PyQt4-4.11.1 snapshot (fix FTBFS)
- re-enable -assistant subpkg

* Wed May 28 2014 Rex Dieter <rdieter@fedoraproject.org> 4.11-1
- PyQt-4.11
- Obsoletes: PyQt4-assistant
- use configure-ng.py (may as well, configure.py is broken)

* Mon May 12 2014 Rex Dieter <rdieter@fedoraproject.org> 4.10.4-2
- rebuild (f21-python)

* Sun Mar 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- PyQt-4.10.4 (#1076001)
- s/python/python2/

* Fri Mar 14 2014 Rex Dieter <rdieter@fedoraproject.org> 4.10.3-6
- polish/improve uic multilib issues (#1076346)
- -doc.noarch,-qsci-api subpkgs
- python3-PyQt4: python3-dbus support

* Mon Feb 17 2014 Rex Dieter <rdieter@fedoraproject.org> 4.10.3-5
- flesh out python(3)-qt4 related provides

* Fri Dec 06 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.3-4
- rebuild (phonon)

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.3-3
- simpler phonon_detect.patch

* Thu Nov 14 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.3-2
- fix build against phonon-4.7+ (kde#306261)

* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.3-1
- 4.10.3

* Mon Oct 07 2013 Than Ngo <than@redhat.com> - 4.10.2-3
- fix license tag
- add missing buildroot

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-1
- 4.10.2

* Tue May 07 2013 Than Ngo <than@redhat.com> - 4.10.1-5
- add qtassistant macro

* Fri May 03 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-4
- fix dbus/mainloop hacks (#957867)

* Thu May 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-3
- ImportError: cannot import name uic (#958736)

* Fri Apr 26 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-2
- filter private shared objects
- %%{python_sitelib}/dbus/mainloop/qt.so should be in %%python_sitearch (#957260)
- .spec cleanup
- -assistant subpkg

* Mon Apr 22 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Tue Apr 02 2013 Than Ngo <than@redhat.com> - 4.10-3
- adapt rhel patch

* Fri Mar 22 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10-2
- introduce qscintilla, webkit feature macros

* Sun Mar 03 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10-1
- 4.10

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Than Ngo <than@redhat.com> - 4.9.6-2
- adapt rhel patch

* Sun Dec 09 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.6-1
- 4.9.6

* Sun Oct 28 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.5-3
- rebuild (sip)

* Thu Oct 11 2012 Than Ngo <than@redhat.com> - 4.9.5-2
- update webkit patch

* Mon Oct 01 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.5-1
- PyQt-4.9.5

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 4.9.4-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 4.9.4-4
- make with_python3 be conditional on fedora

* Mon Jul 30 2012 Than Ngo <than@redhat.com> - 4.9.4-3
- update webkit patch

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.4-1
- 4.9.4

* Sun Jun 24 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-1
- 4.9.3

* Fri Jun 22 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-1
- 4.9.2

* Thu Jun 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-4
- PyQt4 opengl-types.sip multilib conflict (#509415)

* Fri May 04 2012 Than Ngo <than@redhat.com> - 4.9.1-3
- add rhel/fedora condition

* Sun Mar  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 4.9.1-2
- Add upstream patch (via Debian) to fix FTBFS on ARM

* Sat Feb 11 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-1
- 4.9.1

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 09 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9-2
- upstream doItemsLayout patch

* Fri Dec 23 2011 Rex Dieter <rdieter@fedoraproject.org> 4.9-1
- 4.9

* Tue Dec 20 2011 Than Ngo <than@redhat.com> - 4.8.6-4
- Provides: pyqt4

* Wed Dec 14 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.6-3
- -devel: Provides: -webkit-devel

* Fri Nov 18 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.6-2
- Provides: python(3)-qt4

* Wed Oct 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.6-1
- 4.8.6

* Mon Oct 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.5-2
- pkgconfig-style deps
- Provides: -webkit
- s/python3-PyQt4/python3-%%name/

* Wed Aug 10 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.5-1
- 4.8.5

* Sat Jul 23 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.4-4
- rebuild (qt48)

* Thu Jun 16 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.4-3
- rebuild

* Wed Jun 08 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.4-2
- squash more rpaths

* Mon May 02 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.4-1
- 4.8.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Rex Dieter <rdieter@fedoraproject.org> 4.8.3-1
- PyQt4-x11-gpl-4.8.3

* Sat Jan 15 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.8.3-0.1.454d07a16153
- 4.8.3 snapshot
- Little typo (#668289)

* Fri Dec 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.8.2-1
- PyQt4-x11-gpl-4.8.2

* Sat Oct 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.8.1-1
- PyQt4-x11-gpl-4.8.1

* Wed Oct 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.8-3
- fix pyuic_shbang.patch
- drop implicit-linking patch (no longer needed)

* Sun Oct 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.8-2
- drop BR: qt-assistant-adp-devel (these deprecated bindings are no longer included)

* Sat Oct 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.8-1
- PyQt-x11-gpl-4.8

* Sat Oct 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.7-3
- backport patch to fix kdebindings/pykde ftbfs
- drop sip-devel min version a bit to match reality

* Wed Sep 29 2010 jkeating - 4.7.7-2
- Rebuilt for gcc bug 634757

* Wed Sep 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.7-1
- PyQt-x11-gpl-4.7.7

* Mon Sep 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.6-2
- backport pyuic fix for python2

* Thu Sep 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.6-1
- PyQt-x11-gpl-4.7.6

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 4.7.4-3
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.4-1
- PyQt-x11-gpl-4.7.4

* Sat May 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.3-3
- BR: qt4-webkit-devel

* Mon Apr 26 2010 David Malcolm <dmalcolm@redhat.com> - 4.7.3-2
- add python 3 subpackages (#586196)

* Sat Apr 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.3-1
- PyQt-x11-gpl-4.7.3

* Sun Mar 21 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.7.2-2
- rebuild against fixed qt to get QtMultimedia detected properly

* Thu Mar 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.2-1
- PyQt-x11-gpl-4.7.2

* Sun Mar 14 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.7-5
- fix implicit linking when checking for QtHelp and QtAssistant
- remove Python 3 code from Python 2.6 directory, fixes FTBFS (#564633)

* Sat Mar 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.7-4
- BR qt-assistant-adp-devel

* Tue Feb 23 2010 Than Ngo <than@redhat.com> - 4.7-3
- fix multilib conflict because of timestamp

* Sun Feb 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7-2
- rebuild

* Fri Jan 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7-1
- PyQt-x11-gpl-4.7 (final)

* Thu Jan 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7-0.1.20091231
- PyQt-x11-gpl-4.7-snapshot-20091231

* Fri Nov 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-5
- phonon bindings missing (#541685)

* Wed Nov 25 2009 Than Ngo <than@redhat.com> - 4.6.2-4
- fix conditional for RHEL

* Wed Nov 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-3
- PyQt4-4.6.2 breaks QStringList in QVariant, rebuild with sip-4.9.3 (#541211)

* Wed Nov 25 2009 Than Ngo <than@redhat.com> - 4.6.2-2
- fix conditional for RHEL

* Fri Nov 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-1
- PyQt4-4.6.2

* Thu Nov 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.1-2.1
- rebuild (for qt-4.6.0-rc1, f13+)

* Mon Nov 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.1-2
- Requires: sip-api(%%_sip_api_major) >= %%_sip_api

* Fri Oct 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.1-1
- PyQt4-4.6.1

* Thu Oct 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.1-0.1.20091014
- PyQt4-4.6.1-snapshot-20091014 (#529192)

* Tue Jul 28 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5.4-1
- PyQt4-4.5.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-1
- PyQt4-4.5.2

* Thu Jul 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-2
- fix build with qt-4.5.2
- PyQt4-devel multilib conflict (#509415)

* Tue Jun 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-1
- PyQt-4.5.1

* Fri Jun 05 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5-1
- PyQt-4.5

* Thu May 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5-0.2.20090520
- fix generation of sip_ver

* Thu May 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5-0.1.20090520
- PyQt-4.5-snapshot-20090520
