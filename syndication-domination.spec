%global commit ca0ea3b56decaf6ee668e4ab32278499389ca35f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20240211

Name:           syndication-domination
Version:        1.0%{?gitdate:^%{gitdate}.git%{shortcommit}}
Release:        %autorelease
Summary:        A simple RSS/Atom parser library

License:        AGPL-3.0-or-later
URL:            https://gitlab.com/gabmus/syndication-domination
%if 0%{?gitdate}
Source:         %{url}/-/archive/%{commit}/syndication-domination-%{commit}.tar.bz2
%else
Source:         %{url}/-/archive/%{version}/syndication-domination-%{version}.tar.bz2
%endif
# https://gitlab.com/gabmus/syndication-domination/-/merge_requests/2
Patch:          0001-Install-into-python.platlibdir.patch

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
%autosetup -p1 %{?gitdate:-n %{name}-%{commit}}


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
%{python3_sitearch}/syndom%{python3_ext_suffix}


%changelog
%autochangelog
