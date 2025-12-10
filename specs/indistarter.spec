# Disable parallel build
%global _smp_build_ncpus 1

%global gittag v2.5.1
#%%global commit 1abc907b93a1ba402ca28652de42c81b90c80250
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#%%global date 20230125

Name:           indistarter
%if "%{?gittag}"
Version:        2.5.1
%else
Version:        2.3.1^%{date}%{shortcommit}
%endif
Release:        %autorelease
Summary:        GUI to start, stop and control an INDI server

License:        GPL-3.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND BSD-3-Clause AND MPL-1.1
URL:            https://github.com/pchev/%{name}
%if "%{?gittag}"
Source0:        %{url}/archive/%{gittag}/%{name}-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
%endif

# This patch avoid stripping debuginfo from binary
# Since this is Fedora specific we don't ask upstream to include
Patch100:       indistarter-2.0.0_fix_debuginfo.patch

ExclusiveArch:  %{fpc_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  fpc-src
BuildRequires:  lazarus-lcl-nogui
BuildRequires:  lazarus-lcl-qt6
BuildRequires:  lazarus-tools

%description
Indistarter is a user interface to run a INDI server.
You can configure different profile for your astronomical equipment.
The INDI server can be launched locally or remotely on another computer.
In this last case a ssh tunnel is established to allow local client connection.

%prep
%if "%{?gittag}"
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif


%build
# Configure script requires non standard parameters
./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}

%make_build fpcopts="-O1 -gw3 -fPIC" LCL_PLATFORM=qt6


%install
%make_install PREFIX=%{buildroot}%{_prefix}


%check
# Menu entry
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
# Appdata file check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%license gpl-3.0.txt LICENSE
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/indigui
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/pixmaps/*.png


%changelog
%autochangelog
