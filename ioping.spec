Name:           ioping
Version:        1.3
Release:        %{autorelease}
Summary:        Simple disk I/O latency monitoring tool
License:        GPLv3+
URL:            https://github.com/koct9i/ioping
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
%description
ioping lets you monitor I/O latency in real time. It shows disk latency in 
the same way as ping shows network latency.

%prep
%autosetup

%build
export CFLAGS="-Wextra -pedantic -funroll-loops -ftree-vectorize %{optflags}"
export LDFLAGS="%{?__global_ldflags}"
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%doc changelog README.md
%license LICENSE
%{_bindir}/ioping
%{_mandir}/man1/ioping.1*

%changelog
%autochangelog
