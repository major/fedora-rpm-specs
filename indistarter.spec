%global commit 52da97ea4c5a1325ca0e25e01218cb278face660
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20220410

Name:           indistarter
Version:        2.3.1^%{date}%{shortcommit}
Release:        3%{?dist}
Summary:        GUI to start, stop and control an INDI server

License:        GPLv3+
URL:            https://github.com/pchev/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# This patch avoid stripping debuginfo from binary
# Since this is Fedora specific we don't ask upstream to include
Patch100:       indistarter-2.0.0_fix_debuginfo.patch

ExclusiveArch:  %{fpc_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  lazarus
BuildRequires:  libappstream-glib
BuildRequires:  make

%description
Indistarter is a user interface to run a INDI server.
You can configure different profile for your astronomical equipment.
The INDI server can be launched locally or remotely on another computer.
In this last case a ssh tunnel is established to allow local client connection.

%prep
%autosetup -n %{name}-%{commit} -p1


%build
# Configure script requires non standard parameters
./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}

# Doesn't like parallel building so we can't use make macro
make fpcopts="-O1 -gw3 -fPIC"


%install
make install PREFIX=%{buildroot}%{_prefix}

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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1^2022041052da97e-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1^2022041052da97e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

%autochangelog
