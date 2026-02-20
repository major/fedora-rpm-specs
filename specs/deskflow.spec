# Disable X11 for RHEL 10+
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]

%global rdnn_name org.deskflow.deskflow
%global qt6ver 6.7.0

Name:		deskflow
Version:	1.26.0
Release:	1%{?dist}
Summary:	Share mouse and keyboard between multiple computers over the network

License:	GPL-2.0-only
URL:		https://github.com/%{name}/%{name}
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:	%{ix86}

BuildRequires:	cmake >= 3.24
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
BuildRequires:	openssl-devel >= 3.0
BuildRequires:	cmake(Qt6Core) >= %{qt6ver}
BuildRequires:	cmake(Qt6LinguistTools) >= %{qt6ver}
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(libei-1.0) >= 1.3
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libportal) >= 0.8.0
%if %{with x11}
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xtst)
%endif
Requires:	hicolor-icon-theme

%description
Deskflow is software that mimics the functionality of a KVM switch, which
historically would allow you to use a single keyboard and mouse to control
multiple computers by physically turning a dial on the box to switch the
machine you're controlling at any given moment.

Deskflow does this in software, allowing you to tell it which machine to
control by moving your mouse to the edge of the screen, or by using a
key press to switch focus to a different system.


%prep
%autosetup -p1


%conf
%cmake -DSKIP_BUILD_TESTS=1 %{!?with_x11:-DBUILD_X11_SUPPORT=OFF}


%build
%cmake_build


%install
%cmake_install

# Add deskflow-server and deskflow-client as shell script
echo -e "#!/bin/sh\n%{_bindir}/%{name}-core server \$@" > %{buildroot}/%{_bindir}/%{name}-server
echo -e "#!/bin/sh\n%{_bindir}/%{name}-core client \$@" > %{buildroot}/%{_bindir}/%{name}-client
chmod 755 %{buildroot}/%{_bindir}/%{name}-server  %{buildroot}/%{_bindir}/%{name}-client

# For some reason, LICENSE_EXCEPTION is not in tarball, but generated
cp %{buildroot}%{_datadir}/licenses/deskflow/LICENSE_EXCEPTION .

# remove the html because koji does not build it
rm -fr %{buildroot}%{_docdir}/%{name}/html

%check
export QT_QPA_PLATFORM=minimal
%ifarch s390x
# XXX: Allow it to fail for now
# Cf. https://github.com/deskflow/deskflow/issues/8203
%{__ctest} --test-dir  "%{_vpath_builddir}/src/unittests" --output-on-failure --force-new-ctest-process %{?_smp_mflags} || :
%{_vpath_builddir}/bin/legacytests || :
%else
%{__ctest} --test-dir  "%{_vpath_builddir}/src/unittests" --output-on-failure --force-new-ctest-process %{?_smp_mflags}
%{_vpath_builddir}/bin/legacytests
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn_name}.desktop


%files
%license LICENSE LICENSE_EXCEPTION
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-core
%{_bindir}/%{name}-client
%{_bindir}/%{name}-server
%{_datadir}/applications/%{rdnn_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{rdnn_name}.png
%{_datadir}/icons/hicolor/*/apps/%{rdnn_name}*.svg
%{_datadir}/%{name}/translations/*.qm
%{_metainfodir}/%{rdnn_name}.metainfo.xml


%changelog
* Wed Feb 18 2026 Neal Gompa <ngompa@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Dec 01 2025 Ding-Yi Chen <dingyichen@gmail.com> - 1.25.0-1
- Update to version 1.25.0
  + Resolves: 2416455
  + New BuildRequires: cmake(Qt6LinguistTools)
  + Add translations
  + Add svg icons

* Thu Nov 20 2025 Ding-Yi Chen <dingyichen@gmail.com> - 1.24.0-2
- ExcludeArch: i686

* Thu Nov 20 2025 Ding-Yi Chen <dingyichen@gmail.com> - 1.24.0-1
- Update to version 1.24.0
  + Resolves: rhbz#2383142
  + Upstream removed deskflow-server and deskflow-client
  + Upstream provide deskflow-core [client|server] instead
  + shell script deskflow-server and deskflow-client are created
  + html doc included
- Resolves: rhbz#2400833 Deskflow incorrectly replaces Synergy package 
  + deskflow no longer provide or conflict with synergy

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jun 13 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.22.0-1
- Update to version 1.22.0
- Resolves: rhbz#2369204

* Sun Apr 20 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.21.2-1
- Update to 1.21.2

* Sat Mar 15 2025 Neal Gompa <ngompa@fedoraproject.org> - 1.20.1-1
- Update to 1.20.1

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
