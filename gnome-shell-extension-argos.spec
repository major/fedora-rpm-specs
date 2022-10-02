%global uuid argos@pew.worldwidemann.com

%global forgeurl https://github.com/p-e-w/argos
%global commit 118056863633ccc1bf927079ed0ba131576232b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20220712

Name:           gnome-shell-extension-argos
Version:        3^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Create GNOME Shell extensions in seconds

License:        GPLv3
URL:            %{forgeurl}
Source:         %{url}/archive/%{commit}/argos-%{commit}.tar.gz
# add support for GNOME 43
Patch:          %{url}/pull/141.patch#/argos-gnome-43.diff

BuildArch:      noarch

Requires:       gnome-shell

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
%autosetup -p1 -n argos-%{commit}


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
