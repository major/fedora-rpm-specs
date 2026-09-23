Name:		audioreach-conf
Version:	1.1.1
Release:	%autorelease
Summary:	AudioReach configuration files

License:	BSD-3-Clause
URL:		https://github.com/AudioReach/audioreach-conf
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/AudioReach/audioreach-conf/pull/91
Patch0:		91.patch
# https://github.com/AudioReach/audioreach-conf/pull/92
Patch1:		92.patch
# https://github.com/AudioReach/audioreach-conf/pull/93
Patch2:		93.patch

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
The %{name} package provides configuration files for various AudioReach
components for different vendor, business unit (BU), chipset and board.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%autosetup -p1

# noarch pkgconfig path fix
sed -i -e 's|pkgconfigdir = $(libdir)/pkgconfig|pkgconfigdir = $(datadir)/pkgconfig|g' qcom/Makefile.am

%conf
autoreconf -fiv
%configure --with-qcom

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/audioreach
%config(noreplace) %{_sysconfdir}/audioreach/card-defs.xml
%dir %{_datadir}/audioreach
%{_datadir}/audioreach/acdbdata

%files devel
%{_includedir}/audioreach
%{_datadir}/pkgconfig/kvh2xml.pc

%changelog
%autochangelog
