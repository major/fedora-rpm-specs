%global with_snapshot 1
%global gitdate 20230306
%global commit e71fbbfed95ea084533c28aa1af3afc900838436
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name:			input-leap
Version:		2.4.0%{?with_snapshot:^%{gitdate}git%{shortcommit}}
Release:		%autorelease
Summary:		Share mouse and keyboard between multiple computers over the network

License:		GPL-2.0-only
URL:			https://github.com/%{name}/%{name}
%if %{with_snapshot}
Source0:		%{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
Source1:		about.png

# https://github.com/input-leap/input-leap/pull/1621
Patch0:			appdata-xml.patch

BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	cmake3
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	gmock-devel
BuildRequires:	gulrak-filesystem-devel
BuildRequires:	gtest-devel
BuildRequires:	libappstream-glib
BuildRequires:	libcurl-devel
BuildRequires:	libSM-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXtst-devel
BuildRequires:	libX11-devel
BuildRequires:	openssl-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-linguist
Requires:		hicolor-icon-theme

# https://github.com/input-leap/input-leap/issues/1414
Provides:		barrier = %version-%release
Obsoletes:		barrier <= 2.4.0

%description
Input Leap is software that mimics the functionality of a KVM switch, which
historically would allow you to use a single keyboard and mouse to control 
multiple computers by physically turning a dial on the box to switch the 
machine you're controlling at any given moment. 

Input Leap does this in software, allowing you to tell it which machine to 
control by moving your mouse to the edge of the screen, or by using a 
keypress to switch focus to a different system.

%prep
%if %{with_snapshot}
%autosetup -n %{name}-%{commit} -p1
# version stage = snapshot
sed -i -e "s|release|snapshot|" cmake/Version.cmake
%else
%autosetup -p1
%endif

# lets change the logo :)
# https://github.com/input-leap/input-leap/pull/1620
cp %{SOURCE1} src/gui/res/image/

%build
%cmake \
%if %{with_snapshot}
	-DINPUTLEAP_REVISION=%{shortcommit} \
%endif
	-DINPUTLEAP_BUILD_TESTS=ON \
	-DINPUTLEAP_USE_EXTERNAL_GTEST=True
%cmake_build

%install
%cmake_install

%check
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license LICENSE
%doc ChangeLog README.md doc/%{name}.conf.example*
%{_bindir}/%{name}c
%{_bindir}/%{name}s
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}c.1*
%{_mandir}/man1/%{name}s.1*

%changelog
%autochangelog
