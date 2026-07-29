%global bname ykman-gui
Name: yubikey-manager-qt
Summary: Application for configuring any YubiKey over all USB interfaces
Version: 1.2.5
Release: %autorelease
URL: https://developers.yubico.com/yubikey-manager-qt/
Source0: https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1: https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
Source2:  gpgkey-6690D8BC.gpg
Patch1: yubikey-manager-qt-1.2.5-remove-cloud-upload.patch

License: BSD-2-Clause

BuildRequires: gnupg2
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: python3
BuildRequires: libyubikey
BuildRequires: python3-yubikey-manager >= 4
BuildRequires: qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel
BuildRequires: qt5-qtquickcontrols qt5-qtgraphicaleffects pyotherside
BuildRequires: desktop-file-utils
Requires:      pyotherside 
Requires:      qt5-qtquickcontrols
Requires:      python3-yubikey-manager
ExcludeArch:   %{ix86}


%description
Cross-platform application for configuring any YubiKey over all USB interfaces.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n %{name}
%patch 1 -p1
sed -i 's|python |python3 |g' ykman-cli/ykman-cli.pro
sed -i 's|python |python3 |g' ykman-gui/ykman-gui.pro


%build
#qmake-qt5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}" QMAKE_STRIP="/bin/true";
%{qmake_qt5}
#make %{?_smp_mflags}
%{make_build}

%install
make install INSTALL_ROOT="%{buildroot}"
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 0644 resources/icons/ykman.png %{buildroot}%{_datadir}/pixmaps/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications resources/%{bname}.desktop

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{bname}
%{_datadir}/applications/%{bname}.desktop
%{_datadir}/pixmaps/ykman.png

%changelog
%autochangelog
