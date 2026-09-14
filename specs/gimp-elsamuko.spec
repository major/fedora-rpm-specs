%global commit 983091f34bef9074e5fba28f8d3e0b492e5f9e8b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gimp-elsamuko
Version:        30
Release:        %autorelease
Summary:        Script collection for the GIMP
License:        GPL-3.0-or-later
URL:            https://github.com/elsamuko/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  libappstream-glib
Requires:       gimp >= 3.0
BuildArch:      noarch

%description
A collection of scripts for GIMP that provides effects such as Technicolor,
rounded corners, the Obama "Hope" poster style, vintage looks, and sharpening.

%prep
%autosetup -n %{name}-%{commit}

%install
install -d %{buildroot}%{_datadir}/gimp/3.0/scripts
install -p -m 0644 scripts/*.scm \
    -t %{buildroot}%{_datadir}/gimp/3.0/scripts

install -D -p -m 0644 %{name}.metainfo.xml \
    %{buildroot}%{_metainfodir}/com.github.elsamuko.%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{name}.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_datadir}/gimp/3.0/scripts/*.scm
%{_metainfodir}/com.github.elsamuko.%{name}.metainfo.xml

%changelog
%autochangelog
