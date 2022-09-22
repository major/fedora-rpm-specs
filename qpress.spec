Name:           qpress
Version:        11
Release:        %autorelease
Summary:        A portable file archiver using QuickLZ

License:        GPLv2
URL:            https://www.quicklz.com
Source0:        %{url}/%{name}-%{version}-source.zip
Patch0:         01-include-unistd.patch

BuildRequires:  gcc-c++
BuildRequires:  coreutils

Provides:       bundled(quicklz) = 1.4.1

%description
qpress is a portable file archiver using QuickLZ and designed to utilize fast
storage systems to their max. It's often faster than file copy because the
destination is smaller than the source.

%prep
%autosetup -c -p1

%build
%set_build_flags
$CXX $CXXFLAGS -o qpress qpress.cpp aio.cpp quicklz.c utilities.cpp $LDFLAGS

%install
install -Dpm0755 -t %{buildroot}/%{_bindir} %{name}

%files
%{_bindir}/%{name}

%changelog
%autochangelog
