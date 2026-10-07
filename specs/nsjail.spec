%global _lto_cflags %{nil}

Name:		nsjail
Version:	3.6
Release:	3%{?dist}
License:	Apache-2.0
Summary:	A lightweight process isolation tool
URL:		https://github.com/google/nsjail
# git clone https://github.com/google/nsjail.git
# cd nsjail
## this is 3.6
# git checkout f78475530b46d0186111a9096b30725f816b55fe
## get kafel
# git submodule update --init
# cd ..
# mv nsjail nsjail-3.6
# tar cvfj nsjail-3.6.tar.bz2 nsjail-3.6/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		s390x-support.patch
Patch1:		ppc64le-support.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	git
BuildRequires:	libnl3-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	pkg-config
BuildRequires:	protobuf3-compiler
BuildRequires:	protobuf3-devel

%description
A lightweight process isolation tool that utilizes Linux namespaces, cgroups,
rlimits and seccomp-bpf syscall filters, leveraging the Kafel BPF language
for enhanced security.

%prep
%setup -q
%patch -P0 -p1 -b .s390x
%patch -P1 -p1 -b .ppc64le

sed -i 's|-O2|%{optflags}|g' Makefile
sed -i 's|-O2|%{optflags}|g' kafel/build/Makefile.mk

%build
export LDFLAGS="%{build_ldflags}"
%make_build

%install
%make_install

%check
# test suite is fragile and poorly suited to rpm builds
# make test

%files
%license LICENSE
%doc README.md
%{_bindir}/nsjail
%{_mandir}/man1/nsjail.*

%changelog
* Tue Oct  6 2026 Tom Callaway <spot@fedoraproject.org> - 3.6-3
- add support for ppc64le

* Tue Oct  6 2026 Tom Callaway <spot@fedoraproject.org> - 3.6-2
- cleanup spec (properly use License/Summary fields)
- split BRs on separate lines
- add support for s390x

* Tue Sep 29 2026 Tom Callaway <spot@fedoraproject.org> - 3.6-1
- initial package
