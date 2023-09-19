%global gittag v0.9.86
#%%global commit b0f6c7ba092f2526481ce8340a349685e51db9a3
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#%%global date 20220410

Name:           ccdciel
%if "%{?gittag}"
Version:        0.9.86
%else
Version:        0.9.79^%{date}%{shortcommit}
%endif
Release:        %autorelease
Summary:        CCD capture software

License:        GPL-3.0-or-later
URL:            http://www.ap-i.net/ccdciel/
%if "%{?gittag}"
Source0:        https://github.com/pchev/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
%else
Source0:        https://github.com/pchev/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
%endif


# Patch to avoid stripping debuginfo from executable
# Since this is Fedora specific we don't ask upstream to include
Patch100:       ccdciel-0.9.85_fix_debuginfo.patch

ExclusiveArch:  %{fpc_arches}
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  fpc
BuildRequires:  qt5pas-devel
%if 0%{?fedora} >= 39
BuildRequires:  fpc-src
BuildRequires:  lazarus-lcl-nogui
BuildRequires:  lazarus-lcl-qt5
BuildRequires:  lazarus-tools
%else
BuildRequires:  lazarus >= 1.6.2
%endif

# CCDciel requires libpasastro to function properly
# but rpm doesn't find this autorequire
Requires:       libpasastro%{?_isa}
Requires:       libpasraw%{?_isa}

Recommends:     astrometry, astrometry-tycho2
Recommends:     libindi


%description
CCDciel is a free CCD capture software intended for the amateur astronomer. 
It include all the features required to perform digital imaging 
CCD observation of celestial objects.
Using the standard drivers protocol INDI and ASCOM it can connect and control 
the CCD camera, the focuser, the filter wheel and the telescope mount.
It tightly integrates with Skychart to provide telescope control while
Indistarter can be used to control INDI server drivers


%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.


%prep
%if "%{?gittag}"
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

# Make sure we don't use bundled libraries
rm -rf library/*


%build
# Configure script requires non standard parameters
./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}

# Ccdciel doesn't like parallel building so we don't use macro.
# We pass options to fpc compiler for generate debug info.
make fpcopts="-O1 -gw3 -fPIC"


%install
make install PREFIX=%{buildroot}%{_prefix}

# Copy relevant documentation
cp -p doc/doc_%{name}_en.pdf %{buildroot}%{_pkgdocdir}


%check
# Menu entry
desktop-file-validate %{buildroot}%{_datadir}/applications/net.ap_i.%{name}.desktop

# Appdata file check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/net.ap_i.%{name}.metainfo.xml


%files
%license LICENSE gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/net.ap_i.%{name}.desktop
%{_datadir}/metainfo/net.ap_i.%{name}.metainfo.xml
%{_datadir}/icons/*/*/*/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png


%files      doc
%{_pkgdocdir}


%changelog
%autochangelog
