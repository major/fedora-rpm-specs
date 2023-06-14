Name:           fabtests
Version:        1.18.0
Release:        %autorelease
Summary:        Test suite for libfabric API
# include/jsmn.h and common/jsmn.c are licensed under MIT.
# All other source files permit distribution under BSD. Some of them
# additionaly expressly allow the option to be licensed under GPLv2.
# See the license headers in individual source files to see which those are.
License:        BSD and (BSD or GPLv2) and MIT
Url:            https://github.com/ofiwg/libfabric
Source:         https://github.com/ofiwg/libfabric/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Patch0:         0001-adjust-shebang-lines-in-rft_yaml_to_junit_xml-and-ru.patch
BuildRequires:  libfabric-devel >= %{version}
BuildRequires:  valgrind-devel
BuildRequires:  gcc
BuildRequires:  make
Requires:       python3-pytest

%description
Fabtests provides a set of examples that uses libfabric - a high-performance
fabric software library.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p2

%build
%configure --with-valgrind
make %{?_smp_mflags} V=1

%install
%make_install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_datadir}/%{name}/
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*
%doc AUTHORS README
%license COPYING

%changelog
%autochangelog
