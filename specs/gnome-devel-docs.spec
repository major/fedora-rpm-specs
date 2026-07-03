Name: gnome-devel-docs
Version: 40.3
Release: %autorelease
Summary: GNOME developer documentation

# accessibility-devel-guide and optimization-guide are under the GFDL-1.1-or-later
# hig is licensed under CC-BY-SA-4.0
# optimization-guide is under the GFDL 1.1 or later
# platform-demos is licensed under CC-BY-SA-3.0 WITH GNOME-examples-exception
# platform-overview is licensed under CC-BY-SA-3.0
# programming-guidelines is licensed under CC-BY-SA-3.0
License: GFDL-1.1-or-later AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC-BY-SA-3.0 WITH GNOME-examples-exception
URL: https://developer.gnome.org
Source0: https://download.gnome.org/sources/%{name}/%{gnome_major_version}/%{name}-%{gnome_tarball_version}.tar.xz

%gnome_check_version

BuildArch: noarch
BuildRequires: docbook-utils
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: make
BuildRequires: yelp-tools

%description
This package contains documents which are targeted for GNOME developers.
It contains, e.g., the Human Interface Guidelines, the Integration Guide
and the Platform Overview.

%prep
%autosetup -p1 -n %{name}-%{gnome_tarball_version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%find_lang %{name} --all-name --with-gnome


%files -f %{name}.lang
%doc README AUTHORS NEWS
%license COPYING COPYING.GFDL

%changelog
%autochangelog
