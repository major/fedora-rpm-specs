%global altname  QEverCloud

%global commit          71aefa15289f6861b747af8a6b02122f326e9a3a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20210724

Name:       qevercloud
Summary:    Unofficial Evernote Cloud API for Qt5
Version:    6.1.0
Release:    %autorelease

License:    MIT
URL:        https://github.com/d1vanov/QEverCloud
Source0:    %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExclusiveArch: %{qt5_qtwebengine_arches}

BuildRequires: make
BuildRequires: cmake
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5WebEngineCore)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: doxygen
BuildRequires: qt5-doctools

%description
This library presents the complete Evernote SDK for Qt. All the functionality
that is described on Evernote site is implemented and ready to use.
In particular OAuth authentication is implemented.

%package devel
Summary:       Headers files for developing with %{altname}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications that use %{altname}.

%package doc
Summary: Documentation for %{commit}
BuildArch: noarch
Requires: qt5-qtbase

%description doc
%{summary}.

%prep
%autosetup -n %{altname}-%{commit}

%build
%cmake -DBUILD_QCH_DOCUMENTATION=ON \
       -DCMAKE_INSTALL_LIBDIR=%{_qt5_libdir} \
       -DQHELPGENERATOR_EXECUTABLE=%{_bindir}/qhelpgenerator-qt5
%cmake_build
make doc -C %{_vpath_builddir}

%install
%cmake_install

install -Dpm0644 -t %{buildroot}%{_qt5_docdir} \
  %{_vpath_builddir}/%{altname}.qch
mkdir -p %{buildroot}%{_qt5_docdir}/%{altname}
cp -aR %{_vpath_builddir}/doc/html/* %{buildroot}%{_qt5_docdir}/%{altname}

%check
%{_vpath_builddir}/QEverCloud/test_QEverCloud

%files
%license LICENSE
%{_qt5_libdir}/libqt5qevercloud.so.6*

%files devel
%{_includedir}/qt5qevercloud
%{_qt5_libdir}/libqt5qevercloud.so
%{_qt5_libdir}/cmake/QEverCloud-qt5/

%files doc
%doc docs CHANGELOG.md README.md
%license LICENSE
%{_qt5_docdir}/%{altname}.qch
%{_qt5_docdir}/%{altname}

%changelog
%autochangelog