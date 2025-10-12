%global git_commit 9c7ec82dfebef238a61e5a6788f043420d30193f
%global git_date 20250901

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		softwedge
Version:	0.1^%{git_suffix}
Release:	1%{?dist}
Summary:	A serial software keyboard wedge for *nix X11
License:	GPL-2.0-only
URL:		https://github.com/theatrus/softwedge
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
BuildRequires:	gcc
BuildRequires:	libX11-devel
BuildRequires:	libXtst-devel

%description
Small Linux utility which forwards data from a serial port (such as
from a tty, or a barcode scanner) and re-issues the data as X11 key press
events.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

%build
# Included Makefile isn't much useful
gcc %{build_cflags} %{build_ldflags} -o %{name} -Isw sw/main.c sw/softwedge.c -lX11 -lXtst

%install
install -Dpm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README
%{_bindir}/softwedge

%changelog
* Mon Sep 01 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1^20250901git9c7ec82d-1
- Initial version
