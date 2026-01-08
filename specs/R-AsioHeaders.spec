Name:           R-AsioHeaders
Version:        %R_rpm_version 1.30.2-1
Release:        %autorelease
Summary:        Asio C++ Header Files

License:        BSL-1.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Obsoletes:      %{name}-devel < 1.30.2-1

Provides:       bundled(asio) = 1.30.2
Requires:       openssl-devel
Requires:       openssl-devel-engine
Recommends:     boost-devel

%description
'Asio' is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous model using
a modern C++ approach. It is also included in Boost but requires linking when
used with Boost. Standalone it can be used header-only (provided a recent
compiler). 'Asio' is written and maintained by Christopher M. Kohlhoff, and
released under the 'Boost Software License', Version 1.0.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
