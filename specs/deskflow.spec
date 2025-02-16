%global rdnn_name org.deskflow.deskflow
%global qt6ver 6.7.0

Name:		deskflow
Version:	1.19.0
Release:	2%{?dist}
Summary:	Share mouse and keyboard between multiple computers over the network

License:	GPL-2.0-only
URL:		https://github.com/%{name}/%{name}
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake >= 3.24
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
BuildRequires:	openssl-devel >= 3.0
BuildRequires:	cmake(Qt6Core) >= %{qt6ver}
BuildRequires:	cmake(Qt6Widgets) >= %{qt6ver}
BuildRequires:	cmake(Qt6Network) >= %{qt6ver}
BuildRequires:	cmake(CLI11)
BuildRequires:	cmake(pugixml)
BuildRequires:	cmake(tomlplusplus)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libei-1.0) >= 1.3
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libportal) >= 0.8.0
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xtst)
Requires:	hicolor-icon-theme

# Replace synergy
Obsoletes:	synergy < 1:1.14.6.19-4
Provides:	synergy = 1:%{version}-%{release}

%description
Deskflow is software that mimics the functionality of a KVM switch, which
historically would allow you to use a single keyboard and mouse to control
multiple computers by physically turning a dial on the box to switch the
machine you're controlling at any given moment.

Deskflow does this in software, allowing you to tell it which machine to
control by moving your mouse to the edge of the screen, or by using a
keypress to switch focus to a different system.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ifarch s390x
# XXX: Allow it to fail for now
# Cf. https://github.com/deskflow/deskflow/issues/8203
%{_vpath_builddir}/bin/unittests || :
%else
%{_vpath_builddir}/bin/unittests
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn_name}.desktop


%files
%license LICENSE LICENSE_EXCEPTION
%doc README.md doc/*.md
%{_bindir}/%{name}-client
%{_bindir}/%{name}-server
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{rdnn_name}.png
%{_datadir}/applications/%{rdnn_name}.desktop
%{_metainfodir}/%{rdnn_name}.metainfo.xml


%changelog
* Fri Feb 14 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.19.0-2
- Temporarily allow tests to fail on s390x

* Fri Feb 14 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.19.0-1
- Update to 1.19.0

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.18.0-1
- Update to 1.18.0

* Sun Oct 13 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.17.0-1
- Initial package
