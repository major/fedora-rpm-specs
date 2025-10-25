%global with_snapshot   0
#%%global shortcommit     1552170
#%%global checkout        g%%{shortcommit}
#%%global upversion       1.3-4
%global postrelease     .post4
%global debug_package   %{nil}

Summary:        AMD Radeon video cards monitoring utility
Name:           radeontop
Version:        1.4
Release:        %autorelease
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/clbr/%{name}

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-no-rebuild.patch

BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  sed

%description
RadeonTop is a monitoring utility for AMD Radeon cards from R600 and up.

%prep
%autosetup -p1 -n %{name}-%{version}%{?shortcommit:-%{checkout}}
sed -i -e 's/unknown/%{version}/' getver.sh

%build
%set_build_flags
%make_build 

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}
%find_lang %{name}

# Add AppStream metadata
install -Dm 0644 -p %{name}.metainfo.xml \
        %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
# Validate Appstream metadata
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml

%files -f %{name}.lang
%doc README.md 
%license COPYING
%{_bindir}/%{name}
# Workaround failure to build on /usr/lib64
%{_libdir}/lib%{name}_xcb.so
%{_mandir}/man1/%{name}.1*
#AppStream metadata
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
