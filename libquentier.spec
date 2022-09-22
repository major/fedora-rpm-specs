# Force out of source build
%undefine __cmake_in_source_build

%global commit          04b7e7d8415b2610d30ce727db9cebc77387928e
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20220710

Name:       libquentier
Summary:    Set of Qt/C++ APIs for feature rich desktop clients for Evernote service
Version:    0.5.0
Release:    %autorelease

License:    GPLv3 or LGPLv3
URL:        https://github.com/d1vanov/libquentier
Source0:    %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:     libquentier-4ce8e3b-fix_translations_install.patch

ExclusiveArch: %{qt5_qtwebengine_arches}

BuildRequires: cmake
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineCore)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5WebSockets)
BuildRequires: cmake(Qt5WebChannel)
BuildRequires: cmake(libxml2)
BuildRequires: cmake(QEverCloud-qt5)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: boost-devel
BuildRequires: libtidy-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: make

%description
This library presents a set of Qt/C++ APIs useful for applications working as
feature rich desktop clients for Evernote service. The most important and
useful components of the library are the following:

 - Local storage - persistence of data downloaded from Evernote service in
   a local SQLite database
 - Synchronization - the logics of exchanging new and/or modified data
   with Evernote service
 - Note editor - the UI component capable for notes displaying and editing

The library is based on the lower level functionality provided by QEverCloud
library. It also serves as the functional core of Quentier application.

%package devel
Summary:       Headers files for developing with %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications that use %{name}.

%package doc
Summary: Documentation for %{name}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake -DUSE_QT5=1 \
       -DCMAKE_INSTALL_LIBDIR=%{_qt5_libdir} \
       -DQt5_LUPDATE_EXECUTABLE=%{_bindir}/lupdate-qt5 \
       -DQt5_LRELEASE_EXECUTABLE=%{_bindir}/lrelease-qt5 \
       -DUSE_LD_GOLD=0
%cmake_build
cd %{_vpath_builddir}
make lupdate
make lrelease
make doc

%install
%cmake_install
cd %{_vpath_builddir}
mkdir -p %{buildroot}%{_qt5_docdir}/%{name}
cp -aR doc/html/* %{buildroot}%{_qt5_docdir}/%{name}

%files
%doc CONTRIBUTING.md README.md
%license COPYING.LESSER COPYING.txt
%{_qt5_libdir}/libqt5quentier.so.0*
%dir %{_datadir}/libquentier
%{_datadir}/libquentier/translations

%files devel
%{_includedir}/quentier
%{_qt5_libdir}/libqt5quentier.so
%{_qt5_libdir}/cmake/Libquentier-qt5/

%files doc
%doc CONTRIBUTING.md README.md
%license COPYING.LESSER COPYING.txt
%{_qt5_docdir}/%{name}

%changelog
%autochangelog
