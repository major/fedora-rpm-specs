Name:           libaiff
Version:        6.0
%global so_version 2
Release:        %autorelease
Summary:        Open-source implementation of the AIFF format

# SPDX
License:        MIT
# The following build-system files do not contribute to the licenses of the
# binary RPMs:
#
# FSFAP-no-warranty-disclaimer:
#   - m4/ax_append_compile_flags.m4
#   - m4/ax_append_flag.m4
#   - m4/ax_check_compile_flag.m4
#   - m4/ax_require_defined.m4
SourceLicense:  %{license} AND FSFAP-no-warranty-disclaimer
URL:            http://aifftools.sourceforge.net/libaiff/
# While the latest SourceForge release linked from the above URL is 5.0,
# development by the original author, Marco Trillo, has continued at:
%global forgeurl https://github.com/mtszb/libaiff
Source:         %{forgeurl}/archive/v%{version}/libaiff-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
LibAiff is an open-source library, providing C applications transparent read &
write operations for Audio Interchange File Format (AIFF) files, with the goal
of supporting all of its features.

%package        devel
Summary:        Development files for LibAiff

Requires:       libaiff%{?_isa} = %{version}-%{release}

%description    devel
The libaiff-devel package contains libraries and header files for developing
applications that use LibAiff.


%prep
%autosetup


%conf
autoreconf --force --install --verbose
%configure


%build
%make_build


%install
%make_install


# Upstream does not provide any tests.


%files
%license LICENSE
%{_libdir}/libaiff.so.%{so_version}{,.*}


%files devel
%doc README
%doc MANUAL.html
%{_includedir}/libaiff/
%{_libdir}/libaiff.so


%changelog
%autochangelog
