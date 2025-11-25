# molequeue currently supports Qt5 only

%global gitcommit 0a35627edc490a79ac8bb17f1ed5c3d993074b91
%global gitdate 20241024
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:    molequeue
Summary: Desktop integration of high performance computing resources
Version: 0.9.0
Release: %autorelease -s %{gitdate}git%{shortcommit}
License: BSD-3-Clause
URL:     https://github.com/OpenChemistry/%{name}
Source0: https://github.com/OpenChemistry/%{name}/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz

## Main building
BuildRequires: make
BuildRequires: cmake
BuildRequires: qt5-qtbase-devel, qt5-rpm-macros
BuildRequires: qt5-qtwebkit-devel
%if 0%{?fedora}
BuildRequires: qjson-qt5-devel
%endif
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtxmlpatterns-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: python3-devel
%if 0%{?rhel}
BuildRequires: epel-rpm-macros
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
MoleQueue is an open-source, cross-platform, system-tray resident desktop
application for abstracting, managing, and coordinating the execution of tasks
both locally and on remote computational resources. Users can set up local and
remote queues that describe where the task will be executed. Each queue can
have programs, with templates to facilitate the execution of the program. Input
files can be staged, and output files collected using a standard interface.
Some highlights:

* Open source distributed under the liberal 3-clause BSD license
* Cross platform with nightly builds on Linux, Mac OS X and Windows
* Intuitive interface designed to be useful to whole community
* Support for local executation and remote schedulers (SGE, PBS, SLURM)
* System tray resident application managing queue of queues and job lifetime
* Simple, lightweight JSON-RPC 2.0 based communication over local sockets
* Qt 5 client library for simple integration in Qt applications

%package libs
Summary: Shared and private libraries of %{name}

%description libs
Shared and private libraries of %{name}.

%package  devel
Summary:  Development files of %{name}
Requires: qt5-qtbase-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary: HTML documentation of %{name}
BuildArch: noarch
%description doc
HTML documentation of %{name}.

%prep
%autosetup -n %{name}-%{gitcommit}

%if 0%{?fedora}
rm -rf thirdparty/qt5json
%endif

%build
%cmake -Wno-dev \
 -DENABLE_RPATH:BOOL=OFF \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DENABLE_TESTING:BOOL=OFF \
 -DBUILD_DOCUMENTATION:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

pushd %{__cmake_builddir}/docs
doxygen
popd

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/doc

cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=MoleQueue
Comment=Manage HPC jobs from the system tray
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
EOF

install -Dpm0644 molequeue/app/icons/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
desktop-file-install %{name}.desktop --dir %{buildroot}%{_datadir}/applications

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files libs
%doc README.md
%license LICENSE
%{_libdir}/libMoleQueue*.so
%{_libdir}/%{name}/

%files devel
%{_libdir}/cmake/%{name}/
%{_includedir}/%{name}/

%files doc
%doc README.md %{__cmake_builddir}/docs/html
%license LICENSE

%changelog
%autochangelog
