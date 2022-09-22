%global forgeurl https://github.com/debrouxl/tfdocgen
%global commit a9d4bf89b9a54cdbddb970b3079d802a34d69cdb
%if 0%{?el7}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global forgesource %{forgeurl}/archive/%{commit}/tfdocgen-%{commit}.tar.gz
%global date 20220124
%else
%forgemeta
%endif

Name:           tfdocgen
Version:        1.00
%if 0%{?el7}
Release:        %autorelease -s %{date}git%{shortcommit}
%else
Release:        %autorelease
%endif
Epoch:          1
Summary:        TiLP framework documentation generator

License:        GPLv2+
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  glib2-devel

%description
The tfdocgen program is a program used by the libti* libraries to generate
their HTML documentation from sources and misc files. You don't need this
package unless you want to develop on the libti* libraries.

%prep
%autosetup -n %{name}-%{commit}/trunk

%build
autoreconf -ifv
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
