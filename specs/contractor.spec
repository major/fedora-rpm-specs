Name:           contractor
Version:        0.3.5
Release:        %autorelease
Summary:        Desktop-wide extension service

License:        GPL-3.0-or-later
URL:            https://github.com/elementary/contractor
Source:         %{url}/archive/%{version}/contractor-%{version}.tar.gz

# Install into libexecdir instead of bindir
# https://github.com/elementary/contractor/pull/36
Patch:          %{url}/pull/36.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  meson

# data/meson.build
BuildRequires:  pkgconfig(dbus-1)
# src/meson.build
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)

# For %%{_datadir}/dbus-1/services/ directory:
Requires:       dbus-common

%description
An extension service that allows apps to use the exposed functionality
of registered apps. This way, apps don't have to have the functions hard
coded into them.


%prep
%autosetup -p1


%conf
%meson


%build
%meson_build


%install
%meson_install

# Create the the directory where other programs put their contracts
mkdir -p %{buildroot}/%{_datadir}/contractor


# Upstream does not provide any tests.


%files
%doc README.md
%license COPYING

%{_libexecdir}/contractor

%dir %{_datadir}/contractor
%{_datadir}/dbus-1/services/org.elementary.contractor.service


%changelog
%autochangelog
