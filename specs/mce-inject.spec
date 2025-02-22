%global date 20241112
%global commit ca81c1dbed5c7e30fe79d44953ccfeaab98d2b4f
%global shortcommit %global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mce-inject
Version:        0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Linux machine check injector tool

License:        GPL-2.0-only
URL:            https://git.kernel.org/pub/scm/utils/cpu/mce/mce-inject.git
Source:         %{url}/snapshot/%{name}-%{commit}.tar.gz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
mce-inject allows to inject machine check errors on the software level into a
running Linux kernel. This is intended for validation of the kernel machine
check handler.

%prep
%autosetup -n %{name}-%{commit} -p1

# Preseve timestamps on install
sed -i 's/install -m/install -pm/g' Makefile

# https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin
sed -i 's:$(prefix)/sbin:%{_bindir}:g' Makefile

%build
%make_build CFLAGS="%{build_cflags}"

%install
%make_install destdir="%{buildroot}"

%files
%doc README test/
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%autochangelog
