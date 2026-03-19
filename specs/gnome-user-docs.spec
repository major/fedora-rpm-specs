%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           gnome-user-docs
Version:        50.0
Release:        %autorelease
Summary:        GNOME User Documentation

License:        CC-BY-SA-3.0
URL:            https://help.gnome.org/
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools

%description
This package contains end-user documentation for the GNOME desktop
environment.

%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%configure
%make_build

%install
%make_install

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md

%changelog
%autochangelog
