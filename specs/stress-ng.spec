Name:		stress-ng
Version:	0.18.09
Release:	%autorelease
Summary:	Stress test a computer system in various ways

License:	GPL-2.0-or-later
URL:		https://github.com/ColinIanKing/stress-ng
Source0:	https://github.com/ColinIanKing/stress-ng/archive/V%{version}/%{name}-%{version}.tar.gz
# darn is not supported in Power ISA < 3.0, while Fedora aims for Power ISA 2.07
Patch0:     0_18_01-poewrpc-remove-darn.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	glibc-devel
BuildRequires:	kernel-headers
BuildRequires:	keyutils-libs-devel
BuildRequires:	libaio-devel
BuildRequires:	libattr-devel
%if %{undefined rhel}
BuildRequires:	libbsd-devel
%endif
BuildRequires:	libcap-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	lksctp-tools-devel
BuildRequires:	libatomic
BuildRequires:	zlib-devel
BuildRequires:	Judy-devel

%description
Stress test a computer system in various ways. It was designed to exercise
various physical subsystems of a computer as well as the various operating
system kernel interfaces.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

%install
install -p -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -p -m 644 -D %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -pm 644 bash-completion/%{name} \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%changelog
%autochangelog
