Name:       ibus-qt
Version:    1.3.4
Release:    %autorelease
Summary:    Qt IBus library and Qt input method plugin
License:    GPL-2.0-or-later
URL:        https://github.com/ibus/ibus/wiki
Source0:    https://github.com/ibus/ibus-qt/releases/download/%{version}/%{name}-%{version}-Source.tar.gz

#Patch0:     %%{name}-HEAD.patch
Patch0:     %{name}-HEAD.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  qt4-devel
BuildRequires:  dbus-devel
BuildRequires:  ibus-devel
BuildRequires:  libicu-devel
BuildRequires:  doxygen
Requires:       ibus

%description
Qt IBus library and Qt input method plugin.

%package devel
Summary:    Development tools for ibus qt
Requires:   %{name} = %{version}-%{release}

%description devel
The ibus-qt-devel package contains the header files for ibus qt library.

%package docs
Summary:    Development documents for ibus qt
Requires:   %{name} = %{version}-%{release}

%description docs
The ibus-qt-docs package contains developer documentation for ibus qt library.

%prep
%autosetup -S git -n %{name}-%{version}-Source

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_usr} \
    -DLIBDIR=%{_libdir}
%cmake_build
%cmake_build -- docs

%install
%cmake_install

%ldconfig_scriptlets

%files
# -f {name}.lang
%doc AUTHORS README INSTALL
%{_libdir}/libibus-qt.so.*
%{_libdir}/qt4/plugins/inputmethods/libqtim-ibus.so

%files devel
%{_includedir}/*
%{_libdir}/libibus-qt.so

%files docs
%doc %__cmake_builddir/docs/html

%changelog
%autochangelog

