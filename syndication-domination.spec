Name:           syndication-domination
Version:        1.0
Release:        %autorelease
Summary:        A simple RSS/Atom parser library

License:        AGPL-3.0-only
URL:            https://gitlab.com/gabmus/syndication-domination
Source:         %{url}/-/archive/%{version}/syndication-domination-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(pybind11)
BuildRequires:  pkgconfig(tidy)
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11

%global _description %{expand:
A simple RSS/Atom parser library written in C++, with Python bindings.}

%description %_description


%package -n python3-syndom
Summary:        %{summary}

%description -n python3-syndom %_description


%prep
%autosetup -p1 -n syndication-domination-%{version}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files -n python3-syndom
%license LICENSE
%doc README.md
%{python3_sitelib}/syndom%{python3_ext_suffix}


%changelog
%autochangelog
