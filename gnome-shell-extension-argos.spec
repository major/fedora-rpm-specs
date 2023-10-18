%global uuid argos@pew.worldwidemann.com

%global forgeurl https://github.com/p-e-w/argos
%global commit e2d68ea23eed081fccaec06c384e2c5d2acb5b6b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230404

# Supporting GNOME 45 requires applying a patch that does not support
# older releases
%if 0%{?fedora} >= 39
%bcond_without gnome45
%else
%bcond_with gnome45
%endif

Name:           gnome-shell-extension-argos
Version:        3^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Create GNOME Shell extensions in seconds

License:        GPL-3.0-only
URL:            %{forgeurl}
Source:         %{url}/archive/%{commit}/argos-%{commit}.tar.gz
Patch:          %{forgeurl}/pull/150.patch#/argos-gnome-45.diff

BuildArch:      noarch

%if %{with gnome45}
Requires:       gnome-shell >= 45.0
%else
Requires:       gnome-shell < 45.0
%endif

%description
Most GNOME Shell extensions do one thing: Add a button with a dropdown menu to
the panel, displaying information and exposing functionality. Even in its
simplest form, creating such an extension is a nontrivial task involving a
poorly documented and ever-changing JavaScript API.

Argos lets you write GNOME Shell extensions in a language that every Linux user
is already intimately familiar with: Bash scripts.

More precisely, Argos is a GNOME Shell extension that turns executables'
standard output into panel dropdown menus. It is inspired by, and fully
compatible with, the BitBar app for macOS. Argos supports many BitBar plugins
without modifications, giving you access to a large library of well-tested
scripts in addition to being able to write your own.


%prep
%autosetup -N -n argos-%{commit}
%autopatch -M 99 -p1

%if %{with gnome45}
%autopatch -m 100 -p1
%endif


%build


%install
mkdir -p %{buildroot}/%{_datadir}/gnome-shell/extensions/
cp -pr %{uuid} %{buildroot}%{_datadir}/gnome-shell/extensions/


%files
# asked upstream to include license text:
# https://github.com/p-e-w/argos/pull/115
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
%autochangelog
