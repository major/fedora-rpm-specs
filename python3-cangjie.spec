%global module_name cangjie
%global forgeurl https://github.com/Cangjians/pycangjie

Name:             python3-%{module_name}
Summary:          Python bindings to libcangjie
Version:          1.3
Release:          %{autorelease}
%forgemeta
License:          LGPL-3.0-only
URL:              http://cangjians.github.io/projects/pycangjie
Source0:          %{forgesource}
# Replace use of distutils (removed from Python3.12)
# https://patch-diff.githubusercontent.com/raw/Cangjians/pycangjie/pull/39
Patch0:           https://patch-diff.githubusercontent.com/raw/Cangjians/pycangjie/pull/39.patch

BuildRequires:    make
BuildRequires:    autoconf automake libtool
BuildRequires:    python3dist(cython) < 3~~
BuildRequires:    python3-devel
BuildRequires:    libcangjie-devel >= 1.2


%description
Python bindings to libcangjie, the library implementing Cangjie and Quick
input methods.


%prep
%autosetup -p1 -n pycangjie-%{version}


%build
autoreconf -i
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f '{}' \;


%check
make check


%files
%doc COPYING README.md docs/*.md
%{python3_sitearch}/%{module_name}


%changelog
%autochangelog
