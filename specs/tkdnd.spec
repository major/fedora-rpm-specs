%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global forgeurl https://github.com/petasis/tkdnd/

Name:           tkdnd
Version:        2.9.5
Release:        %autorelease
Summary:        Tk extension that adds native drag & drop capabilities

%global tag tkdnd-release-test-v%{version}
%forgemeta

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  tk-devel
Requires: tcl(abi) = 8.6



%description
Tk Drag & Drop: tkdnd is an extension that adds native drag & drop capabilities
to the tk toolkit. It can be used with any tk version equal or greater to 8.4.
Under unix the drag & drop protocol in use is the XDND protocol version 4
(also used by the QT toolkit, KDE & GNOME Desktops).

%prep
%forgesetup
#%%setup -q -n %{name}%{version}

%build
%configure --enable-symbols
make %{?_smp_mflags}

%install
make libdir=%{tcl_sitearch} DESTDIR=%{buildroot} install \
        INSTALL_DATA="install -pm 644" INSTALL_LIBRARY="install -pm 755"
chmod +x %{buildroot}%{tcl_sitearch}/%{name}%{version}/libtcl9%{name}%{version}.so


%files
%doc doc/*
%{_mandir}/mann/tkDND.n.gz
%{tcl_sitearch}/%{name}%{version}/


%changelog
%autochangelog
