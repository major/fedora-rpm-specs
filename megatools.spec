%global snapshot 20230212

Name:           megatools
Version:        1.11.1
Release:        %autorelease
Summary:        Command line client for MEGA
License:        GPL-3.0-or-later
URL:            http://megatools.megous.com/
Source0:        http://megatools.megous.com/builds/builds/%{name}-%{version}.%{snapshot}.tar.gz
Source1:        http://megatools.megous.com/builds/builds/%{name}-%{version}.%{snapshot}.tar.gz.asc
Source2:        %{name}.rpmlintrc

BuildRequires:  asciidoc
BuildRequires:  docbook2X
BuildRequires:  meson
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)

%description
Megatools is a collection of programs for accessing Mega service from a command
line of your desktop or server.

Megatools allow you to copy individual files as well as entire directory trees
to and from the cloud. You can also perform streaming downloads for example to
preview videos and audio files, without needing to download the entire file.

You can register an account using a "megareg" tool, with the benefit of having
true control of your encryption keys.

Megatools are robust and optimized for fast operation - as fast as Mega servers
allow. Memory requirements and CPU utilization are kept at minimum.

%prep
%autosetup -n %{name}-%{version}.%{snapshot}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license LICENSE
%doc NEWS README TODO LICENSE
%{_bindir}/mega*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*


%changelog
%autochangelog
