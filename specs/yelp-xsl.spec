%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           yelp-xsl
Version:        49.0
Release:        %autorelease
Summary:        XSL stylesheets for the yelp help browser

License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-3-Clause
URL:            https://download.gnome.org/sources/yelp-xsl
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  gettext-devel
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  python3-libxml2
BuildRequires:  /usr/bin/ducktype
BuildRequires:  /usr/bin/xmllint
BuildRequires:  /usr/bin/xsltproc

%description
This package contains XSL stylesheets that are used by the yelp help browser.


%package devel
Summary: Developer documentation for yelp-xsl
Requires: %{name} = %{version}-%{release}

%description devel
The yelp-xsl-devel package contains developer documentation for the
XSL stylesheets in yelp-xsl.


%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install


%files
%doc AUTHORS README.md
%license COPYING COPYING.GPL COPYING.LGPL
%{_datadir}/yelp-xsl

%files devel
%{_datadir}/pkgconfig/yelp-xsl.pc


%changelog
%autochangelog
