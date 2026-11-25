%global qt_minver 6.8

%global commit 3ff2c1bd56c11368c43451b5e9cedbcbde4ecb5d
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20261117


Name:           slitherer
Version:        0~git%{commitdate}.%{shortcommit}
Release:        4%{?dist}
Summary:        Simple QtWebView based runner for web applications

License:        MPL-2.0 and BSD-3-Clause
URL:            https://gitlab.com/VelocityLimitless/Projects/slitherer
Source:         %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# Temporary patch to force xcb platform
# Works around https://bugzilla.redhat.com/show_bug.cgi?id=2483236
# Shouldn't really be upstreamed unless we can't find any better way
# to fix the bug
Patch:          0001-Force-xcb-platform-to-work-around-RHBZ-2483236.patch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  cmake(Qt6Core) >= %{qt_minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt_minver}
BuildRequires:  cmake(Qt6Qml) >= %{qt_minver}
BuildRequires:  cmake(Qt6Quick) >= %{qt_minver}
BuildRequires:  cmake(Qt6WebView) >= %{qt_minver}

# Ensure that QtWebEngine has the fix for QTBUG-142823
Requires:      qt6-qtwebengine%{?_isa} >= 6.10.1-5

%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

%description
%{summary}.

%package -n anaconda-webui-opener-slitherer
Summary:        Simple QtWebView based runner for Anaconda installer Web UI
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       anaconda-webui
# Only Fedora Workstation and the netinstall ISO don't want this by default
Supplements:    (anaconda-webui unless (fedora-release-identity-workstation or fedora-release-identity-basic or fedora-release-identity-server))
# Cf. https://fedoraproject.org/wiki/Changes/Anaconda_WebUI_Opener
Provides:       anaconda-webui-opener
Conflicts:      anaconda-webui-opener
# Provide alternate name
Provides:       %{name}-anaconda-webui-opener = %{version}-%{release}
Provides:       %{name}-anaconda-webui-opener%{?_isa} = %{version}-%{release}

%description -n anaconda-webui-opener-slitherer
%{summary}.


%prep
%autosetup -n %{name}-%{commit} -S git_am


%conf
%cmake_qt6


%build
%cmake_build


%install
%cmake_install


# Anaconda launcher executables
ln -sr %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-anaconda
cat > %{buildroot}%{_bindir}/anaconda-webui-opener <<'ANACONDA_EOF'
#!/bin/sh

export SLITHERER_DESKTOP_ID="liveinst"
export SLITHERER_WINDOW_ICON_NAME="org.fedoraproject.AnacondaInstaller"

exec slitherer-anaconda "$@"
ANACONDA_EOF
chmod +x %{buildroot}%{_bindir}/anaconda-webui-opener


%files
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}

%files -n anaconda-webui-opener-slitherer
%{_bindir}/%{name}-anaconda
%{_bindir}/anaconda-webui-opener


%changelog
* Tue Nov 24 2026 Neal Gompa <ngompa@fedoraproject.org> - 0~git20261117.3ff2c1b-4
- Fix the anaconda-webui-opener script to correctly export argv variable

* Mon Nov 23 2026 Neal Gompa <ngompa@fedoraproject.org> - 0~git20261117.3ff2c1b-3
- Adjust webui-opener supplements to exclude Workstation and installer images

* Mon Nov 23 2026 Neal Gompa <ngompa@fedoraproject.org> - 0~git20261117.3ff2c1b-2
- Fix the anaconda-webui-opener script and mark as executable

* Tue Nov 17 2026 Neal Gompa <ngompa@fedoraproject.org> - 0~git20261117.4f45c18-1
- Bump to new git snapshot
- Add anaconda-webui-opener subpackage

* Wed Sep 02 2026 Adam Williamson <adamwill@fedoraproject.org> - 0~git20251108.d230dba-6
- Force xcb platform to work around dropdown bugs (#2483236)

* Fri Jul 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20251108.d230dba-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Mar 02 2026 Neal Gompa <ngompa@fedoraproject.org> - 0~git20251108.d230dba-4
- Add dependency to ensure QtWebEngine has fix for QTBUG-142823

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20251108.d230dba-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Nov 26 2025 Neal Gompa <ngompa@fedoraproject.org> - 0~git20251108.d230dba-2
- Rebuild for Qt 6.10.1

* Sat Nov 08 2025 Neal Gompa <ngompa@fedoraproject.org> - 0~git20251108.d230dba-1
- Bump to new git snapshot

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20250617.1e00f77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 17 2025 Neal Gompa <ngompa@fedoraproject.org> - 0~git20250617.1e00f77b-1
- Initial package

