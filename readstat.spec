%bcond_with check

%global forgeurl https://github.com/WizardMac/ReadStat
Version:        1.1.9
%forgemeta

Name:           readstat
Release:        %autorelease
Summary:        Read (and write) data sets from SAS, Stata, and SPSS
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
# Fix use after free
Patch0:         https://github.com/WizardMac/ReadStat/pull/298.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake

BuildRequires:  gettext-devel
BuildRequires:  libtool

%description
Originally developed for Wizard, ReadStat is a command-line tool and
MIT-licensed C library for reading files from popular stats packages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools package contains tools about %{name}.

%prep
%forgeautosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%if %{with check}
%check
make check
%endif

%files
%license LICENSE
%doc README.md
%{_libdir}/libreadstat.so.1*

%files devel
%{_includedir}/readstat.h
%{_libdir}/libreadstat.so

%files tools
%{_bindir}/extract_metadata
%{_bindir}/readstat
%{_mandir}/man1/extract_metadata.1.gz
%{_mandir}/man1/readstat.1.gz

%changelog
%autochangelog
