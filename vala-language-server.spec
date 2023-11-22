Name:           vala-language-server
Summary:        Language server for the Vala programming language
Version:        0.48.7
Release:        %autorelease

# The entire source is LGPLv2+, except plugins/gnome-builder/vala_langserv.py, which is GPLv3+.
# It is not installed when the "plugins" meson option is set to false.
# Since GNOME Builder 41, the VLS the plugin has been included.
License:        LGPLv2+

URL:            https://github.com/Prince781/vala-language-server
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  vala                        >= 0.48.12
BuildRequires:  vala-devel                  >= 0.48.12

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)    >= 1.4.4
BuildRequires:  pkgconfig(jsonrpc-glib-1.0) >= 3.28
BuildRequires:  pkgconfig(scdoc)

Requires:       glib2-static%{?_isa}
Requires:       json-glib%{?_isa}
Requires:       jsonrpc-glib%{?_isa}
Requires:       libgee%{?_isa}
Requires:       libvala%{?_isa}             >= 0.48.12

Recommends:     gobject-introspection-devel

Suggests:       gnome-builder


%description
Provides code intelligence for Vala (and also Genie).
Used with an editor and a plugin that supports the Language Server Protocol.


%prep
%autosetup -n %{name}-%{version}

%build
%meson -Dplugins=false
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md

%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
