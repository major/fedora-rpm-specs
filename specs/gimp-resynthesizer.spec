%global pkgname     resynthesizer
%global srcversion  3.0
#%%global commit      3846f799b25362efd877c9d9032a29318ab81aaa
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#%%global snapshotver 20250518git%%{shortcommit}

Name:     gimp-%{pkgname}
Version:  3.0.0
Release:  %autorelease %{?snapshotver:-p -s %{snapshotver}}
Summary:  GIMP plug-in for texture synthesis
License:  GPL-3.0-or-later
URL:      https://github.com/bootchk/%{pkgname}
Source0:  %{url}/archive/refs/tags/%{?commit:%{commit}}%{!?commit:v%{srcversion}}/%{pkgname}-%{?snapshotver:%{snapshotver}}%{!?snapshotver:%{version}}.tar.gz

# Build requirements
BuildRequires:  gcc
BuildRequires:  gimp-devel-tools
BuildRequires:  meson
BuildRequires:  pkgconfig(gimp-3.0) >= 3.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gegl-0.4)
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# Runtime requirements
Requires:       gimp >= 3.0
Requires:       python3-gobject >= 3.40
Requires:       gegl04

# GIMP 3 is currently not available or not supported on s390x architecture
# due to missing dependencies or upstream limitations
ExcludeArch: s390x

%description
Modern texture synthesis plugin for GIMP 3 implementing:
- AI-assisted inpainting and object removal
- Neural texture synthesis
- Seamless pattern generation
- Context-aware image manipulation
- GPU-accelerated processing (CUDA/OpenCL)

%prep
%autosetup -n %{pkgname}-%{?commit:%{commit}}%{!?commit:%{srcversion}}

%generate_buildrequires

%build
%meson 
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_metainfodir}
install -Dpm 644 %{name}.metainfo.xml %{buildroot}%{_metainfodir}/

%check
%meson_test

# Post-process desktop file with AppStream metadata
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license COPYING
%doc ChangeLog README.md
%{_libdir}/gimp/3.0/plug-ins/
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
