%bcond_without tests

%global appstream_id io.github.syllo.nvtop

Name:           nvtop
Version:        3.0.1
Release:        %autorelease
Summary:        GPU process monitoring for AMD, Intel and NVIDIA

# BSD-3-Clause: include/ini.h, src/ini.c
# LGPL-2.1-or-later: include/list.h - this combines into GPL-3.0-or-later
# some cmake modules are BSD-3-Clause or MIT but those are not shipped out
License:        GPL-3.0-or-later and BSD-3-Clause
URL:            https://github.com/Syllo/nvtop
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# these might be upstreamable
Patch0:         %{name}-fix-icon-path.diff
Patch1:         %{name}-fix-appstream-path.diff
# these can be upstreamed. Will do once verifying the metadata shows properly
Patch2:         %{name}-fix-icon-in-appstream.diff
Patch3:         %{name}-fix-screenshot-urls-in-appstream.diff

BuildRequires:  cmake >= 3.10
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ncursesw)
%if %{with tests}
%if 0%{?el8}
# EL8 gtest doesn't ship pkgconfig
BuildRequires:  gtest-devel
%else
BuildRequires:  pkgconfig(gtest)
%endif
%endif
Requires:       hicolor-icon-theme

%description
Nvtop stands for Neat Videocard TOP, a (h)top like task monitor for AMD, Intel
and NVIDIA GPUs. It can handle multiple GPUs and print information about them in
a htop familiar way.


%prep
%autosetup -p1


%build
%if %{with tests}
%cmake -DBUILD_TESTING=ON
%else
%cmake
%endif
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appstream_id}.metainfo.xml
%if %{with tests}
%ctest
%endif


%files
%license COPYING
%doc README.markdown
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{appstream_id}.metainfo.xml


%changelog
%autochangelog
