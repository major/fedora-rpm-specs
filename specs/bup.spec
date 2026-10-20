# The test suite is long and needs a fairly complete environment;
# build with --without tests to skip it.
%ifarch s390x
%bcond tests 0
%else
%bcond tests 1
%endif

Name:           bup
Version:        0.34
Release:        1%{?dist}
Summary:        Very efficient backup system based on the git packfile format

License:        LGPL-2.0-only
URL:            https://bup.github.io/
# GitHub archives have lib/bup/source_info.py expanded via export-subst,
# which bup needs to report its version when not built from a checkout.
Source0:        https://github.com/bup/bup/archive/%{version}/%{name}-%{version}.tar.gz
Source3:        README-bup-web.Fedora.md
Source2:        bup-web.service

# Fixes the test suite to account for Fedora's root permissions
Patch0:         fedora-test-suite.patch

BuildRequires:  bash
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  python3-devel
BuildRequires:  python3dist(tornado)
BuildRequires:  systemd

%if %{with tests}
BuildRequires:  acl
BuildRequires:  attr
BuildRequires:  par2cmdline
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pyxattr)
BuildRequires:  rsync
BuildRequires:  perl-interpreter
BuildRequires:  man-db
%endif

Requires:       python3dist(tornado)
Requires:       git-core
Requires:       python3dist(pyxattr)
Recommends:     par2cmdline
Suggests:       python3dist(fuse)

%description
bup is a program that backs things up. It uses a rolling checksum
algorithm (similar to rsync) to split large files into chunks, and
stores them in the git packfile format, so it is very efficient with
large files, VM images, and databases, and only stores identical
chunks once. It supports incremental backups to local or remote
repositories, par2-based recovery, a FUSE view of the repository, and
an optional web interface.

%prep
%autosetup -p1
# Avoid /usr/bin/env shebangs (rejected by brp-mangle-shebangs)
sed -i '1s|^#!/usr/bin/env bash|#!/usr/bin/bash|' lib/cmd/bup-import-rdiff-backup


%conf
# bup's configure is hand-written, not autoconf: it takes no --prefix
# style options and only reads CC/CFLAGS/CPPFLAGS/LDFLAGS from the
# environment, recording them in config/config.vars for the makefile.
# The build adds -Werror; don't let new compiler warnings break builds.
%set_build_flags
export CFLAGS="$CFLAGS -Wno-error"
# Pin the python we build against (configure only probes up to 3.14
# before falling back to python3-config).
export BUP_PYTHON_CONFIG=python%{python3_version}-config
./configure --with-pylint=no


%build
%make_build

%install
# Install paths are plain make variables (no configure options).
# LIBDIR holds bup's python modules and the compiled _helpers.so.
%make_install \
    PREFIX=%{_prefix} \
    BINDIR=%{_bindir} \
    LIBDIR=%{_libdir}/bup \
    MANDIR=%{_mandir} \
    DOCDIR=%{_pkgdocdir}

# Installing the systemd service, and the related readme
mkdir -p %{buildroot}%{_userunitdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_userunitdir}/bup-web.service
install -p -m 0644 %{SOURCE3} %{buildroot}%{_pkgdocdir}

# The modules live outside site-packages, so byte-compile explicitly.
%py_byte_compile %{python3} %{buildroot}%{_libdir}/bup/bup

%if %{with tests}
%check
%make_build test
%endif

%post
%systemd_user_post bup-web.service

%preun
%systemd_user_preun bup-web.service

%postun
%systemd_user_postun_with_restart bup-web.service

%files
%license LICENSE
%doc README.md
%{_bindir}/bup
%{_libdir}/bup/
%{_mandir}/man1/bup*.1*
%{_mandir}/man5/bup*.5*
%{_pkgdocdir}/*.html
%{_pkgdocdir}/*.md
%{_userunitdir}/bup-web.service

%changelog
* Fri Oct 16 2026 Steve Cossette <steve@ninjasinpajamas.com> - 0.34-1
- Initial Release
