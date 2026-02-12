%global _legacy_common_support 1
%global forgeurl https://gitlab.utu.fi/vesoik/tpcclib

Name:           libtpcimgio
# upstream has gone from versioning series 1.x to 0.x in the new GitLab repository
Epoch:          1
Version:        0.8.0
Release:        %autorelease
Summary:        Turku PET Centre for image file input and output procedures

# upstream only supports 64 bit architectures
ExcludeArch:    %{ix86}

%global tag  v%{version}

%forgemeta
License:        GPL-3.0-or-later

URL:            %forgeurl
Source0:        %forgesource

# fedora related changes are in my fork
# - generate shared objects
# - only build tpcmisc
# - clean up compiler flags
Patch:          https://gitlab.com/sanjayankur31/tpcclib/-/merge_requests/2.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libtpcmisc-devel


%description
The libtpcimgio library is a collection of commonly used C files
in Turku PET Centre for image file input and output procedures.
Libtpcimgio library supports Analyze 7.5, Ecat 6.x, Ecat 7.x and
partly interfile formats.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static libraries for %{name}

%description    static
This package contains static libraries for %{name}.

%prep
%forgeautosetup -S git

sed -i 's/\r$//' changelog.md
sed -i 's/\r$//' readme.md


%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license license.md
%doc readme.md changelog.md
%{_bindir}/%{name}
%{_bindir}/%{name}big
%{_libdir}/%{name}.so.0.0.0
%{_libdir}/%{name}.so.0

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}.h

%files static
%license license.md
%{_libdir}/%{name}.a

%changelog
%autochangelog
