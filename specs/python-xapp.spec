%global forgeurl https://github.com/linuxmint/python-xapp
%global tag      %{version}

Name:           python-xapp
Version:        3.0.4
Release:        %{autorelease}
%{forgemeta}
Summary:        Python bindings for xapps

License:        LGPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%description
%{summary}.


%package -n python3-xapp
Summary:       %{summary}

BuildSystem:   meson
BuildRequires: python3-rpm-macros

Requires:      gtk3
Requires:      python3-gobject-base
Requires:      python3-psutil
Requires:      xapps

%description -n python3-xapp
%{summary}.


%prep
%autosetup -p1 -n python3-xapp-%{version}


%files -n python3-xapp
%license COPYING debian/copyright
%doc PKG-INFO debian/changelog
%{python3_sitelib}/xapp/


%changelog
%autochangelog
