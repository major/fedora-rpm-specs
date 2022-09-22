%global uuid argos@pew.worldwidemann.com

# https://github.com/p-e-w/argos is unmaintained, temporarily use
# mwilck's version which has the most comprehensive updates for GNOME 3.36+
%global forgeurl https://github.com/mwilck/argos
%global commit 028b2294f69b812adc2b3419daa5798237382aeb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20220711

Name:           gnome-shell-extension-argos
Version:        3^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Create GNOME Shell extensions in seconds

License:        GPLv3
URL:            %{forgeurl}
Source:         %{url}/archive/%{commit}/argos-%{commit}.tar.gz

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
