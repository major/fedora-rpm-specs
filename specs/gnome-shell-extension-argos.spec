%global uuid argos@pew.worldwidemann.com

%global forgeurl https://github.com/p-e-w/argos
%global commit 13264042ae8b8a6f9f4778c623780e38e5d1cd89
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20250327

Name:           gnome-shell-extension-argos
Version:        3^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Create GNOME Shell extensions in seconds

License:        GPL-3.0-only
URL:            %{forgeurl}
Source:         %{url}/archive/%{commit}/argos-%{commit}.tar.gz#/argos-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?fedora} >= 42
BuildRequires:  gnome-shell-rpm-generators
%else
Requires:       (gnome-shell >= 45.0 with gnome-shell < 49.0)
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
%autosetup -n argos-%{commit} -p1


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
